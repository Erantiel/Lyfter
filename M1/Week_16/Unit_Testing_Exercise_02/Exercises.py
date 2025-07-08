def ex_03_sum_list(list):
    total_sum = 0
    for index in list:
        total_sum = total_sum + index
    return total_sum


def ex_04_reverse_string(string):
    try:
        new_string = ''
        for index in range(len(string)-1,-1,-1):
            new_string = new_string + string[index]
        return new_string
    except TypeError:
        return TypeError


def ex_05_number_of_upper_and_lower_cases(string):
    upper_case_letters = 0
    lower_case_letters = 0
    for index in range(0, len(string)):
        if string[index].isupper():
            upper_case_letters += 1
        elif string[index].islower():
            lower_case_letters += 1
    return f'\nString: {string}. \nUpper case letters: {upper_case_letters}. \nLower case letters: {lower_case_letters}'


def ex_06_order_words_alphabetically_using_hyphen(string):
    list_of_words = string.split('-')
    list_of_words.sort()
    return '-'.join(list_of_words)


def ex_07_number_is_prime(list_of_numbers):
    prime_number_list = []
    for number in list_of_numbers:
        if number == 1:
            print("The number 1 is neither prime or composite.")
            continue
        elif number == 2:
            prime_number_list.append(number)
        else:
            for divider in range (2, number):
                if number % divider == 0:
                    break
                elif number % divider == 1:
                    if number != divider+1:
                        continue
                    else:
                        prime_number_list.append(number)
                    break
    return f'The following numbers are the prime numbers found inside the list entered: {prime_number_list}'