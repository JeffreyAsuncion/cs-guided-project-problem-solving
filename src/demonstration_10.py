"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    # Your code here
    input_str = input_str.split(' ')
    # result = inputNums
    result = [int(i) for i in input_str]
    result.sort()
    maxNum = result[-1]
    minNum = result[0]
    return f"{maxNum} {minNum}"


print(max_and_min("1 2 3 4 5"))# -> "5 1"
print(max_and_min("1 2 -3 4 5"))# -> "5 -3"
print(max_and_min("1 9 3 4 -5"))# -> "9 -5"
