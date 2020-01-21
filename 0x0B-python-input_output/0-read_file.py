#!/usr/bin/python3
def read_file(filename=""):
    """Open, read and show the content of a file"""
    with open(filename, mode="r", encoding="utf-8") as fd:
        print(fd.read(), end="")
