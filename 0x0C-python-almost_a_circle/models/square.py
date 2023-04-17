#!/usr/bin/python3
from models.rectangle import Rectangle
"""define a class square that inherits from Rectangle"""


class Square(Rectangle):
    """initialize the rectangle instance"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size> representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,self.width)
