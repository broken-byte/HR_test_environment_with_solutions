from searching.medium_problems.swap_nodes.classes.Tree import Tree
from searching.medium_problems.swap_nodes.classes.TreeFactory import TreeFactory
from searching.medium_problems.swap_nodes.classes.IndicesPartitioner import IndicesPartitioner
from searching.medium_problems.swap_nodes.classes.QueryProcessor import QueryProcessor


def swap_nodes_brute_force(indices: list, queries: list) -> list:
    partitioned_indices: list = partition_indices_for_tree_construction(indices)
    tree: Tree = construct_tree_from(partitioned_indices)
    processed_queries: list = process_queries_for_tree_swapping_given_depth_limit(queries, tree.depth)
    tree.perform_swapped_traversals_with(processed_queries)
    return tree.results


def partition_indices_for_tree_construction(indices: list) -> list:
    indices_partitioner: IndicesPartitioner = IndicesPartitioner(indices)
    partitioned_indices: list = indices_partitioner.partition_indices()
    return partitioned_indices


def construct_tree_from(partitioned_indices: list) -> Tree:
    tree_factory: TreeFactory = TreeFactory()
    tree_factory.construct_tree_with(partitioned_indices)
    tree: Tree = tree_factory.get_constructed_tree()
    return tree


def process_queries_for_tree_swapping_given_depth_limit(queries: list, depth_limit: int) -> list:
    query_processor: QueryProcessor = QueryProcessor(queries)
    processed_queries: list = query_processor.process_queries_with_depth_limit(depth_limit)
    return processed_queries
