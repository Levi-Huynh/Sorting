MERGE SORT

N cards in hand

1. divide in 1/2 (keep dividing) until you have subarrys of len 1
(list of len 1 are sorted!) HALVING INTO SMALLER PIECES INTO SINGULAR 

2. merge sorted lists together
 (2 sorted at a time & put together!)
- sort each set of 2 cards
-compare each a set of 2, with another set of 2, [COMPARE the first card from
both sets (ITERATIVE PIECE HERE)] ==> into a new set (new set created for each new comparison rounds),  (REPEAT)

def recursive_merge_sort(arr):
if len(arr) > 1:
#divide
left = merge_sort(arr[0:len(arr/2)]) # sort array are goning to be returned up the #callstack by all the merge sort calls were making
right = merge_sort(arr[len(arr)/2:])

arr = merge(left, right) #merge() normally definied as helper function

return arr

def merge(arrA, arrB):
# create new array of size [len(arrA ) +len(arrB)] for merged elements O(1)
# b/c already sorted:
# for all elements: O(n) below
#if all elements in arrA have been merged, put next element in arrB into merged array
#if all elements in arrB have been merged, put next element in arrA into merged array
#elif next element in arrA smaller, add to merged array (only compare if still elements in arrA or arrB )
#pop stuff off?

RT of merge sort? 
Ologn  * ?? (due to merge function = O(n))
Ologn * O(n) => O n log n

MANY LANG USE MERGE SORT , or hybrid of MERGE SORT 