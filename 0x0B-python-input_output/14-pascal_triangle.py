#!/usr/bin/python3
def pascal_triangle(n):
    """ Pascal Math"""
    tri =[]
    if n <= 0:
        return tri
    for row in range(n):
       for col in range(row+1):
          if col == 0:
             tri.append([1])
          elif col == row:
             tri[row].append(1)
          else:
             tri[row].append(tri[row-1][col]+tri[row-1][col-1])
    return tri
