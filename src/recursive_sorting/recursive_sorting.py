# TO-DO: complete the helpe function below to merge 2 sorted arrays
"""
How It Works
This is a “divide and conquer” algorithm. First, the original collection must be divided in half 
until we have broken the entire thing down to single collections with a length of 1.

What is special about lists or arrays with a single element? They are already sorted! 
It is impossible for a single element to not be sorted.

Then, we are able to “merge” these sorted pieces back together.

Runtime
The “divide” part of this algorithm requires us to cut a collection of elements in half until its length is 1. 
If our collection contains n elements, we will have to perform more halving operations as n grows larger. 
However, the rate of growth not quite linear. This part of the algorithm has a runtime of O(log(n)).

The “conquer” (merge) part of this algorithm requires no more than a single pass through each sorted sub-collection, giving it a runtime of O(n).
Since we divide, then conquer we can think about the total runtime of Merge Sort as O(log(n)) + O(n) or O(n log(n) )
https://codereview.stackexchange.com/questions/154135/recursive-merge-sort-in-python

"""


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    #merged_arr = [0] * elements
    leftindex, rightindex = 0, 0
    result = []
    # while zero is less than len of arrA & arrB
    while leftindex < len(arrA) and rightindex < len(arrB):
        if arrA[leftindex] < arrB[rightindex]:  # check to see if arrA[0] < arrB[0]
            # add to result array if arrA < arrB
            result.append(arrA[leftindex])
            leftindex += 1  # way to account for all the elements for each appended & find the remaining
            print("leftindex:", leftindex, "result left<right", result)
        else:
            result.append(arrB[rightindex])
            rightindex += 1
            print("rightindex:", rightindex, "result left>right:", result)
    # TO-DO
    result += arrA[leftindex:]
    result += arrB[rightindex:]
    return result  # ordered array with everything thats left
# https://www.geeksforgeeks.org/iterative-merge-sort/

# TO-DO: implement the Merge Sort function below USING NONRECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        mid = int(len(arr)/2)  # find the mid of array
        L = arr[:mid]  # split array to left
        R = arr[mid:]  # split array to right

        merge_sort(L)  # sort first half
        merge_sort(R)  # sort 2nd half

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1  # iterates through i
            else:
                arr[k] = R[j]
                j += 1  # iteraties through j
            k += 1  # iterates through k

    # check if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1  # moves through towards right
            k += 1  # moves through towards right and makes each k = i
        while j < len(R):
            arr[k] = R[j]
            j += 1  # moves through towards right of remaining j
            k += 1  # moves through towards right and makes remaining j = k
    print("merge:", arr)
    return arr


merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# TO-DO: implement the Merge Sort function below USING RECURSION
"""
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    half = len(arr)
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)
"""


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
