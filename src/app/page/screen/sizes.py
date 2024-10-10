from typing import NamedTuple

from selenium.webdriver.chrome.webdriver import WebDriver


class ScreenSizes(NamedTuple):
    width: int
    height: int


def get_screen_size(driver: WebDriver) -> ScreenSizes:
    return ScreenSizes(
        width=driver.get_window_size()['width'],
        height=driver.get_window_size()['height']
    )
