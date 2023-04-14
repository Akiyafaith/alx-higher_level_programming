#!/usr/bin/python3
"""define a function"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    methods = []
    atts = []
    for att in dir(obj):
        #if not (att.startswith("__") and att.endswith("__")):
            if callable(getattr(obj,att)):
                methods.append(att)

            else:
                atts.append(att)
    return sorted(atts) + sorted(methods)
