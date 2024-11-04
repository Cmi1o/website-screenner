import tkinter as tk


class UI:
    def __init__(self):
        self.user_input = ''
        
        self.root = tk.Tk()
        self.root.title('Отсканировать продавца')
        
        label = tk.Label(self.root, text='Добро пожаловать! Введите ссылку на магазин:')
        label.pack(pady=10)
        
        self.entry = tk.Entry(self.root, width=100)
        self.entry.pack(pady=10)
        
        button = tk.Button(self.root, text='Отсканировать', command=self.save_text)
        button.pack(pady=10)
        
        self.root.mainloop()
    
    def save_text(self):
        self.user_input = self.entry.get()
        self.root.destroy()
    
    def get_user_input(self):
        return self.user_input

