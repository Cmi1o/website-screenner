import pyautogui as GU

import constants


class ScreenshotMaker:
    def take_screenshot(self, serial_number: int) -> None:
        GU.screenshot(constants.SCREENSHOT_PATH.format(serial_number))


screens_maker = ScreenshotMaker()
