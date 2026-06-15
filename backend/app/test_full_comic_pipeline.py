from services.story_generator import StoryGenerator
from services.image_generator import ImageGenerator
from services.comic_builder import ComicBuilder

from utils.parser import parse_comic_response
from models.comic_page_request import ComicPageRequest


story_generator = StoryGenerator()
image_generator = ImageGenerator()
comic_builder = ComicBuilder()


story = story_generator.generate(
    "An alien visits an abandoned city",
    4
)

comic = parse_comic_response(story)

image_paths = []

for index, panel in enumerate(comic.panels):

    image = image_generator.generate(panel)

    image_path = f"panel_{index + 1}.png"

    image.save(image_path)

    image_paths.append(image_path)


request = ComicPageRequest(
    title=comic.title,
    image_paths=image_paths,
    captions=[
        f"Panel {i+1}"
        for i in range(len(comic.panels))
    ],
    layout="classic"
)

output = comic_builder.build(
    request,
    "generated/comic_page.png"
)

print(output)