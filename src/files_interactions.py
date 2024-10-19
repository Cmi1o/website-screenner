import os

from docx import Document
from PIL import Image
from imagehash import dhash


def compare_pngs(first_serial_number: int, second_serial_number: int) -> bool:
    first_path = f'assets/screenshot_{first_serial_number}.png'
    second_path = f'assets/screenshot_{second_serial_number}.png'
    
    return dhash(Image.open(first_path)) == dhash(Image.open(second_path))


def delete_file(serial_number: int) -> None:
    os.remove(f'assets/screenshot_{serial_number}.png')


def add_picture_to_docx(photo_serial_number: int) -> None:
    doc = Document()
    
    doc.add_picture(
        image_path_or_stream=f'assets/screenshot_{photo_serial_number}.png',
        width=Image.open(f'assets/screenshot_{photo_serial_number}.png').size[0], 
        height=Image.open(f'assets/screenshot_{photo_serial_number}.png').size[1]
    )
    doc.save('results.docx')
