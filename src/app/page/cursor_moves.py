import pyautogui as GU

from decorators import delayed


class Cursor:
    @staticmethod
    @delayed()
    def accept_cookies(has_taskbar: bool=True) -> None:
        y = GU.size().height * 0.9 if has_taskbar else GU.size().height * 0.925
        
        GU.moveTo(
            x=GU.size().width * 0.35,  # 0 coordinate is on the left
            y=y  # 0 coordinate is on the top
        )
        GU.click()
    
    @staticmethod
    def move_to_top() -> None:
        GU.moveTo(x=GU.size().width // 2, y=0 + 1)
    
    @staticmethod
    @delayed()
    def remove_automatic_software_banner() -> None:
        GU.moveTo(
            x=GU.size().width - 34,
            y=GU.size().height * 0.13
        )
        GU.click()


cursor = Cursor()
