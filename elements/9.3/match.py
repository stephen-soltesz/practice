#!/usr/bin/python

import collections


def main():
    print match('([]){()}')
    print match('[()[]{()()}]')
    print match('{)')
    print match('[()[]{()()')


def pair(l, r):
    return ((l, r) == ('(', ')') or
            (l, r) == ('[', ']') or
            (l, r) == ('{', '}'))


def match(exp):
    s = collections.deque()
    for field in exp:
        if field in ['[', '{', '(']:
            s.append(field)
        elif field in [']', '}', ')']:
            l = s.pop()
            if not pair(l, field):
                return False, (l, field)

    if len(s) > 0:
        return False, tuple(s)

    return True, None


if __name__ == '__main__':
    main()
