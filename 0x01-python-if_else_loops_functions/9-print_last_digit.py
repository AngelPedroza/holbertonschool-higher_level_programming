#!/usr/bin/python3.4
def print_last_digit(number):
    ld = number
    if number > 0:
        ld = number % 10
    elif number < 0:
        ld = number % -10
        ld = ld * -1
    print("{}".format(ld), end='')
    return ld
