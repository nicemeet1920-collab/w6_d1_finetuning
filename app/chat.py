from app.model import load_model
from app.knowledge import load_knowledge, find_relevant_examples


assistant = load_model()

dataset = load_knowledge()


SYSTEM_PROMPT = """
You are QuickCart Customer Support AI.

Your job is to answer customer questions clearly,
politely and honestly.

Rules:

1. Use the provided support information.
2. Do not invent company policies.
3. Do not make up prices, dates or order information.
4. Keep the answer short and useful.
5. If the information is not available, say that you
   do not have enough information.
6. Never pretend that you checked an order.
7. Ask for an order number only when it is needed.
8. Use simple English.
"""


def generate_reply(question):

    examples = find_relevant_examples(
        dataset,
        question,
        top_k=3
    )

    context = ""

    for score, user_question, answer in examples:

        if score > 0:

            context += f"""
Example Question:
{user_question}

Example Answer:
{answer}

"""


    prompt = f"""
{SYSTEM_PROMPT}

Relevant support information:

{context}

Customer question:

{question}

Write the best customer support reply.
"""


    result = assistant(
        prompt,
        max_new_tokens=100,
        do_sample=False
    )

    return result[0]["generated_text"]