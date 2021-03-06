"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
"""


def multiply_nums(nums):
    # Your code here
    # list comprehension
    nums = nums.split(", ")
    product = 1
    for num in nums:
        product *= int(num)
    return product

def multiply_nums_list_comprehension(nums):
    # list comprehension
    temp = 1
    product = [temp := temp * int(num) for num in nums.split(", ")]
        # product *= int(num)
    return product

print(multiply_nums("2, 3"))# ➞ 6
print(multiply_nums("1, 2, 3, 4"))# ➞ 24
print(multiply_nums("54, 75, 453, 0"))# ➞ 0
print(multiply_nums("10, -2"))# ➞ -20

# TODO 
# need to fix the list comprehension
print(multiply_nums_list_comprehension("2, 3"))# ➞ 6
print(multiply_nums_list_comprehension("1, 2, 3, 4"))# ➞ 24
print(multiply_nums_list_comprehension("54, 75, 453, 0"))# ➞ 0
print(multiply_nums_list_comprehension("10, -2"))# ➞ -20
