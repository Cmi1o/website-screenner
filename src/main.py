import constants
import user_interface

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from files_interactions import compare_pngs, delete_file
from app.driver_builder import options
from app.page import cursor, page_render_delay, PageDriver
from app.page.loading import prepare_page
from screenshots import screens_maker
from get_url import next_page_url


def main() -> None:
    ui = user_interface.UI()
    url = ui.get_user_input()
    
    with webdriver.Chrome(options) as driver:
        driver.get(url)
        
        page_driver = PageDriver(driver)
        pages_count = 1
        page_screens_count = 0
        screens_count = 0
        is_last_photo = False
        has_next_page = True
        
        prepare_page()
        cursor.accept_cookies(has_taskbar=True)
        cursor.remove_automatic_software_banner()
        cursor.move_to_top()
        
        while has_next_page:
            screen_height = page_driver.screen_size.height
            
            while page_screens_count < constants.MAX_SCREENS_COUNT and not is_last_photo:
                page_screens_count += 1
                screens_count += 1
                
                screens_maker.take_screenshot(serial_number=screens_count)
                
                if not screens_count == 1:
                    if compare_pngs(screens_count - 1, screens_count) is True:
                        delete_file(screens_count)
                        
                        is_last_photo = True
                        screens_count -= 1
                        page_screens_count -= 1
                
                page_driver.scroll_down(screen_height * constants.PAGE_SCROLL_PERCENT)
                page_render_delay(1.5)
            
            if page_driver.is_next_page_button_found():
                pages_count += 1
                
                page_screens_count = 0
                is_last_photo = False
                
                page_driver.open_new_tab(
                    url=next_page_url(
                        base_url=url, 
                        page_number=pages_count
                    )
                )
                prepare_page()
            
            else:
                has_next_page = False


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, WebDriverException) as error:
        if isinstance(error, WebDriverException):
            print('Network error')
