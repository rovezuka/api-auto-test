import pytest
import requests
from unittest.mock import patch
from main import get_tallest_hero

MOCK_RESPONSE = [
        {
            "name": "Hero1",
            "appearance": {"gender": "Male", "height": ["6'8", '203 cm']},
            "work": {"occupation": "Scientist"}
        },
        {
            "name": "Hero2",
            "appearance": {"gender": "Male", "height": ["6'2", '188 cm']},
            "work": {"occupation": "Doctor"}
        },
        {
            "name": "Hero3",
            "appearance": {"gender": "Male", "height": ['-', '0 cm']},
            "work": {"occupation": "Student"}
        },
        {
            "name": "Hero4",
            "appearance": {"gender": "Male", "height": ['205', '62.5 meters']},
            "work": {"occupation": "Professional Criminal"}
        },
        {
            "name": "Hero5",
            "appearance": {"gender": "Female", "height": ["6'3", '191 cm']},
            "work": {"occupation": "Criminal, former Scientist"}
        },
        {
            "name": "Hero6",
            "appearance": {"gender": "Female", "height": ["5'5", '165 cm']},
            "work": {"occupation": "Green Lantern, Adventurer, Artist"}
        },
        {
            "name": "Hero7",
            "appearance": {"gender": "Female", "height": ['-', '0 cm']},
            "work": {"occupation": "Adventurer; former master mechanic, professional criminal, mercenary"}
        },
        {
            "name": "Hero8",
            "appearance": {"gender": "Female", "height": ['1000', '304.8 meters']},
            "work": {"occupation": "Insurance Investigator"}
        },
        {
            "name": "Hero9",
            "appearance": {"gender": "Male", "height": ["6'8", '203 cm']},
            "work": {"occupation": "-"}
        },
        {
            "name": "Hero10",
            "appearance": {"gender": "Male", "height": ["6'2", '188 cm']},
            "work": {"occupation": "-"}
        },
        {
            "name": "Hero11",
            "appearance": {"gender": "Male", "height": ['-', '0 cm']},
            "work": {"occupation": "-"}
        },
        {
            "name": "Hero12",
            "appearance": {"gender": "Male", "height": ['205', '62.5 meters']},
            "work": {"occupation": "-"}
        },
        {
            "name": "Hero13",
            "appearance": {"gender": "Female", "height": ["6'3", '191 cm']},
            "work": {"occupation": "-"}
        },
        {
            "name": "Hero14",
            "appearance": {"gender": "Female", "height": ["5'5", '165 cm']},
            "work": {"occupation": "-"}
        },
        {
            "name": "Hero15",
            "appearance": {"gender": "Female", "height": ['-', '0 cm']},
            "work": {"occupation": "-"}
        },
        {
            "name": "Hero16",
            "appearance": {"gender": "Female", "height": ['1000', '304.8 meters']},
            "work": {"occupation": "-"}
        }
    ]

@patch('requests.get')
def test_male_work(mock_get):
    mock_response = MOCK_RESPONSE
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: mock_response

    tallest_hero = get_tallest_hero("Male", True)
    assert tallest_hero['name'] == "Hero4"

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