#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Return a set of common elements in two sets."""
    # Create an empty set to store common elements
    common = set()

    # Add all common elements to the set
    for elem in set_1:
        if elem in set_2:
            common.add(elem)

    return common
