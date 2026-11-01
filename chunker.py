def chunk_text(text, chunk_size, overlap):

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

print(chunk_text("abcdefghijklmnopqrstuvwxyz", 10, 3))
    
    