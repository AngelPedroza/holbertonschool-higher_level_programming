#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = {}
    for x in my_list:
        if x not in seen:
            seen[x] = 1
        else:
            seen[x] += 1
    suma = 0
    for i in seen:
        suma = suma + i
    return suma
