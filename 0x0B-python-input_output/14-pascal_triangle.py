#!/usr/bin/python3
def pascal_triangle(n):
    """ Pascal Math"""
    res = []
    if n <= 0:
        return res
    for row in range(n):
        for col in range(row + 1):
            if col == 0:
                res.append([1])
            elif col == row:
                res[row].append(1)
            else:
                res[row].append(res[row - 1][col] + res[row - 1][col - 1])
    return res
