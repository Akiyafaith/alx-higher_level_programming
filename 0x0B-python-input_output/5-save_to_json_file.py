#!/usr/bin/python3
import json
"""defines a function that writes an Object to a text file,
using a JSON representation"""


def save_to_json_file(my_obj, filename):
    try:
        with open(filename, 'w') as fn:
            json.dump(my_obj, fn)
    except TypeError as e:
        raise TypeError(f"{my_obj} is not JSON serializable")
