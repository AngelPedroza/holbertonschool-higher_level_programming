#!/usr/bin/python3.4
for i in range(97, 123):
    if i == 113 or i == 101:
        continue
    else:
        print("{}".format(chr(i)), end="")
