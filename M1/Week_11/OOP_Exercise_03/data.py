import csv
from actions import Student

def write_csv_file(file_name, list_of_students):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','Classroom','Spanish Grade','English Grade','Social Studies Grade','Science Grade'])
        for student in list_of_students:
            writer.writerow([student.name,student.classroom,student.spanish_grade,student.english_grade,student.social_studies_grade,student.science_grade])


def open_csv_file(file_name):
    list_of_students = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row['Name'],row['Classroom'],row['Spanish Grade'],row['English Grade'],row['Social Studies Grade'],row['Science Grade'])
                list_of_students.append(student)
        return list_of_students
    except FileNotFoundError:
        print('File does not exist yet. First export it in order to read it.')