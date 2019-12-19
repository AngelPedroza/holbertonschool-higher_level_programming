#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    count = 0
    for i in a_dictionary:
        if a_dictionary[i] is None:
            return None
        if count == 0:
            high = a_dictionary[i]
        if a_dictionary[i] > high:
            high = a_dictionary[i]
        count += 1
    for x in a_dictionary:
        if a_dictionary[x] == high:
            break
    if high == 0:
        return None
    return x
