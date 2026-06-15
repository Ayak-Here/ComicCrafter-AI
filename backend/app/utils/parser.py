import re

from models.comic_response import ComicResponse


def parse_comic_response(
    text: str
) -> ComicResponse:

    title_match = re.search(
        r"TITLE:\s*(.*?)\s*CHARACTER:",
        text,
        re.DOTALL
    )

    title = (
        title_match.group(1).strip()
        if title_match
        else "Untitled Comic"
    )

    character_match = re.search(
        r"CHARACTER:\s*(.*?)\s*CAPTION 1:",
        text,
        re.DOTALL
    )

    character = (
        character_match.group(1).strip()
        if character_match
        else ""
    )

    caption_matches = re.findall(
        r"CAPTION\s+\d+:\s*(.*?)(?=PANEL\s+\d+:)",
        text,
        re.DOTALL
    )

    captions = [
        caption.strip()
        for caption in caption_matches
    ]

    panel_matches = re.findall(
        r"PANEL\s+\d+:\s*(.*?)(?=CAPTION\s+\d+:|$)",
        text,
        re.DOTALL
    )

    panels = [
        panel.strip()
        for panel in panel_matches
    ]

    return ComicResponse(
        title=title,
        character=character,
        captions=captions,
        panels=panels
    )