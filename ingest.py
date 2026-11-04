import chromadb

from loader import load_all_pdfs
from chunker import chunk_text
from sentence_transformers import SentenceTransformer

 
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("documents")
 
if __name__ == "__main__":
     docs = load_all_pdfs("docs")
     for doc in docs:
         chunks = chunk_text(doc["text"], 2000, 200)
         vectors = model.encode(chunks).tolist()
         ids = []
         metadatas =[]
         for i in range(len(chunks)):
             ids.append(doc["source"] + "'" + str(i))
             metadatas.append({"source": doc ["source"], "chunk": i})
         collection.upsert(ids=ids, documents=chunks, embeddings=vectors, metadatas=metadatas)
     print(collection.count())
    
             
             
             
 