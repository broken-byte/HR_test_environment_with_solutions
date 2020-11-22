from unittest import TestCase, TestLoader, TextTestRunner
from typing import Callable, Dict
import functools
import time

from func_timeout import func_set_timeout, FunctionTimedOut

from test_utilities.test_variables import console_break_line


class FunctionalityTestContainerTemplate(TestCase):
    pass


def make_test_function(test_data: dict, test_function, timed: bool = False, timeout: int = 0) -> Callable[[dict], None]:
    if timed:
        @complexity_timer
        @func_set_timeout(timeout)
        def test_template(self):
            try:
                params: dict = test_data["params"]
                print(f"Parameters in this test: {params}\n")
                expected = test_data["expected"]
                actual = test_function(**params)
                print(console_break_line)
                self.assertEqual(expected, actual, f"algorithm being tested: {test_function.__name__}")
            except FunctionTimedOut as e:
                print(f"algorithm did not meet time complexity requirements! timeout is set at {timeout} seconds.\n")
    else:
        def test_template(self):
            params: dict = test_data["params"]
            print(f"Parameters in this test: {params}\n")
            expected = test_data["expected"]
            actual = test_function(**params)
            print(console_break_line)
            self.assertEqual(expected, actual, f"algorithm being tested: {test_function.__name__}")
    return test_template


def complexity_timer(function_template):
    @functools.wraps(function_template)
    def wrapper_timer(self):
        tic = time.perf_counter()
        function_template(self)
        tock = time.perf_counter()
        time_log = f'finished in {tock - tic:0.10f} seconds\n'
        print(time_log)
    return wrapper_timer


def dynamically_generate_tests(data: dict, function_being_tested, timed: bool = False, timeout: int = 60):
    for test_name, test_data in iter(data.items()):
        unittest_function = make_test_function(test_data, function_being_tested, timed=timed, timeout=timeout)
        setattr(FunctionalityTestContainerTemplate, f"{test_name}", unittest_function)


def run_dynamic_tests():
    suite = TestLoader().loadTestsFromTestCase(FunctionalityTestContainerTemplate)
    TextTestRunner(verbosity=2).run(suite)
