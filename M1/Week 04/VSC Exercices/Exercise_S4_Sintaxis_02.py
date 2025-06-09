name = input("Type your name: ")
last_name = input("Type your last name: ")
age = int(input("Type your age: "))

if age < 2:
    age_range = "baby"
elif age < 9:
    age_range = "child"
elif age < 12:
    age_range = "pre-adolescent"
elif age < 18:
    age_range = "adolescent"
elif age < 30:
    age_range = "young adult"
elif age < 60:
    age_range = "adult"
else:
    age_range = "senior citizen"

print(f'{name} {last_name} which is {age} year(s) old is a(n) {age_range}.')