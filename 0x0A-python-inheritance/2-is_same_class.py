#!/usr/bin/python3
"""define a  function"""


def is_same_class(obj, a_class):
    """ return True if the object is exactly an instance of the specified class
    otherwise False"""
    return type(obj) == a_class
