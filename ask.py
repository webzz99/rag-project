import sys
from answer import answer

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python ask.py "your question"')
    else:
        question = sys.argv[1]
        print(answer(question))
        