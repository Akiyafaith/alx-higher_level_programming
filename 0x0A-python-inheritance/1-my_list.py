#!/usr/bin/python3

"""define a class MyList that inherits from list"""


class MyList(list):
    """define a instance method, that prints the list,
    but sorted (ascending sort)"""
    def print_sorted(self):
        print(sorted(self))
