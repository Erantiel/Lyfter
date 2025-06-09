def reverse_string_char(string):
    for index in range(len(string)-1,-1,-1):
        print(string[index], end="")


def main():
    string = ".desrever txeT"
    reverse_string_char(string)


main()