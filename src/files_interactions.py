import os

import constants

from docx import Document
from PIL import Image
from imagehash import dhash


def compare_pngs(first_serial_number: int, second_serial_number: int) -> bool:
    first_path = constants.BASE_SCREENSHOT_PATH.format(first_serial_number)
    second_path = constants.BASE_SCREENSHOT_PATH.format(second_serial_number)
    
    return dhash(Image.open(first_path)) == dhash(Image.open(second_path))


def delete_file(serial_number: int) -> None:
    os.remove(f'assets/screenshot_{serial_number}.png')


def add_picture_to_docx(photo_serial_number: int) -> None:
    doc = Document()
    path = constants.BASE_SCREENSHOT_PATH.format(photo_serial_number)
    
    doc.add_picture(
        image_path_or_stream=path,
        width=Image.open(path).size[0], 
        height=Image.open(path).size[1]
    )
    doc.save('results.docx')
