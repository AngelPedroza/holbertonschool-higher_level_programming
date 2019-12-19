#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    num = []
    for i in roman_string:
        if i == 'I':
            num.append(1)
        if i == 'V':
            num.append(5)
        if i == 'X':
            num.append(10)
        if i == 'L':
            num.append(50)
        if i == 'C':
            num.append(100)
        if i == 'D':
            num.append(500)
        if i == 'M':
            num.append(1000)
    res = 0
    bool = False
    for x in range(len(num)):
        if bool is True:
            bool = False
            continue
        if (x + 1) < len(num):
            if num[x] < num[x + 1]:
                res += num[x + 1] - num[x]
                bool = True
                continue
            else:
                res += num[x]
        if (x + 1) == len(num):
            res += num[x]
    return res
