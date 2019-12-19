import math 
from math import sqrt

"""
For Space Time Complexity Question to ask:
-ARE WE ADDING MORE SPACE? /ITEM INSTANTIATION/ ARE WE CREATING ANYTHING
-
"""

# O(1) space complexity example
#
# Same additional space used no matter how big `n` is.
def foo(n):
  total = 0 # creating O(1) space here 

  for i in range(n): #no space complexity 
    total += i #not creating more space, just manipulating total var 

  return total

# O(n) space complexity example
#
# Additional space used is proportional to `n` (DIFF SCOPE, MULT. INNER LOOP IS O(1))
def bar(n):
  sums = [] #O(1)

  for i in range(n): #not creating space complexity if the code inside it isn't adding space, but if it is, space is added for n size in this exanple
    sums.append(i + i) #O(1) space

  return sums

# O(n^2) space complexity example
#
# Additional space used increases by the square of `n`
def baz(n):
  times_table = [] #O(1)

  for i in range(n): #(n)
    row = [] #O(1)

    for j in range(n): #(n)
      row.append(j * i) #O(1)
    
      #for i in range (10): # this would be O(1)

    times_table.append(row)

  return times_table
