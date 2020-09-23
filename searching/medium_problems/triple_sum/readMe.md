## Pairs

[Pairs HackerRank Link](https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search&h_r=next-challenge&h_v=zen)

### Problem
Given 3 arrays a, b, c of different sizes, find the number of distinct triplets (p, q, r) where p is an element of a, 
written as p a, q in b, and r in c, satisfying the criteria: p <= q, and q >= r.

For example, given a = [3, 5, 7], b = [3, 6] and c = [4, 6, 9], we find four distinct triplets: (3, 6, 4), (3, 6, 6), 
(5, 6, 4), and (5, 6, 6).
### Function Description

Complete the triplets function in the editor below. It must return the number of distinct triplets that can be formed 
from the given arrays.

triplets has the following parameter(s):

- a, b, c: three arrays of integers .

##### Input Format:
The first line contains 3 integers len(a), len(b), and len(c), the sizes of the three arrays.
The next  lines contain space-separated integers numbering  respectively.

##### Constraints:
- 1 <= len(a), len(b), len(c) <= 10^5
- 1 <= all elements in a, b, c <= 10^8

##### Output Format:
An integer representing the number of distinct triplets.