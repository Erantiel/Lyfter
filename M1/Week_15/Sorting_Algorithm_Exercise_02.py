def bubble_sort(list):
    bubble = 0
    for index in range(len(list) - 1, 0, -1):
        changes = False
        for position in range(len(list) - 1, 0 + bubble, -1):
            current_element = list[position]
            previous_element = list[position - 1]

            print(f'--Iteration {index},{position}. Current element: {current_element}. Previous element: {previous_element}.')

            if previous_element > current_element:
                print('The previous element is higher than the current element. Interchanging...')
                list[position] = previous_element
                list[position - 1] = current_element
                changes = True
        bubble += 1
    if not changes:
        return


list_a = [71, -34, 11, 1, 110, 45, -12]
list_b = [1,2,3,5,4]
bubble_sort(list_a)
print(list_a)
bubble_sort(list_b)
print(list_b)