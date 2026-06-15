import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from .base_image_provider import BaseImageProvider
from utils.constants import HF_IMAGE_MODEL


load_dotenv()


class HFProvider(BaseImageProvider):

    def __init__(self):
        self.client = InferenceClient(
            provider="nscale",
            api_key=os.getenv("HF_TOKEN")
        )

    def generate_image(
        self,
        prompt: str,
        style: str = "Comic"
    ):

        if style == "Manga":

            style_prompt = """
            manga style,
            black and white,
            Japanese manga artwork,
            detailed ink drawing,
            expressive characters,
            speed lines,
            professional manga panel
            """

        elif style == "Webtoon":

            style_prompt = """
            webtoon style,
            vibrant colors,
            Korean webtoon artwork,
            digital painting,
            clean lineart,
            highly detailed,
            vertical comic style
            """

        else:

            style_prompt = """
            comic book style,
            graphic novel illustration,
            consistent character design,
            professional comic panel,
            highly detailed artwork,
            cinematic lighting,
            vibrant colors,
            storytelling composition
            """

        enhanced_prompt = f"""
        {style_prompt}

        {prompt}
        """

        image = self.client.text_to_image(
            enhanced_prompt,
            model=HF_IMAGE_MODEL
        )

        return image