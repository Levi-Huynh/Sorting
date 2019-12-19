Point of RT complexity:

main big 0 RT classifications :

-compare arbitrary algorithms of functions and pieces of code
    -algo: take in lots of diff inputs & outputs (2 algo, may have very little in common)
    -bridge algo differences by using big 0 classifications
        -Graph 
            y-axis: # operations
            x-axis: # input size 
                (as input x increases) ,  how many more (# operations performed, y increases)?

Listed in order of classifications:
 O(c) - constant time (best RT, no huge increase in # of operations per input)  --> inside parenth are some static constant 
 O(log n) - logarithmic time    --> some function
 O(n) -Linear Time  --> function
 O(nlogn) - Log-Linear Time --> function
 O(n^c) Quadratic Time  --> function
 O(c^n) Exponential Time (worst RT, large increase in #operations per input)  --> function

#CONSTANT TIME DEF:
Algo in question executes the same # of operations regardless of size of input
So for any input size n, a constant time algo performs the same number of operations every time

constant time graph examples:
-200 or 2 balls, putting hand in to choose ball always 1 operation

constant time example code:
-def print_100th_element(array):
    print(array[99])
-def loop_50_times(array):  (even though the number of operations is large, still considered constant time )
    for i in range(50):
    print(array[i])
-
hash tables (language agnostic) (objects in js, dictionary in python)
-keys, values stored. use keys to fetch associated values 
-DS, insert data into array or hashtable/ by key tell hash table where to go to get that value


insert data into array or has table- already indexed by index in array or hash table

#LOG TIME DEF:
-The Algo, uncreases the # of operations it performs as a logarithmic function of the input size n
-Function log n grows very slowly, so as n gets larger, the # of operations the algorithm needs to perform does not increase by very much!!!
- ^ B/C of this great run time complexity!

exmples:    
-Dictionary- 
-Books on book shelf ordered ABC (if G wont look where A is)
-> if book starts with G, wont lookin A -> General notion of where element exists:
    ->Binary Search - 
        -useful for when data is already sorted or almost sorted
        -


#learn to use your emotions (pride for your work etc) with your job ##focus on this! #tireness===> use your emotions pride of your job #i promise you
Jesus that I will not talk smack on this job you've given me I love you, and i promise to use this amazing oppt to give you the best my best. forgive me
help me to fullfull this promise in jesus name i pray amen.


#to focus on work on your CS skills 

def binary search(sorted_arr, target):
    low = 0, high = len(sorted_arr) -1 
    midpoint = (high-low) //2
    if target ==sorted_arr[midpoint]: #if target equals array at midpoint
        return midpoint #return the midpoint
    elif target < sorted_arr[midpoint]: #if target less than element at midpoint
        return binary_search(sorted_arr[:midpoint]) #do binary search of elements after midpoint of sorted Array since elements [midpoint:] will already be                                                         smaller than midpoint .. dont need to check those!  
    else:
        return binary_search(sorted_arr[midpoint:]) #else do binary search of elements before midpoint (to find midpoint)

target is less than element at the midpoint, then dont need to look at the other half of SORTED ARRAY (elements are)

-log n Even with input size increasing => # of operations stays somewhat the same

LINEAR TIME DEF:
-The algo in question increases the number of ops it performs as a -linear function- of the input size n.
-The number of a*dditional operations* the algo needs to perform grows in *direct proportion* to the increase in input size *n*.
-line can be to left or right, but as long as in direction proportion

exmples:
-counting
-Look & see a coin to sucritinize whats being counted/inspected
-washing dogs one at a time

def search(array, target): 
    for el in array:  #inspect 1 at a time, cant do binary, not sorted 
        if target == el:
            return True
        return False


def print all elements twice(arr):
    for el in arr:
        print(el)
    for el in arr:
        print(el)
#RT classification = 2*n (2 is static ) #of thing we're doing per element does not depend on input size 

def print up to n(n):
    for i in range(n):
        print(i)
        #number of loops we're performing in direct proportion to integer (n -> n+1 adds iteration to our foor loop)

#Log-Linear Time Def
Looking over every single element & doing some work on each one
-increrases the # of operations it performs as a log-linear function of the input size n

-applied to problem of sorting 
-look at each ball (scan of each element)
-logn (work to put that element where it should be in total items)
-log linear times sorting


Log-linear Time Graph
# of operations overtake # input size n 

Log-linear Time Examples - reserve to apply to sorting algos (gold standard for sorting algos)
-

Sorting Algorithms: n(logn)
-Quicksort
-Mergesort
-Heapsort
-Timesort 


def mult_2(n)