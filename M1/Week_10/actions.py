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
            print('\nTypo Error. Please a valid grade between 0 to 100.\n')


def ask_for_name():
    loop = True
    while loop == True:
        name = input("\nType the student's name: ")
        for char in name:
            if not char.isalpha():
                print('\nPlease, enter a valid name for a student.')
            else:
                return name


def ask_for_classroom():
    loop = True
    while loop == True:
        classroom = input('Type their classroom: ')
        number = classroom[0]
        letter = classroom[1]

        if len(classroom) > 2:
            print('\nPlease, enter a valid classroom: first a number followed by a letter.\n')
        elif number.isdigit():
            if letter.isalpha():
                return classroom
            else:
                print('\nPlease, enter a valid classroom: first a number followed by a letter.\n')
        else:
            print('\nPlease, enter a valid classroom: first a number followed by a letter.\n')



def add_student():
    student = {
        'Name':ask_for_name(),
        'Classroom':ask_for_classroom(),
        'Spanish Grade':ask_for_grade('Spanish'),
        'English Grade':ask_for_grade('English'),
        'Social Studies Grade':ask_for_grade('Social Studies'),
        'Science Grade':ask_for_grade('Science')
    }
    return student


def average_note_every_student(list):
    list_of_students = list
    list_of_average_notes = []
    counter = 0

    for student in list_of_students:
        list_of_average_notes.append({'Name':student['Name'],'Average Grade':(int(student['Spanish Grade'])+int(student['English Grade'])+int(student['Social Studies Grade'])+int(student['Science Grade']))/4})
    sorted_list = sorted(list_of_average_notes, key=lambda item:item['Average Grade'], reverse=True)
    for value in sorted_list:
        if counter < 3:
            print('The top 3 students are:\n')
            print(value)
            counter += 1


def average_note_all_students(list):
    list_of_students = list
    total_average_note = 0
    total_grades_number = 0

    for student in list_of_students:
        total_average_note = total_average_note + (int(student['Spanish Grade'])+int(student['English Grade'])+int(student['Social Studies Grade'])+int(student['Science Grade']))
        total_grades_number += 4
    
    total_average_note = total_average_note / total_grades_number
    print(f'\nThe average value of all students grades is: {total_average_note}')