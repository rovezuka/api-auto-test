import requests
import re


def get_tallest_hero(gender: str, has_work: bool):
    # извлечь числовое значение из строки height
    def extract_height(height_str):
        if 'cm' in height_str:
            match = re.search(r'(\d+)', height_str)
            return int(match.group(1)) if match else 0
        elif 'meters' in height_str:
            match = re.search(r'(\d+(\.\d+)?)', height_str)
            return int(float(match.group(1)) * 100) if match else 0
        return 0

    # отправить запрос к API для получения списка героев
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Запрос к API завершился со статус кодом {response.status_code}")

    heroes = response.json()
    for hero in heroes:
        print(hero['appearance']['height'])

    # отфильтровать героев по полу и наличию работы
    filtered_heroes = [
        hero for hero in heroes
        if hero['appearance']['gender'].lower() == gender.lower()
           and (hero['work']['occupation'] != '-' if has_work else hero['work']['occupation'] == '-')
    ]


    # найти самого высокого героя
    tallest_hero = max(filtered_heroes, key=lambda hero: extract_height(hero['appearance']['height'][1]))

    return tallest_hero

print(get_tallest_hero('Male', True))


