import pytest
from unittest.mock import patch
from main import get_tallest_hero
from data import MOCK_RESPONSE

@patch('requests.get')
def test_male_work(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Male", True)
    assert tallest_hero['name'] == "Hero0"

@patch('requests.get')
def test_male(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Male", False)
    assert tallest_hero['name'] == "Hero12"

@patch('requests.get')
def test_female_work(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Female", True)
    assert tallest_hero['name'] == "Hero8"

@patch('requests.get')
def test_female(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Female", False)
    assert tallest_hero['name'] == "Hero16"

@patch('requests.get')
def test_empty_gender(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(ValueError):
        get_tallest_hero("", False)

@patch('requests.get')
def test_digits_gender(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(TypeError):
        get_tallest_hero(123, False)

@patch('requests.get')
def test_other_gender(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(ValueError):
        get_tallest_hero("non-binary", False)

@patch('requests.get')
def test_string_work_true(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(TypeError):
        get_tallest_hero("Male", "true")

@patch('requests.get')
def test_string_work_false(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(TypeError):
        get_tallest_hero("Female", "false")

@patch('requests.get')
def test_uppercase_gender(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("MALE", True)
    assert tallest_hero['name'] == "Hero0"

@patch('requests.get')
def test_lowercase_gender(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("female", False)
    assert tallest_hero['name'] == "Hero16"

@patch('requests.get')
def test_upper_lower_cases_gender(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("FeMaLe", False)
    assert tallest_hero['name'] == "Hero16"

@patch('requests.get')
def test_spaces_gender(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Male   ", False)
    assert tallest_hero['name'] == "Hero12"

@patch('requests.get')
def test_spaces_and_spaces_gender(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("   Female   ", True)
    assert tallest_hero['name'] == "Hero8"

@patch('requests.get')
def test_no_heroes_match_criteria(mock_get):
    mock_response = [
        {
            "name": "Hero",
            "appearance": {"gender": "Male", "height": ["-", "0 cm"]},
            "work": {"occupation": "-"}}
    ]
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    with pytest.raises(ValueError):
        get_tallest_hero("Male", True)