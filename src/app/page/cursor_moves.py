import pyautogui as GUI

from decorators import delayed


class Cursor:
    @staticmethod
    @delayed()
    def accept_cookies(has_taskbar: bool = True) -> None:
        y = GUI.size().height * 0.9 if has_taskbar else GUI.size().height * 0.925

        GUI.moveTo(
            x=GUI.size().width * 0.35,  # 0 coordinate is on the left
            y=y,  # 0 coordinate is on the top
        )
        GUI.click()

    @staticmethod
    def move_to_top() -> None:
        GUI.moveTo(x=GUI.size().width // 2, y=0 + 1)

    @staticmethod
    @delayed()
    def remove_automatic_software_banner() -> None:
        GUI.moveTo(x=GUI.size().width - 34, y=GUI.size().height * 0.13)
        GUI.click()


cursor = Cursor()
