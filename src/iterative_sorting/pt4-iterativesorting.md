What is an algorithm?
steps that solves set of problems

takes an input => [does something] => output

^^ how slow or fast is this 

1) common sense
2) compete /compare complexities: big -0 notation

main big 0 RT classifications :

-compare arbitrary algorithms of functions and pieces of code
    -algo: take in lots of diff inputs & outputs (2 algo, may have very little in common)
    -bridge algo differences by using big 0 classifications
        -Graph 
            y-axis: # operations
            x-axis: # input size 
                (as input x increases) ,  how many more (# operations performed, y increases)?

Big O can tell us:
-how much longer a function takes/its performance with changes/increase in size of n

*RUN TIME:
-Total number of steps
-

Listed in order of classifications:
 O(c) - constant time (best RT, no huge increase in # of operations per input)  --> inside parenth are some static constant 
 O(log n) - logarithmic time    --> some function
 O(n) -Linear Time  --> function ex/looping once (add 1 step per)
 O(nlogn) - Log-Linear Time --> function ex/python sort()
 O(n^c) Quadratic Time  --> function ()
 O(c^n) Exponential Time (worst RT, large increase in #operations per input)  --> function ex/insertion sort
 O(n!) ex. BOGO sort 