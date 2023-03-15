#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    # Get a list of the dictionary keys and sort it
    sorted_keys = sorted(a_dictionary.keys())

    # Loop through the sorted keys and print the key-value pairs
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
