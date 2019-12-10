#!/usr/bin/python3.4
def uppercase(str):
    for i in range(len(str)):
        y = str[i]
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            y = chr(ord(str[i]) - 32)
        print("{}".format(y), end='')
    print()
