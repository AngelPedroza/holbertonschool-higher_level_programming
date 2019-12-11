#!/usr/bin/python3.4
for i in range(ord('z'), ord('a') - 1, -1):
    y = chr(i)
    if i % 2 != 0:
        y = chr(i - 32)
    print("{}".format(y), end='')
