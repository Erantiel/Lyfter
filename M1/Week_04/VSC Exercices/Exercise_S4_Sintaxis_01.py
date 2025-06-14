string_variable = "String "
string_number_variable = "5"
integer_variable = 5
float_variable = 3.25
list_integer_variable = [1, 2, 3]
list_sting_variable = ["A", "B", "C"]
boolean_true_variable = True
boolean_false_variable = False

#Exercise examples: The f' method was not used because its logic allows for printing different data. The print statements commented out at the beginning are because they produce an error.

print(string_variable + string_variable) #Print the text twice in a row.
# print(string_variable + integer_variable) #This fails because you can only add string + string.
# print(integer_variable + string_variable) #This fails because you can only add integer + integer.
print(list_integer_variable + list_integer_variable) #Add the two lists together to create a single list.
#print(string_variable + list_integer_variable) #This fails because you can only add a string (that is not a list) to another string.
print(float_variable + integer_variable) #Adds the two variables and returns a float.
print(boolean_true_variable + boolean_false_variable) #Treats True as 1 and False as 0 which converts the sum to an integer and returns the result.

#Own variations-------------------------------------------------------------------------------------------------------------------

print(string_variable + str(integer_variable)) #Converts the integer to a string so it can be concatenated and give a result.
#print(integer_variable + int(string_variable)) #This only works if the sting is a number and not text.
print(integer_variable + int(string_number_variable)) #This does work since the text inside the sting is a number, however you can't add more numbers with spaces or commas.
print(list_integer_variable + list_sting_variable) #This joins lists into a single list even if the data types are not the same.
#print(string_variable + list_sting_variable) #This fails because you can only add a string (that is not a list) to another string.
print(boolean_true_variable + integer_variable) #This is possible because of how the boolean True is interpreted, which is displayed as 1.