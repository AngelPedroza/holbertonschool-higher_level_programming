#!/usr/bin/python3
def number_of_lines(filename=""):
    """Return the lines of a file opened"""
    with open(filename, mode="r", encoding="utf-8") as fd:
        return len(fd.readlines())
