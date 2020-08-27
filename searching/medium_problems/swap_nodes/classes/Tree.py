from math import log

from searching.medium_problems.swap_nodes.classes.Node import Node
# TODO: Change level constructor so that it appends sequentially, not in pairs, since everything is in order
# TODO: Connect levels
# TODO: Create Swap function


class Tree:

    def __init__(self):
        self.root = Node(1)
        self.indices: list = []
        self.partitioned_indices: list = []
        self.tree_levels: list = []
        self.traversal_path: list = []

    def construct_with(self, indices: list):
        self.indices = indices
        self.partition_indices_into_levels()
        self.construct_tree_levels_with_partitioned_indices()
        self.connect_levels()

    def partition_indices_into_levels(self):
        indices_length: int = len(self.indices)
        number_of_tree_levels: int = int(log(indices_length + 1, 2))
        for level_number in range(number_of_tree_levels):
            partition = self.construct_partition_with(level_number)
            self.partitioned_indices.append(partition)

    def construct_tree_levels_with_partitioned_indices(self):
        self.tree_levels.append([self.root])
        for indices_partition in self.partitioned_indices:
            nodes: list = self.construct_nodes_with(indices_partition)
            self.tree_levels.append(nodes)

    def connect_levels(self):
        pass

    def construct_partition_with(self, level_number: int) -> list:
        start_index: int = 2 ** level_number - 1
        size: int = 2 ** level_number
        end_index: int = start_index + size
        partition: list = self.indices[start_index: end_index]
        return partition

    @staticmethod
    def construct_nodes_with(indices_partition) -> list:
        nodes: list = []
        for index_pair in indices_partition:
            left = Node(index_pair[0]) if index_pair[0] != -1 else None
            right = Node(index_pair[1]) if index_pair[1] != -1 else None
            node_pair = left, right
            nodes.append(node_pair)
        return nodes

    def get_in_order_traversal(self) -> list:
        self.traversal_path.clear()
        return self.traversal_path

