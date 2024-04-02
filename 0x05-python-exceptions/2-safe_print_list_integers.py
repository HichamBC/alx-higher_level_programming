#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0

    for i in range(x):
        try:
            item = my_list[i]
        except IndexError:
            raise
        if type(item) == int:
            num += 1
            print("{:d}".format(item), end="")

    print()
    return num
