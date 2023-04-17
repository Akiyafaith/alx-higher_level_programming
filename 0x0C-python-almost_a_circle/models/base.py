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
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    """define a class method that writes the JSON string
    representation of list_objs to a file"""
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        fname = cls.__name__ + ".json"
        with open(fname, "w") as fn:
            fn.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
                ))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    def load_from_file(cls):
        """returns a list of instances"""
        fn = "{}.json".format(cls.__name__)
        try:
            with open(fn, mode="r", encoding="utf-8") as f:
                objs_json = cls.from_json_string(f.read())
                objs = []
                for obj in objs_json:
                    objs.append(cls.create(**obj))
                return objs
        except FileNotFoundError:
            return []
