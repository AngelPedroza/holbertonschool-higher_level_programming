#!/usr/bin/python3
from math import factorial

def combination(n, r):
    """Pascal math way"""
    return int(factorial(n) / (factorial(r) * factorial(n -r)))

def pascal_triangle(n):
    """Concat each elemnt"""
    res = []
    if n <= 0:
        return res

    for j in range(n):
        row = []
        for i in range(j + 1):
            row.append(combination(j, i))
        res.append(row)
    return res
