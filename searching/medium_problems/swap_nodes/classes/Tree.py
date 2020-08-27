from math import log

from searching.medium_problems.swap_nodes.classes.Node import Node
# TODO: Create test cases for tree class and node class and implement the tree class
# TODO: Try Iterative approach
    #TODO: fix partitioner of indices


class Tree:

    def __init__(self):
        self.root = Node(1)
        self.tree_levels: list = []
        self.leveled_indices: list = []
        self.traversal_path: list = []

    def construct_with(self, indices: list):
        self.partition_indices_into_levels(indices)

    def partition_indices_into_levels(self, indices: list):
        indices_length: int = len(indices)
        number_of_tree_levels: int = int(log(indices_length + 1, 2))
        partitioned_indices: list = []
        for level in range(number_of_tree_levels):
            start_index: int = 2**level - 1
            size: int = 2**level
            end_index: int = start_index + size
            partition: list = indices[start_index: end_index]
            partitioned_indices.append(partition)
        self.leveled_indices = partitioned_indices

    def construct_tree_levels_with(self, leveled_indices: list):
        pass

    def get_in_order_traversal(self) -> list:
        self.traversal_path.clear()
        return self.traversal_path

