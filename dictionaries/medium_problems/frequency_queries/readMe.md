## Frequency Queries

------------

[Frequency Queries HackerRank Link](https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps)

You are given q queries. Each query is of the form of two integers described below:

    (1, x) -  : Insert x in your data structure.
    (2, y) -  : Delete one occurence of y from your data structure, if present.
    (3, z) -  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

(The queries are given in the form of a 2-D array)

The function must return an array of integers where each element 
is a 1 if there is at least one element value with the 
queried number of occurrences in the current array, or 
0 if there is not. 

(Basically, an array with the accurate 
results of the z operation (operation 3))