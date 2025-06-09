def catch_value_error(number):
    data = {
        'Integer' : 0,
        'Validation' : True 
    }
    try:
        data['Integer'] = int(number)
        data['Validation'] = False
        return data
    except ValueError as ex:
        print(f'\nError [ValueError]: Input is not an integer number. \nDetails: {ex}')
        return data
        

def ask_current_number():
    data = {
        'Integer' : 0,
        'Validation' : True
    }
    while data['Validation'] == True:
        data = catch_value_error(input('\nType a number: '))
    return data['Integer']

def ask_operation_method():
    data = {
        'Integer' : 0,
        'Validation' : True
    }
    while data['Validation'] == True:
        try:
            data = catch_value_error(input('\nWhat do you want to do: \n1) Add\n2) Subtract\n3) Multiply\n4) Divide\n5) Start Again\n'))
            if data['Integer'] < 1 or data['Integer'] > 5:
                raise ValueError()
        except ValueError:
            print('\nThe value entered is not in between 1 and 5. Enter a valid number.')
            data['Validation'] = True
    return data['Integer']

def ask_second_number():
    data = {
        'Integer' : 0,
        'Validation' : True
    }
    while data['Validation'] == True:
        data = catch_value_error(input('\nType a number: '))
    return data['Integer']


def processs_method_entered(current_number, option_selected, second_number):
        if option_selected == 1:
            return current_number + second_number
        elif option_selected == 2:
            return current_number - second_number
        elif option_selected == 3:
            return current_number * second_number
        elif option_selected == 4:
            return current_number / second_number

def main():
    try:
        status = True
        while status == True:
            current_number = 0
            option_selected = 0
            current_number = ask_current_number()
            while option_selected < 5:
                option_selected = ask_operation_method()
                if option_selected < 5:
                    second_number = ask_second_number()
                    try:
                        current_number = processs_method_entered(current_number, option_selected, second_number)
                        print(f'\nThe total is: {current_number}')
                    except ZeroDivisionError as ex:
                        print(f'\nError [ZeroDivisionError]: You tried to devide {current_number} by {second_number} and this is not possible. Details: {ex}')
    except Exception as ex:
        print({ex})


main()