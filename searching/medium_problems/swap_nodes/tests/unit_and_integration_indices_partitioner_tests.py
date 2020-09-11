from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.IndicesPartitioner import IndicesPartitioner


class UnitAndIntegrationIndicesPartitionerTester(TestCase):

    def setUp(self):
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        self.indices_partitioner: IndicesPartitioner = IndicesPartitioner(indices)

    def tearDown(self):
        self.indices_partitioner = None

    def test_that_indices_partitioner_can_partition_indices_into_levels(self):
        expected: list = [
            [2, 3],
            [-1, -1, -1, -1]
        ]
        actual: list = self.indices_partitioner.partition_indices()
        self.assertEqual(expected, actual)

    def test_that_indices_partitioner_can_construct_a_size_1_partition_with_index_and_number_of_non_null_nodes(self):
        expected: list = [2, 3]
        actual: list = self.indices_partitioner.construct_partition_with(current_index=0,
                                                                         count_of_non_null_nodes_in_previous_level=1)
        self.assertEqual(expected, actual)

    def test_that_indices_partitioner_can_construct_a_size_2_partition_with_index_and_number_of_non_null_nodes(self):
        expected: list = [-1, -1, -1, -1]
        actual: list = self.indices_partitioner.construct_partition_with(current_index=1,
                                                                         count_of_non_null_nodes_in_previous_level=2)
        self.assertEqual(expected, actual)
