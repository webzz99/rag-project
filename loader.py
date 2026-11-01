from pypdf import PdfReader
import os
def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text = text + page.extract_text()
    return text



def load_all_pdfs(folder):
    results = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = folder + "/" + filename
            text = load_pdf(path)
            results.append({"source": filename, "text": text})
    return results
if __name__=="__main__":
    for doc in load_all_pdfs("docs"):
        print(doc["source"], len(doc["text"]))
