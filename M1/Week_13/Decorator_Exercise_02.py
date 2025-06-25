def check_numeric(func):
    def wrapper(*args):
        result = func(*args)
        for index, arg in enumerate(args):
            try:
                float(arg)
            except ValueError:
                print(f'The input <{arg}> is not a number.')
                try:
                    result.pop(index)
                except AttributeError:
                    pass
        return result
    return wrapper

@check_numeric
def arguments(*args):
    list_of_arg = []
    for index, arg in enumerate(args):
        list_of_arg.append(arg)
    return list_of_arg

@check_numeric
def no_return_list(*args):
    for index, arg in enumerate(args):
        return arg

result = arguments(2,'H','4')
print(result)

no_list = no_return_list('K')
print(no_list)
