#!/usr/bin/python3
def add_integer(a, b=98):
    """
''add_integer(a, b=98)'' add two integers numbers.
You can use a integer or float number like parameter,
once inside of the function each parameter us cast to
integer. If some parameter is diffrent type from int
or float the functione raise TypeError with a message.
    """
    if type(a) in [int, float]:
        num1 = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) in [int, float]:
        num2 = int(b)
    else:
        raise TypeError("b must be an integer")

    if type(num1) is int and type(num2) is int:
        return num1 + num2
