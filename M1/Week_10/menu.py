def menu():
    option_selected = 0
    loop = True
    while loop == True:
        try:
            option_selected = int(input('\nSelect one of the following in order to continue:\n1.Add Student.\n2.See all students information.' \
            '\n3.Top 3 students with the best average grade.\n4.See an average grade of all students.\n5.Export data.\n6.Import data.\n7.Close program.\n'))
            if option_selected < 1  or option_selected > 7:
                raise ValueError()
            return option_selected
        except ValueError as e:
            print('\nTypo Error. Please, select a valid option.\n')