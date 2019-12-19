#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    bool = False
    for i in a_dictionary:
            if a_dictionary[i] == value:
                bool = True
                break
    if bool is True:
        dic = {}
        for i in a_dictionary:
            if a_dictionary[i] != value:
                dic[i] = a_dictionary[i]
        return dic
    return a_dictionary
