#! python
# logoAndSize.py - this script will change the size of every image files that they can fit into
#  500x500px and add to them special logo at the right bottom corner
# XI 2020 Arnold Cytrowski
import os
from PIL import Image

SQUARE_FILESIZE = 500
LOGO_FILENAME = 'catlogo.png'

logo_im = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_im.size

os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
    if not(filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue

    image = Image.open(filename)
    width, height = image.size

    if width > SQUARE_FILESIZE and height > SQUARE_FILESIZE:
        if width > height:
            height = int((SQUARE_FILESIZE / width) * height)
            width = SQUARE_FILESIZE
        else:
            width = int((SQUARE_FILESIZE / height) * width)
            height = SQUARE_FILESIZE

        print(f'Resizing {filename}...')
        image = image.resize((width, height))

        print(f'Adding logo to {filename}...')
        image.paste(logo_im, (width - logo_width, height - logo_height), logo_im)

        image.save(os.path.join('withLogo', filename))

