#!/usr/bin/python3.4
from calculator_1 import add, sub, mul, div
import sys

if len(sys.argv) == 4:

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sing = sys.argv[2]

    optr = {'+': add,
            '-': sub,
            '*': mul,
            '/': div}

    for i in optr:
        if sing == i:
            res = optr[i](a, b)
            print("{} {:} {} = {}".format(a, i, b, res))
            exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
else:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
