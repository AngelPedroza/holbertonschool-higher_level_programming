#!/usr/bin/python3
def raise_exception():
    try:
        a = "hola"
        print(a / 2)
    except TypeError:
        raise TypeError
