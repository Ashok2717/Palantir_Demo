import faiss
import uuid
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb import PersistentClient

# Load model and initialize FAISS index with ID mapping
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

client = PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection("my_collection")

# def get_embedding(text):
#     return embedding_model.encode(text).tolist()

def get_embedding(text):
    raw_embedding = embedding_model.encode(text)
    return normalize_vector(raw_embedding)

def normalize_vector(vector):
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return (vector / norm).tolist()

def ingest_stories_to_local_db(stories):

    for story in stories:
        vector_id = str(uuid.uuid4())
        embedding = get_embedding(story['text'])
        namespace = story["namespace"]

        metadata = {
            "blobType": "application/json",
            "loc.lines.from": 1,
            "loc.lines.to": 9,
            "source": "blob",
            "text": story['text'],
            "namespace":namespace
        }

        print("metadata::",metadata)
        print("namespace::",namespace)
        print("embedding::",embedding)

        try:
           collection.add(
            ids=[vector_id],
            metadatas=[metadata],
            embeddings=[embedding],
            documents=[story['text']]
        )
           print(f"Ingested: {vector_id}")
        except Exception as e:
           print(f"Failed to ingest: {e}")


