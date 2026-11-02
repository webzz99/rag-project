from sentence_transformers import SentenceTransformer
from chunker import chunk_text
from loader import load_pdf

model = SentenceTransformer("all-MiniLM-L6-v2")

if __name__ == "__main__":
    text = load_pdf("docs/ai-regulation.pdf")
    chunks = chunk_text(text, 2000, 200)
    vectors = model.encode(chunks)
    print(vectors.shape)