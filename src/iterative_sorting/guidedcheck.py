# BASE cases: WHERE RECURSION NEEDS TO STOP EXECUTION (OR ELSE INFINITE)
# LAST LINE: HOW RECURSIVE FUNCTION MOVES TOWARD DEFINED BASE CASES!


def recurse_checkarray(arr, el):
    if len(arr) == 0:
        return False
    if arr[0] == el:  #ONLY CHECKing if first element of arr is equal to el. checks 
        return True
    return recurse_checkarray(arr[1:], el)


mine = [4, 5, 6, 3, 2, 3, 5, 7]

print(recurse_checkarray(mine, 7))
