first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number == 30 or second_number == 30 or third_number == 30:
    print("Correct.")
elif first_number + second_number + third_number == 30:
    print("Correct.")
else:
    print("Incorrect.")