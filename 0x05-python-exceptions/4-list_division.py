#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            quotient = 0
            if type(my_list_1[i]) not in (int, float):
                print("wrong type")
            elif type(my_list_2[i]) not in (int, float):
                print("wrong type")
            elif my_list_2[i] == 0:
                print("division by 0")
            else:
                quotient = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        finally:
            new_list.append(quotient)
    return new_list
