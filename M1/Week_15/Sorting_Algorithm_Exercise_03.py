class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, head):
        self.head = head
        self.size = 0


    def print_structure(self):
        current_node = self.head
        if current_node is not None:
            while (current_node is not None):
                print(current_node.data)
                current_node = current_node.next
        else:
            print(current_node)


    def push(self, node):
        current_node = node
        current_node.next = self.head
        self.head = current_node
        self.size += 1


    def pop(self):
        current_node = self.head
        top = current_node.next
        self.head = top


    def bubble_sort(self, last_node):
        for index in range(0, self.size):
            node = last_node
            changes = False
            for position in range(0, self.size - index):
                node_current = node.data
                node_next = node.next.data
                if node.data < node.next.data:
                    node.data = node_next
                    node.next.data = node_current
                    changes = True
                node = node.next
        if not changes:
            return


forth_node = Node(56)
third_node = Node(2)
second_node = Node(21)
first_node = Node(78)

structure = Stack(first_node)
structure.push(second_node)
structure.push(third_node)
structure.push(forth_node)
structure.print_structure()
structure.bubble_sort(forth_node)
print('Sorting the stack...')
structure.print_structure()