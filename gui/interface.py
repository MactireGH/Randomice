import tkinter as tk
from tkinter import ttk

def run_app():
    """Функция для сборки пользовательского интерфейса."""

    root = tk.Tk()
    root.title('Randomice')
    root.geometry('1024x500')

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True, padx=10, pady=10)

    label = ttk.Label(notebook, text="Добро пожаловать в Randomice!", font=("Segoe UI", 14))
    label.pack(pady=30)

    root.mainloop()