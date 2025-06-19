class Student():
    def __init__(self,name,classroom,spanish_grade,english_grade,social_studies_grade,science_grade):
        self.name = name
        self.classroom = classroom
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade


    def __repr__(self):
        return f'Name: {self.name}, Classroom: {self.classroom}, Spanish Grade: {self.spanish_grade}, English Grade: {self.english_grade}, Social Studies Grade: {self.social_studies_grade}, Science Grade: {self.science_grade}'


    def __str__(self):
        return f'Name: {self.name}, Classroom: {self.classroom}, Spanish Grade: {self.spanish_grade}, English Grade: {self.english_grade}, Social Studies Grade: {self.social_studies_grade}, Science Grade: {self.science_grade}'


def ask_for_grade(topic):
    grade = 0
    loop = True
    while loop == True:
        try:
            grade = int(input(f'Type the grade obtained in {topic}: '))
            if grade < 0 or grade > 100:
                raise ValueError()
            return grade
        except ValueError as e:
            print('\nPlease enter a valid grade between 0 to 100.\n')


def ask_for_name():
    loop = True
    counter = 0
    while loop == True:
        name = input("\nType the student's name: ")
        for char in name:
            if char.isalpha() or char.isspace():
                if counter == len(name)-1:
                    return name
                else:
                    counter += 1
                    continue
            else:
                print('\nPlease, enter a valid name for a student.')
                counter = 0


def ask_for_classroom():
    loop = True
    while loop == True:
        classroom = input('Type their classroom: ')
        number = classroom[0]
        letter = classroom[1]

        if len(classroom) > 2 or len(classroom) < 1:
            print('\nPlease, enter a valid classroom: first a number followed by a letter.\n')
        elif number.isdigit():
            if letter.isalpha():
                return classroom
            else:
                print('\nPlease, enter a valid classroom: first a number followed by a letter.\n')
        else:
            print('\nPlease, enter a valid classroom: first a number followed by a letter.\n')



def add_student():
    student = Student(
        ask_for_name(),
        ask_for_classroom(),
        ask_for_grade('Spanish'),
        ask_for_grade('English'),
        ask_for_grade('Social Studies'),
        ask_for_grade('Science'),
    )
    return student


def average_note_every_student(list):
    list_of_students = list
    list_of_average_notes = []
    counter = 0

    for student in list_of_students:
        list_of_average_notes.append({'Name':student.name,'Average Grade':(student.spanish_grade+student.english_grade+student.social_studies_grade+student.science_grade)/4})
    sorted_list = sorted(list_of_average_notes, key=lambda item:item['Average Grade'], reverse=True)
    print('\nThe top 3 students are:')
    for value in sorted_list:
        if counter < 3:
            print(value)
            counter += 1


def average_note_all_students(list):
    list_of_students = list
    total_average_note = 0
    total_grades_number = 0

    for student in list_of_students:
        total_average_note = total_average_note + student.spanish_grade + student.english_grade + student.social_studies_grade + student.science_grade
        total_grades_number += 4
    
    total_average_note = total_average_note / total_grades_number
    print(f'\nThe average value of all students grades is: {total_average_note}')