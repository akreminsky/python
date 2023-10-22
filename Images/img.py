import os

from PIL import Image, ImageDraw


def rect_drawer(image):
    draw = ImageDraw.Draw(image)
    rect = image.width / 10
    shape = (image.width / 2 - rect, image.height / 2 - rect, image.width / 2 + rect, image.height / 2 + rect)
    draw.rectangle(shape)
    draw.multiline_text((image.width / 2 - rect + 2, image.height / 2), 'Hello\nWorld')
    return image


def converter(ext_in: str, ext_out: str) -> None:
    for file in os.listdir(os.getcwd()):
        if file.endswith(ext_in):
            image = Image.open(file)
            rect_drawer(image).save(f'{os.path.splitext(file)[0]}{ext_out}')


converter(".jpeg", ".png")
