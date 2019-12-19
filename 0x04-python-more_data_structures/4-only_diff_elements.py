#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    final = []
    for x in set_1:
        if x not in set_2:
            final.append(x)
    for y in set_2:
        if y not in set_1:
            final.append(y)
    return final
