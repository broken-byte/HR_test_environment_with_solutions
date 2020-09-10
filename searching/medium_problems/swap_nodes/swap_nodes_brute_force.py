from searching.medium_problems.swap_nodes.classes.Tree import Tree


# TODO: Refactor to separate Tree class into 3 classes: A tree constructor, a query processor, and the Tree itself
def swap_nodes_brute_force(indices: list, queries: list) -> list:
    tree: Tree = Tree()
    tree.construct_with(indices)
    tree.process_swap_queries(queries)
    tree.perform_swap_operations_with_all_processed_queries()
    return tree.results
