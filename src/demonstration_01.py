"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

Write a function that retrieves the first n elements from a list
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

- [0 to n] python we have a slice (takes a sub section of a list and returns that data as a list)
- [start inclusive : end exclusive]
- in JS / TS `.slice` method
"""

# check if n is greater than then length of the list
    # then return "invalid" to the caller
# otherwise if n is equal to zero
    # return an empty list

# otherwise
# return the slice of [length of the list : ]
    # return the slice of [0 : n]


def last(a, n):
    # check if n is greater than then length of the list
    if n > len(a):
        return "invalid"
    elif n == 0:
        return []
    else:
        return a[len(a) - n : len(a)]
        #return a[-n:]

print(last([1, 2, 3, 4, 5], 1)) # ➞ [5]
print(last([4, 3, 9, 9, 7, 6], 3)) # ➞ [9, 7, 6]
print(last([1, 2, 3, 4, 5], 7)) # ➞ "invalid"
print(last([1, 2, 3, 4, 5], 0)) # ➞ []
