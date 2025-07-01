class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoubleEndedQueue:
    def __init__(self, head):
        self.head = head
        self.tail = None


    def print_structure(self):
        current_node = self.head
        if current_node is not None:
            while (current_node is not None):
                print(current_node.data)
                current_node = current_node.next
        else:
            print(current_node)


    def push_right(self, node):
        current_node = self.head

        while (current_node.next is not None):
            current_node = current_node.next
        
        current_node.next = node


    def push_left(self, node):
        current_node = self.head
        self.head = node
        self.head.next = current_node


    def pop_right(self):
        current_node = self.head

        while (current_node is not None):
            top = current_node
            current_node = current_node.next
        
        current_node = self.head
        while (current_node.next != top and current_node.next is not None):
            current_node = current_node.next
        if current_node.next is not None:
            current_node.next = None
        else:
            current_node.data = None


    def pop_left(self):
        if self.head:
            self.head = self.head.next


forth_node = Node("Forth node")
third_node = Node("Third node")
second_node = Node("Second node")
first_node = Node("First node")
negative_01 = Node("-1")
negative_02 = Node("-2")

structure = DoubleEndedQueue(first_node)
print('---Adding to the right---')
structure.push_right(second_node)
structure.push_right(third_node)
structure.push_right(forth_node)
structure.print_structure()
print('---Adding to the left---')
structure.push_left(negative_01)
structure.push_left(negative_02)
structure.print_structure()
print('---Deleting from right---')
structure.pop_right()
structure.print_structure()
print('---Deleting from left---')
structure.pop_left()
structure.print_structure()