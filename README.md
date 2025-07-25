# Randomice

**Randomice** — это программа для случайного, но контролируемого распределения лабораторных животных по группам, разработанная специально для задач доклинических исследований.

---

Программа позволяет:
- Автоматически распределять животных по группам
- Учитывать заданное стандартное отклонение масс животных
- Исключать животных, которые нарушают равномерность группировки
- Гарантировать равное количество животных в группах
- Работать на устаревших системах, включая Windows 7

---

## Интерфейс

- Построен с использованием `tkinter`
- Ввод данных:
  - Общее количество животных
  - Желаемое количество животных **в каждой группе**
  - Допустимое стандартное отклонение в долях процента (0.1 = 10%)
- Результат отображается в виде:
  - Списка групп
  - Средней массы и отклонения
  - Списка исключённых животных

---

## Особенности

- Совместимость с **Windows 7** (без `api-ms-win-core-path-l1-1-0.dll`)
- Работает без установки Python (через `.exe`)
- Строгая проверка **внутригруппового и межгруппового** отклонения
- Удобный графический интерфейс

---

## Быстрый старт

Если у вас есть Python 3.7.9:

```bash
pip install -r requirements.txt
python main.py
```

---

## Сборка `.exe` (для Windows)

```bash
pyinstaller main.py --name Randomice --onefile --noconsole --win-private-assemblies
```

---

## Зависимости

- Python 3.7.9
- numpy

Список всех зависимостей — в [`requirements.txt`](requirements.txt)

---

## Лицензия

MIT License

---

## Авторы

- Никита Золотарёв
- Юлия Вечерская
