from abc import ABC, abstractmethod


class BaseImageProvider(ABC):

    @abstractmethod
    def generate_image(self, prompt: str):
        pass