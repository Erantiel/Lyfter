def check_numeric(func):
    def wrapper(*args):
        for index, arg in enumerate(args):
            try:
                float(arg)
                print(f'Arg: {index}, Number: {arg}')
            except ValueError:
                print(f'The input <{arg}> is not a number.')
        func(*args)
    return wrapper

@check_numeric
def arguments(argument_1, argument_2,argument_3):
    pass


arguments(2,'H','4')