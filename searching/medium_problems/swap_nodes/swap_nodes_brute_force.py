from searching.medium_problems.swap_nodes.classes.Tree import Tree
from searching.medium_problems.swap_nodes.classes.TreeFactory import TreeFactory
from searching.medium_problems.swap_nodes.classes.IndicesPartitioner import IndicesPartitioner


# TODO: Refactor to create a query processor class, and reduce scope of Tree to only worry about swapping and holding
#  root
def swap_nodes_brute_force(indices: list, queries: list) -> list:
    indices_partitioner: IndicesPartitioner = IndicesPartitioner(indices)
    partitioned_indices: list = indices_partitioner.partition_indices()

    tree_factory: TreeFactory = TreeFactory()
    tree_factory.construct_tree_with(partitioned_indices)
    tree: Tree = tree_factory.get_constructed_tree()

    tree.process_swap_queries(queries)
    tree.perform_swap_operations_with_all_processed_queries()

    return tree.results
