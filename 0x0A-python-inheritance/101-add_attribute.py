#!/usr/bin/python3

"""define a function"""


def add_attribute(obj, attribute, value):
    """adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
