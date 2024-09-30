from typing import Any
import pyautogui as GU

from app.page.loading import page_render_delay


class make_delay:
    def __init__(self, delay: int=1) -> None:
        self.delay = delay
    
    def __call__(self, func: Any) -> Any:
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            page_render_delay(self.delay)
            return result
        
        return wrapper


class Cursor:
    @staticmethod
    @make_delay()
    def accept_cookies(has_taskbar: bool=True) -> None:
        y = GU.size().height * 0.9 if has_taskbar else GU.size().height * 0.925
        
        GU.moveTo(
            x=GU.size().width * 0.35,  # координата 0 находится слева
            y=y  # координата 0 находится сверху
        )
        GU.click()
    
    @staticmethod
    def move_to_top() -> None:
        GU.moveTo(x=GU.size().width // 2, y=0 + 1)
    
    @staticmethod
    @make_delay()
    def remove_automatic_software_banner() -> None:
        GU.moveTo(
            x=GU.size().width - 34, 
            y=GU.size().height * 0.13
        )
        GU.click()


cursor = Cursor()
