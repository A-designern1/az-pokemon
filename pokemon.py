import requests

class Pokemon:
    def __init__(self, weight, order, name):
        self.weight = weight
        self.order = order
        self.name = name

    def PrintInf(self):
        print('name - ' + self.name)
        print('weight - '+ str(self.weight))
        print('order - ' + str(self.order))




while True:
    print('id or name of pokemon')
    id_or_name = input()
    url = 'https://pokeapi.co/api/v2/pokemon/{id or name}/'
    u = url.replace("{id or name}", id_or_name)
    req = requests.get(u)
    poke = req.json()
    pokemon = Pokemon(poke['weight'],poke['order'],poke['name'])
    print('command:')
    command = input()
    if command == 'get inf':
        pokemon.PrintInf()



