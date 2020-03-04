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


def sorted(books):
    return all(books[i].genre <= books[i+1].genre for i in range(len(books)-1))

def insertion_sort(numbers):
    for i in range(1, len(numbers)): #O(n)
        current_num= numbers[i] <- #O(1) #each time in this loop, saving to var curr_num not doing anything to code unless while conditions True

        j=i #O(1) #tracks every number to left of i that we need to compare 
        while j >0 and current_num <numbers[j-1]: #O(n) worst case, 0(1) best case (no while loop ran) #RUN CODE BELOW if current j value is less  than j value to left. 
           numbers[j] = numbers[j-1] #O(1) #swap if curr_num < number to the left of it numbers[j-1] (duplicates left value temp to right)
            j -= 1  #O(1) #KEEPS WHILE LOOP RUNNNING TO THE LEFT (BY MOVING NEW j TO LEFT TO RUN THIS CODE) & only stops while loop if curr_num < numbers[j-1]
        numbers[j] = current_num #O(1) #j represents where curr_num should be inserted. position curr_num into right spot, rep by j
                                    # if array is already sorted up to that point numbers[j] = numbers[i] //no change in original arr
                                    # THIS IS EXECUTED IF CONDITION OF WHILE LOOP ISN'T TRUE & CURR NUMBER IS NO LONGER LESS THAN NUM[J-1]
                                    #numbers[j] becomes curr_num 
        return numbers

#big(O) 
#worst case bigO => nested loops n^2
#when have loops:  take a look at code inside & multiply by times for loop runs