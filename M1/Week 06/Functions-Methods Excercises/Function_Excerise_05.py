def catch_lower_upper_case(string):
    upper_letters = 0
    lower_letters = 0

    for char in string:
        if char.isupper():
            upper_letters += 1
        elif char.islower():
            lower_letters += 1
        else:
            error = "Catching spaces, numbers and special characters is too much work for now. I know the user can be stupid but maybe another day when the topic is relevant."
            
    return print(f'There are {upper_letters} upper cases and {lower_letters} lower cases in the phrase: {string}')

def main():
    string = "Text with lower And Uppper Cases."
    catch_lower_upper_case(string)

main()