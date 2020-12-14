"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def repeat_it(input_str):
    # Your code here
    # initialize a new_str
    new_str = ""
    counter = 0
    #for each letter in input_str uppercase and multiply and addd to list
    for i, letter in enumerate(input_str):
        if i == 0:
            letter = letter.upper()
            new_str = letter + "-"
        elif i == len(input_str) - 1:
            new_str += letter.upper() + (letter.lower()*(i))
        else:
            new_str += letter.upper() + (letter.lower()*(i) + "-")
    
        
    # return the result new_str
    return new_str

print(repeat_it("abcd"))# -> "A-Bb-Ccc-Dddd"
print(repeat_it("RqaEzty"))# -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(repeat_it("cwAt"))# -> "C-Ww-Aaa-Tttt"

