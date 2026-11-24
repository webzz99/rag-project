import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("documents")


def retrieve(question, n_results):
    vector = model.encode(question).tolist()
    results = collection.query(query_embeddings=[vector], n_results=n_results)
    return results

if __name__ == "__main__":
    found = retrieve("What principles underpin the regulatory framework for AI?", 4)
    for i in range(len(found["documents"][0])):
        print(found["metadatas"][0][i]["source"], found["metadatas"][0][i]["chunk"])
        print(found["documents"][0][i][:800])
    
    