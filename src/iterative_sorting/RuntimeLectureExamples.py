import math 
from math import sqrt

import math 
from math import sqrt

#Rules for forloops
"""
#is this why God taught me to workout so hard all these years b/c he knew I needed the recharge during some times
1) analyze each line
2) if for loop
-   analyze lines inside (instantiating variable = O(1)) 
- take total big(0)
-multiply by complexity of loop

3)
## Lines on the same scope = addition
### in (addition) scenario, if one bigO trumps another, drop the weaker bigO & keep the worst case scenario
(O(n) > O(1) && O(n) > O(log(n)))

## Lines on diff scope = multiply 

4) 
# When the input is halved (or another division) every step of the loop
# Think logarithmic! 
 O(log(n)) is more optimal than O(n)

"""
# O (1)
def mult_2(n):
  return n * 2

#O (n)
def foo(n): # we multiply the loop with the runtime inside it to get O(N) * O(1)
  for i in range(0, n):   # O(N) <- n b/c we only will conduct this operation up to the # n or up to range n
    print(i)              # O(1)  <- 1 b/c we only do 1 operation


# O(n^2)
def bar(n):
    s = 0 #O(1) (constant time)

    for i in range(n):         # runs n times /runs n # of  operations
        for j in range(n):       # runs n times / runs n # of operations
            s += i * j   #O(1) -constant time         # total n * n times, or n^2 times  O(n^2)

    return s                #(s=0) and (for i loop) are in the same scope so 0(1) + O(n) , but can take off O(1) keep worst case O(n)



# O(n sqrt n)
def baz(n):
    s = 0 #O(1)

    for i in range(n):                 # n times / runs n # of operations
        for j in range(int(sqrt(n))):    # sqrt(n) times /  runs sqrt(n) # operations 
            s += i * j                     # <--1 <-- n * sqrt(n) times = runtime=  # O(n sqrt n)

    return s



# O(2n^2) => (O(n^2))
def frotz(n):
    s = 0

    for i in range(n):            # n / runs n # of operations
        for j in range(2 * n):      # 2n / runs 2 * n number of # operations 
            s += i * j                # <-- n * 2n == 2 * n^2

    return s


# When the input is halved (or another division) every step of the loop
# Think logarithmic! 
# O (log(n))
def divider(n):
  while n >= 0:
    n = n/2