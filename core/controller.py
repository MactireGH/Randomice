import tkinter as tk
from tkinter import messagebox, simpledialog
from core.mathfunc import randomize_animals, calculate_mean, calculate_std_deviation


def get_user_input(elements):
    """Функция для считывания и валидации введённых значений."""

    animals_count = int(elements['animals_count'].get())
    animals_group = int(elements['animals_group'].get())

    if elements['is_use_deviation'].get():
        deviation = float(elements['deviation'].get())

        if deviation < 0:
            messagebox.showerror("Неверный ввод", "Отклонение не может быть отрицательным!")
            return None
    else:
        deviation = None

    if animals_group > animals_count:
        if animals_count <= 0 or animals_group <= 0 or animals_count:
            messagebox.showerror('Неверный ввод','Все значения должны быть положительными!')
        messagebox.showerror('Неверный ввод', 'Количество групп, не может быть больше количества животных!')

    return animals_count, animals_group, deviation


def get_individual_masses(animals_count: int):
    """Функция для вызова окна получения индивидуальных масс животных."""

    animals = []

    for i in range(animals_count):
        while True:
            person = round(simpledialog.askfloat('Ввод данных', f'Введите массу животного {i + 1}'), 2)

            if person is not None and person > 0.0:
                animals.append((f'Животное {i + 1}', person))
                break
            else:
                messagebox.showerror("Ошибка", "Масса должна быть положительным числом.")

    return animals


def get_user_output(groups, elements):
    """Функция для вывода сформированных групп в правый блок."""

    elements['output_text'].delete(1.0, tk.END)

    for i, group in enumerate(groups):
        elements['output_text'].insert(tk.END, f"Группа {i + 1}:\n")

        for animal in group:
            elements['output_text'].insert(tk.END, f"  {animal[0]} (масса: {animal[1]} г)\n")

        group_masses = [m for _, m in group]
        std_dev = calculate_std_deviation(group_masses)
        mean_mass = calculate_mean(group_masses)
        if elements['is_use_deviation'].get():
            elements['output_text'].insert(tk.END, f"  Средняя масса: {mean_mass:.2f} г, Стандартное отклонение: {std_dev / mean_mass * 100:.2f}%\n\n")
        else:
            elements['output_text'].insert(tk.END, f"  Средняя масса: {mean_mass:.2f} г\n\n")

        # Проверка стандартного отклонения между группами
        if elements['is_use_deviation'].get():
            group_means = [calculate_mean([m for _, m in group]) for group in groups]
            overall_std_dev = calculate_std_deviation(group_means)
            overall_mean = calculate_mean(group_means)
            elements['output_text'].insert(tk.END, f"Стандартное отклонение между группами: {overall_std_dev / overall_mean * 100:.2f}%\n")

def processing(elements):
    result = get_user_input(elements)

    if result is None:
        return

    animals_count, animals_group, deviation = result
    animals = get_individual_masses(animals_count)

    # передаём deviation как есть
    groups = randomize_animals(animals, deviation, animals_group)
    get_user_output(groups, elements)

