import random

random_number = random.randint(1, 10)
user_number = 0

while user_number != random_number:
    user_number = int(input("Guess the magic number between 1 and 10: "))
    if user_number == random_number:
        print(f'Correct! You guessed it right.')
    else:
        print(f'Bad luck guessing the number, try again.')