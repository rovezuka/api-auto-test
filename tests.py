import pytest
from unittest.mock import patch
from main import get_tallest_hero
from data import MOCK_RESPONSE

# Тестирование функции с параметрами: пол - "Male", наличие работы - True
@patch('requests.get')
def test_male_work(mock_get):
    """
    Тестирует случай, когда пол героя "Male" и он имеет работу.
    Ожидается, что самым высоким героем будет "Hero0".
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Male", True)
    assert tallest_hero['name'] == "Hero0"

# Тестирование функции с параметрами: пол - "Male", наличие работы - False
@patch('requests.get')
def test_male(mock_get):
    """
    Тестирует случай, когда пол героя "Male" и он не имеет работы.
    Ожидается, что самым высоким героем будет "Hero12".
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Male", False)
    assert tallest_hero['name'] == "Hero12"

# Тестирование функции с параметрами: пол - "Female", наличие работы - True
@patch('requests.get')
def test_female_work(mock_get):
    """
    Тестирует случай, когда пол героя "Female" и она имеет работу.
    Ожидается, что самым высоким героем будет "Hero8".
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Female", True)
    assert tallest_hero['name'] == "Hero8"

# Тестирование функции с параметрами: пол - "Female", наличие работы - False
@patch('requests.get')
def test_female(mock_get):
    """
    Тестирует случай, когда пол героя "Female" и она не имеет работы.
    Ожидается, что самым высоким героем будет "Hero16".
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Female", False)
    assert tallest_hero['name'] == "Hero16"

# Тестирование функции с пустым значением пола
@patch('requests.get')
def test_empty_gender(mock_get):
    """
    Тестирует вызов функции с пустым значением пола.
    Ожидается выброс исключения ValueError.
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(ValueError):
        get_tallest_hero("", False)

# Тестирование функции с полом, заданным числом
@patch('requests.get')
def test_digits_gender(mock_get):
    """
    Тестирует вызов функции с полом, переданным в виде числа.
    Ожидается выброс исключения TypeError.
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(TypeError):
        get_tallest_hero(123, False)

# Тестирование функции с любым значением пола, кроме "Male" и "Female"
@patch('requests.get')
def test_other_gender(mock_get):
    """
    Тестирует вызов функции с любым значением пола, кроме "Male" и "Female" ("non-binary").
    Ожидается выброс исключения ValueError.
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(ValueError):
        get_tallest_hero("non-binary", False)

# Тестирование функции с любым типом значения, кроме bool для наличия работы (строка вместо bool)
@patch('requests.get')
def test_string_work_true(mock_get):
    """
    Тестирует вызов функции с некорректным типом значения для наличия работы ("true").
    Ожидается выброс исключения TypeError.
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(TypeError):
        get_tallest_hero("Male", "true")

# Тестирование функции с полом, переданным в верхнем регистре
@patch('requests.get')
def test_uppercase_gender(mock_get):
    """
    Тестирует вызов функции с полом, переданным в верхнем регистре ("MALE").
    Ожидается, что самым высоким героем будет "Hero0".
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("MALE", True)
    assert tallest_hero['name'] == "Hero0"

# Тестирование функции с полом, переданным с пробелами в конце
@patch('requests.get')
def test_spaces_gender(mock_get):
    """
    Тестирует вызов функции с полом, переданным с пробелами в конце ("Male   ").
    Ожидается, что самым высоким героем будет "Hero12".
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Male   ", False)
    assert tallest_hero['name'] == "Hero12"

# Тестирование функции с полом, переданным с пробелами в начале и конце
@patch('requests.get')
def test_spaces_and_spaces_gender(mock_get):
    """
    Тестирует вызов функции с полом, переданным с пробелами в начале и конце ("   Female   ").
    Ожидается, что самым высоким героем будет "Hero8".
    """
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("   Female   ", True)
    assert tallest_hero['name'] == "Hero8"

# Тестирование функции, когда ни один герой не соответствует критериям
@patch('requests.get')
def test_no_heroes_match_criteria(mock_get):
    """
    Тестирует случай, когда ни один герой не соответствует критериям поиска.
    Ожидается выброс исключения ValueError.
    """
    mock_response = [
        {
            "name": "Hero",
            "appearance": {"gender": "Male", "height": ["-", "0 cm"]},
            "work": {"occupation": "-"}
        }
    ]
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(ValueError):
        get_tallest_hero("Male", True)