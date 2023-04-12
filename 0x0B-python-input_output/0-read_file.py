#!/usr/bin/python3

""""define a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """returns NONE"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
