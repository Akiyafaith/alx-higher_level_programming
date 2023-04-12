#!/usr/bin/python3
"""defines a function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """return the number of characters added"""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
