from loader import load_pdf
def chunk_text(text, chunk_size, overlap):

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

if __name__ == "__main__":
    text = load_pdf("docs/ai-regulation.pdf")
    chunks = chunk_text(text, 2000, 200)
    print(len(chunks))
    print(chunks[10])