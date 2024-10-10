from selenium.webdriver.chrome.webdriver import WebDriver


__all__ = (
    'scroll_down',
)


def scroll_down(driver: WebDriver, step: float=515) -> None:
    driver.execute_script(f'window.scrollBy(0, {step})')
