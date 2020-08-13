

class StringInterLeaver:

    def __init__(self, s1: str, s2: str):
        self.string_1: str = s1
        self.string_2: str = s2
        self.interleaves: list = []

    def get_all_possible_inter_leaves(self):
        self.recursive_inter_leaves(0, 0, "")
        return self.interleaves

    def recursive_inter_leaves(self, i: int, j: int, result: str):
        if i == len(self.string_1) and j == len(self.string_2):
            self.interleaves.append(result)
            return
        if i < len(self.string_1):
            self.recursive_inter_leaves((i + 1), j, result + self.string_1[i])
        if j < len(self.string_2):
            self.recursive_inter_leaves(i, (j + 1), result + self.string_2[j])
