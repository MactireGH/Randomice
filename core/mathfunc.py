import numpy as np
import random as rd


def calculate_std_deviation(masses):
    """Вычисляет стандартное отклонение масс."""

    return np.std(masses)

def calculate_mean(masses):
    """Вычисляет среднее значение масс."""

    return np.mean(masses)

def is_within_std_dev_limit(group_masses, new_mass, max_std_dev=0.1):
    new_group_masses = group_masses + [new_mass]
    std_dev = calculate_std_deviation(new_group_masses)
    mean_mass = calculate_mean(new_group_masses)

    if mean_mass == 0:
        return False  # нельзя делить на 0, явно превышает

    return std_dev / mean_mass <= max_std_dev

def split_evenly(animals, group_size):
    """Делит список животных на равные группы."""

    groups = [[] for _ in range(group_size)]

    for i, animal in enumerate(animals):
        groups[i % group_size].append(animal)

    return groups



def randomize_animals(animals, max_std_dev=None, group_size=None):
    rd.shuffle(animals)

    if max_std_dev is None:
        # Простое равномерное распределение по группам
        return split_evenly(animals, group_size)

    best_groups = None
    best_score = float('inf')

    for _ in range(1000):  # пробуем 1000 рандомных перестановок
        rd.shuffle(animals)
        groups = split_evenly(animals, group_size)

        # Проверим, все ли группы удовлетворяют стандартному отклонению
        valid = True
        for group in groups:
            masses = [mass for _, mass in group]
            if not is_within_std_dev_limit([], 0, max_std_dev=max_std_dev) or len(masses) <= 1:
                continue
            std_dev = calculate_std_deviation(masses)
            mean = calculate_mean(masses)
            if std_dev / mean > max_std_dev:
                valid = False
                break

        if not valid:
            continue

        # Считаем межгрупповое отклонение
        group_means = [calculate_mean([m for _, m in g]) for g in groups]
        overall_std = calculate_std_deviation(group_means)
        overall_mean = calculate_mean(group_means)
        score = overall_std / overall_mean  # чем меньше, тем лучше

        if score < best_score:
            best_score = score
            best_groups = groups

    return best_groups if best_groups else split_evenly(animals, group_size)