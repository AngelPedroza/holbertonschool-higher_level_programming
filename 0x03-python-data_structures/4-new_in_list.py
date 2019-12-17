#!/usr/bin/pythn3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    lenght = len(my_list)
    if idx < 0 or idx >= lenght:
        return new_list

    new_list[idx] = element
    return new_list
