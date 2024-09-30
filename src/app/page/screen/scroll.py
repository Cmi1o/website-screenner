from selenium.webdriver.chrome.webdriver import WebDriver


__all__ = (
    'scroll_down',
)

def scroll_down(driver: WebDriver) -> None:
    driver.execute_script('window.scrollBy(0, 800)')
