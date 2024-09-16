import pytest
from main import get_tallest_hero

@pytest.mark.parametrize("gender, has_work, expected_name", [
    ("Male", True, "Utgard-Loki"),
    ("Male", False, "Ymir"),
    ("Female", True, "Giganta"),
    ("Female", False, "Ardina"),
    ("MALE", True, "Utgard-Loki"),  # Верхний регистр
    ("   Female   ", True, "Giganta"),  # Пробелы в начале и конце
    ("Male   ", False, "Ymir")  # Пробелы в конце
])
def test_get_tallest_hero(gender, has_work, expected_name):
    """
    Тестирование функции с разными параметрами пола и наличия работы.
    Ожидается корректное возвращение самого высокого героя в зависимости от параметров.
    """
    tallest_hero = get_tallest_hero(gender, has_work)
    assert tallest_hero['name'] == expected_name


@pytest.mark.parametrize("gender, has_work, exception_type", [
    ("", False, ValueError),  # Пустой пол
    (123, False, TypeError),  # Пол передан числом
    ("non-binary", False, ValueError),  # Пол не "Male" и не "Female"
    ("Male", "true", TypeError)  # Наличие работы передано строкой
])
def test_get_tallest_hero_invalid_inputs(gender, has_work, exception_type):
    """
    Тестирование функции с некорректными параметрами.
    Ожидается выброс соответствующих исключений.
    """
    with pytest.raises(exception_type):
        get_tallest_hero(gender, has_work)