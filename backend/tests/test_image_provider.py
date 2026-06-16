from services.image.image_factory import get_image_provider


provider = get_image_provider()

image = provider.generate_image(
    "A comic book style robot exploring an abandoned city"
)

image.save("provider_test.png")

print("Provider image generated successfully!")