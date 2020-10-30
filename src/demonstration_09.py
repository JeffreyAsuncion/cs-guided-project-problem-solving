"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""

# find the length of the str
    # if odd 
        # return str[len(str)/2 +1]
    # otherwise even
        # return str[len(str):len(str)+2]
def get_middle(input_str):
    # find the length of the str
    length = len(input_str)
    # if odd
    if length % 2 != 0 : 
        return input_str[(length//2)]
    # otherwise even
    else:
        # return str[len(str):len(str)+2]
        return input_str[((length//2)-1) : ((length//2)+1)]

print(get_middle("test"))# -> "es"
print(get_middle("testing"))# -> "t"
print(get_middle("middle"))# -> "dd"
print(get_middle("A"))# -> "A"