#!/usr/bin/python3
"""define a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
