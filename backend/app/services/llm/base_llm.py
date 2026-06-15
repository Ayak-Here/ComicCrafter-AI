from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def generate_story(
        self,
        prompt: str,
        panel_count: int
    ):
        pass