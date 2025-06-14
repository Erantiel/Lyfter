my_list = [1,2,3,4,5,6,7,8,9]

first_deleted_position = my_list.pop(0)
last_deleted_position = my_list.pop(len(my_list)-1)

my_list.insert(0,last_deleted_position)
my_list.insert(len(my_list),first_deleted_position)

print(my_list)