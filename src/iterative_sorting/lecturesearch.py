names = [
    'Artem',
    'Austin',
    'Chad',
    'Dustin',
    'Elissa',
    'Emily',
    'Jamar',
    'Justin',
    'Katherine',
    'Kyran',
    'Levi',
    'Reed',
    'Ronny',
    'Wilfred',
    'Yasirah',
]

# O(n) RT Complexity
#Worst case or longest RT = whatever the last index is (the longest number of searches to find value of last index, or FALSE/CANT FIND)

def linear_search(array, value): #rt complexity: O(n) The longer the array more steps it may take to find name
    for name in array:
        if name == value:
            return True
    return False

#BINARY SEARCH
# COMPLEXITY: 
    #FIGURING OUT: WHAT CONDITIONS STOP LOOP 
    #HOW MANY TIMES LOOP RUNS
    #DIVIDES ARR AT EVERY STEP (SMELLS LIKE LOG N!!!) => HALVING TOTAL AMOUNT OF INPUT MUST DEAL WITH
    #HOW IS EACH STEP RELATED TO SIZE OF ARRAY
# STARTS AT MIDDLE CHECK IF RIGHT SOLUTION, OR GREATER OR LESS THAN
#MORE EFFICEINT -EVERY MOMENT ASK T/F BIGGER/LOWER, DECIDE TO GO UP OR DOWN 
# BINARY SEARCH= BEST WAY TO SEARCH IF LIST IS SORTED
# while loop may be easier to use our pointers (end, start, middle). ANYTIME HAVE TO CHANGE INPUT ON GO, FOR LOOP MAYBE HARD
# WHILE LOOP, EASIER TO DECIDE WHEN TO BREAK IN LOOP
# FOR STRINGS COMPARSION BASED ON FIRST LETTER OF ALPHA
# USE REFERENCE ARRAY IF GET STUCK ON CREATING START/END POINTERS
#Time complexity is O(nlogn) (and this is the number of times the inner loop repeats itself).
#Outer loop runs n times. For the bth iteration of the outer loop, the inner loop runs log_3(n-b) times.
#WORST CASE HERE IS IF NOTHING IS FOUND -CONSIDER RT OF LOOP: DIVIDES ARRAY EACH STEP => LOG N
#2^n NOT EFFICIENT!

# LOG N RT COMPLEXITY 
def binary_search(array, value):
    start = 0    #pointer to point to beginning of array (so we can point to new middle)
    end = len(array) - 1 #pointer to point to end array (so can point to new middle)

    found = False #FLAG VALUE

    while not found and start <= end: #MAKE SURE END INDEX DOESNT GET SMALLER THAN START INDEX (START SHOULD BE ACTUAL START, END SHOULD BE ACTUAL END ELSE NO LONGER BE VALID POINTERS)
        middle = (start + end) // 2        
        # if found break
        if array[middle] == value:
            found = True #SWITCH FLAG. THIS WILL EVER ONLY RETURN TRUE OF FOUND = VALUE AFTER RUNNING WHILE LOOP. ELSE FALSE ALWAYS.
        else: #TEACHING ARRAY TO COMPARE NEXT CORRECT VALUE IF MIDDLE != VALUE
            if value < array[middle]:
                # Value is < middle => search lower half
                end = middle - 1 # moves the middle 1 to left, rerun IF CHECK FOR NEW MIDDLE VALUE
            else:
                # else search upper half
                start = middle + 1 #moves the middle 1 to right , rerun IF CHECK FOR NEW MIDDLE VALUE

    return found


print(binary_search(names, 'Katherine'))
print(binary_search(names, 'Ronny'))
print(binary_search(names, 'Justin'))
print(binary_search(names, 'Doug'))
