#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    # Compute the symmetric difference between the two sets
    diff = set_1.symmetric_difference(set_2)

    return diff
