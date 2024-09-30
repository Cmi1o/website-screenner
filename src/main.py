import constants

from selenium import webdriver

from app.files_interactions import compare_pngs, delete_file
from app.driver_builder import options
from app.page import (
    scroll_down,
    page_render_delay
)
from app.page import cursor
from app.page.loading import prepare_page
from app.screenshots import screens_maker


def main() -> None:
    with webdriver.Chrome(options) as driver:
        driver.get('https://www.wildberries.ru/seller/1158424')
        
        screens_count = 0
        is_last_photo = False
        
        prepare_page()
        cursor.accept_cookies(has_taskbar=False)
        cursor.remove_automatic_software_banner()
        cursor.move_to_top()
        
        while screens_count <= constants.max_screens_count and not is_last_photo:
            screens_count += 1
            screens_maker.take_screenshot(serial_number=screens_count)
            
            if not screens_count == 1:
                if compare_pngs(screens_count - 1, screens_count) is True:
                    is_last_photo = True
                    delete_file(screens_count)
            
            scroll_down(driver)
            page_render_delay(1.5)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Ты вручную завершил работу')
