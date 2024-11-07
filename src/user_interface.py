import tkinter as tk


class StartingUI:
    def __init__(self):
        self.user_input = ""
        self.canceled = False

        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.cancel)
        self.root.title("Отсканировать продавца")

        label = tk.Label(self.root, font=("Arial", 12), text="Добро пожаловать! Введите ссылку на магазин:")
        label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=80)
        self.entry.pack(pady=10)

        button = tk.Button(self.root, text="Отсканировать", command=self.save_text)
        button.pack(pady=10)

        button = tk.Button(self.root, text="Отменить", command=self.cancel)
        button.pack(pady=10)

        self.root.mainloop()

    def save_text(self):
        self.user_input = self.entry.get()
        self.root.destroy()

    def get_user_input(self):
        return self.user_input

    def cancel(self):
        self.canceled = True
        self.root.destroy()


class ErrorUI:
    def __init__(self, error_message):
        self.root = tk.Tk()
        # self.root.protocol("WM_DELETE_WINDOW", self.cancel)
        self.root.title("Ошибка")

        label = tk.Label(self.root, font=("Arial", 12), text="Произошла следующая ошибка:\n" + error_message)
        label.pack(pady=100)

        self.root.mainloop()
