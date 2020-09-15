## Pairs

[Pairs HackerRank Link](https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search&h_r=next-challenge&h_v=zen)

### Problem
You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a 
difference equal to a target value.

For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the 
condition: 2 - 1 = 1, 3 - 2 = 1, and 4 - 3 = 1. 
### Function Description

Complete the pairs function below. It must return an integer representing the number of element pairs having the 
required difference.

pairs has the following parameter(s):

- k: an integer, the target difference
- arr: an array of integers

##### Input Format:
The first line contains two space-separated integers n and k, the size of arr and the target value.
The second line contains  space-separated integers of the array arr.

##### Constraints:
- 2 <= n <= 10^5
- 0 < k < 10^9
- 0 < arr[i] < 2^31 - 1
- Each integer arr[i] will be unique
##### Output Format:
An integer representing the number of pairs of integers whose difference is k.