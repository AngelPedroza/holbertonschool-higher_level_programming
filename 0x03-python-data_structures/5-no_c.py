#!/usr/bin/python3.4
def no_c(my_string):
    new_list = list(my_string)
    for i in new_list:
        if i == 'c' or i == 'C':
            new_list.remove(i)
    new_string = "".join(new_list)
    return new_string
