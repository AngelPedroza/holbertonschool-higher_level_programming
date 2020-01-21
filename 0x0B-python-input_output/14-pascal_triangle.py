#!/usr/bin/python3
from math import factorial


def pascal_triangle(n):
    """Concat each elemnt"""
    res = []
    if n <= 0:
        return res

    for j in range(n):
        row = []
        for i in range(j + 1):
            row.append(int(factorial(j) / (factorial(i) * factorial(j - i))))
        res.append(row)
    return res
