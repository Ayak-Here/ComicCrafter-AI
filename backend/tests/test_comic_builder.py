from services.comic_builder import ComicBuilder
from models.comic_page_request import ComicPageRequest
from test_data import TITLE, CAPTIONS, IMAGE_PATHS


builder = ComicBuilder()

request = ComicPageRequest(
    title=TITLE,
    image_paths=IMAGE_PATHS,
    captions=CAPTIONS,
    layout="classic"
)

output = builder.build(request)

print("Comic page created:", output)