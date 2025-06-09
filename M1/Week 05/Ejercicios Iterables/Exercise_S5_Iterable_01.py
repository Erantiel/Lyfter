first_list = ["Printing","lists","one","the","is","but"]
second_list = ["two","alternating","after","other","weird","functional"]

index = 0

for list_one in first_list:
	while (index < len(second_list)):
		word = second_list[index]
		print(f"{list_one} {word}")
		index += 1
		break