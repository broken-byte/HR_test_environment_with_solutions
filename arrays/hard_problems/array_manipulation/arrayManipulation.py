'''
The below code fails when the inputs are exceedingly large
and doesn't return the answer fast enough. Further optimization
is needed...
'''
def arrayManipulation(n, queries):
    arr = [0 for x in range(0, n)]

    # Go through rows of queris matrix and update array values between a and b by k
    for row in queries:
        # adjust a since this is 1 index array
        a = row[0] - 1
        # Don't adjust b since range() is not inclusive and this is
        b = row[1]
        k = row[2]

        # Go through elements between a and b (inclusive) and update value by k
        for i in range(a, b):
            arr[i] += k

    return max(arr)

'''
Below is an explanation by yanikjay1
---------------------------------------
the best way to understand it is form a simple example.

say there are 4 of us in a line: 1. me 2. you 3. bob 4. 

sue and we all start out with zero points.

This can be represented as (where my points are in the first index, 

your in the second, bob's in the third, sue's in fourth):

0 0 0 0

Furthermore, we go through rounds, where in each round a contiguous 

block of us can receive some set amount of points.

So in round one, say 2 points are awarded to anything in the range of start 

index = 1, and end index = 2. This means that you and bob, who are in 

the range, get 2 points.

But rather than write the current score as: 0 2 2 0

We instead want to write the score as:

0 2 0 -2

Because we want each value to represent how much greater/less than it is 

from the previous-index value. Doing this allows us to only ever need to 

change two elements in the list for a given round.

Now say we play one more round, and 1 point is awarded to all people in range 

of index = 0 to index = 1. This gives you

1 2 -1 -2

All I did was add the point value to the start index, and subtract it from the 

"end index + 1".

Then calculating the max is simply a matter of going through that list, adding 

each element to an accumulator variable (as this summing process reveals the 

actual value of an element at any given point - e.g., you would have 3 points 

at the end because your score is the result of 1 + 2), and having a variable 

which keeps track of the running max.

And an implementation by greatFaiber (in Ruby):

def arrayManipulation(n, queries)
    arr = Array.new(n + 1, 0)
    queries.each do |q|
        arr[q.first - 1] += q.last
        arr[q[1]] -= q.last
    end
    tmp = 0
    max = 0
    arr.each do |n|
        tmp += n
        max = tmp if tmp > max
    end
    max
end

IMPLEMENT THIS IN PYTHON!
'''

# OPTIMAL SOLUTION
def arrayManipulations(n , queries):
    arr = [0 for x in range(n)]
    for rows in queries:
        a = rows[0]
        b = rows[1]
        k = rows[2]
        a = a - 1 
        arr[a] += k
        arr[b] -= k

    temp = 0
    max = 0
    for x in arr:
        temp += x 
        if temp > max:
            max = temp
        
    return max

    # I still dont understand this but we'll get there!
        



    


