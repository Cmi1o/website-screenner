import os

import constants

from typing import Literal

from docx import Document
from docx.shared import Inches
from docx.enum.section import WD_ORIENT
from PIL import Image
from imagehash import dhash


TOrientation = Literal['landscape', 'portrait']

class FilesManager:
    def __init__(self, page_url: str) -> None:
        self._source_page_url = page_url
        self.page_url = page_url.split('/')[-1]
        self._docx_path =  self.__absolute_path(f'assets/{self.page_url}.docx')
    
    @staticmethod
    def __absolute_path(file_path: str) -> str:
        return os.path.abspath(file_path)
    
    def _get_photo_path(self, photo_serial_number: int) -> str:
        return constants.SCREENSHOT_PATH.format(
            hash(self._source_page_url),
            photo_serial_number
        )
    
    def compare_pngs(self, first_serial_number: int, second_serial_number: int) -> bool:
        first_path = self._get_photo_path(first_serial_number)
        second_path = self._get_photo_path(second_serial_number)
        
        return dhash(Image.open(first_path)) == dhash(Image.open(second_path))
    
    def delete_file(self, serial_number: int) -> None:
        os.remove(self._get_photo_path(serial_number))
    
    def create_new_folder(self, path: str) -> None:
        os.mkdir(self.__absolute_path(path))
    
    def create_new_docx(self, path: str | None=None) -> None:
        path = self.__absolute_path(
            path if path else f'assets/{self.page_url}.docx'
        )
        
        doc = Document()
        doc.save(path)
        self._docx_path = path
    
    def is_exist(self, path: str) -> bool:
        return os.path.exists(self.__absolute_path(path))
    
    def add_picture_to_docx(
        self,
        photo_serial_number: int,
        docx_path: str | None=None
    ) -> None:
        docx_path = self.__absolute_path(docx_path if docx_path else self._docx_path)
        doc = Document(docx_path)
        
        doc.add_picture(
            self._get_photo_path(
                photo_serial_number
            ),
            width=Inches(constants.INCHES_IMAGE_COUNT)
        )
        doc.save(docx_path)
    
    def switch_orientation(
        self, 
        orientation: TOrientation,
        docx_path: str | None=None, 
        section: int=0
    ) -> None:
        docx_path = self.__absolute_path(docx_path if docx_path else self._docx_path)
        
        doc = Document(docx_path)
        doc_section = doc.sections[section]
        
        doc_section.orientation = getattr(WD_ORIENT, orientation.upper())
        doc_section.page_width = doc_section.page_height
        doc_section.page_height = doc_section.page_width
        
        doc.save(path)
