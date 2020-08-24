from .Node import Node
# TODO: Create test cases for tree class and node class and implement the tree class


class Tree:

    def __init__(self):
        self.root = Node(1)
        self.indices: list = []

    def construct_with(self, indices: list):
        self.indices = [
                [2, 3],
                [-1, -1],
                [-1, -1]
            ]
        self.construct(self.root.data, 0)

    def construct(self, node_index: int, indices_reference):
        if node_index == -1:
            return

        node: Node
        if indices_reference == 0:
            node = self.root
        else:
            node = Node(node_index)
        # TODO: Check the indices lookups here, I think there's a chance that things might go out of range
        node.left = self.indices[indices_reference][0]
        self.construct(node.left, indices_reference + 1)

        node.right = self.indices[indices_reference][1]
        self.construct(node.right, indices_reference + 2)

    def get_in_order_traversal(self) -> list:
        return []
