from PIL import Image
import click
from datetime import datetime


@click.command()
@click.option("-path", default='', help='image path')
@click.option("-w", default=200, help='width new image')
@click.option("-h", default=200, help='high new image')
def resize(path, w, h):
    """Resize image """
    now = datetime.now()

    if path != '':
        image = Image.open(path)
        # The file format of the source file.
        print(image.format)
        # The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
        print(image.mode)
        # Image size, in pixels. The size is given as a 2-tuple (width, height).
        print(image.size)
        # Colour palette table, if any.
        print(image.palette)

        new_image = image.resize((w, h))
        dt_string = now.strftime("%d%m%Y%H%M%S")
        new_name = f'{dt_string}_{w}_{h}.{image.format}'
        new_image.save(f'output/{new_name}')

        print('>>>>>>> new image <<<<<<<<')
        print(image.size)
        print(new_image.size)


@click.command()
@click.option("-path", default='', help='image path')
def tspncy(path):
    """Transparency image """

    now = datetime.now()
    img = Image.open(path)
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_data.append((255, 255, 255, 0))
        else:
            if item[0] > 150:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

    img.putdata(new_data)
    dt_string = now.strftime("%d%m%Y%H%M%S")
    new_name = f'{dt_string}_transparency.png'
    print('>>>>>>> new image <<<<<<<<')
    print(new_name)
    img.save(f'output/{new_name}', "PNG")
