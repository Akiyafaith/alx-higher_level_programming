#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the same list if idx is out of range
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])  # Copy all items except the one at idx
    return new_list
