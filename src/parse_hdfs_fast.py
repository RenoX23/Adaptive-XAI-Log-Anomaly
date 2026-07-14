import os
import re
import time
import pandas as pd

def get_event_id(msg):
    if "Receiving block" in msg and "src:" in msg and "dest:" in msg: return 1
    if "BLOCK* NameSystem.allocateBlock:" in msg: return 2
    if "PacketResponder" in msg and "terminating" in msg: return 3
    if "Received block" in msg and "of size" in msg and "from" in msg: return 4
    if "BLOCK* NameSystem.addStoredBlock:" in msg: return 5
    if "Received block" in msg and "src:" in msg and "dest:" in msg and "of size" in msg: return 6
    if "Transmitted block" in msg: return 7
    if "Starting thread to transfer block" in msg: return 8
    if "Served block" in msg: return 9
    if "NameSystem: BLOCK* ask" in msg and "to replicate" in msg: return 10
    if "Verification succeeded" in msg: return 14
    if "Exception java.net.SocketTimeoutException" in msg: return 15
    if "PacketResponder" in msg and "Exception java.io.EOFException" in msg: return 16
    if "received exception java.io.IOException: Could not read from stream" in msg: return 17
    if "Deleting block" in msg: return 18
    if "Receiving empty packet" in msg: return 19
    if "Exception in receiveBlock" in msg and "Connection reset by peer" in msg: return 20
    if "writeBlock" in msg and "Connection reset by peer" in msg: return 21
    if "Redundant addStoredBlock request received" in msg: return 22
    if "PacketResponder" in msg and "Exception java.net.SocketTimeoutException" in msg: return 23
    if "Interruped while waiting for IO" in msg: return 24
    if "Exception in receiveBlock" in msg and "java.io.EOFException" in msg: return 25
    if "Changing block file offset" in msg: return 26
    if "Exception writing block" in msg and "to mirror" in msg: return 27
    if "Exception in receiveBlock" in msg and "Interruped while waiting for IO" in msg: return 28
    if "PacketResponder" in msg and "Exception java.io.IOException: Broken pipe" in msg: return 29
    if "is valid, and cannot be written to" in msg: return 30
    if "Failed to transfer" in msg and "Connection reset by peer" in msg: return 31
    if "NameSystem.delete:" in msg and "is added to invalidSet" in msg: return 32
    if "Unexpected error trying to delete block" in msg: return 33
    if "addStoredBlock request received" in msg and "But it does not belong to any file" in msg: return 34
    if "Got exception while serving" in msg: return 35
    return 1 # default

def parse_hdfs_fast():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hdfs_log = os.path.join(base_dir, 'data', 'HDFS.log')
    anomaly_csv = os.path.join(base_dir, 'data', 'HDFS_500k_anomaly_label.csv')
    
    labels = pd.read_csv(anomaly_csv)
    normal_blks = set(labels[labels['Label'] == 'Normal']['BlockId'].head(5000))
    anomaly_blks = set(labels[labels['Label'] == 'Anomaly']['BlockId'].head(5000))
    target_blks = normal_blks.union(anomaly_blks)
    
    block_events = {b: [] for b in target_blks}
    
    start = time.time()
    with open(hdfs_log, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            blk_match = re.search(r'(blk_-?\d+)', line)
            if not blk_match:
                continue
            blk = blk_match.group(1)
            if blk in target_blks:
                msg = " ".join(line.split()[5:])
                eid = get_event_id(msg)
                block_events[blk].append(eid)
                
            if i > 0 and i % 1000000 == 0:
                print(f"Processed {i} lines in {time.time() - start:.2f}s")
                
    out_data = []
    for blk, events in block_events.items():
        if len(events) > 0:
            label = 'Anomaly' if blk in anomaly_blks else 'Normal'
            out_data.append({'BlockId': blk, 'Label': label, 'EventId': ' '.join(map(str, events))})
            
    out_df = pd.DataFrame(out_data)
    out_csv = os.path.join(base_dir, 'data', 'HDFS_10k_full_sequences.csv')
    out_df.to_csv(out_csv, index=False)
    print(f"Done! Saved {len(out_df)} intact sequences to {out_csv}")

if __name__ == '__main__':
    parse_hdfs_fast()
