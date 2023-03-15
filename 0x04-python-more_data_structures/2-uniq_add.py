#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    # Create an empty set to store unique integers
    unique_integers = set()

    # Add all unique integers to the set
    for elem in my_list:
        if isinstance(elem, int):
            unique_integers.add(elem)

    # Compute the sum of all unique integers
    result = sum(unique_integers)

    return result
