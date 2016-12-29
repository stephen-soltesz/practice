#!/usr/bin/python

import collections


def main():
    print rpn('1729')
    print rpn('3,4,+,2,x,1,+')
    print rpn('1,1,+,-2,x')
    print rpn('-641,6,/,28,/')


def push(a, val):
    a.insert(0, val)


def pop(a):
    a.pop(0)


def evaluate(a, b, o):
    a = float(a)
    b = float(b)
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == 'x':
        return a * b
    elif o == '/':
        return a / b
    else:
        raise Exception('unknown operator: "%s"' % o)


def rpn(exp):
    s = collections.deque()
    for field in exp.split(','):
        if field in ['+', '-', 'x', '/']:
            b = s.pop()
            a = s.pop()
            v = evaluate(a, b, field)
            s.append(v)
        else:
            s.append(field)

    assert(len(s) == 1)
    v = s.pop()
    return float(v)


if __name__ == '__main__':
    main()
