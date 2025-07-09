from datetime import datetime

def bubble_sort(list):
    start_time = datetime.now()
    for index in range(0, len(list) - 1):
        changes = False
        for position in range(0, len(list) - 1 - index):
            current_element = list[position]
            next_element = list[position + 1]

            if current_element > next_element:
                list[position] = next_element
                list[position + 1] = current_element
                changes = True
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f'Time taken to complete the cycle: {elapsed_time}')
    if not changes:
        return


list_a = [71, -34, 11, 1, 110, 45, -12]
list_b = [1,2,3,5,4]
print('Starting first execution...')
bubble_sort(list_a)
print(f'First execution results: {list_a}')
print('Starting second execution...')
bubble_sort(list_b)
print(f'Second execution results: {list_b}')