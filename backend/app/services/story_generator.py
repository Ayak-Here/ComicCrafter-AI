from services.llm.llm_factory import get_llm_provider


class StoryGenerator:

    def __init__(self):
        self.llm = get_llm_provider()

    def generate(
        self,
        prompt: str,
        panel_count: int = 4
    ):
        return self.llm.generate_story(
            prompt,
            panel_count
        )