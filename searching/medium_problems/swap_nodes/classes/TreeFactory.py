from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree


class TreeFactory:

    def __init__(self):
        self.tree_root = None
        self.partitioned_indices: list = []
        self.tree_levels: list = []

    def get_constructed_tree(self) -> Tree:
        constructed_tree: Tree = Tree()
        constructed_tree.root = self.tree_root
        constructed_tree.tree_levels = self.tree_levels.copy()
        constructed_tree.depth = len(self.tree_levels) - 1
        return constructed_tree

    def construct_tree_with(self, partitioned_indices: list):

        self.tree_root: Node = Node(1)
        self.partitioned_indices = partitioned_indices
        self.construct_tree_levels_with_partitioned_indices()
        self.connect_levels()

    def construct_tree_levels_with_partitioned_indices(self):
        self.tree_levels.append([self.tree_root])
        for indices_partition in self.partitioned_indices:
            nodes: list = self.construct_nodes_with(indices_partition)
            self.tree_levels.append(nodes)

    @staticmethod
    def construct_nodes_with(indices_partition) -> list:
        nodes: list = []
        for data in indices_partition:
            node: Node = Node(data) if data != -1 else None
            nodes.append(node)
        return nodes

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
        left_child_index: int = 0
        right_child_index: int = 1
        for parent in parents:
            if parent is not None:
                parent.left = children[left_child_index]
                parent.right = children[right_child_index]
                left_child_index += 2
                right_child_index += 2

