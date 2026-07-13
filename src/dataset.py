import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np

class LogSequenceDataset(Dataset):
    def __init__(self, sequences_csv, window_size=10, is_train=True, train_ratio=0.8, seed=42, vocab=None):
        self.window_size = window_size
        self.is_train = is_train
        
        df = pd.read_csv(sequences_csv)
        df['EventIdList'] = df['EventId'].apply(lambda x: str(x).split() if pd.notna(x) else [])
        
        normal_df = df[df['Label'] == 'Normal'].copy()
        anomaly_df = df[df['Label'] == 'Anomaly'].copy()
        
        normal_df = normal_df.sample(frac=1, random_state=seed).reset_index(drop=True)
        train_size = int(len(normal_df) * train_ratio)
        
        if is_train:
            self.data = normal_df.iloc[:train_size].reset_index(drop=True)
        else:
            test_normal = normal_df.iloc[train_size:]
            self.data = pd.concat([test_normal, anomaly_df]).sample(frac=1, random_state=seed).reset_index(drop=True)
            
        if vocab is None:
            all_events = set()
            for seq in normal_df.iloc[:train_size]['EventIdList']:
                all_events.update(seq)
            self.vocab = {event: idx + 2 for idx, event in enumerate(sorted(all_events))}
            self.vocab['<PAD>'] = 0
            self.vocab['<UNK>'] = 1
        else:
            self.vocab = vocab
            
        self.sequences = self.data['EventIdList'].tolist()
        self.labels = self.data['Label'].apply(lambda x: 0 if x == 'Normal' else 1).tolist()
        
        self.samples = []
        if self.is_train:
            # Flatten into sliding windows for Next-Event Prediction
            for seq in self.sequences:
                indexed_seq = [self.vocab.get(event, self.vocab['<UNK>']) for event in seq]
                # Unconditionally pad sequence to extract sliding windows for every event
                indexed_seq = [self.vocab['<PAD>']] * self.window_size + indexed_seq
                    
                for i in range(len(indexed_seq) - self.window_size):
                    window = indexed_seq[i:i + self.window_size]
                    target = indexed_seq[i + self.window_size]
                    self.samples.append((window, target))
        else:
            # Keep entire sequences for Block-Level Evaluation
            for idx, seq in enumerate(self.sequences):
                indexed_seq = [self.vocab.get(event, self.vocab['<UNK>']) for event in seq]
                # Unconditionally pad sequence to evaluate every event
                indexed_seq = [self.vocab['<PAD>']] * self.window_size + indexed_seq
                self.samples.append((indexed_seq, self.labels[idx]))
                
    def __len__(self):
        return len(self.samples)
        
    def __getitem__(self, idx):
        if self.is_train:
            window, target = self.samples[idx]
            return torch.tensor(window, dtype=torch.long), torch.tensor(target, dtype=torch.long)
        else:
            seq, label = self.samples[idx]
            return torch.tensor(seq, dtype=torch.long), torch.tensor(label, dtype=torch.long)
    
    def get_vocab(self):
        return self.vocab

def get_dataloaders(sequences_csv, window_size=10, batch_size=32, train_ratio=0.8, seed=42):
    train_dataset = LogSequenceDataset(sequences_csv, window_size, is_train=True, train_ratio=train_ratio, seed=seed)
    vocab = train_dataset.get_vocab()
    
    test_dataset = LogSequenceDataset(sequences_csv, window_size, is_train=False, train_ratio=train_ratio, seed=seed, vocab=vocab)
    
    # Train uses standard batch_size to batch sliding windows efficiently
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    # Test uses batch_size=1 to handle variable length sequences cleanly
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)
    
    return train_loader, test_loader, vocab
