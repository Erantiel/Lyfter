my_list = [0,1,2,3,4,5,6,7,8,9,10,11,11,11,11,11,11,11,11]
index = 0

while (index < len(my_list)):
    if my_list[index] % 2 == 1:
        my_list.pop(index)
    elif my_list[index] % 2 == 0:
        index += 1

print(my_list)