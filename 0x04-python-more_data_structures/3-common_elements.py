#!/usr/bin/python3
def common_elements(set_1, set_2):
    final = []
    for x in set_2:
        if x in set_1:
            final.append(x)
    return final
