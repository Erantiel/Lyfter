class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, head):
        self.head = head


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


    def pop(self):
        current_node = self.head
        top = current_node.next
        self.head = top


forth_node = Node("Forth node")
third_node = Node("Third node")
second_node = Node("Second node")
first_node = Node("First node")

structure = Stack(first_node)
print('---Adding to the Stack---')
structure.push(second_node)
structure.push(third_node)
structure.push(forth_node)
structure.print_structure()
print(f'---This is the First Value: {forth_node.data}.---')
print('---Deleting from the Stack---')
structure.pop()
structure.print_structure()
print('---Deleting One More---')
structure.pop()
structure.print_structure()
print('---Reaching the Last Value---')
structure.pop()
structure.print_structure()
print('---No more values---')
structure.pop()
structure.print_structure()