#recursive lecture Dec 5

#HELP CHAnnel questions


#recursive fn calls itself
# how do we analyze them? 
#HOW MANY TIMES DO WE RECURSE x f(n) complexity

#O(n)
def n_demo(n):
    print(n) #rt O(1)
    # base case/ when to break loop
    if n == 0: #o(1)
        return
    print(n) #o(1)
    # recursive case 
    n_demo(n-1) # O(n) <-- recurse this many times. # RECURSIVE CASE BY NATURE: WILL KEEP REPEATING, UNTIL BASE CASE OCCURS #rt O(n) 
                # total RT = O(1) x O(n)

n_demo(5)

# O(n^2)
def two_n_demo(n): 
    print(n)
    if n==0:
        return
    two_n_demo(n-1) #O(n)   
    two_n_demo(n-1) #O(n) 
                        #for lines 27 & 28 above, each iteration of n, exponentially increases the # of operations  think pyramid
                        # for each next n, calls exponentially increases by 2. 1st n = 2 calls, 2nd n = 4 calls, 3rd n = 8 calls n=15 for n=4 etc
                        # 31 for n =5 
                        # 2 recursive cases with linear argument (n-1) => 2^n
                        # 3 recurisve cases will be 3^n

#O(logn)
def divide_n_demo(n):
    print(n) #O(1)
    if n <=1: #O(1)
        return
    divide_n_demo(n/2) #O(logn) x O(1)

# ^ to make this O(n log n), can add an operation like for loop to create n * logn operations = O(n logn)

#O(2^logn)=>O(n)
def divide_n_demo1(n):
    print(n) #O(1)
    if n <=1: #O(1)
        return
    divide_n_demo1(n/2) #O(logn) x O(1)
    divide_n_demo1(n/2)
        #rt: 2^(logn)==>O(n), if calls recursive 3 times is 3^(logn)