import tkinter as tk

from tkinter import ttk
from core.labels import label_ru
from core.controller import processing


def get_create_main_tab(surface):
    """Функция для создания вкладки управления."""

    frame = ttk.Frame(surface)

    # Контейнер с двумя колонками
    frame_content = ttk.Frame(frame)
    frame_content.pack(fill='both', expand=True)

    # Настройка растягивания по ширине
    frame_content.columnconfigure(0, weight=0)  # левый блок (фиксированный)
    frame_content.columnconfigure(1, weight=1)  # правый блок (растягивается)
    frame_content.rowconfigure(0, weight=1)

    # Левый блок
    # Левый блок: Главное
    frame_input = ttk.LabelFrame(frame_content, text=label_ru['input_data'])
    frame_input.grid(row=0, column=0, sticky='ns', padx=10, pady=5)

    grid_input = ttk.Frame(frame_input)
    grid_input.pack(padx=10, pady=10)

    # Левый блок: Ввод поля - Количество животных
    ttk.Label(grid_input, text=label_ru['animals_count']).grid(row=0, column=0, sticky='w', padx=5)
    animals_count = ttk.Entry(grid_input, width=15)
    animals_count.grid(row=0, column=1, sticky='w', padx=10, pady=5)

    # Левый блок: Ввод поля - Количества групп
    ttk.Label(grid_input, text=label_ru['animals_group']).grid(row=1, column=0, sticky='w', padx=5)
    animals_group = ttk.Entry(grid_input, width=15)
    animals_group.grid(row=1, column=1, padx=10, pady=5, sticky='w')

    # Левый блок: Ввод поля - Стандартное отклонение
    ttk.Label(grid_input, text=label_ru['deviation']).grid(row=2, column=0, sticky='w', padx=5)
    deviation = ttk.Entry(grid_input, width=15)
    deviation.grid(row=2, column=1, padx=10, pady=5, sticky='w')

    # Левый блок: Фрейм кнопки управления
    frame_button = ttk.LabelFrame(frame_input)
    frame_button.pack(fill='x', padx=10, pady=(0, 10))

    button_result = ttk.Button(frame_button, text=label_ru['calculate'], command=lambda: processing(elements))
    button_result.pack(pady=10, fill='x')

    # Левой блок: Фрейм Настройки
    frame_settings = ttk.LabelFrame(frame_input, text=label_ru['settings'])
    frame_settings.pack(fill='x', padx=10, pady=10)

    # Левый блок: Настройка - Стандартного отклонения
    is_use_deviation = tk.BooleanVar(value=True)

    def toggle_deviation_state():
        if is_use_deviation.get():
            deviation.configure(state='normal')
        else:
            deviation.configure(state='disabled')

    checkbox_deviation = ttk.Checkbutton(frame_settings, text=label_ru['use_std_dev'], variable=is_use_deviation, command=toggle_deviation_state)
    checkbox_deviation.pack(anchor='w', padx=5, pady=5)

    # Правый блок
    # Правый блок: Главное
    frame_output = ttk.LabelFrame(frame_content, text=label_ru['results'])
    frame_output.grid(row=0, column=1, sticky='nsew', padx=10, pady=5)

    frame_output.columnconfigure(0, weight=1)
    frame_output.rowconfigure(0, weight=1)

    frame_text = tk.Text(frame_output, height=15, wrap='word')
    frame_text.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    # Правый блок: Скроллбар в окне результатов
    scrollbar = ttk.Scrollbar(frame_output, command=frame_text.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')

    frame_text.config(yscrollcommand=scrollbar.set)

    elements = {
        "animals_count": animals_count,
        "animals_group": animals_group,
        "deviation": deviation,
        "output_text": frame_text,
        "button_result": button_result,
        "is_use_deviation": is_use_deviation
    }

    return frame, elements