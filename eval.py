from query import retrieve

TESTS = [
    {"question": "What are the five principles that underpin the UK AI regulation framework?", "phrase": "Contestability and redress"},
    {"question": "Will the principles be put on a statutory footing initially?", "phrase": "statutory footing"},
    {"question": "What are the four key elements of the framework?", "phrase": "4 key elements"},
    {"question": "What statutory duty does the government anticipate introducing for regulators?", "phrase": "due regard to the principles"},
    {"question": "How much is the AI sector estimated to contribute to the UK economy in GVA?", "phrase": "3.7 billion"},
    {"question": "What does consultation question 18 ask about regulators and government?", "phrase": "best placed to apply the principles"},
    {"question": "What do the principles say about governance across the AI life cycle?", "phrase": "good governance at all stages of the AI life cycle"},
    {"question": "What will the central monitoring and evaluation function do?", "phrase": "central M&E function"},
    {"question": "Which tools could help organisations embed the principles into business processes?", "phrase": "non-regulatory tools for trustworthy AI"},
    {"question": "How does the framework propose to define AI?", "phrase": "Defining AI based on its unique characteristics"},
    {"question": "How many legal frameworks indirectly control the development and use of AI?", "phrase": "at least 18 legal frameworks"},
    {"question": "Who should lead the AI risk management team?", "phrase": "AI governance officer"},
    {"question": "How does the AI risk toolkit define a risk?", "phrase": "potential future event that affects your objectives"},
    {"question": "What does GDS encourage departments to keep and share about AI risks?", "phrase": "central log of AI risks"},
    {"question": "How is the risk score calculated from likelihood and impact?", "phrase": "product of the likelihood and impact scores"},
]


def normalise(text):
    return " ".join(text.lower().split())


def run_eval(k):
    hits = 0
    for test in TESTS:
        found = retrieve(test["question"], k)
        chunks = found["documents"][0]
        hit = False
        for chunk in chunks:
            if normalise(test["phrase"]) in normalise(chunk):
                hit = True
        if hit:
            hits = hits + 1
            print("HIT ", test["question"])
        else:
            print("MISS", test["question"])
    print(hits, "out of", len(TESTS), "at k =", k)


if __name__ == "__main__":
    run_eval(4)
    run_eval(10)