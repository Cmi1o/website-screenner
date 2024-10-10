import constants

from selenium import webdriver

from files_interactions import compare_pngs, delete_file
from app.driver_builder import options
from app.page import (
    scroll_down,
    page_render_delay
)
from app.page import cursor
from app.page.loading import prepare_page
from app.page.screen.buttons import is_next_page_button_found
from app.page.screen.sizes import get_screen_size
from app.page.tabs import open_new_tab
from screenshots import screens_maker
from get_url import next_page_url


def main() -> None:
    url = 'https://www.wildberries.ru/seller/1158424'
    
    with webdriver.Chrome(options) as driver:
        driver.get(url)
        
        pages_count = 1
        page_screens_count = 0
        screens_count = 0
        is_last_photo = False
        has_next_page = True
        
        prepare_page(driver)
        cursor.accept_cookies(has_taskbar=False)
        cursor.remove_automatic_software_banner()
        cursor.move_to_top()
        
        while has_next_page:
            screen_height = get_screen_size(driver).height
            
            while page_screens_count < constants.MAX_SCREENS_COUNT and not is_last_photo:
                page_screens_count += 1
                screens_count += 1
                
                screens_maker.take_screenshot(serial_number=screens_count)
                
                if not screens_count == 1:
                    if compare_pngs(screens_count - 1, screens_count) is True:
                        is_last_photo = True
                        delete_file(screens_count)
                
                scroll_down(
                    driver=driver,
                    step=screen_height * constants.PAGE_SCROLL_PERCENT
                )
                page_render_delay(1.5)
            
            if is_next_page_button_found(driver):
                pages_count += 1
                
                page_screens_count = 0
                is_last_photo = False
                
                open_new_tab(
                    url=next_page_url(
                        base_url=url, 
                        page_number=pages_count
                    ),
                    driver=driver
                )
                prepare_page(driver)
            
            else:
                has_next_page = False


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Ты вручную завершил работу')
