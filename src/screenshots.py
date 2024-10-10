import pyautogui as GU


class ScreenshotMaker:
    def take_screenshot(self, serial_number: int) -> None:
        GU.screenshot(f'assets/screenshot_{serial_number}.png')


screens_maker = ScreenshotMaker()
