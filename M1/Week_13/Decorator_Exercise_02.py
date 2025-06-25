def check_numeric(func):
    def wrapper(*args):
        result = func(*args)
        counter = 0
        for index, arg in enumerate(args):
            try:
                float(arg)
                result.append({f'Arg {counter}':f'Number {arg}'})
                counter += 1
            except ValueError:
                print(f'The input <{arg}> is not a number.')
        return result
    return wrapper

@check_numeric
def arguments(*args):
    list_of_arg = []
    return list_of_arg

result =arguments(2,'H','4')
print(result)