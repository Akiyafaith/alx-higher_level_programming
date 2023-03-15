#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    # Create a new list with the same elements as the input list
    result = [elem for elem in my_list]

    # Replace all occurrences of the search element with the replace element
    for i in range(len(result)):
        if result[i] == search:
            result[i] = replace

    return result
