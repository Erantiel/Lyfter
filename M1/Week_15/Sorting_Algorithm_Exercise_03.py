class Node:
    data: str
    next: float

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head):
            self.head = head
            self.size = 2

    def print_structure(self):
        current_node = self.head
            
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def bubble_sort(self):
        for index in range(0, self.size):
            node = self.head
            changes = False
            for position in range(0, self.size - index):
                node_current = node.data
                node_next = node.next.data
                if node.data > node.next.data:
                    node.data = node_next
                    node.next.data = node_current
                    changes = True
                node = node.next
        if not changes:
            return


third_node = Node(15)
second_node = Node(-12, third_node)
first_node = Node(76, second_node)

structure = LinkedList(first_node)
structure.print_structure()
print('Sorting the Linked List...')
structure.bubble_sort()
structure.print_structure()