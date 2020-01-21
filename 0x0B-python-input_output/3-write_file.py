#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Write a message in a file (created if not exist or overwrite if exist)
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
