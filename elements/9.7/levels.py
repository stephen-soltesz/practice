#!/usr/bin/python

import collections


def main():
    print levels([])


def levels(tree):
    s = collections.deque()
    s.append(tree)
    r = []
    while len(s) > 0:
        l = collections.deque()
        v = []
        while len(s) > 0:
            t = s.pop()
            if t.left:
                l.append(t.left)
            if t.right:
                l.append(t.right)
            v.append(t.value)
        if v:
            r.append(v)
        s = l

    return r


if __name__ == '__main__':
    main()
