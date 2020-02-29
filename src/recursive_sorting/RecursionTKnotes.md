HOW TO ID WHEN PROB CAN BE Solved with recursion 
-How to use recursion to solve it

-reflection of mirrors
-fractal math pattern (tree structures)
-sum of 2 previous values in fib sequence (except for zero & 1)
-seirpinksi triangle

Def of Recursion:
-base case (or cases) that specific when recursion terminates
(without which pc runs infinite, or out of resources)
- Rule or rules that reduce __all other cases,__ towards a base case! (Repeats rule over & over until reach base case)

def recurse_factorial(n):
    if n==0:
        return 1
    return n * recurse_factorial(n-1) (all the way down to n==0) (for n, mult by term before it) __dont mult by zero

def iter_factorial(n):
    answer=1
    for i in range(n, 0, -1): #0 (is exclusive, so -1 added to include 0, steps thru to 0)
        answer *= i
        return answer 

RANGE
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to end.
step	Optional. An integer number specifying the incrementation. Default is 1
range(start, stop, step)


HOW TO KNOW WHEN TO USE RECURSION? (variation of these phrases or key words)
-When a part of step repeats
-compute nth term of... 
-list the first n terms off.. ""
-generate all possible permutations.. 

PROS & CONS
Intuitive- 
clean (define function over and over )
Tangible starting point/framework of how to start problem

Cons:
NOT PERFORMANT (iterations, have finer grain control than recursive of how things are looped)
Mind Bending?

