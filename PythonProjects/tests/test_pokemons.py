import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token ='0d56b4a3bd94390e2d7a3c794bcee769'
header = {'Content-type': 'application/json', 'trainer_token' : token}
trainer_id = '33468'

def test_status_code():
    response = requests.get(url=f'{url}/trainers')
    assert response.status_code == 200

'''def test_part_of_response():
    response_get = requests.get(url=f'{url}/pokemons', params = {'trainer_id': trainer_id})
    assert response_get.json()["data"][0]["name"] == 'kartana'''

def test_part_of_response():
    response_get = requests.get(url=f'{url}/trainers/{trainer_id}')
    assert response_get.json()["trainer_name"] == 'Margo'


'''@pytest.Mark.parametrize('key', 'value',[('name', 'kartana'),('trainer_id', trainer_id),('pokemon_id', '26789')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{url}/pokemons', params = {'trainer_id': trainer_id})
    assert response_parametrize.json(["data"][0][key]) == value'''