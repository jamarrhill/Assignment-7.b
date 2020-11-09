# Name: Jamar Hill
# Date: 11/8/2020
# Description: Assignment 7.b

"""Define a function that reverses a list of numbers"""
def reverse_list(vals):
    """First variable is in the zero position"""
    fst = 0
    """Last variable is in the -1 position"""
    lst = len(vals)-1
    """formula to replace first positions variable with last position variable, while counting backward form this position"""
    while fst < lst:
        t = vals[fst]
        vals[fst] = vals[lst]
        vals[lst] = t
        fst += 1
        lst -= 1

"""Testing for this formula"""
vals = [7, -3, 12, 9]
reverse_list(vals)
print(vals)