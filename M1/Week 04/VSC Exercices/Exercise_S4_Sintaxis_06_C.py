number = 0
countdown = 0
total = 0

while number == 0:
    number = int(input("Please enter a number greater than 0: "))

while number > countdown:
    countdown = countdown + 1
    total = total + countdown

print(f'The sum of the total numbers is: {total}')