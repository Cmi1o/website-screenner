import os

import constants

from docx import Document
from PIL import Image
from imagehash import dhash


class FilesManager:
    def __init__(self, page_url: str) -> None:
        self.page_url = page_url
    
    @staticmethod
    def __absolute_path(file_path: str) -> str:
        return os.path.abspath(file_path)
    
    def _get_photo_path(self, photo_serial_number: int) -> str:
        return constants.SCREENSHOT_PATH.format(
            hash(self.page_url),
            photo_serial_number
        )
    
    def compare_pngs(self, first_serial_number: int, second_serial_number: int) -> bool:
        first_path = self._get_photo_path(first_serial_number)
        second_path = self._get_photo_path(second_serial_number)
        
        return dhash(Image.open(first_path)) == dhash(Image.open(second_path))
    
    def delete_file(self, serial_number: int) -> None:
        os.remove(self._get_photo_path(serial_number))
    
    def create_new_docx(self, path: str | None=None) -> None:
        doc = Document()
        doc.save(path if path else f'assets/{self.page_url}.docx')
    
    def add_picture_to_docx(
        self, 
        photo_serial_number: int, 
        path: str | None=None
    ) -> None:
        doc = Document(path if path else f'assets/{self.page_url}.docx')
        
        doc.add_picture(self._get_photo_path(
            photo_serial_number
        ))
        doc.save(path if path else f'assets/result_{self.page_url}.docx')
