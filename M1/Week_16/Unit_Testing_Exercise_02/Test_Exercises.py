import Exercises

def test_ex_03_sum_list_positive_numbers():
    # Arrange
    list = [1,2,3]
    # Act
    result = Exercises.ex_03_sum_list(list)
    # Assert
    assert result == 6


def test_ex_03_sum_list_negative_numbers():
    # Arrange
    list = [-1,-2,-3]
    # Act
    result = Exercises.ex_03_sum_list(list)
    # Assert
    assert result == -6


def test_ex_03_sum_list_positive_and_negative_numbers():
    # Arrange
    list = [-1,-2,-3,3,2,1]
    # Act
    result = Exercises.ex_03_sum_list(list)
    # Assert
    assert result == 0


def test_ex_04_reverse_string_short_string():
    # Arrange
    string = 'Camera'
    reversed_string = string[::-1]
    # Act
    result = Exercises.ex_04_reverse_string(string)
    # Assert
    assert result == reversed_string


def test_ex_04_reverse_string_with_spaces():
    # Arrange
    string = 'Hello World'
    reversed_string = string[::-1]
    # Act
    result = Exercises.ex_04_reverse_string(string)
    # Assert
    assert result == reversed_string


def test_ex_04_reverse_string_with_numbers_type_error():
    # Arrange
    string = 245
    # Act
    result = Exercises.ex_04_reverse_string(string)
    # Assert
    assert result == TypeError


def test_ex_05_number_of_upper_and_lower_cases_only_upper_case():
    # Arrange
    string = 'HELLO'
    # Act
    result = Exercises.ex_05_number_of_upper_and_lower_cases(string)
    # Assert
    assert result == f'\nString: {string}. \nUpper case letters: 5. \nLower case letters: 0'


def test_ex_05_number_of_upper_and_lower_cases_only_lower_case():
    # Arrange
    string = 'hello'
    # Act
    result = Exercises.ex_05_number_of_upper_and_lower_cases(string)
    # Assert
    assert result == f'\nString: {string}. \nUpper case letters: 0. \nLower case letters: 5'


def test_ex_05_number_of_upper_and_lower_cases_ignores_special_characters():
    # Arrange
    string = 'Hello??!!'
    # Act
    result = Exercises.ex_05_number_of_upper_and_lower_cases(string)
    # Assert
    assert result == f'\nString: {string}. \nUpper case letters: 1. \nLower case letters: 4'


def test_ex_06_order_words_alphabetically_using_hyphen_only_strings():
    # Arrange
    string = 'Zac-Animal-Bus'
    # Act
    result = Exercises.ex_06_order_words_alphabetically_using_hyphen(string)
    # Assert
    assert result == 'Animal-Bus-Zac'

def test_ex_06_order_words_alphabetically_using_hyphen_with_numbers_as_string():
    # Arrange
    string = 'Zac-Animal-75'
    # Act
    result = Exercises.ex_06_order_words_alphabetically_using_hyphen(string)
    # Assert
    assert result == '75-Animal-Zac'


def test_ex_06_order_words_alphabetically_using_hyphen_with_special_characters():
    # Arrange
    string = 'Zac-Animal-?'
    # Act
    result = Exercises.ex_06_order_words_alphabetically_using_hyphen(string)
    # Assert
    assert result == '?-Animal-Zac'


def test_ex_07_number_is_prime_number_is_neither_prime_nor_composite():
    # Arrange
    list_of_numbers = [1,2,3]
    # Act
    result = Exercises.ex_07_number_is_prime(list_of_numbers)
    # Assert
    assert result != f'The following numbers are the prime numbers found inside the list entered: {list_of_numbers}'


def test_ex_07_number_is_prime_number_small_list():
    # Arrange
    list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    # Act
    result = Exercises.ex_07_number_is_prime(list_of_numbers)
    # Assert
    assert result == f'The following numbers are the prime numbers found inside the list entered: [2, 3, 5, 7, 11, 13]'


def test_ex_07_number_is_prime_number_big_list():
    # Arrange
    list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    # Act
    result = Exercises.ex_07_number_is_prime(list_of_numbers)
    # Assert
    assert result == f'The following numbers are the prime numbers found inside the list entered: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]'