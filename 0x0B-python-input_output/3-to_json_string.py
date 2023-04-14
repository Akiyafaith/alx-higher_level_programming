#!/usr/bin/python3
import json

"""defines a function"""


def to_json_string(my_obj):
    """returns: the JSON representation of an object (string)"""
    return json.dumps(my_obj, default=default)
