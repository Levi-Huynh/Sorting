

# Recursive sorting:
What are the base cases for this problem?
If my code has not currently arrived at a base case, how does it move towards a base case?

def recurse_factorial(n):
    if n == 0:
        return 1
    return n * recurse_factorial(n - 1)

    Diving a bit deeper into what this function is doing, the first two lines are our base case. In other words, this is the situation in which our recursive function needs to stop execution. If we don’t have a base case that our recursive function eventually converges to, then our recursive function will just run in an infinite loop and never produce useful output.
    The last line is how our recursive function moves towards our defined base case. We have our given starting input n, we have specified in our function that once n reaches 0, we return. So what about all the values in between? Well, we can move towards our base case by continually subtracting 1 from our input n, then feeding that new input to our recursive function. Eventually, our recursive function will be called with n = 0, at which point, it’s arrived at our defined base case and stops recursing, returning us an answer


# merge sort:
Runtime
The “divide” part of this algorithm requires us to cut a collection of elements in half until its length is 1. If our collection contains n elements, we will have to perform more halving operations as n grows larger. However, the rate of growth not quite linear. This part of the algorithm has a runtime of O(log(n)).

The “conquer” (merge) part of this algorithm requires no more than a single pass through each sorted sub-collection, giving it a runtime of O(n).

Since we divide, then conquer we can think about the total runtime of Merge Sort as O(log(n)) + O(n) or O(n log(n) )
def merge_sort( arr ):
    if len( arr ) > 1: 
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces

def merge_helper( a, b ):
    merged_arr = []

    # starting at beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`

    return merged_arr


# Quick Sort
How It Works
Another divide and conquer algorithm, Quick Sort requires us to…

Choose a pivot
Move everything smaller than the pivot to one side
Move everything larger than the pivot to the other side
Repeat steps 1-3 on the left-hand side and right-hand side of the partition
def quick_sort( arr ):
    if len(arr) > 1:
        # choose a pivot
        # loop through all elements in arr
            # if element < pivot, move to LHS of pivot
        # quick_sort( LHS )
        # quick_sort( RHS )
    
    return arr
    
    #questions:
    -how is results.append(i+i) creating space complexity of O(1)
    -what is callstack for recursion
    -