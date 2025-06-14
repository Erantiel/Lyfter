grade_countdown = 0
approved = 0
not_approved = 0
average_grade = 0
average_approved = 0
average_not_approved = 0
average_passsing = 0
average_failing = 0

grade_amount = int(input("Enter the number of notes: "))

while grade_countdown < grade_amount:
    grade_countdown = grade_countdown + 1
    grade = int(input(f'Enter the grade #{grade_countdown}: '))
    if grade > 69:
        approved = approved + 1
        average_grade = average_grade + grade
        average_approved = average_approved + grade
    else:
        not_approved = not_approved + 1
        average_grade = average_grade + grade
        average_not_approved = average_not_approved + grade

try:
    average_passsing = average_approved/approved
except ZeroDivisionError:
    print("0")

try:
    average_failing = average_not_approved/not_approved
except ZeroDivisionError:
    print("0")

print(f'The number of approved notes is: {approved} and the number of failed notes is: {not_approved}.'\
      f'The total grade point average is: {average_grade/grade_amount}.'\
      f'The average of passing grades is: {average_passsing} and the average of failing grades is: {average_failing}.')