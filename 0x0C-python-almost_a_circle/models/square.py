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
    @property
    def size(self):
       """ get the size attributes"""
       return self.width

    @size.setter
    def size(self, value):
       """setter for the size attribute"""
       self.width = value
       self.height = value

    """public method that assigns attributes"""
    def update(self, *args, **kwargs):
        if args:
            att = ["id", "size", "x", "y"]
            for n in range(len(args)):
                setattr(self, att[n], args[n])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        return {
                "id": self.id,
                'size': self.size,
                "x": self.x,
                "y": self.y
            }
