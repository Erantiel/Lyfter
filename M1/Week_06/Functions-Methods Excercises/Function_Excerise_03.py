def sum_of_numbers(list_of_numbers):
    total_sum = 0
    for number in list_of_numbers:
        total_sum = total_sum + number
    return print(total_sum)


def main():
    list_of_numbers = [11,27,31,49,]
    sum_of_numbers(list_of_numbers)


main()