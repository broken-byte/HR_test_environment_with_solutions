## Greedy Florist

-------

[Greedy Florist HackerRank Link](https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms)

A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the 
money he makes. 

To do this, he decides he'll multiply the price of each flower by the number of that customer's previously 
purchased flowers plus 1. The first flower will be original price, (0 + 1) * (original price), the next will be 
(1 + 1) * (original price) and so on.

Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers, determine the minimum cost to purchase all of the flowers.

For example, if there are k = 3 friends that want to buy n = 4 flowers that cost c = [1,2,3,4] each will buy one of the flowers priced [2,3,4] at the original price. Having each purchased  x = 1 flower, the first flower in the list, c[0], will now cost (current purchase  + previous purchases) x c[0] = (1 + 1) x 1 = 2. The total cost will be 2 + 3 + 4 + 2 = 11.

### Function Description

Complete the getMinimumCost function in the editor below. It should return the minimum cost to purchase all of the flowers.

getMinimumCost has the following parameter(s):

c: an array of integers representing the original price of each flower
k: an integer, the number of friends
