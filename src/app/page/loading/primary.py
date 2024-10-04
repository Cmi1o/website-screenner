import pyautogui as GU

from selenium.webdriver.chrome.webdriver import WebDriver

from app.page.screen.scroll import scroll_down
from .render import page_render_delay


def prepare_page(driver: WebDriver) -> None:
    GU.hotkey('win', 'up')  # fullscreen
    
    page_render_delay(3)
    scroll_down(driver, 350)
