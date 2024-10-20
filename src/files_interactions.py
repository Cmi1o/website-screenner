import hashlib
import os

import constants

from docx import Document
from PIL import Image
from imagehash import dhash


class FilesManager:
    def __init__(self, page_url: str) -> None:
        self.page_url = page_url
    
    def _get_path(self, photo_serial_number: int) -> str:
        return constants.SCREENSHOT_PATH.format(
            hashlib.sha256(self.page_url.encode()).hexdigest(),
            photo_serial_number
        )
    
    def compare_pngs(self, first_serial_number: int, second_serial_number: int) -> bool:
        first_path = self._get_path(first_serial_number)
        second_path = self._get_path(second_serial_number)
        
        return dhash(Image.open(first_path)) == dhash(Image.open(second_path))
    
    def delete_file(self, serial_number: int) -> None:
        os.remove(self._get_path(serial_number))
    
    def add_picture_to_docx(
        self, 
        photo_serial_number: int, 
        path: str | None=None
    ) -> None:
        doc = Document()
        
        doc.add_picture(self._get_path(
            photo_serial_number
        ))
        doc.save(path if path else f'assets/result_{self.page_url}.docx')
