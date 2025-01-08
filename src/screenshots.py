import pyautogui as GUI

import constants


def take_screenshot(page_url: str, serial_number: int) -> None:
    GUI.screenshot(constants.SCREENSHOT_PATH.format(hash(page_url), serial_number))
