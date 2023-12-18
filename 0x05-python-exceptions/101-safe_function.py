#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return (res)
    except ZeroDivisionError as error_message:
        print("Exception: {}".format(error_message), file=sys.stderr)
    except IndexError as error_message:
        print("Exception: {}".format(error_message), file=sys.stderr)
        return (None)
