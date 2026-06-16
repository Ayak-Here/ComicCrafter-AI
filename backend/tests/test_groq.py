from services.story_generator import StoryGenerator
from utils.parser import parse_comic_response


generator = StoryGenerator()

response = generator.generate(
    "A robot discovers an abandoned city.",
    panel_count=6
)

comic = parse_comic_response(response)

print("\nTITLE:")
print(comic.title)

print("\nTOTAL PANELS:")
print(len(comic.panels))

for index, panel in enumerate(comic.panels, start=1):
    print(f"\nPANEL {index}:")
    print(panel)