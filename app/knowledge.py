from datasets import load_dataset


DATASET_PATH = "data/customer_support.jsonl"


def load_knowledge():

    return load_dataset(
        "json",
        data_files=DATASET_PATH,
        split="train"
    )


def find_relevant_examples(dataset, question, top_k=3):

    question_words = set(
        question.lower().split()
    )

    scored_examples = []

    for item in dataset:

        user_text = item["messages"][0]["content"]

        user_words = set(
            user_text.lower().split()
        )

        score = len(
            question_words.intersection(user_words)
        )

        scored_examples.append(
            (score, user_text, item["messages"][1]["content"])
        )

    scored_examples.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return scored_examples[:top_k]