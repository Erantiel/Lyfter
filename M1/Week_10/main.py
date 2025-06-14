import menu
import data
import actions

def main():
    student_list = []
    loop = True
    
    
    while loop  == True:
        option_selected = menu.menu()
        if option_selected == 1:
            student_list.append(actions.add_student())
        elif option_selected == 2:
            if student_list == []:
                print('\nPlease, first import the file in order to read it.')
            else:
                for student in student_list:
                    print(f'{student}\n')
        elif option_selected == 3:
            if student_list == []:
                print('\nPlease, first import the file in order to evaluate the top 3 students.')
            else:
                actions.average_note_every_student(student_list)
        elif option_selected == 4:
            if student_list == []:
                print('\nPlease, first import the file in order to evaluate average note of all students.')
            else:
                actions.average_note_all_students(student_list)
        elif option_selected == 5:
            if student_list == []:
                print('\nNo data to export. First add a student or import a file in order to export anything.')
            else:
                data.write_csv_file('M1/Week_10/Students_Notes.csv',student_list)
        elif option_selected == 6:
            student_list = data.open_csv_file('M1/Week_10/Students_Notes.csv')
        else:
            quit()


main()