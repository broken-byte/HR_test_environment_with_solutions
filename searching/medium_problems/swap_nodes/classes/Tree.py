from math import log

from searching.medium_problems.swap_nodes.classes.Node import Node
# TODO: implement self.connect()
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

    @staticmethod
    def connect(parents: list, children: list):
        for parent in parents:
            pass

    @staticmethod
    def get_non_null_node_count_in(partition: list):
        non_node_count: int = 0
        for data in partition:
            if data != -1:
                non_node_count += 1
        return non_node_count

    def construct_partition_with(self, current_index: int, count_of_non_null_nodes_in_previous_level: int) -> list:
        start_index: int = current_index
        size: int = count_of_non_null_nodes_in_previous_level
        end_index: int = start_index + size
        sequential_partition: list = []
        for index in range(start_index, end_index):
            sequential_partition.extend(self.indices[index])
        return sequential_partition

    @staticmethod
    def construct_nodes_with(indices_partition) -> list:
        nodes: list = []
        for data in indices_partition:
            node: Node = Node(data) if data != -1 else None
            nodes.append(node)
        return nodes

    def get_in_order_traversal(self) -> list:
        self.traversal_path.clear()
        return self.traversal_path

