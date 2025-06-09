highest_number = 0

for countdown in range(3):
    user_number = int(input("Enter a number up to 3 times to find out which is the largest: "))
    if user_number > highest_number:
        highest_number = user_number

print(f'The highest number among those admitted is: {highest_number}.')