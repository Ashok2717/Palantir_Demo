from sentence_transformers import SentenceTransformer
import chromadb
import faiss 

dimension = 384
vector_store = faiss.IndexFlatL2(dimension)


embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return embedding_model.encode(text).astype('float32')


def search_chat_input(chat_input, top_k=5):
    embedding = get_embedding(chat_input).reshape(1, -1)
    return vector_store.search(embedding, top_k)


# client = chromadb.Client()
# collection = client.get_or_create_collection("my_collection")

# def get_embedding(text):
#     return embedding_model.encode(text).tolist()


# def search_chat_input(chat_input, top_k=5):
#     embedding = get_embedding(chat_input)

#     results = collection.query(
#         query_embeddings=[embedding],
#         n_results=top_k
#     )

#     for i in range(len(results['ids'][0])):
#         print(f"--- Match {i+1} ---")
#         print("ID:", results['ids'][0][i])
#         print("Document:", results['documents'][0][i])
#         print("Metadata:", results['metadatas'][0][i])
#         print("Distance (approx.):", results['distances'][0][i])
#         print()

#     return results
