from pydantic import BaseModel


class ComicResponse(BaseModel):
    title: str
    character: str
    captions: list[str]
    panels: list[str]