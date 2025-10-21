import json


def open_json(file_name):
    try:
        with open(file_name, "r") as file:
            list = json.load(file)
            return list
    except FileNotFoundError:
        return []


def create_json(list, file_name):
    with open(file_name, "w") as file:
        file.write(json.dumps(list, indent=4))