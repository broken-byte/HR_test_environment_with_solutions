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


unit_test_case_classes: list = [
    UnitNodeTester,
    UnitTreeFactoryTester,
    UnitAndIntegrationIndicesPartitionerTester,
    UnitAndIntegrationQueryProcessorTester
]


integration_test_case_classes: list = [
    IntegrationTreeTester,
    IntegrationTreeFactoryTester
]

super_integration_test_case_classes: list = [
    BruteForceSwapNodesTester
]

all_test_case_classes = []
all_test_case_classes.extend(unit_test_case_classes)
all_test_case_classes.extend(integration_test_case_classes)
all_test_case_classes.extend(super_integration_test_case_classes)


def test_runner(test_case_classes: list):
    loader = unittest.TestLoader()
    suites: list = []
    for test_case_class in test_case_classes:
        suite: unittest.TestSuite = loader.loadTestsFromTestCase(test_case_class)
        suites.append(suite)

    suite_of_suites: unittest.TestSuite = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner()
    results = runner.run(suite_of_suites)


if __name__ == '__main__':
    test_runner(all_test_case_classes)
