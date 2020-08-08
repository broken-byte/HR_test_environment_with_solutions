I haven't seen a well organized solution for this problem that utilizes graph theory, so here goes:

This problem is decemptively complex. I initially thought it was a bubble sort modification. However, the key here is that you can swap **any two elements in the array.** This is not possible using the traditional sorting algorithms (Bubble sort, merge sort, selection sort, quick sort, etc.) You must know the proper, sorted order *before* you determine the minium swaps. This way you can see where each element *should* be before determining swapping. 

So, create the sorted version of the given array to compare to. Ok, great, but now how do we know what the minimum number of swaps are? **Graph theory**.

See, turning our array into a unidirectional graph where each element points to the element it should replace creates a *cycle*. 

![](https://i.ytimg.com/vi/f7IIW0HVUcQ/maxresdefault.jpg)

In the graph above, we have A = [0, 2, 3, 4, 1, 6, 5].
Our sorted array should be   A = [0, 1, 2, 3, 4, 5, 6]

As you can see, we create a cycle where 0 wants to go to 0, 1 wants to go to 2, etc.

The theory is that the minimum number of swaps needed to sort a any given cycle is equal to 
the size of the cycle - 1. for example, in our above array we have:

1 -> 2 -> 3 -> 4 -> 1

this cycle is length: 4, so the minimum number of swaps needed should be 3! Let's see if that makes sense...







