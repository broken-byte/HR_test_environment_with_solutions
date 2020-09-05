from math import log

from searching.medium_problems.swap_nodes.classes.Node import Node
# TODO: Currently, every swap only reorganizes the child level in a parent swap. the lower levels wont be in order.
#       Fix this.


class Tree:

    def __init__(self):
        self.root = Node(1)
        self.indices: list = []
        self.partitioned_indices: list = []
        self.tree_levels: list = []
        self.processed_queries: list = []
        self.depth: int = 0
        self.in_order_traversal_path: list = []
        self.in_order_traversal_paths: list = []

    def perform_in_order_traversal(self, current_node: Node):
        if current_node.left is not None:
            self.perform_in_order_traversal(current_node.left)

        self.in_order_traversal_path.append(current_node.data)

        if current_node.right is not None:
            self.perform_in_order_traversal(current_node.right)

    def perform_swaps_with(self, level_indices_to_be_swapped: list):
        for tree_level_index in level_indices_to_be_swapped:
            self.swap_nodes_in_tree_level_with(tree_level_index - 1)  # level indices start at 0

    def swap_nodes_in_tree_level_with(self, tree_level_index: int):
        i: int = 0
        j: int = 1
        parents: list = self.tree_levels[tree_level_index]
        children: list = self.tree_levels[tree_level_index + 1]
        while j <= len(children):
            self.swap_child_nodes_at(i, j, tree_level_index + 1)
            i += 2
            j += 2
        self.connect(parents, children)

    def swap_child_nodes_at(self, i: int, j, tree_level):
        self.tree_levels[tree_level][i], self.tree_levels[tree_level][j] = self.tree_levels[tree_level][j], \
                                                                           self.tree_levels[tree_level][i]

    def process_swap_queries(self, queries: list):
        for k in queries:
            depths_to_be_swapped: list = []
            multiple: int = 1
            product: int = multiple*k
            while product <= self.depth:
                depths_to_be_swapped.append(product)
                multiple += 1
                product = multiple * k
            self.processed_queries.append(depths_to_be_swapped)

    def construct_with(self, indices: list):
        self.indices = indices
        self.partition_indices_into_levels()
        self.construct_tree_levels_with_partitioned_indices()
        self.connect_levels()
        self.depth = len(self.tree_levels) - 1

    def partition_indices_into_levels(self):
        indices_length: int = len(self.indices)
        current_index: int = 0
        number_of_non_null_nodes_in_previous_level: int = 1
        while current_index < indices_length:
            partition = self.construct_partition_with(current_index, number_of_non_null_nodes_in_previous_level)
            self.partitioned_indices.append(partition)
            current_index += len(partition) // 2
            number_of_non_null_nodes_in_previous_level = self.get_non_null_node_count_in(partition)

    def construct_tree_levels_with_partitioned_indices(self):
        self.tree_levels.append([self.root])
        for indices_partition in self.partitioned_indices:
            nodes: list = self.construct_nodes_with(indices_partition)
            self.tree_levels.append(nodes)

    def connect_levels(self):
        connection_i: int = 0
        connection_j: int = 1
        number_of_connection_steps: int = len(self.tree_levels) - 1
        for _ in range(number_of_connection_steps):
            parents: list = self.tree_levels[connection_i]
            children: list = self.tree_levels[connection_j]
            self.connect(parents, children)
            connection_i += 1
            connection_j += 1

    def construct_partition_with(self, current_index: int, count_of_non_null_nodes_in_previous_level: int) -> list:
        start_index: int = current_index
        size: int = count_of_non_null_nodes_in_previous_level
        end_index: int = start_index + size
        sequential_partition: list = []
        for index in range(start_index, end_index):
            sequential_partition.extend(self.indices[index])
        return sequential_partition

    @staticmethod
    def get_non_null_node_count_in(partition: list):
        non_node_count: int = 0
        for data in partition:
            if data != -1:
                non_node_count += 1
        return non_node_count

    @staticmethod
    def construct_nodes_with(indices_partition) -> list:
        nodes: list = []
        for data in indices_partition:
            node: Node = Node(data) if data != -1 else None
            nodes.append(node)
        return nodes

    @staticmethod
    def connect(parents: list, children: list):
        left_child_index: int = 0
        right_child_index: int = 1
        for parent in parents:
            if parent is not None:
                parent.left = children[left_child_index]
                parent.right = children[right_child_index]
                left_child_index += 2
                right_child_index += 2
