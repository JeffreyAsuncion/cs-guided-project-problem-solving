"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_ctr = 0
    for letter in input_str:
        if letter in vowels:
            vowel_ctr += 1
    return vowel_ctr

print(get_count("aaaaaaaa"))

