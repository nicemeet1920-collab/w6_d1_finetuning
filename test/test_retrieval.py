from app.knowledge import load_knowledge, find_relevant_examples


dataset = load_knowledge()


test_questions = [
    "How long will my order take?",
    "I want to return my item",
    "Can I cancel my order before shipping?",
    "Where can I track my order?",
    "My product arrived damaged",
    "Do you have cash on delivery?",
    "How do I contact support?",
    "When will I get my refund?",
]


print("\n==============================")
print("RETRIEVAL TEST")
print("==============================")


for question in test_questions:

    results = find_relevant_examples(
        dataset,
        question,
        top_k=1
    )

    score, matched_question, answer = results[0]

    print("\nUser Question:")
    print(question)

    print("\nMatched Question:")
    print(matched_question)

    print("\nScore:")
    print(score)

    print("\nRetrieved Answer:")
    print(answer)

    print("------------------------------")