#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    module = number % -10
else:
    module = number % 10
if module > 5:
    print("Last digit of {} is {} ".format(number, module), end=" ")
    print("and is greater than 5")
elif module == 0:
    print("Last digit of {} is {} and is 0".format(number, module))
elif module < 6 and module != 0:
    print("Last digit of {} is {} ".format(number, module), end=" ")
    print("and is less than 6 and not 0")
