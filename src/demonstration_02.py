"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
"""
import numpy as np

def add_indexes(numbers):
    # Your code here
    new_lst = []
    for i, element in enumerate(numbers):
        new_lst.append(int(i)+int(element))

    return new_lst

print(add_indexes([0, 0, 0, 0, 0]))# ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5]))# ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1]))# ➞ [5, 5, 5, 5, 5]
