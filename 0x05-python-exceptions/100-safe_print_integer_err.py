#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False

    return True
