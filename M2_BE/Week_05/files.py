import json


def open_json(file_name):
    try:
        with open(file_name, "r") as file:
            list = json.load(file)
            return list
    except FileNotFoundError:
        return []