list_of_keys = ["Name", "Email"]
employee = {
    "Name" : "John",
    "Email" : "john@ecorp.com",
    "Access Level" : 5,
    "Age" : 28
}

for name in list_of_keys:
    employee.pop(name)

print(employee)