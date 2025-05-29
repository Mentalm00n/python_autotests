import requests

url = 'https://api.pokemonbattle.ru/v2'
token ='0d56b4a3bd94390e2d7a3c794bcee769'
header = {'Content-type': 'application/json', 'trainer_token' : token}
trainer_id = '33468'

'''#1 создать покемона
body_create = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url = f'{url}/pokemons', headers = header, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)'''

# список покемонов - найти pokemon_id_1 для #2 +
params = {
            "trainer_id": trainer_id,
            "status": 1,
            "in_pokeball": 0
        }

response_list = requests.get(url = f'{url}/pokemons', params = params)
print(response_list.text) #необязательно печатать
pokemon_id_1 = response_list.json()["data"][0]["id"] 
print(pokemon_id_1)

# отправить в нокаут
'''params_knockout = {
            "trainer_id": trainer_id,
            "status": 1,
            "in_pokeball": 1
        }

response_list_knockout = requests.get(url = f'{url}/pokemons', params = params_knockout)
pokemon_id_2 = response_list_knockout.json()["data"][0]["id"] 
print(pokemon_id_2)
message = response_list_knockout.json()['message']
print(message)

body_knockout = {
    "pokemon_id": pokemon_id_2
}

response_knockout = requests.post(url = f'{url}/pokemons/knockout', headers = header, json = body_knockout)
print(response_knockout.text) #необязательно печатать
'''

#2 изменить покемона
body_update = {
    "pokemon_id": pokemon_id_1,
    "name": "кусь",
    "photo_id": 2
}

response_update = requests.put(url = f'{url}/pokemons', headers = header, json = body_update)
print(response_update.text)

#3 поймать в покебол
body_add = {
    "pokemon_id": pokemon_id_1
}

response_add = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_add)


'''message = response_add.json()['message']
print(message)'''