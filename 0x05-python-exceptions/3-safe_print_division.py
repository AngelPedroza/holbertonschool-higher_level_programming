#!/usr/bin/pyhton3
def safe_print_division(a, b):
    try:
        res = None
        res = a / b
        return res
    except:
        return None
    finally:
        print("Inside result: {}".format(res))
