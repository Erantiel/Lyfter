import Model as mod
import csv
import os

def create_category_file(category):
    if not os.path.isdir('Data'):
        os.makedirs('Data')
    with open('Data/List_of_categories.txt', 'a') as file:
        file.write(f'{category}\n')


def open_category_file():
    try:
        with open('Data/List_of_categories.txt', 'r') as file:
            list = []
            for line in file.readlines():
                list.append(line.replace('\n',''))
            return list
    except FileNotFoundError:
        return FileNotFoundError


def add_financial_flow(type, category, description, amount):
    try:
        if description == '' or type == '' or category == '':
            raise TypeError
        elif float(amount):
            float_amount = float(amount)
            object = mod.Financial_Flow(type, category, description, float_amount)
            return object
    except ValueError:
        return ValueError
    except TypeError:
        return TypeError


def create_financial_flow_file(object):
    headers = ['Type', 'Category', 'Description', 'Amount']
    list = [{'Type':object.type, 'Category':object.category, 'Description':object.description, 'Amount':object.amount}]
    try:
        with open('Data/Financial_Flow.csv', 'r') as csvfile:
            with open('Data/Financial_Flow.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writerows(list)
    except FileNotFoundError:
        with open('Data/Financial_Flow.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(list)


def open_financial_flow_file():
    data = []
    try:
        with open('Data/Financial_Flow.csv', 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
                return data
    except FileNotFoundError:
        return FileNotFoundError