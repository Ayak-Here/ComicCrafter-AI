import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    provider="nscale",
    api_key=os.getenv("HF_TOKEN")
)

image = client.text_to_image(
    "A comic book style robot exploring an abandoned city",
    model="black-forest-labs/FLUX.1-schnell"
)

image.save("test_image.png")

print("Image saved successfully!")