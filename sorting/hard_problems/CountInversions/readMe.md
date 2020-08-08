## Count Inversions

-------

[Count Inversions HackerRank Link](https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting)

In an array, arr, the elements at indices i and j (where i < j) form an inversion if arr[i] > arr[j]. In other words, inverted elements arr[i] and arr[j] are considered to be "out of order". To correct an inversion, we can swap adjacent elements.

For example, consider the dataset arr = [2, 4, 1]. It has two inversions: (4, 1) and (2, 1). To sort the array, we must perform the following two swaps to correct the inversions:
arr = [2, 4, 1] -> swap(arr[1], arr[2]), swap(arr[0], arr[1]) -> arr = [1, 2, 4]

### Function Description

Complete the function countInversions in the editor below. It must return an integer representing the number of inversions required to sort the array.

countInversions has the following parameter(s):

arr: an array of integers to sort .
