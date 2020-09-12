from unittest import TestCase

from searching.medium_problems.swap_nodes.classes.QueryProcessor import QueryProcessor


class UnitTreeTester(TestCase):

    def test_that_query_processor_can_process_queries_2_4_with_depth_limit_of_5(self):
        swap_queries: list = [2, 4]
        query_processor: QueryProcessor = QueryProcessor(swap_queries)
        depth_limit: int = 5

        expected: list = [[2, 4], [4]]
        actual: list = query_processor.process_queries_with_depth_limit(depth_limit)

        self.assertEqual(expected, actual)

    def test_that_query_processor_can_process_queries_1_1_with_depth_limit_of_2(self):
        swap_queries: list = [1, 1]
        query_processor: QueryProcessor = QueryProcessor(swap_queries)
        depth_limit: int = 2

        expected: list = [[1, 2], [1, 2]]
        actual: list = query_processor.process_queries_with_depth_limit(depth_limit)

        self.assertEqual(expected, actual)

