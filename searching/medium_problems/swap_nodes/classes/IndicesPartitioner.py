

class IndicesPartitioner:

    def __init__(self, indices: list):
        self.indices: list = indices
        self.partitioned_indices: list = []

    def partition_indices(self):
        self.partition_indices_into_levels()
        return self.partitioned_indices

    def partition_indices_into_levels(self):
        indices_length: int = len(self.indices)
        current_index: int = 0
        number_of_non_null_nodes_in_previous_level: int = 1
        while current_index < indices_length:
            partition = self.construct_partition_with(current_index, number_of_non_null_nodes_in_previous_level)
            self.partitioned_indices.append(partition)
            current_index += len(partition) // 2
            number_of_non_null_nodes_in_previous_level = self.get_non_null_node_count_in(partition)

    def construct_partition_with(self, current_index: int, count_of_non_null_nodes_in_previous_level: int) -> list:
        start_index: int = current_index
        size: int = count_of_non_null_nodes_in_previous_level
        end_index: int = start_index + size
        sequential_partition: list = []
        for index in range(start_index, end_index):
            sequential_partition.extend(self.indices[index])
        return sequential_partition

    @staticmethod
    def get_non_null_node_count_in(partition: list):
        non_node_count: int = 0
        for data in partition:
            if data != -1:
                non_node_count += 1
        return non_node_count
