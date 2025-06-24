def print_info(func):
    def wrapper(*args):
        for index, arg in enumerate(args):
            print(f'Number {index+1} = {arg}')
        result = func(*args)
        print(f'Result = {result}')

    return wrapper

@print_info
def sum(number_1, number_2):
    print('This function is about to execute a sum...')
    return number_1 + number_2


sum(2,5)