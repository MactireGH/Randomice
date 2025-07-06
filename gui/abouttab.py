import tkinter as tk
from tkinter import ttk
import webbrowser

def open_github():
    webbrowser.open_new("https://github.com/MactireGH/Randomice")  # замените при необходимости

def get_create_about_tab(surface):
    """Создание вкладки 'О программе'."""
    frame = ttk.Frame(surface)

    # Заголовок и версия
    ttk.Label(frame, text="Randomice", font=("Arial", 14, "bold")).pack(pady=(10, 0))
    ttk.Label(frame, text="Версия: 0.1 (2025)", font=("Arial", 10)).pack()

    # Авторы
    ttk.Label(frame, text="Авторы: Никита Золотарёв, Юлия Вечерская").pack(pady=2)

    # GitHub
    ttk.Label(frame, text="Ссылка на исходный код:", font=("Arial", 9, "italic")).pack()
    github_link = tk.Label(frame, text="GitHub", fg="blue", cursor="hand2")
    github_link.pack()
    github_link.bind("<Button-1>", lambda e: open_github())

    # Информация о программе
    info_text = tk.Text(frame, height=14, wrap='word')
    info_text.pack(fill='both', expand=True, padx=20, pady=10)

    info_text.insert(tk.END,
        "Программа Randomice предназначена для отбора лабораторных животных\n"
        "в рамках подготовки к доклиническим исследованиям.\n\n"
        "Алгоритм обеспечивает случайное, но равномерное распределение животных\n"
        "по группам с возможностью учета стандартного отклонения массы — при необходимости.\n\n"
        "Функциональные особенности:\n"
        "- Интуитивный графический интерфейс\n"
        "- Контроль стандартного отклонения внутри и между группами\n"
        "- Равномерное распределение при любом числе групп\n"
        "- Гибкая настройка параметров отбора\n\n"
        "Программа разработана с прицелом на максимальную совместимость и может работать даже на системах Windows 7 без установленного пакета "
        "api-ms-win-core-path-l1-1-0.dll (на системах без UCRT и Windows 10)."
    )
    info_text.config(state='disabled')

    ttk.Label(frame, text="© 2025 Никита Золотарёв, Юлия Вечерская").pack(pady=5)

    return frame