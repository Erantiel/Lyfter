import os
import json


def open_json():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []


def create_json(tasks):
    with open("tasks.json", "w") as file:
        file.write(json.dumps(tasks, indent=4))