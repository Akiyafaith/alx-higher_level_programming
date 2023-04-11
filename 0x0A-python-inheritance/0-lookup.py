#!/usr/bin/python3
"""define a function"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    methods = []
    for att in dir(obj):
        if not att.startswith("_"):
            methods.append(att)
    return methods
