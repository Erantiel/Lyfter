def print_info(func):
    def wrapper(*args):
        try:
            for index, arg in enumerate(args):
                float(arg)
                print(f'Number {index+1} = {arg}')
            result = func(*args)
            return result
        except ValueError:
            return print('Error. Please input a valid number.')
        except TypeError:
            return print('Error. Do not use a string to input a number.')

    return wrapper

@print_info
def sum(number_1, number_2):
    if number_1 == int and number_2 == int:
        print('This function is about to execute a sum...')
    return number_1 + number_2

print(sum(2,3))