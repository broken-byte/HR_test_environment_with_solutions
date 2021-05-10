from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from dictionaries.medium_problems.frequency_queries.test_resources.functionality_test_data import \
    functionality_test_data


def brute_force(queries):
    frequency_queries = FrequencyQueries()
    frequency_queries.frequency_queries(queries)
    return frequency_queries.z_array


class FrequencyQueries:

    def __init__(self):
        self.element_counter = {}
        self.frequency_counter = {}
        self.z_array = []

    def frequency_queries(self, queries):
        for query in queries:
            self.query_calculator(query)

    def query_calculator(self, query):
        operation_flag = query[0]
        element = query[1]

        if operation_flag == 1:
            self.append(element)

        elif operation_flag == 2:
            self.delete(element)

        elif operation_flag == 3:
            self.verify_frequency_of(element)

    def append(self, x):
        if x not in self.element_counter:
            self.element_counter[x] = 1
            self.add_frequency(1)
        else:
            element_frequency = self.element_counter[x]
            self.subtract_frequency(element_frequency)

            self.element_counter[x] += 1

            element_frequency = self.element_counter[x]
            self.add_frequency(element_frequency)

    def delete(self, y):
        if y in self.element_counter:
            element_frequency = self.element_counter[y]
            self.subtract_frequency(element_frequency)
            
            self.element_counter[y] -= 1

            element_frequency = self.element_counter[y]
            self.add_frequency(element_frequency)

            if self.element_counter[y] == 0:
                self.element_counter.pop(y)

    def verify_frequency_of(self, z):
        if z in self.frequency_counter:
            if self.frequency_counter[z] == 0:
                self.z_array.append(0)
            else: 
                self.z_array.append(1)
        else:
            self.z_array.append(0)

    def add_frequency(self, frequency):
        if frequency not in self.frequency_counter:
            self.frequency_counter[frequency] = 1
        else: 
            self.frequency_counter[frequency] += 1

    def subtract_frequency(self, frequency):
        if frequency in self.frequency_counter:
            if self.frequency_counter[frequency] == 0:
                # Do nothing, the frequency is not present in element_counter
                return
            self.frequency_counter[frequency] -= 1


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()
