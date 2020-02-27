# TO-DO: Complete the selection_sort() function below
"""
def selection_sort(elements):  # If `elements` is a collection, remember it will be passed by reference, not value

  # How many loops will be needed to complete this algorithm?: n-1 elements
    # How do we know when we are ready to swap values?  when the choosen smallest element is smaller than the indexed element its being compared to 
    # And how do we keep track of which values should be swapped? have a seperate loop & loop through length of the array

  # What, if anything needs to be returned?
"""
""""
def centered_average(nums): #also theres methods for min, max, length, sum 
  min_num = nums[0]
  max_nums = nums[0]
  sum = 0
  len = 0
  for n in nums:
    sum += n
    length +=1
    if n < min_num:
      min_num = n
    
    if n > max_num:
      max_num =n
  
return (sum- min_num - max_num)/ (length -2)
"""

"""
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        if      



        # TO-DO: swap




    return arr
"""


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):  # range index starts at 0
      # THIS LOOP IS JUST YOUR COUNTER
        cur_index = i
        smallest_index = cur_index  # same thing
        # TO-DO: find next smallest element in unsorted array
        # (hint, can do in 3 loc)
        # comparision loop: starts as i +1 (index of range) and ends at length of array
        for j in range(cur_index, len(arr)):

          # ^ STARTS OVER HERE EACH TIME, WITH THE CUR_INDEX THAT YOU START AT MOVED UP +1 EACH TIME
            if arr[smallest_index] > arr[j]:  # indexed value > arr[j]: #comparison value
              # ^ DOES THIS UNTIL "NEW LOOP IS DONE "
                smallest_index = j

        # TO-DO: swap
        # swap found min element with the first element (this moves the old smallest_index, to the
        # position of where the new smallest index WAS, and vice versa )
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # SWAP IS DONE HERE AFTER THE END OF 2ND LOOP , STARTS OVER WITH CURR_INDEX+=1

    return arr


# TO-DO:  implement the Bubble Sort function below
"""
def bubble_sort(elements):  # If `elements` is a collection, remember it will be passed by reference, not value

  # We only need to loop through `elements` until we make a pass that leads to 0 swaps. LOOP THROUGH CERTAIN AMOUNT?  BASE: WHEN PASS =0 SWAP
  #  How do we keep track of whether or not any swaps have occurred? ?? 
  # Do we always need to loop through all elements? (HOW MANY ELEMENTS TO LOOP)
    # Depending on how our loop was set up, which neighbors should be compared? HOW LOOP SET UP? LH COMPARE/ RH COMPARE?
    # Can we do swaps in Python without a `temp` variable?  SWAPS WITHOUT A TEMP? 

  # What, if anything needs to be returned? IF LH/RH < COMPARISION
  In this sorting algorithm, we start at the beginning and compare each element to its right hand neighbor. ==> 
  If the right hand neighbor is smaller, we swap the two neighbors.  COMP > RH : SWAP :?

The above process is repeated until we pass through the entire collection without performing a single swap. 
With each pass, the larger elements will “bubble” toward the right hand side of the collection.

Runtime
If we get really lucky, our collection will already be in (or mostly in) order. In this case,
 we only need to pass through the collection a few times to sort everything. However, in a worse case 
 scenario (a collection in reverse order), we need n-1 passes through the collection for every element to 
 “bubble up” to its correct position. This leads to a runtime of O(n^2).
"""
"""
-with n # cards
-compare the first pair of elements
-if the RHS is less than the LHS, swap
-else do nothing
-iterate through the array, comparing other pairs of the adjacent elements
-if 1 or more swaps performed, repeat process 

"""

# On^2
"""

def bubble_sort(arr):
    swapp = True  # swap occured?
    while swapp:
        swapp = False  # this switches it to swapp to False & doesn't repeat the while loop
        end = len(arr) - 1
        for i in range(0, end):  # up until 2nd to last element
            # print(end)
            if arr[i] > arr[i+1]:

                arr[i], arr[i+1] = arr[i+1], arr[i]
                # redoes while loop / swapp since, arr[i] > arr[i+1]
                swapp = True
        # end -= 1  # here, each time I repeat the while swap, i'm moving the end, closer to start

    return arr
"""

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapp = True
    while swapp:
        swapp = False  # doesn't allow swapp to repeat unless arr[i] > arr[i+1]
        pointer = len(arr)-1
        for i in range(0, pointer):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapp = True  # repeat swap

        # each time repeat the while loop, move closer to start of array (normal for while loop?)
        pointer -= 1
        return arr


print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    pass
