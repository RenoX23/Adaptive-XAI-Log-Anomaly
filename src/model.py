import torch
import torch.nn as nn
import pandas as pd
import numpy as np

class LogLSTM(nn.Module):
    def __init__(self, vocab_size, embedding_dim=384, hidden_size=64, num_layers=2, pretrained_embeddings_path=None, vocab=None):
        """
        LSTM-based model for Next-Event Prediction (DeepLog paradigm).
        
        Args:
            vocab_size (int): Size of the vocabulary (number of unique events + special tokens).
            embedding_dim (int): Dimensionality of the event embeddings. Defaults to 384 (all-MiniLM-L6-v2 size).
            hidden_size (int): Number of features in the hidden state of the LSTM.
            num_layers (int): Number of recurrent layers.
            pretrained_embeddings_path (str, optional): Path to the saved semantic embeddings CSV.
            vocab (dict, optional): Vocabulary mapping EventId (str) to index (int). Required if loading pretrained embeddings.
        """
        super(LogLSTM, self).__init__()
        
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.hidden_size = hidden_size
        
        # 1. Embedding Layer
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        
        if pretrained_embeddings_path is not None and vocab is not None:
            self._load_pretrained_embeddings(pretrained_embeddings_path, vocab)
            
        # 2. LSTM Layer
        # batch_first=True -> Input/Output format: (batch_size, sequence_length, feature_dimension)
        self.lstm = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )
        
        # 3. Fully Connected Output Layer
        # Maps the final hidden state to the vocabulary size to predict the next event
        self.fc = nn.Linear(hidden_size, vocab_size)
        
    def _load_pretrained_embeddings(self, path, vocab):
        """
        Loads pre-trained sentence-transformer embeddings and initializes the embedding layer.
        """
        print(f"Loading pre-trained embeddings from {path}...")
        try:
            embeddings_df = pd.read_csv(path)
            # Create a weight matrix of shape (vocab_size, embedding_dim)
            weight_matrix = np.zeros((self.vocab_size, self.embedding_dim))
            
            # Populate weight matrix
            # Special tokens (<PAD>, <UNK>) will remain initialized as zeros
            events_found = 0
            for _, row in embeddings_df.iterrows():
                event_id = str(int(row['EventId'])) if pd.notna(row['EventId']) else ""
                if event_id in vocab:
                    idx = vocab[event_id]
                    # The rest of the columns are the embedding dimensions
                    vector = row.drop('EventId').values.astype(np.float32)
                    if len(vector) == self.embedding_dim:
                        weight_matrix[idx] = vector
                        events_found += 1
                        
            # Set the embedding layer weights
            self.embedding.weight = nn.Parameter(torch.tensor(weight_matrix, dtype=torch.float32))
            # NOTE: Uncomment the line below to freeze embeddings during training
            # self.embedding.weight.requires_grad = False
            
            print(f"Successfully loaded {events_found} pre-trained embeddings into the embedding layer.")
        except Exception as e:
            print(f"Failed to load pre-trained embeddings: {e}. Falling back to random initialization.")

    def forward(self, x):
        """
        Forward pass.
        
        Args:
            x (torch.Tensor): Input sequence tensor of shape (batch_size, window_size)
            
        Returns:
            logits (torch.Tensor): Output logits of shape (batch_size, vocab_size)
        """
        # x shape: (batch_size, window_size)
        out = self.embedding(x)  
        # out shape: (batch_size, window_size, embedding_dim)
        
        # Pass through LSTM
        # out: hidden states for all time steps
        # h_n, c_n: final hidden state and cell state
        out, (h_n, c_n) = self.lstm(out)
        # out shape: (batch_size, window_size, hidden_size)
        
        # Extract the hidden state of the last time step
        final_hidden_state = out[:, -1, :] 
        # final_hidden_state shape: (batch_size, hidden_size)
        
        # Compute logits for the next event
        logits = self.fc(final_hidden_state) 
        # logits shape: (batch_size, vocab_size)
        
        return logits

if __name__ == "__main__":
    # Quick sanity check
    batch_size = 32
    window_size = 10
    vocab_size = 50
    
    model = LogLSTM(vocab_size=vocab_size)
    dummy_input = torch.randint(0, vocab_size, (batch_size, window_size))
    
    logits = model(dummy_input)
    print(f"Input shape: {dummy_input.shape}")
    print(f"Logits shape: {logits.shape}")
    assert logits.shape == (batch_size, vocab_size), "Output shape mismatch!"
    print("Model forward pass successful.")
