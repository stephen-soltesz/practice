#!/usr/bin/python

import random
import sys

# deterministic
random.seed(0)


# 30, 71, 90
def main():
    v = int(sys.argv[1])
    a = [ int(random.random() * 100) for i in range(40) ]
    a = list(sorted(a))
    i = [ x for x in range(len(a)) ]
    print i
    print a
    u = len(a) - 1
    l = 0
    print l, u
    while l <= u:
        m = (u + l) // 2
        if a[m] == v:
            print l, u, m, a[m]
            break
        elif a[m] < v:
            l = m + 1
            print l, u, m, a[m]
        elif a[m] > v:
            u = m - 1
            print l, u, m, a[m]

main()
