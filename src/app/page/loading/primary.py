import pyautogui as GUI

from .render import page_render_delay


def prepare_page() -> None:
    GUI.hotkey('win', 'up')  # fullscreen

    page_render_delay(3)
