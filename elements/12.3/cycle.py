#!/usr/bin/python

import random
import sys
import time

# Deterministic.
random.seed(0)


# 30, 71, 90
def main():
    a = [ int(random.random() * 100) for i in range(40) ]
    a = list(set(sorted(a)))
    b = a # a[32:] + a[:32]
    print b
    i = [ x for x in range(len(b)) ]
    print zip(i, b)

    u = len(b) - 1
    l = 0
    print l, u
    while l < u:
        m = (u + l) // 2
        if b[l] < b[m]:
            l = m
        else:
            u = m

        print l, u, m, b[m]
        time.sleep(1)

        #if a[m] == v:
        #    print l, u, m, a[m]
        #    break
        #elif a[m] < v:
        #    l = m + 1
        #    print l, u, m, a[m]
        #elif a[m] > v:
        #    u = m - 1
        #    print l, u, m, a[m]


if __name__ == '__main__':
    main()
