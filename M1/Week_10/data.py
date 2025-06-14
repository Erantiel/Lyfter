import csv

def write_csv_file(file_name, list_of_students):
    headers = (
	'Name',
	'Classroom',
	'Spanish Grade',
    'English Grade',
    'Social Studies Grade',
    'Science Grade'
    )
    with open(file_name, 'w') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(list_of_students)


def open_csv_file(file_name):
    list_of_students = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_of_students.append(row)
        return list_of_students
    except FileNotFoundError:
        print('File does not exist yet. First export it in order to read it.')