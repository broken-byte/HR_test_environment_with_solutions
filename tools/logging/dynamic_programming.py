from tabulate import tabulate


def log_memoization_table(memoization_table, iterable_1=None, iterable_2=None, testable: bool = False) -> str:
    if iterable_1 is not None:
        pass  # TODO: Add a way to add the iterable as the header of the table
        if iterable_2 is not None:
            pass  # TODO: Add a way to add both iterables as headers to the table
    else:
        tabulated_memo: str = tabulate(memoization_table.items(), tablefmt="fancy_grid")
        if testable:
            return tabulated_memo
        else:
            print(tabulated_memo)
