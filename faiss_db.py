import faiss
import numpy as np
import os
import pickle

index_file = "vector.index"
metadata_file = "metadata.pkl"

class LocalVectorStore:
 def init(self, dimension):
  self.dimension = dimension
  if os.path.exists(index_file) and os.path.exists(metadata_file):
   with open(metadata_file, "rb") as f:
     self.metadata = pickle.load(f)
     self.index = faiss.read_index(index_file)
  else:
     self.index = faiss.IndexFlatL2(dimension)
     self.metadata = []

def add(self, vector, meta):
    self.vectors.append(vector)
    self.metadata.append(meta)
    self.index.add(np.array([vector], dtype='float32'))

def search(self, vector, k=5):
    D, I = self.index.search(np.array([vector], dtype='float32'), k)
    return [self.metadata[i] for i in I[0] if i < len(self.metadata)]

def save(self):
    faiss.write_index(self.index, index_file)
    with open(metadata_file, "wb") as f:
        pickle.dump(self.metadata, f)