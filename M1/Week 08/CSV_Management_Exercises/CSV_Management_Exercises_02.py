import csv

def add_game_to_list():
    game_to_add = {
		'name': input('Name of the game: '),
		'genre': input('Genre of the game: '),
		'developer': input('Developer of the game: '),
		'esrb_calification': input('ESRB Calification: '),
	}
    return game_to_add


def open_csv_file(file_path):
    list_of_games = []
    try:
        with open(file_path, 'r', newline='') as file:
                reader = csv.DictReader(file, delimiter='\t')
                for row in reader:
                    list_of_games.append(row)
                return list_of_games
    except FileNotFoundError:
        return []


def write_csv_file(file_path, list_of_games, headers):
    with open(file_path, 'w') as file:
        writer = csv.DictWriter(file, headers, delimiter = '\t')
        writer.writeheader()
        writer.writerows(list_of_games)


def main():
    games_headers = (
	'name',
	'genre',
	'developer',
	'esrb_calification',
)
    list_of_games = open_csv_file('games.csv')
    counter = int(input('How many game do you want to add?'))
    for countdown in range(0,counter):
        list_of_games.append(add_game_to_list())
    write_csv_file('games.csv', list_of_games, games_headers)
    

main()