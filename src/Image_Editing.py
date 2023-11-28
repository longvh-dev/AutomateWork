# Image Resizing and Cropping
def resize_image(input_path, output_path, width, height):
    from PIL import Image

    image = Image.open(input_path)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(output_path)


def crop_image(input_path, output_path, left, top, right, bottom):
    from PIL import Image

    image = Image.open(input_path)
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)


# Adding Watermark to Image
def add_watermark(input_path, output_path, watermark_text):
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont

    image = Image.open(input_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 36)
    draw.text((10, 10), watermark_text, fill = (255, 255, 255, 128), font = font)

    image.save(output_path)


# Create Image Thumbnails

def create_thumbnail(input_path, output_path, size=(128, 128)):
    from PIL import Image
    image = Image.open(input_path)
    image.thumbnail(size)
    image.save(output_path)
