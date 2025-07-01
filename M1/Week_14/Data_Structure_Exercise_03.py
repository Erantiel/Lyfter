class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'pre_order':
            return self.pre_order_print(structure.root, '')
        elif traversal_type == 'in_order':
            return self.in_order_print(structure.root, '')
        elif traversal_type == 'post_order':
            return self.post_order_print(structure.root, '')
        else:
            print('\nTraversal type ' +str(traversal_type) + " is not supported.\n")


    def pre_order_print(self, start, traversal):
        if start:
            traversal += (str(start.data) + " ")
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal


    def in_order_print(self, start, traversal):
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.data) + " ")
            traversal = self.in_order_print(start.right, traversal)
        return traversal


    def post_order_print(self, start, traversal):
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += (str(start.data) + " ")
        return traversal


structure = BinaryTree(1)
structure.root.left = Node(2)
structure.root.right = Node(3)
structure.root.left.left = Node(4)
structure.root.left.right = Node(5)
structure.root.right.left = Node(6)
structure.root.right.right = Node(7)
structure.root.right.right.right = Node(8)

print(structure.print_tree('pre_order'))
structure.print_tree('my_invented_order')
print(structure.print_tree('in_order'))
print(structure.print_tree('post_order'))