from sentence_transformers import SentenceTransformer
import chromadb
from chromadb import PersistentClient
import faiss 
import numpy as np

# Initialize ChromaDB client and embedding model
client = PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection("my_collection")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# def get_embedding(text):
#     return embedding_model.encode(text).tolist()

# def search_chat_input(chat_input, top_k=5):
#     embedding = get_embedding(chat_input)

#     results = collection.query(
#         query_embeddings=[embedding],
#         n_results=top_k
#     )

#     # Display results
#     for i in range(len(results['ids'][0])):
#         print(f"--- Match {i+1} ---")
#         print("ID:", results['ids'][0][i])
#         print("Document:", results['documents'][0][i])
#         print("Metadata:", results['metadatas'][0][i])
#         print("Distance (approx.):", results['distances'][0][i])
#         print()

#     return results

def get_embedding(text):
    raw_embedding = embedding_model.encode(text)
    return normalize_vector(raw_embedding)

def normalize_vector(vector):
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return (vector / norm).tolist()



def search_chat_input(chat_input, top_k=5):
    embedding = get_embedding(chat_input)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )
    return results
