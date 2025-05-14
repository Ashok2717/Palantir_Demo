import faiss
import uuid
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb

# Load model and initialize FAISS index with ID mapping
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

dimension = 384
index = faiss.IndexFlatL2(dimension)
index_with_ids = faiss.IndexIDMap(index)

# Dictionary to store metadata
id_to_metadata = {}

def get_embedding(text):
    return embedding_model.encode(text).astype('float32')
   

def ingest_stories_to_local_db(stories):
    embeddings = []
    ids = []

    for story in stories:
        vector_id = str(uuid.uuid4())
        embedding = get_embedding(story['text'])

        metadata = {
            "id": vector_id,
            "blobType": "application/json",
            "loc.lines.from": 1,
            "loc.lines.to": 9,
            "source": "blob",
            "text": story['text'],
            "namespace": story['namespace']
        }

        # Store metadata externally (you can also save this to disk)
        id_to_metadata[vector_id] = metadata

        # Store embedding and numeric ID (convert UUID to int64)
        embeddings.append(embedding)
        ids.append(int(uuid.UUID(vector_id).int & (2**63 - 1)))

        print(f"✅ Ingested: {vector_id}")

    # Convert to numpy arrays
    embeddings_np = np.vstack(embeddings).astype('float32')
    ids_np = np.array(ids, dtype='int64')

    print("embeddings_np::",embeddings_np)
    print("ids_np::")
    # Add to FAISS
    index_with_ids.add_with_ids(embeddings_np, ids_np)


print("index_with_ids::",index_with_ids)





# client = chromadb.Client()
# collection = client.create_collection("my_collection")

# def get_embedding(text):
#     return embedding_model.encode(text).tolist()

# def ingest_stories_to_local_db(stories):

#     for story in stories:
#         vector_id = str(uuid.uuid4())
#         embedding = get_embedding(story['text'])
#         namespace = story["namespace"]

#         metadata = {
#             "blobType": "application/json",
#             "loc.lines.from": 1,
#             "loc.lines.to": 9,
#             "source": "blob",
#             "text": story['text'],
#             "namespace":namespace
#         }

#         print("metadata::",metadata)
#         print("namespace::",namespace)
#         # print("embedding::",embedding)

#         # collection.add( 
#         # vectors=[{
#         #     "id": vector_id,
#         #     "values": embedding,
#         #     "metadata": metadata
#         #  }],
#         #  namespace=namespace
#         # )

#         collection.add(
#          ids=[vector_id],
#         #  namespace=[namespace],
#          metadatas=[metadata],
#          embeddings=[embedding],
#          documents=[story['text']]
#         )

#         print(f"✅ Ingested: {vector_id}")



