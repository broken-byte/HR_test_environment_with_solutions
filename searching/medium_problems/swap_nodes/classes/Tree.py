from searching.medium_problems.swap_nodes.classes.Node import Node


class Tree:

    def __init__(self):
        self.root = None
        self.tree_levels: list = []
        self.depth: int = 0
        self.in_order_traversal_path: list = []
        self.results: list = []

    def perform_swap_operations_with_(self, processed_queries: list):
        for processed_query in processed_queries:
            self.perform_swap_operations_with(processed_query)
            self.perform_in_order_traversal(self.root)
            result: list = self.in_order_traversal_path.copy()
            self.results.append(result)
            self.in_order_traversal_path.clear()

    def perform_swap_operations_with(self, processed_query: list):
        for tree_level_index in processed_query:
            self.swap_nodes_in_tree_level_with(tree_level_index - 1)  # level indices start at 0

    def swap_nodes_in_tree_level_with(self, tree_level_index: int):
        parents: list = self.tree_levels[tree_level_index]
        for parent_node in parents:
            if parent_node is not None:
                parent_node.left, parent_node.right = parent_node.right, parent_node.left

    def perform_in_order_traversal(self, current_node: Node):
        if current_node.left is not None:
            self.perform_in_order_traversal(current_node.left)

        self.in_order_traversal_path.append(current_node.data)

        if current_node.right is not None:
            self.perform_in_order_traversal(current_node.right)
