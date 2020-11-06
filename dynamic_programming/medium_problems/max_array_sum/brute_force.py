

def max_subset_sum(arr: list) -> int:
    sub_set_generator: SubsetGenerator = SubsetGenerator(arr)
    return sub_set_generator.get_max_sub_set_sum()

# TODO: Only noncontigious subsets are valid for sum comparison, need to change alg to account for thats

class SubsetGenerator:
    def __init__(self, array: list):
        self.memo: set = set()
        self.array: list = array
        self.sub_sets: list = []
        self.current_max_sum: int = 0

    def get_max_sub_set_sum(self):
        self.recursively_look_for_max_sub_set_sum(0)
        return self.current_max_sum

    def recursively_look_for_max_sub_set_sum(self, summation: int, index=0):
        if index == len(self.array):
            return
        else:
            self.recursively_look_for_max_sub_set_sum(summation, index + 1)
            self.recursively_look_for_max_sub_set_sum(summation + self.array[index], index + 1)


if __name__ == '__main__':
    gen: SubsetGenerator = SubsetGenerator([1, 2, 3])
    print(gen.get_max_sub_set_sum())
