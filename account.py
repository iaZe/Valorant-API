import requests

gameName = 'CAP iaZe'
tagLine = 'BARA'

def get_valorant_data():
    url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}'
    headers = {'X-Riot-Token': 'token'}
    response = requests.get(url, headers=headers)
    return response.json()
print(get_valorant_data())

def get_puuid():
    data = get_valorant_data()
    return data['puuid']
print(get_puuid())

def get_valorant_match():
    url = f'https://br.api.riotgames.com/val/match/v1/matchlists/by-puuid/{get_puuid}'
    headers = {'X-Riot-Token': 'token'}
    response = requests.get(url, headers=headers)
    return response.json()
print(get_valorant_match())
