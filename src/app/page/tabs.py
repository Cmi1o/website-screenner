from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver


def open_new_tab(url: str, driver: WebDriver, body: WebElement | None=None) -> None:
    if not body:
        body = driver.find_element(By.TAG_NAME, 'body')
    
    body.send_keys(Keys.CONTROL + 't')  # open new tab
    driver.get(url)
