my_list = []
countdown = 10
highest_number = 0

for index in range(0,countdown):
    current_number = int(input(f"Type a number up to {countdown} time(s): "))
    countdown -= 1
    my_list.append(current_number)
    if current_number > highest_number:
        highest_number = current_number

print(f"{my_list}. The highest number entered was: {highest_number}.")
