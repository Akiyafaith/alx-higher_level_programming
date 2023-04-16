#!/usr/bin/python3
"""define a class Base"""


class Base:
    __nb_objects = 0

    """initialize an instance of the class Base"""
    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
