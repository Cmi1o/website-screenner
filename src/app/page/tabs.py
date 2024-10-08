from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver


def open_new_tab(url: str, driver: WebDriver) -> None:
    body = driver.find_element(By.TAG_NAME, 'body')
    
    body.send_keys(Keys.CONTROL + 't')
    driver.get(url)
