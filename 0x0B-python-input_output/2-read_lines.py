#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Show a specific number of lines of a file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        n_lines = len(f.readlines())

    if nb_lines <= 0 or nb_lines >= n_lines:
        with open(filename, mode="r", encoding="utf-8") as fd:
            for line in fd:
                print(line, end="")
    else:
        with open(filename, mode="r", encoding="utf-8") as fd:
            for i in range(nb_lines):
                print(fd.readline(), end="")
