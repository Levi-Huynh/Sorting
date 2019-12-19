# TO-DO: Complete the selection_sort() function below 
"""
def selection_sort(elements):  # If `elements` is a collection, remember it will be passed by reference, not value

  # How many loops will be needed to complete this algorithm?: n-1 elements
    # How do we know when we are ready to swap values?  when the choosen smallest element is smaller than the indexed element its being compared to 
    # And how do we keep track of which values should be swapped? have a seperate loop & loop through length of the array

  # What, if anything needs to be returned?
"""

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): #range index starts at 0, ends at lenght of array -1
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element in unsorted array
        # (hint, can do in 3 loc) 
        for j in range (cur_index, len(arr)): #comparision loop: starts as i +1 (index of range) and ends at length of array 

          if arr[smallest_index] > arr[j]:
            smallest_index = j


        # TO-DO: swap
        #swap found min element with the first element
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]



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

def bubble_sort( arr ):
  swapp = True   
  while swapp:
    swapp = False
    for i in range(0, len(arr)-1):
      if arr[i] >arr[i+1]:

        arr[i], arr[i+1] = arr[i+1], arr[i]
        swapp = True



    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr