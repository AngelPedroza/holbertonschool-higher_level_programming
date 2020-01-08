#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for a in range(x):
            print("{}".format(my_list[a]), end="")
    except:
        a = a - 1
    finally:
        print()
        return a + 1
