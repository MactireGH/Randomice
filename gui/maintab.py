import tkinter as tk
from tkinter import ttk

def get_create_main_tab(surface):
    """Функция для создания вкладки управления."""

    frame = ttk.Frame(surface)
    frame_content = ttk.Frame(frame)
    frame_content.pack(fill='both', expand=True)

    # Левый блок
    # Левый блок: Главное
    frame_input = ttk.LabelFrame(frame_content, text='Ввод данных')
    frame_input.pack(side='left', fill='y', padx=10, pady=5)

    grid_input = ttk.Frame(frame_input)
    grid_input.pack(padx=10, pady=10)

    # Левый блок: Ввод поля - Количество животных
    ttk.Label(grid_input, text='Количество животных:').grid(row=0, column=0, sticky='w', padx=5)
    animals_count = ttk.Entry(grid_input, width=15)
    animals_count.grid(row=0, column=1, sticky='w', padx=10, pady=5)

    # Левый блок: Ввод поля - Количества групп
    ttk.Label(grid_input, text='Количество групп:').grid(row=1, column=0, sticky='w', pady=5)
    animals_group = ttk.Entry(grid_input, width=15)
    animals_group.grid(row=1, column=1, padx=10, pady=5, sticky='w')

    # Левый блок: Ввод поля - Стандартное отклонение
    ttk.Label(grid_input, text='Стандартное отклонение:').grid(row=2, column=0, sticky='w', pady=5)
    deviation = ttk.Entry(grid_input, width=15)
    deviation.grid(row=2, column=1, padx=10, pady=5, sticky='w')

    # Левый блок: Кнопка получения результатов
    button_result = ttk.Button(frame_input, text='Рассчитать')
    button_result.pack(pady=10, fill='x')

    # Правый блок
    # Правый блок: Главное
    frame_output = ttk.LabelFrame(frame_content, text='Результаты')
    frame_output.pack(side='right', fill='y', padx=10)

    frame_text = tk.Text(frame_output, height=15, wrap='word')
    frame_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)

    # Правый блок: Скроллбар в окне результатов
    scrollbar = ttk.Scrollbar(frame_output, command=frame_text.yview)
    scrollbar.pack(side='right', fill='y')

    elements = {
        "animals_count": animals_count,
        "animals_group": animals_group,
        "deviation": deviation,
        "output_text": frame_text,
        "button_result": button_result
    }

    return frame, elements