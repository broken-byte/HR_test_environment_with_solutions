## Ice Cream Parlor

[Ice Cream Parlor HackerRank Link](https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search)

### Problem
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, 
they pool their money to buy ice cream. On any given day, the parlor 
offers a line of flavors. Each flavor has a cost associated with it.

Given the value of "money" and the "cost" of each flavor for  trips to the Ice Cream Parlor, 
help Sunny and Johnny choose two distinct flavors such that they spend their 
entire pool of money during each visit. ID numbers are the 1- based index 
number associated with a "cost". For each trip to the parlor, print the ID 
numbers for the two types of ice cream that Sunny and Johnny purchase as 
two space-separated integers on a new line. You must print the smaller ID 
first and the larger ID second.

For example, there are n = 5 flavors having cost = [2, 1, 3, 5, 6]. Together 
they have money = 5 to spend. They would purchase flavor ID's 1 and 3 for a 
cost of 2 + 3 = 5. Use 1 based indexing for your response.

- Two ice creams having unique IDs  and  may have the same cost (i.e., ).
- There will always be a unique solution.

### Function Description

Complete the function whatFlavors in the editor below. It must determine 
the two flavors they will purchase and print them as two space-separated 
integers on a line.

whatFlavors has the following parameter(s):

- cost: an array of integers representing price for a flavor
- money: an integer representing the amount of money they have to spend

##### Input Format:

The first line contains an integer, t, the number of trips to the ice cream parlor.

Each of the next t sets of 3 lines is as follows:

The first line contains money.
The second line contains an integer, n, the size of the array cost.
The third line contains n space-separated integers denoting the cost[i].

##### Constraints:
- 1 <= t <= 50
- 2 < k < 10^9
- 2 < n < 5*10^4
- 1 <= cost[i] <= 10^9

##### Output Format:
Print two space-separated integers denoting the respective indices for the 
two distinct flavors they choose to purchase in ascending order. Recall that 
each ice cream flavor has a unique ID number in the inclusive range from 1 to |cost|.

##### A Note about the File Structure...
I omitted a time complexity test suite since the test data was so convoluted on HR that
I took a HARD pass. The optimal solution still runs lightning fast though, I promise :)