def insertion_sort(numbers):
    #loop over all the numbers starting at index 1
    for i in range(1, len(numbers)):
        # save each number into a temporary variable
        current_num = numbers[i]
        j = i
        # loop until we reach the end of array or the number we are comparing is not smaller than its neighbor
        while j > 0 and current_num < numbers[j - 1]:
            # move the left number over to the right 1 spot
            numbers[j] = numbers[j-1]        
            j -= 1
        # save the temporary number in its correct spot
        numbers[j] = current_num
​
    return numbers

"""
Divide & Conquor:
-split big problem into a bunch of smaller easy problems
-when dealing with divide, normally some logn rt
-

1. Find a pivot P (can be arr[0])
2. [values < P] + P + [P< values]
    LHS                      RHS
     |                         |                      
3.  quicksort               quick sort #after sort will bubble itself back up to align into right spot relative to p
   #divide until you have an small/easy enough equation you can conquer 

4. repeat until len arr =1 or 0 (base case)


Basically for code below, you're choosing a pivot each time, with each new set of left & right 
asking left and right to choose a new pivot, and sor itself out
#never actually ask if numbers are in right place in relation to neighbors
#^ just appends / create the pivot value , and appends new left & right array until bubbles right order to top

which is faster recursive or iterative (insert sort)? 
-in this case recursion! 700 versus 30 miliseconds
-worst case is recurisve called everytime
-combo of both functions is  n(complexity of what we call at every level in total) * log n(number of times we recurse) -> O(n logn)
"""

# O(n)
​def partition(data): #will also sort whatever arr passed
    left = []
    pivot = data[0]
    right = []
​
    for val in data[1:]:
        if val <= pivot:
            left.append(val)    
        else:
            right.append(val)
​
    return left, pivot, right #tuple 
​
​#O(logn)
def quick_sort(numbers):
    # base case
    if len(numbers) <= 1:
        return numbers
    
    left, pivot, right = partition(numbers) #calling left, pivot and right here to equal arg from quick_sort into partition (just needts to be in order, foobar names)
    # recursive step
    return quick_sort(left) + [pivot] + quick_sort(right) # + joins 2 arrays
​

​
​
​
​
​
​
​
​
​
​
​
​
​
def sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
​
large_array = [randint(0, 1000) for i in range(100000)]
​
# print("test 10 numbers")
# small_array = copy(large_array[0:10])
# print(f"Array is sorted? {sorted(small_array)}")
# start = time.time()
# insertion_sort(small_array)
# end = time.time()
# print("Insertion sort took:  " + str((end - start)*1000) + " milliseconds")
# print(f"Array is sorted? {sorted(small_array)}")
# print('')
  
​
# print("test 1000 numbers")
# medium_array = copy(large_array[0:1000])
# print(f"Array is sorted? {sorted(medium_array)}")
# start = time.time()
# insertion_sort(medium_array)
# end = time.time()
# print("Insertion sort took:  " + str((end - start)*1000) + " milliseconds")
# print(f"Array is sorted? {sorted(medium_array)}")
# print('')
​
# print("test 10000 numbers")
# print(f"Array is sorted? {sorted(large_array)}")
# start = time.time()
# insertion_sort(large_array)
# end = time.time()
# print("Insertion sort took:  " + str((end - start)*1000) + " milliseconds")
# print(f"Array is sorted? {sorted(large_array)}")
# print('')
​
print("---------------- QUICKSORT ------------------")
print("test 10 numbers")
small_array = copy(large_array[0:10])
print(f"Array is sorted? {sorted(small_array)}")
start = time.time()
sorted_array = quick_sort(small_array)
end = time.time()
print("Quick sort took:  " + str((end - start)*1000) + " milliseconds")
print(f"Array is sorted? {sorted(sorted_array)}")
print('')
  
​
print("test 1000 numbers")
medium_array = copy(large_array[0:1000])
print(f"Array is sorted? {sorted(medium_array)}")
start = time.time()
sorted_array = quick_sort(medium_array)
end = time.time()
print("Quick sort took:  " + str((end - start)*1000) + " milliseconds")
print(f"Array is sorted? {sorted(sorted_array)}")
print('')
​
print("test 10000 numbers")
print(f"Array is sorted? {sorted(large_array)}")
start = time.time()
sorted_array = quick_sort(large_array)
end = time.time()
print("Quick sort took:  " + str((end - start)*1000) + " milliseconds")
print(f"Array is sorted? {sorted(sorted_array)}")
print('')









