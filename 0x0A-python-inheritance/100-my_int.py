#!/usr/bin/python3

""""define a class MyInt that inherits from int"""


class MyInt(int):

    """the invert == operator"""
    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        """the invert != operator"""
        return int(self) == int(other)
