#!/usr/bin/python

def reverse_int(i):
    s = str(abs(i))
    r = ''.join(reversed(s))
    if i >= 0:
        return int(r)
    else:
        return int('-' + r)


for i in (123, 2435, 5678, -321):
    print i, reverse_int(i)
