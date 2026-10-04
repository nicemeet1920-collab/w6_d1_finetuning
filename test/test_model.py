from app.model import load_model
from app.knowledge import load_knowledge, find_relevant_examples


# Load customer support knowledge
dataset = load_knowledge()

# Load language model
assistant = load_model()


# User question
question = "Can I return my product?"


# Find relevant examples
results = find_relevant_examples(
    dataset,
    question,
    top_k=3
)


print("\n==============================")
print("RETRIEVED KNOWLEDGE")
print("==============================")

for score, user_text, answer in results:
    print(f"\nScore: {score}")
    print(f"Question: {user_text}")
    print(f"Answer: {answer}")


# Build context for the model
context = "\n".join(
    [
        f"Customer Question: {user_text}\n"
        f"Support Answer: {answer}"
        for score, user_text, answer in results
    ]
)


messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful customer support assistant. "
            "Answer the customer's question using the provided "
            "customer support knowledge. "
            "Do not invent policies. "
            "If the knowledge does not contain the answer, "
            "say that you do not have enough information."
        )
    },
    {
        "role": "user",
        "content": (
            f"Customer support knowledge:\n\n"
            f"{context}\n\n"
            f"Customer question: {question}\n\n"
            f"Give a short and helpful answer."
        )
    }
]


# Generate response
result = assistant(
    messages,
    max_new_tokens=80
)


print("\n==============================")
print("FINAL MODEL RESPONSE")
print("==============================")

print(result)