import constants

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import tkinter as tk
from tkinter import messagebox

from files_interactions import compare_pngs, delete_file
from app.driver_builder import options
from app.page import cursor, page_render_delay, PageDriver
from app.page.loading import prepare_page
from screenshots import screens_maker
from get_url import next_page_url


def ui() -> str:
    global user_input
    def save_text():
        global user_input
        user_input = entry.get()
        root.destroy()  # Закрываем окно после сохранения текста
        return user_input

    # Создаем основное окно
    root = tk.Tk()
    root.title("Приветственное окно")

    # Создаем виджет Label для приветствия
    label = tk.Label(root, text="Добро пожаловать! Введите ссылку:")
    label.pack(pady=10)

    # Создаем виджет Entry для ввода текста
    entry = tk.Entry(root, width=100)
    entry.pack(pady=10)

    user_input = ""

    # Создаем виджет Button для сохранения текста
    button = tk.Button(root, text="Отсканировать", command=save_text)
    button.pack(pady=10)

    # Запускаем основной цикл обработки событий
    root.mainloop()

    # После закрытия окна, переменная user_input будет содержать введенный текст
    return user_input


def main() -> None:
    url = ui()
    # url = 'https://www.wildberries.ru/seller/1158424'
    
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
