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
        return split_evenly(animals, group_size), []

    best_groups = None
    best_excluded = None
    best_score = float('inf')

    for _ in range(1000):  # пробуем 1000 перестановок
        rd.shuffle(animals)

        groups = [[] for _ in range(group_size)]
        group_masses = [[] for _ in range(group_size)]
        excluded = []

        for animal in animals:
            placed = False
            for i in range(group_size):
                if len(groups[i]) >= len(animals) // group_size:
                    continue

                new_masses = group_masses[i] + [animal[1]]
                mean = calculate_mean(new_masses)
                std = calculate_std_deviation(new_masses)

                if mean == 0 or std / mean <= max_std_dev:
                    groups[i].append(animal)
                    group_masses[i].append(animal[1])
                    placed = True
                    break

            if not placed:
                excluded.append(animal)

        # Проверка межгруппового отклонения
        group_means = [calculate_mean(gm) for gm in group_masses if gm]
        overall_mean = calculate_mean(group_means)
        overall_std = calculate_std_deviation(group_means)

        if overall_mean == 0 or overall_std / overall_mean > max_std_dev:
            continue  # отклоняем вариант

        # Выбираем лучший (с наименьшим межгрупповым отклонением)
        score = overall_std / overall_mean
        if score < best_score:
            best_score = score
            best_groups = groups
            best_excluded = excluded

        # Удаляем неполные группы
        final_groups = []
        final_excluded = best_excluded.copy() if best_excluded else []

        for group in best_groups:
            if len(group) < len(animals) // group_size:
                final_excluded.extend(group)
            else:
                final_groups.append(group)

        return final_groups, final_excluded

    return best_groups if best_groups else [], best_excluded if best_excluded else animals