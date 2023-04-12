#!/usr/bin/python3
"""define a class"""


class BaseGeometry:
    """define a Public instance method"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
