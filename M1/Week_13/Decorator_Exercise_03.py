class User:
    def __init__(self, date_of_birth, age):
        self.date_of_birth = date_of_birth
        self.age = age


def is_adult(func):
    def wrapper(name, user):
        try:
            age = int(user.age)
            if age < 18:
                return print(f'{name} is not an adult.\n')
            else:
                func(name, user)
                return print(f'{name} is an adult.\n')
        except TypeError:
            return print(f'The input <{user.age}> is not a valid age. Please, do not be dumb and type a valid age/number.\n')
        except ValueError:
            return print(f'The input <{user.age}> is not a valid age. Please, do not be dumb and type a valid age/number.\n')
    return wrapper

@is_adult
def set_name(name, user):
    return print(f'The person {name} with date of birth {user.date_of_birth} is {user.age} years old.\n')


user_01 = User('27/11/1996', 28)
user_02 = User('16/09/2010', '14')
set_name('Carlos', user_01)
set_name('Ana', user_02)


