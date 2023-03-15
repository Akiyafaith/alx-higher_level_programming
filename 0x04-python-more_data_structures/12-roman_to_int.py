#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_val = 0

    for char in roman_string[::-1]:
        curr_val = roman_dict[char]

        if curr_val < prev_val:
            result -= curr_val
        else:
            result += curr_val

        prev_val = curr_val

    return result
