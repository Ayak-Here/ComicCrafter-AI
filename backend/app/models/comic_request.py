from pydantic import BaseModel


class ComicRequest(BaseModel):
    prompt: str
    panel_count: int = 4
    layout: str = "classic"