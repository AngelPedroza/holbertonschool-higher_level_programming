#!/usr/bin/python3
def text_indentation(text):
    """
    ''def text_indentation(text):'' Print a new line if
    find the '.', ':' or '?'."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        L = 0
        bool = False

        for i in range(len(text)):
            if text[i] in ['.', ':', '?']:
                print(text[L:i + 1])
                print()
                L = i + 2
                bool = True

        if i + 1 == len(text) and bool is False:
            print(text)
