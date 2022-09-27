import requests

def get_valorant_data():
    url = 'https://br.api.riotgames.com/val/status/v1/platform-data'
    headers = {'X-Riot-Token': 'RGAPI-6a11824f-f9cf-46a4-9646-f5dc7eea2e9b'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_maintenances():
    data = get_valorant_data()
    if data['maintenances'] == []:
        print('OK')
    else:
        print('Maintenances:')
        for maintenance in data['maintenances']:
            print(maintenance['name'])

def get_incidents():
    data = get_valorant_data()
    if data['incidents'] == []:
        print('OK')
    else:
        print('Incidents:')
        for incident in data['incidents']:
            print(incident['name'])

print('Manutenções:')
get_maintenances()
print('Incidentes:')
get_incidents()

