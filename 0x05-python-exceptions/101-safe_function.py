#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(args[0], args[1])
        return res
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
