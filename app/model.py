from transformers import pipeline


MODEL_NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"


def load_model():

    assistant = pipeline(
        "text-generation",
        model=MODEL_NAME
    )

    assistant.model.generation_config.max_length = None

    return assistant