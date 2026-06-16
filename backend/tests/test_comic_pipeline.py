from services.story_generator import StoryGenerator
from utils.parser import parse_comic_response
from services.image_generator import ImageGenerator


story_generator = StoryGenerator()
image_generator = ImageGenerator()

story = story_generator.generate(
    "A robot discovers an abandoned city."
)

comic = parse_comic_response(story)

print("TITLE:", comic.title)

for index, panel in enumerate(comic.panels, start=1):

    print(f"Generating image for Panel {index}...")

    image = image_generator.generate(panel)

    image.save(f"panel_{index}.png")

print("Comic generation completed!")