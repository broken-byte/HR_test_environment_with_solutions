from collections import Counter

from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from dictionaries.medium_problems.count_triplets.test_resources.functionality_test_data import functionality_test_data


def brute_force(array_of_numbers: list, ratio: int) -> int:
    potential_js = Counter()
    potential_ks = Counter()
    number_of_geo_triplets: int = 0
    for number in array_of_numbers:
        if number in potential_ks:
            '''
            Number exists in potentialKs bag! 
            That means that we've found a triplet! 
            Let's increment the numberOfGeoTriplets 
            by how many times its "progressed" to this 
            point (the number of times its appeared in the bag)...
            '''
            number_of_geo_triplets += potential_ks[number]
        if number in potential_js:
            '''
            The number exists in the potentialJs bag! 
            That means that we are on our way to a 
            potential geoTriplet...Let's add/increment 
            it's progression to the potentialKs bag with
            a number of instances equal to how many times 
            its appeared in the potentialJs. 
            '''
            next_geo_progression: int = number * ratio
            potential_ks[next_geo_progression] += potential_js[number]
        '''
        Regardless of whether it exists in either bag, 
        it can always potentially be the start of a geometric 
        progression so let's add it's nextGeoProgression to 
        the potentialJs...
        '''
        next_geo_progression: int = number * ratio
        potential_js[next_geo_progression] += 1
    return number_of_geo_triplets


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()


