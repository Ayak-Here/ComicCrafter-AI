from .hf_provider import HFProvider


def get_image_provider():
    return HFProvider()