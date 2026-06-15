from dataclasses import dataclass


@dataclass
class ComicPageRequest:
    title: str
    image_paths: list[str]
    captions: list[str]
    layout: str = "classic"