import json

def open_json_return_list():
    with open('pokedex.json', 'r') as file:
        list = json.load(file)
        return list


def create_pokemon():
    add_pokemon = {
        "Name": {
            "English": input('Name of the pokemon: ')
        },
        "Type": [
            input('Type of the pokemon: ')
        ],
        "Stats": {
            "HP": input('HP of the pokemon: '),
            "Attack": input('Attack of the pokemon: '),
            "Defense": input('Defense of the pokemon: '),
            "Sp. Attack": input('Speacial Attack of the pokemon: '),
            "Sp. Defense": input('Special Defense of the pokemon: '),
            "Speed": input('Speed of the pokemon: ')
        }
    }
    return add_pokemon


def add_pokemon_to_list(pokemon_list):
    with open('pokedex.json', 'w') as file:
        file.write(json.dumps(pokemon_list, indent=4))


def main():
    pokemon_list = open_json_return_list()
    pokemon_list.append(create_pokemon())
    add_pokemon_to_list(pokemon_list)


main()