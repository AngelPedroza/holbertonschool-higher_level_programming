#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    res = 0
    for i in roman_string:
        if i == 'I':
            res += 1
        if i == 'V':
            res += 5
        if i == 'X':
            res += 10
        if i == 'L':
            res += 50
        if i == 'C':
            res += 100
        if i == 'D':
            res += 500
        if i == 'M':
            res += 1000
    return res
