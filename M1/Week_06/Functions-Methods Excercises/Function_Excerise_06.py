def order_words_alphabetically_using_hyphen(string):
    list_of_words = string.split('-')
    list_of_words.sort()
    return print('-'.join(list_of_words))

def main():
    string = 'watermelon-kiwi-apple-orange'
    order_words_alphabetically_using_hyphen(string)


main()