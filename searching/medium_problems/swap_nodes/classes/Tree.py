from .Node import Node
# TODO: Create test cases for tree class and node class and implement the tree class
# TODO: Construct is not constructing properly, so use print statements/ debugger to see whats up


class Tree:

    def __init__(self):
        self.root = Node(1)
        self.indices: list = []
        self.traversal_path: list = []

    def construct_with(self, indices: list):
        pass
        # TODO: Will try iterative approach, this input style is sooooo confusing haha


    def get_in_order_traversal(self) -> list:
        self.traversal_path.clear()
        self.traverse(self.root)
        return self.traversal_path

    def traverse(self, current_node: Node):
        if current_node.left is not None:
            self.traverse(current_node.left)

        self.traversal_path.append(current_node.data)

        if current_node.right is not None:
            self.traverse(current_node.right)

