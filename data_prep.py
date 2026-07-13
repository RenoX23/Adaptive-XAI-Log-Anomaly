import os
import urllib.request
import re
import csv
import argparse
import polars as pl
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
from sentence_transformers import SentenceTransformer

def main():
    parser = argparse.ArgumentParser(description="Parse logs and prepare sequences out-of-core.")
    parser.add_argument("--log_url", type=str, default="https://raw.githubusercontent.com/logpai/loghub/master/HDFS/HDFS_2k.log", help="URL of the raw log file")
    parser.add_argument("--label_url", type=str, default="https://raw.githubusercontent.com/logpai/loglizer/master/data/HDFS/anomaly_label.csv", help="URL of the anomaly label file")
    parser.add_argument("--dataset_name", type=str, default="HDFS_2k", help="Name of the dataset")
    parser.add_argument("--data_dir", type=str, default="data", help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.data_dir, exist_ok=True)
    
    log_file = os.path.join(args.data_dir, f"{args.dataset_name}.log")
    label_file = os.path.join(args.data_dir, f"{args.dataset_name}_anomaly_label.csv")
    parsed_csv = os.path.join(args.data_dir, f"{args.dataset_name}_parsed.csv")
    seq_csv = os.path.join(args.data_dir, f"{args.dataset_name}_sequences.csv")
    embeddings_csv = os.path.join(args.data_dir, f"{args.dataset_name}_template_embeddings.csv")

    # 1. Download Data
    if not os.path.exists(log_file):
        print(f"Downloading {args.dataset_name} log sample from {args.log_url}...")
        urllib.request.urlretrieve(args.log_url, log_file)
        print("Log download complete.")
    else:
        print(f"{args.dataset_name} log sample already exists.")
        
    if not os.path.exists(label_file):
        print(f"Downloading {args.dataset_name} anomaly labels from {args.label_url}...")
        try:
            urllib.request.urlretrieve(args.label_url, label_file)
            print("Label download complete.")
        except Exception as e:
            print(f"Warning: Failed to download labels. Continuing without labels. Error: {e}")
            label_file = None
    else:
        print(f"{args.dataset_name} anomaly labels already exist.")

    # 2. Parse Logs
    print("Initializing Drain3 Parser...")
    config = TemplateMinerConfig()
    if os.path.exists("drain3.ini"):
        config.load(os.path.dirname(__file__) + "/drain3.ini")
    
    template_miner = TemplateMiner(config=config)

    print("Parsing logs...")
    blk_regex = re.compile(r'blk_-?\d+')
    
    # Process line-by-line and write directly to CSV to prevent OOM
    with open(log_file, 'r', encoding='utf-8') as f, open(parsed_csv, 'w', newline='', encoding='utf-8') as out_f:
        fieldnames = ["LineId", "BlockId", "EventId", "EventTemplate", "RawLog"]
        writer = csv.DictWriter(out_f, fieldnames=fieldnames)
        writer.writeheader()
        
        for line_idx, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            
            result = template_miner.add_log_message(line)
            
            # Extract Block ID if available
            match = blk_regex.search(line)
            block_id = match.group() if match else f"seq_{line_idx}"
            
            writer.writerow({
                "LineId": line_idx + 1,
                "BlockId": block_id,
                "EventId": result["cluster_id"],
                "EventTemplate": result.get("template_mined", result.get("template", "")),
                "RawLog": line
            })

    print(f"Parsed logs saved out-of-core to: {parsed_csv}")
    
    # 3. Extract semantic features using sentence-transformers
    print("Generating dense semantic embeddings for templates using sentence-transformers...")
    clusters = list(template_miner.drain.clusters)
    if clusters:
        cluster_ids = [c.cluster_id for c in clusters]
        templates = [c.get_template() for c in clusters]
        
        # Load the sentence-transformer model
        embedder = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = embedder.encode(templates)
        embeddings_df = pl.DataFrame(embeddings)
        embeddings_df.insert_column(0, pl.Series("EventId", cluster_ids))
        embeddings_df.write_csv(embeddings_csv)
        print(f"Saved semantic embeddings for {len(clusters)} templates to {embeddings_csv}.")

    # 4. Group by BlockId to generate event sequences and merge labels using Polars Lazy API
    print("Generating sequences from parsed logs using Polars Lazy API...")
    
    # scan_csv enables lazy execution out-of-core
    lazy_df = pl.scan_csv(parsed_csv)
    
    # Group by and aggregate to lists
    seq_lazy = (
        lazy_df
        .select(["BlockId", "EventId"])
        .with_columns(pl.col("EventId").cast(pl.String))
        .group_by("BlockId")
        .agg(pl.col("EventId"))
        .with_columns(pl.col("EventId").list.join(" "))
    )
    
    if label_file and os.path.exists(label_file):
        print("Merging sequences with ground-truth labels...")
        labels_lazy = pl.scan_csv(label_file)
        
        # We assume the label file has "BlockId" and "Label" columns
        seq_lazy = seq_lazy.join(labels_lazy, on="BlockId", how="left")
        
        # Fill missing labels
        seq_lazy = seq_lazy.with_columns(
            pl.col("Label").fill_null("Normal")
        )

    # Trigger the lazy computation graph using the streaming engine
    final_df = seq_lazy.collect(engine="streaming")
    
    # Write to CSV
    final_df.write_csv(seq_csv)
    print(f"Generated {final_df.height} numerical sequences with labels.")
    print(f"Sequences saved to: {seq_csv}")

    print(f"\nParsing complete. Found {len(clusters)} unique event templates.")
    
    print("\n--- Top 5 Extracted Templates ---")
    for cluster in clusters[:5]:
        print(f"Event ID: {cluster.cluster_id} | Template: {cluster.get_template()}")

if __name__ == "__main__":
    main()
