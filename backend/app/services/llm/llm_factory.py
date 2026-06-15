from .groq_provider import GroqProvider


def get_llm_provider():
    return GroqProvider()