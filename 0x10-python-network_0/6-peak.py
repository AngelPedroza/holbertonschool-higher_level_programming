#!/usr/bin/env python3
"""Find the peak in an array"""

def find_peak(list_of_integers):
    """Funtion to find the peak"""
    l = list_of_integers

    if l is None:
        return None
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        if l[0] <= l[1]:
            return l[1]
        else:
            return l[0]

    if len(l) >= 3:
        res = 0
        r_left = 0
        r_right = 0
        flag = 0
        for n in range(len(l) - 1):
            if l[n - 1] <= l[n] and l[n + 1] <= l[n] and flag == 0:
                res = l[n]

                if r_left < 0:
                    r_left *= -1
                if r_right < 0:
                    r_right *= -1

                if r_left < l[n] - l[n - 1]:
                    r_left = l[n] - l[n - 1]
                    flag = 1
                else:
                    flag = 0

                if r_right < l[n] - l[n + 1]:
                    r_right = l[n] - l[n + 1]
                    flag = 1
                else:
                    flag = 0

        return res
