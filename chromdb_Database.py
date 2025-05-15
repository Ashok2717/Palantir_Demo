import chromadb
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
import uuid

# Initialize ChromaDB client and embedding model
client = PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection("my_collection")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embedding from text
def get_embedding(text):
    return embedding_model.encode(text).tolist()

def fetch_all_records():
    print("\n All Records:")
    results = collection.get()
    for doc, meta in zip(results['documents'], results['metadatas']):
        print(f"Text: {doc}\nNamespace: {meta['namespace']}\n---")
    return results

def fetch_by_namespace(target_namespace):
    print(f"\n Records in Namespace: {target_namespace}")
    all_items = collection.get()
    for doc, meta in zip(all_items["documents"], all_items["metadatas"]):
        if meta.get("namespace") == target_namespace:
            print(f"Text: {doc}\nNamespace: {meta['namespace']}\n---")

def search_collection(query_text, n_results=5):
    print(f"\n Search Results for: '{query_text}'")
    embedding = get_embedding(query_text)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )
    if results["documents"]:
     for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
       print(f"Text: {doc}\nNamespace: {meta['namespace']}\n---")
    else:
     print("No matching results found.")



def delete_by_namespace(target_namespace):
    print(f"\n Deleting records in Namespace: {target_namespace}")
    all_items = collection.get()
    ids_to_delete = [
        item_id for item_id, meta in zip(all_items["ids"], all_items["metadatas"])
        if meta.get("namespace") == target_namespace
    ]

    if not ids_to_delete:
        print("No records found in that namespace.")
        return

    collection.delete(ids=ids_to_delete)
    print(f"Deleted {len(ids_to_delete)} records from '{target_namespace}'")



# Example Usage
if __name__ == "__main__":

    # Get all records
    fetch_all_records()

    # # Fetch by namespace
    # fetch_by_namespace("story-greenlake")

    # # Search
    # search_collection("biking around Green Lake")

    # # Delete by namespace
    # delete_by_namespace("story-attic-adventure-2")
