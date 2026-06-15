from PIL import Image, ImageDraw, ImageFont
import uuid
from models.comic_page_request import ComicPageRequest
from utils.layouts import LAYOUTS


class ComicBuilder:

    def build(
        self,
        request: ComicPageRequest,
    ):

        image_width = 1024
        image_height = 1024

        captions_height = 120
        title_height = 120

        panel_count = len(request.image_paths)

        rows, cols = LAYOUTS[
            request.layout
        ][panel_count]

        canvas_width = cols * image_width
        canvas_height = (
            rows * (image_height + captions_height)
            + title_height
        )

        canvas = Image.new(
            "RGB",
            (canvas_width, canvas_height),
            "white"
        )

        draw = ImageDraw.Draw(canvas)

        try:
            title_font = ImageFont.truetype(
                "arial.ttf",
                50
            )

            caption_font = ImageFont.truetype(
                "arial.ttf",
                28
            )

        except Exception:
            title_font = ImageFont.load_default()
            caption_font = ImageFont.load_default()

        title_bbox = draw.textbbox(
            (0, 0),
            request.title,
            font=title_font
        )

        title_width = (
            title_bbox[2]
            - title_bbox[0]
        )

        draw.text(
            (
                (canvas_width - title_width) // 2,
                30
            ),
            request.title,
            fill="black",
            font=title_font
        )

        y_offset = title_height

        for index, image_path in enumerate(
            request.image_paths
        ):

            row = index // cols
            col = index % cols

            x = col * image_width

            y = (
                y_offset
                + row * (
                    image_height
                    + captions_height
                )
            )

            image = Image.open(image_path)

            canvas.paste(
                image,
                (x, y)
            )

            draw.rectangle(
                [
                    x,
                    y,
                    x + image_width,
                    y + image_height
                ],
                outline="black",
                width=4
            )

            caption = request.captions[index]

            draw.text(
                (
                    x + 20,
                    y + image_height + 20
                ),
                caption,
                fill="black",
                font=caption_font
            )

        filename = f"{uuid.uuid4().hex}.png"

        output_path = (
            f"generated/{filename}"
        )

        canvas.save(output_path)

        return output_path