import tkinter as tk

from tkinter import ttk
from gui.maintab import get_create_main_tab
from gui.abouttab import get_create_about_tab

def run_app():
    """Функция для сборки пользовательского интерфейса."""

    root = tk.Tk()
    root.title('Randomice')
    root.geometry('1024x500')

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True, padx=10, pady=10)

    main_tab, elements = get_create_main_tab(notebook)
    notebook.add(main_tab, text='Главная')

    about_tab = get_create_about_tab(notebook)
    notebook.add(about_tab, text='О программе')

    root.mainloop()