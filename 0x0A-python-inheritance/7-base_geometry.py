#!/usr/bin/python3
"""define a class BaseGeometry"""


class BaseGeometry:
    """define a public instance method that raises an exception with
    the message area() is not implemented"""
    def area(self):
        raise Exception('area() is not implemented')
    """define a instance method that validates a value.Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than or equal to 0"""
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
