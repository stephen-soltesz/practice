#!/usr/bin/python

import sys
import math
import decimal


def main():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for i in xrange(n):
            line = f.readline().strip()
            print 'Case #%d:' % (i + 1),
            x1, y1, x2, y2, x3, y3 = map(decimal.Decimal, line.split())
            a2, b2, c2 = lengths_squared(x1, y1, x2, y2, x3, y3)

            if (not is_valid_length(a2.sqrt(), b2.sqrt(), c2.sqrt()) or
                not is_valid_slope(x1, y1, x2, y2, x3, y3)):
                print 'not a triangle'
            else:
                kind = get_kind(a2, b2, c2)
                angle = get_angle(a2, b2, c2)
                print kind, angle, 'triangle'


def is_valid_length(l1, l2, l3):
    if l1 == 0:
        return False
    # if l1 + l2 <= l3:
    #     return False
    if l1 + l2 <= l3 or l2 + l3 <= l1 or l3 + l1 <= l2:
        return False
    return True


def is_valid_slope(x1, y1, x2, y2, x3, y3):
    if (slope_intercept(x1, y1, x2, y2) == slope_intercept(x2, y2, x3, y3) or
        slope_intercept(x2, y2, x3, y3) == slope_intercept(x3, y3, x1, y1) or
        slope_intercept(x3, y3, x1, y1) == slope_intercept(x1, y1, x2, y2)):
        return False
    return True


def slope_intercept(x1, y1, x2, y2):
    if x2 - x1 != 0:
        m = (y2 - y1) / (x2 - x1)
        b = -1 * m * x1 + y1
        return m, b
    else:
        return float('nan'), float('nan')


def get_kind(a2, b2, c2):
    if a2 != b2 and b2 != c2 and c2 != a2:
        return 'scalene'
    elif a2 == b2 or b2 == c2:
        return 'isosceles'

    raise Exception('impossible')


def get_angle(a2, b2, c2):
    if a2 + b2 == c2:
        return 'right'
    elif a2 + b2 < c2:
        return 'obtuse'
    elif a2 + b2 > c2:
        return 'acute'

    raise Exception ('impossible')


def lengths_squared(x1, y1, x2, y2, x3, y3):
    a2 = (x1 - x2)**2 + (y1 - y2)**2
    b2 = (x2 - x3)**2 + (y2 - y3)**2
    c2 = (x3 - x1)**2 + (y3 - y1)**2
    return sorted([a2, b2, c2])


main()
