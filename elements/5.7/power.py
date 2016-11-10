#!/usr/bin/python


def power(x, y):
    p = y
    result = 1

    while p > 0:
        if p & 0x1 > 0:
            result = x * result
        x = x * x
        p = p >> 1

    return result


for i in range(10):
    print i, 7**i, power(7, i)
