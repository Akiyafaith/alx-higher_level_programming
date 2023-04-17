#!/usr/bin/python3
import json
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
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries,
        Otherwise, return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    """define a class method that writes the JSON string representation of list_objs to a file"""
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        fname = cls.__name__ + ".json"
        with open(fname, "w") as fn:
            fn.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))
    
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
