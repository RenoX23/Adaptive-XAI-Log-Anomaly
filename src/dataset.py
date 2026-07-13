import os
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd

class LogSequenceDataset(Dataset):
    def __init__(self, sequences_csv, window_size=10, is_train=True, train_ratio=0.8, seed=42, vocab=None):
        """
        PyTorch Dataset for Log Sequences.
        
        Args:
            sequences_csv (str): Path to the sequences CSV file.
            window_size (int): Fixed length for padding/truncating sequences.
            is_train (bool): If True, returns only Normal sequences for training.
                             If False, returns test split containing Normal and Anomaly sequences.
            train_ratio (float): Proportion of normal data to use for training.
            seed (int): Random seed for reproducible splitting.
            vocab (dict, optional): Mapping from EventId (str) to int index. 
        """
        self.window_size = window_size
        self.is_train = is_train
        
        df = pd.read_csv(sequences_csv)
        
        # Parse space-separated EventId string into list of strings
        df['EventIdList'] = df['EventId'].apply(lambda x: str(x).split() if pd.notna(x) else [])
        
        # Split into Normal and Anomaly
        normal_df = df[df['Label'] == 'Normal'].copy()
        anomaly_df = df[df['Label'] == 'Anomaly'].copy()
        
        # Shuffle normal data
        normal_df = normal_df.sample(frac=1, random_state=seed).reset_index(drop=True)
        
        train_size = int(len(normal_df) * train_ratio)
        
        if is_train:
            # Train purely on normal data
            self.data = normal_df.iloc[:train_size].reset_index(drop=True)
        else:
            # Test on the remaining normal data and ALL anomaly data
            test_normal = normal_df.iloc[train_size:]
            self.data = pd.concat([test_normal, anomaly_df]).sample(frac=1, random_state=seed).reset_index(drop=True)
            
        # Build vocabulary from the train set if not provided
        if vocab is None:
            all_events = set()
            for seq in normal_df.iloc[:train_size]['EventIdList']:
                all_events.update(seq)
            # 0: PAD, 1: UNK
            self.vocab = {event: idx + 2 for idx, event in enumerate(sorted(all_events))}
            self.vocab['<PAD>'] = 0
            self.vocab['<UNK>'] = 1
        else:
            self.vocab = vocab
            
        self.sequences = self.data['EventIdList'].tolist()
        # Label: 0 for Normal, 1 for Anomaly
        self.labels = self.data['Label'].apply(lambda x: 0 if x == 'Normal' else 1).tolist()
        
    def __len__(self):
        return len(self.sequences)
        
    def __getitem__(self, idx):
        seq = self.sequences[idx]
        label = self.labels[idx]
        
        # Map EventIds to integer indices
        indexed_seq = [self.vocab.get(event, self.vocab['<UNK>']) for event in seq]
        
        # Truncate or Pad to fixed window_size
        if len(indexed_seq) > self.window_size:
            indexed_seq = indexed_seq[:self.window_size]
        else:
            indexed_seq = indexed_seq + [self.vocab['<PAD>']] * (self.window_size - len(indexed_seq))
            
        return torch.tensor(indexed_seq, dtype=torch.long), torch.tensor(label, dtype=torch.float)
    
    def get_vocab(self):
        return self.vocab


def get_dataloaders(sequences_csv, window_size=10, batch_size=32, train_ratio=0.8, seed=42):
    """
    Creates train and test dataloaders ensuring the test set shares the train set's vocabulary.
    """
    train_dataset = LogSequenceDataset(sequences_csv, window_size, is_train=True, train_ratio=train_ratio, seed=seed)
    vocab = train_dataset.get_vocab()
    
    test_dataset = LogSequenceDataset(sequences_csv, window_size, is_train=False, train_ratio=train_ratio, seed=seed, vocab=vocab)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader, vocab

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--seq_file", type=str, default="data/HDFS_2k_sequences.csv")
    args = parser.parse_args()
    
    if os.path.exists(args.seq_file):
        train_dl, test_dl, vocab = get_dataloaders(args.seq_file)
        print(f"Vocab size: {len(vocab)}")
        print(f"Train batches: {len(train_dl)} | Test batches: {len(test_dl)}")
        
        for batch_seq, batch_label in train_dl:
            print(f"Sample train sequence shape: {batch_seq.shape}")
            print(f"Sample train labels shape: {batch_label.shape}")
            break
    else:
        print(f"Sequence file {args.seq_file} not found.")
