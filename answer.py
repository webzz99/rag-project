import anthropic
from dotenv import load_dotenv
from query import retrieve

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-sonnet-5-5"

def answer(question):
  found = retrieve(question, 10)
  context = ""
  for i in range(len(found["documents"][0])):
    source = found["metadatas"][0][i]["source"]
    chunk_number = found["metadatas"][0][i]["chunk"]
    text = found["documents"][0][i]
    context += "[" + source + " chunk " + str(chunk_number) + "]\n" + text + "\n\n"

  system_prompt = "Answer the question using only the context provided. After each claim, cite its source in square brackets, like [ai-regulation.pdf chunk 30]. If the context does not contain the answer, reply exactly: Not found in the documents."
  user_message = "Context:\n" + context + "\nQuestion: " + question
  response = client.messages.create(model=MODEL, max_tokens=500, system=system_prompt, messages=[{"role": "user", "content": user_message}])
  for block in response.content:
      if block.type == "text":
          return block.text
if __name__ == "__main__":
    print(answer("What are the four key elements of the UK government's AI regulatory framework?"))