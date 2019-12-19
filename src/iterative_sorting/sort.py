def insertion_sort(numbers):
​
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
    print(numbers)
​
​
insertion_sort([5, 6, 1, 9, 7, 2, 3])
insertion_sort([1, 3, 5, 6, 4])
insertion_sort([4, 3, 2, 2, 5, 6, 7, 7])
insertion_sort([])
insertion_sort([1, 2, 3, 4, 5])
​

"""
-COMPARE EACH ITEM TO EACH OTHER
-TAKE EVERY ITEM, LOOK AT EVERY OTHER ITEM => RT COMPLEXITY IS N^2 (WORST CASE IS REVERSE SORT)
-SORT ARR OF BOOKS BY GENRE
-
"""

