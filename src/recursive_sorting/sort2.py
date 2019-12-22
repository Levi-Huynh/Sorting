
#rt O(n^2) (nested loops)
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


    #if we dont pass in copy, may modify array 
    