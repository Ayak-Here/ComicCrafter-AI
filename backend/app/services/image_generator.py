from services.image.image_factory import get_image_provider


class ImageGenerator:

    def __init__(self):
        self.provider = get_image_provider()

    def generate(
        self,
        prompt: str,
        style: str = "Comic"
    ):
        return self.provider.generate_image(
            prompt,
            style
        )