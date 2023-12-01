import requests
import json


def find_starship(starship_name):
    url = f'https://swapi.dev/api/starships/?search={starship_name}'
    response = requests.get(url)
    data = response.json()
    starship = data['results'][0]
    return starship


def find_pilot_info(pilot_url):
    info = requests.get(pilot_url)
    pilot = info.json()
    return {
        'height': pilot['height'],
        'homeworld': requests.get(pilot['homeworld']).json()['name'],
        'homeworld_url': pilot['homeworld'],
        'mass': pilot['mass'],
        'name': pilot['name'],
    }


def create_output_dict(starship_info):
    max_atmosphering_speed = starship_info['max_atmosphering_speed']
    pilots = []
    for pilot_url in starship_info['pilots']:
        pilots.append(find_pilot_info(pilot_url))
    ship_name = starship_info['name']
    starship_class = starship_info['starship_class']
    result = {
        'max_atmosphering_speed': max_atmosphering_speed,
        'pilots': pilots,
        'ship_name': ship_name,
        'starship_class': starship_class,
    }
    return result


millennium_falcon_pilots = find_starship('Millennium Falcon')
if millennium_falcon_pilots:
    result = create_output_dict(millennium_falcon_pilots)
    print(json.dumps(result, indent=2, separators=(',', ': ')))
    with open('millennium_falcon_pilots.json', 'w') as json_file:
        json.dump(result, json_file, indent=2, separators=(',', ': '))
