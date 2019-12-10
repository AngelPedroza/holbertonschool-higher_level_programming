#!/usr/bin/python3.4
for i in range(0, 9):
    for x in range(1, 10):
        if x > i:
            if i != 8:
                print("{}{},".format(i, x), end=" ")
            else:
                print("{}{}".format(i, x))
