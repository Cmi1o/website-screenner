import pyautogui as GUI

import constants


class ScreenshotMaker:
    def take_screenshot(self, page_url: str, serial_number: int) -> None:
        GUI.screenshot(
            constants.SCREENSHOT_PATH.format(hash(page_url), serial_number)
        )


screenshots_maker = ScreenshotMaker()
