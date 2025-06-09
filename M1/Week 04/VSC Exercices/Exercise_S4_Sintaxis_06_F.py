sex = 0
man = 0
woman = 0
countdown_times = 6

for countdown in range(6):
    sex = int(input(f'Enter 1 for female or 2 for male up to {countdown_times} time(s): '))
    while sex != 1 and sex != 2:
        sex = int(input(f'Error! Not valid number. Enter 1 for female or 2 for male up to {countdown_times} times: '))
    if sex == 1:
        woman = woman + 1
        countdown_times = countdown_times - 1
    elif sex == 2:
        man = man + 1
        countdown_times = countdown_times - 1

print(f'The percentage of men is: {man*100/6}%. The percentage of women is: {woman*100/6}%.')