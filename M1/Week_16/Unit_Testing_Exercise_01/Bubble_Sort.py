def bubble_sort(list):
    try:
        changes = False
        for index in range(0, len(list) - 1):
            changes = False
            for position in range(0, len(list) - 1 - index):
                current_element = list[position]
                next_element = list[position + 1]

                if current_element > next_element:
                    list[position] = next_element
                    list[position + 1] = current_element
                    changes = True
        if not changes:
            return
    except TypeError as e:
        return TypeError

list = False
result = bubble_sort(list)
print(result)