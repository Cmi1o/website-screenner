import tkinter as tk

# После закрытия окна, переменная user_input будет содержать введенный текст
# user_input = ""


def start_ui() -> str:
    user_input = ""

    def save_text():
        nonlocal user_input
        user_input = entry.get()
        root.destroy()

    root = tk.Tk()
    root.title("Отсканировать продавца")

    label = tk.Label(root, text="Добро пожаловать! Введите ссылку на магазин:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=100)
    entry.pack(pady=10)

    button = tk.Button(root, text="Отсканировать", command=save_text)
    button.pack(pady=10)

    root.mainloop()
    return user_input
