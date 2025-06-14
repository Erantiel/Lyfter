list_a = ["Country:","Province:","City:"]
list_b = ["Costa Rica","Alajuela","Palmares"]
address = {}
position = 0

for location in list_a:
    for index, value in enumerate(list_b):
        address[location] = value
        if position == index:
            position += 1
            break

print(address)