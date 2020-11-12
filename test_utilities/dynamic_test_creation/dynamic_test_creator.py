from unittest import TestCase, TestLoader, TextTestRunner


class TestContainerTemplate(TestCase):
    pass


def make_test_function(test_data: dict, function_to_be_tested):
    def test_template(self):
        params: dict = test_data["params"]
        expected = test_data["expected"]
        actual = function_to_be_tested(**params)
        self.assertEqual(expected, actual, function_to_be_tested.__name__)
    return test_template


def dynamically_generate_tests(functionality_test_data: dict, function_to_be_tested):
    for test_name, test_data in iter(functionality_test_data.items()):
        test_function = make_test_function(test_data, function_to_be_tested)
        setattr(TestContainerTemplate, f"{test_name}", test_function)


def run_dynamic_tests():
    suite = TestLoader().loadTestsFromTestCase(TestContainerTemplate)
    TextTestRunner(verbosity=2).run(suite)
