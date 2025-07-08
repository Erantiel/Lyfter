from Bubble_Sort import bubble_sort
import random

def test_bubble_sort_small_list_sort():
    # Arrange
    list_to_test = [7,4,2]
    list_to_compare = [7,4,2]
    # Act
    bubble_sort(list_to_test)
    list_to_compare.sort()
    # Assert
    assert list_to_test == list_to_compare


def test_bubble_sort_big_list_over_100_elements_sort():
    # Arrange
    list_to_test = []
    list_to_compare = []
    for index in range (0,150):
        random_number = random.randint(0,150)
        list_to_test.append(random_number)
        list_to_compare.append(random_number)
    # Act
    bubble_sort(list_to_test)
    list_to_compare.sort()
    # Assert
    assert list_to_test == list_to_compare


def test_bubble_sort_empty_list_sort():
    # Arrange
    list_to_test = []
    # Act
    result = bubble_sort(list_to_test)
    # Assert
    assert result ==  None


def test_bubble_sort_no_list_element_sort():
    # Arrange
    list_to_test = 1
    # Act
    result = bubble_sort(list_to_test)
    # Assert
    assert result ==  TypeError