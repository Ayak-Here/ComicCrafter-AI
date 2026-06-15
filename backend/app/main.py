import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from models.story_request import StoryRequest
from services.story_generator import StoryGenerator
from utils.parser import parse_comic_response
from services.image_generator import ImageGenerator
from services.comic_builder import ComicBuilder
import uuid
from utils.file_cleanup import (
    cleanup_generated_files
)
from models.comic_page_request import ComicPageRequest

app = FastAPI(
    title="ComicCrafter API",
    version="1.0.0"
)

os.makedirs(
    "generated",
    exist_ok=True
)

app.mount(
    "/generated",
    StaticFiles(directory="generated"),
    name="generated"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
        "https://comic-crafter-eight.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "ComicCrafter API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/generate-story")
def generate_story(request: StoryRequest):

    generator = StoryGenerator()

    story = generator.generate(
        request.prompt,
        request.panel_count
    )

    comic = parse_comic_response(story)

    return {
        "title": comic.title,
        "character": comic.character,
        "captions": comic.captions,
        "panels": comic.panels
    }


@app.post("/generate-comic")
def generate_comic(request: StoryRequest):

    cleanup_generated_files()

    story_generator = StoryGenerator()
    image_generator = ImageGenerator()
    comic_builder = ComicBuilder()

    story = story_generator.generate(
        request.prompt,
        request.panel_count
    )

    comic = parse_comic_response(story)

    image_paths = []

    for index, panel in enumerate(
        comic.panels,
        start=1
    ):

        image_prompt = f"""
    MAIN CHARACTER:
    {comic.character}

    SCENE:
    {panel}
    """

        try:
            image = image_generator.generate(
                image_prompt,
                request.style
            )
        except Exception as e:
            return {
                "error": str(e)
            }

        image_path = (
            f"generated/{uuid.uuid4().hex}.png"
        )

        image.save(image_path)

        image_paths.append(
            image_path
        )

    comic_request = ComicPageRequest(
        title=comic.title,
        image_paths=image_paths,
        captions=comic.captions,
        layout="classic"
    )

    comic_path = comic_builder.build(
        comic_request
    )

    BASE_URL = os.getenv(
        "BASE_URL",
        "http://127.0.0.1:8000"
    )

    return {
        "title": comic.title,
        "comic_url":
            f"{BASE_URL}/{comic_path}"
    }