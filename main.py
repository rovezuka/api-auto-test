import requests
import re


# Функция для извлечения числового значения из строки, описывающей рост героя
def extract_height(height_str):
    """
    Извлекает числовое значение роста из строки.
    Функция поддерживает два формата роста: в сантиметрах и в метрах.

    Аргументы:
    height_str (str): строка с описанием роста героя, например '185 cm' или '1.85 meters'.

    Возвращает:
    int: числовое значение роста в сантиметрах. Если данные некорректны, возвращает 0.
    """
    # Если рост в сантиметрах, извлекаем целое число
    if 'cm' in height_str:
        match = re.search(r'(\d+)', height_str)
        return int(match.group(1)) if match else 0
    # Если рост в метрах, преобразуем значение в сантиметры
    elif 'meters' in height_str:
        match = re.search(r'(\d+(\.\d+)?)', height_str)
        return int(float(match.group(1)) * 100) if match else 0
    # Если формат не распознан или значение отсутствует, возвращаем 0
    return 0


# Функция для валидации входных данных (пол и наличие работы)
def validate_input(gender, has_work):
    """
    Проверяет корректность переданных аргументов: пол и наличие работы.
    Пол должен быть строкой, а наличие работы – булевым значением.

    Аргументы:
    gender (str): пол героя ('male' или 'female').
    has_work (bool): наличие работы (True для работающих, False для безработных).

    Исключения:
    TypeError: если пол не является строкой или наличие работы не является булевым значением.
    ValueError: если значение пола не соответствует 'male' или 'female'.
    """
    # Проверка, что пол – это строка
    if not isinstance(gender, str):
        raise TypeError("Пол должен быть строкой")

    # Приведение строки к нижнему регистру и удаление лишних пробелов
    gender = gender.lower().strip()

    # Проверка на допустимые значения пола ('male' или 'female')
    if gender not in ('male', 'female'):
        raise ValueError("Пол может быть только 'male' или 'female'")

    # Проверка, что наличие работы передано как булевое значение
    if not isinstance(has_work, bool):
        raise TypeError("Наличие работы должно быть указано значением bool")


# Функция для получения самого высокого героя по полу и наличию работы
def get_tallest_hero(gender: str, has_work: bool):
    """
    Возвращает самого высокого героя, удовлетворяющего указанным критериям: пол и наличие работы.

    Аргументы:
    gender (str): пол героя ('male' или 'female').
    has_work (bool): наличие работы (True для работающих, False для безработных).

    Возвращает:
    dict: данные самого высокого героя.

    Исключения:
    ValueError: если ни один герой не удовлетворяет указанным критериям.
    Exception: если запрос к API завершился ошибкой.
    """
    # Валидация входных данных
    validate_input(gender, has_work)

    # Отправляем запрос к API для получения списка всех героев
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code != 200:
        raise Exception(f"Запрос к API завершился со статус кодом {response.status_code}")

    # Получаем данные героев в формате JSON
    heroes = response.json()

    # Отфильтровываем героев по указанному полу и наличию/отсутствию работы
    filtered_heroes = [
        hero for hero in heroes
        if hero['appearance']['gender'].lower() == gender.lower().strip()
           and (hero['work']['occupation'] != '-' if has_work else hero['work']['occupation'] == '-')
    ]

    # Если нет героев, соответствующих критериям, выбрасываем исключение
    if not filtered_heroes:
        raise ValueError("Нет героев, соответствующих критериям")

    # Находим самого высокого героя из отфильтрованных
    tallest_hero = max(filtered_heroes, key=lambda hero: extract_height(hero['appearance']['height'][1]))

    # Возвращаем данные самого высокого героя
    return tallest_hero