from pydantic import BaseModel


class StoryRequest(BaseModel):
    prompt: str
    panel_count: int = 4
    style: str = "Comic"