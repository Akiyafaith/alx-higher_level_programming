#!/usr/bin/python3

import json

"""define a function that creates an Object from a “JSON file"""


def load_from_json_file(filename):
    """returns: the Python object created from the JSON file"""
    with open(filename) as fn:
        return json.load(fn)
