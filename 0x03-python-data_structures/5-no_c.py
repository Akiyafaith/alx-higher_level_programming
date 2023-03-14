#!/usr/bin/python3
def no_c(my_string):
    """Remove all 'c' and 'C' characters from a string."""
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
