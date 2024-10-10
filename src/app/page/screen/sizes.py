from typing import NamedTuple

from selenium.webdriver.remote.webelement import WebElement


class ScreenSizes(NamedTuple):
    width: int
    height: int


def get_screen_size(body: WebElement) -> ScreenSizes:
    return ScreenSizes(
        width=body.size['width'], 
        height=body.size['height']
    )
