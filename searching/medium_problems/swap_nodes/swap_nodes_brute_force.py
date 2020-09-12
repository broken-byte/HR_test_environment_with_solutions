from searching.medium_problems.swap_nodes.classes.Tree import Tree
from searching.medium_problems.swap_nodes.classes.TreeFactory import TreeFactory
from searching.medium_problems.swap_nodes.classes.IndicesPartitioner import IndicesPartitioner
from searching.medium_problems.swap_nodes.classes.QueryProcessor import QueryProcessor


# TODO: Refactor to create a query processor class, and reduce scope of Tree to only worry about swapping and holding
#  root/tree nodes
def swap_nodes_brute_force(indices: list, queries: list) -> list:
    indices_partitioner: IndicesPartitioner = IndicesPartitioner(indices)
    partitioned_indices: list = indices_partitioner.partition_indices()

    tree_factory: TreeFactory = TreeFactory()
    tree_factory.construct_tree_with(partitioned_indices)
    tree: Tree = tree_factory.get_constructed_tree()

    query_processor: QueryProcessor = QueryProcessor(queries)
    processed_queries: list = query_processor.process_queries_with_depth_limit(tree.depth)

    tree.perform_swap_operations_with_(processed_queries)

    return tree.results
