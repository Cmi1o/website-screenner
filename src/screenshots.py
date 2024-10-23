import pyautogui as GU

import constants


class ScreenshotMaker:
    def take_screenshot(self, page_url: str, serial_number: int) -> None:
        GU.screenshot(constants.SCREENSHOT_PATH.format(
            hash(page_url),
            serial_number
        ))


screens_maker = ScreenshotMaker()
