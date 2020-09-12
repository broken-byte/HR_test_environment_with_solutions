import unittest

from \
    searching.medium_problems.swap_nodes.tests.unit_node_tests \
    import UnitNodeTester

from \
    searching.medium_problems.swap_nodes.tests.unit_and_integration_indices_partitioner_tests \
    import UnitAndIntegrationIndicesPartitionerTester
from \
    searching.medium_problems.swap_nodes.tests.unit_tree_factory_tests \
    import UnitTreeFactoryTester
from \
    searching.medium_problems.swap_nodes.tests.unit_and_integration_query_processor_tests \
    import UnitAndIntegrationQueryProcessorTester

from \
    searching.medium_problems.swap_nodes.tests.integration_tree_factory_tests \
    import IntegrationTreeFactoryTester
from \
    searching.medium_problems.swap_nodes.tests.integration_tree_tests \
    import IntegrationTreeTester

from \
    searching.medium_problems.swap_nodes.tests.test_swap_nodes_brute_force \
    import BruteForceSwapNodesTester

# TODO: Figure out how to make suites lol
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(
    [
        UnitNodeTester(),
        UnitTreeFactoryTester(),
        UnitAndIntegrationIndicesPartitionerTester(),
        UnitAndIntegrationQueryProcessorTester()
    ]
)

suite.addTests(
    [
        IntegrationTreeTester(),
        IntegrationTreeFactoryTester()
    ]
)

suite.addTest(BruteForceSwapNodesTester())

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
