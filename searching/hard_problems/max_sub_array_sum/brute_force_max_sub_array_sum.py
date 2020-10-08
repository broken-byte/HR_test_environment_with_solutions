

def brute_force_max_sub_array_sum(a: list, m: int) -> int:
    sub_arrays: list = get_all_sub_arrays_of_an_array(a)
    sum_of_sub_arrays: list = convert_sub_arrays_to_sums(sub_arrays)
    modulized_sums: list = [s % m for s in sum_of_sub_arrays]
    return max(modulized_sums)


def get_all_sub_arrays_of_an_array(array: list)-> list:
    n: int = len(array)
    sub_arrays: list = []
    for start_index in range(n):
        for group_size in range(start_index + 1, n + 1):
            sub_array: list = []
            for j in range(start_index, group_size):
                sub_array.append(array[j])
            sub_arrays.append(sub_array)
    return sub_arrays


def convert_sub_arrays_to_sums(sub_arrays: list) -> list:
    sum_of_sub_arrays: list = []
    for sub_array in sub_arrays:
        sub_array_sum: int = sum(sub_array)
        sum_of_sub_arrays.append(sub_array_sum)
    return sum_of_sub_arrays


if __name__ == '__main__':
    print(get_all_sub_arrays_of_an_array([1, 2, 3]))
