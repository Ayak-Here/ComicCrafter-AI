import os

from groq import Groq
from dotenv import load_dotenv

from .base_llm import BaseLLM


load_dotenv()


class GroqProvider(BaseLLM):

    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate_story(
    self,
    prompt: str,
    panel_count: int
    ):

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
    You are a comic storyboard generator.

    Generate:
    1. A comic title.
    2. Exactly the number of panels requested.

    Each panel should describe:
    - The scene
    - The characters
    - The action

    Make the descriptions visual and suitable for AI image generation.
    Keep character appearance consistent across panels.

    Output format:

    TITLE:
    <comic title>

    CHARACTER:
    <character description>

    CAPTION 1:
    <short caption>

    PANEL 1:
    <panel description>

    CAPTION 2:
    <short caption>

    PANEL 2:
    <panel description>

    Continue until the requested panel count.

    Rules:
    - Create one CHARACTER description.
    - The CHARACTER description must contain:
    - appearance
    - clothing
    - colors
    - distinctive features
    - Keep the same character across all panels.
    - Keep each panel visual.
    - Keep descriptions concise.
    - Maintain story continuity.
    - Do not write a full story paragraph.
    - Output only the requested number of panels.
    """
                },
                {
                    "role": "user",
                    "content": f"""
    Comic Idea:
    {prompt}

    Number of Panels:
    {panel_count}
    """
                }
            ]
        )

        return response.choices[0].message.content