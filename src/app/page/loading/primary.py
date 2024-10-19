import pyautogui as GU

from .render import page_render_delay


def prepare_page() -> None:
    GU.hotkey('win', 'up')  # fullscreen
    
    page_render_delay(3)
