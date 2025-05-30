import requests

url = 'https://api.pokemonbattle.ru/v2'
token ='0d56b4a3bd94390e2d7a3c794bcee769'
header = {'Content-type': 'application/json', 'trainer_token' : token}
trainer_id = '33468'

#1 создать покемона
body_create = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url = f'{url}/pokemons', headers = header, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

#2 изменить покемона
body_update = {
    "pokemon_id": pokemon_id,
    "name": "кусь",
    "photo_id": 2
}

response_update = requests.put(url = f'{url}/pokemons', headers = header, json = body_update)
print(response_update.text)

#3 поймать в покебол
body_add = {
    "pokemon_id": pokemon_id
}

response_add = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_add)
