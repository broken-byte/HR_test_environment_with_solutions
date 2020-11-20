from unittest import TestCase, TestLoader, TextTestRunner
from typing import Callable
import functools
import time

from test_utilities.test_variables import console_break_line


class FunctionalityTestContainerTemplate(TestCase):
    pass


def make_test_function(
        test_data: dict, function_to_be_tested, timed: bool = False) -> Callable[[dict], None]:
    if timed:
        @complexity_timer
        def test_template(self):
            params: dict = test_data["params"]
            expected = test_data["expected"]
            actual = function_to_be_tested(**params)
            print(console_break_line)
            self.assertEqual(expected, actual, f"algorithm being tested: {function_to_be_tested.__name__}")
    else:
        def test_template(self):
            params: dict = test_data["params"]
            expected = test_data["expected"]
            actual = function_to_be_tested(**params)
            print(console_break_line)
            self.assertEqual(expected, actual, f"algorithm being tested: {function_to_be_tested.__name__}")
    return test_template


def complexity_timer(function_template):
    @functools.wraps(function_template)
    def wrapper_timer(self):
        tic = time.perf_counter()
        function_template(self)
        tock = time.perf_counter()
        time_log = f'\nfinished in {tock - tic:0.10f} seconds'
        print(time_log)
    return wrapper_timer


def dynamically_generate_tests(test_data: dict, function_to_be_tested: Callable[[dict], None], timed: bool = False):
    for test_name, test_data in iter(test_data.items()):
        test_function = make_test_function(test_data, function_to_be_tested, timed=timed)
        setattr(FunctionalityTestContainerTemplate, f"{test_name}", test_function)


def run_dynamic_tests():
    suite = TestLoader().loadTestsFromTestCase(FunctionalityTestContainerTemplate)
    TextTestRunner(verbosity=2).run(suite)
