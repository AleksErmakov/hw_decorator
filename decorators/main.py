import requests
from task_2_dec_path import logger


@logger('new_log.log')
def most_smart_hero(heroes_group, URL):

    global IQ_max
    response = requests.get(URL).json()

    intelligence_heroes = {}
    for heroes in response:
        if heroes['name'] in heroes_group:
            powerstats = heroes['powerstats']
            intelligence_heroes[powerstats['intelligence']] = heroes['name']
            IQ_max = max(intelligence_heroes.keys())
    return f'Самый умный супергерой: {intelligence_heroes[IQ_max]}. Его интеллект = {IQ_max}'


heroes_list = ['Hulk', 'Captain America', 'Thanos']
URL_1 = "https://akabab.github.io/superhero-api/api//all.json"

most_smart_hero(heroes_list, URL_1)
