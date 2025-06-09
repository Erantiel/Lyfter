def number_is_prime(list_of_numbers):
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
    return print(f'The following numbers are the prime numbers found inside the list entered: {prime_number_list}')
            

def main():
    list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    number_is_prime(list_of_numbers)


main()