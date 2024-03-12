#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1

    result = 1
    power = b

    if b < 0:
        power = b * -1
    for _ in range(power):
        result *= a
    if b > 0:
        return result
    else:
        return 1 / result
