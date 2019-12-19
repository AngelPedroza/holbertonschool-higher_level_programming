#!/usr/bin/python3
def weight_average(my_list=[]):
    a = []
    for i in my_list:
        if len(i) == 0:
            a.append((0, 0))
        if len(i) == 1:
            a.append((i[0], 0))
        else:
            a.append(i)

    score = 0
    weight = 0
    for x in a:
        score += (x[0] * x[1])
    for y in a:
        weight += y[1]
    return score / weight
