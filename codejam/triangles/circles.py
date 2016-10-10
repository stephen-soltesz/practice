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
            # x1, y1, x2, y2, x3, y3 = map(float, line.split())
            l1, l2, l3 = lengths(x1, y1, x2, y2, x3, y3)
            a2, b2, c2 = lengths2(x1, y1, x2, y2, x3, y3)
            #print ''
            #print (x1, y1), (x2, y2), (x3, y3)
            #print l1, l2, l3
            #print a2.sqrt(), b2.sqrt(), c2.sqrt()
            # print l1, l2, l3
            #print 'iv ', is_valid(l1, l2, l3)
            #print 'ivs', is_valid_slope(x1, y1, x2, y2, x3, y3)
            # if not is_valid(l1, l2, l3):
            # if not is_valid_slope(x1, y1, x2, y2, x3, y3):
            # assert(is_valid(l1, l2, l3) == is_valid(a2, b2, c2))
            if not is_valid(l1, l2, l3) or not is_valid_slope(x1, y1, x2, y2, x3, y3):
                print 'not a triangle'
            else:
                # kind = get_kind(l1, l2, l3)
                kind = get_kind(a2, b2, c2)
                # angle = get_angle(kind, l1, l2, l3)
                angle = get_angle(kind, a2, b2, c2)
                print kind, angle, 'triangle'


def is_valid(l1, l2, l3):
    if not (l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2):
        return False
    return True


def is_valid_slope(x1, y1, x2, y2, x3, y3):
    # if the slope intercept is equal for any pair of lines, then this is not
    # a valid triangle.
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


def get_kind(l1, l2, l3):
    if l1 != l2 and l2 != l3 and l3 != l1:
        return 'scalene'

    if l1 == l2 or l2 == l3:
        return 'isosceles'

    raise Exception('uhoh')


def get_angle(kind, a2, b2, c2):
    if kind == 'isosceles':
        if b2 == c2:
            print >>sys.stderr, 'found acute isosceles', a2, b2, c2
            return 'acute'
    l = a2 + b2
    # print l3, l
    if c2 == l:
        #print a2, b2, c2, 'r'
        return 'right'
    elif c2 > l:
        #print a2, b2, c2, 'o'
        return 'obtuse'
    elif c2 < l:
        #print a2, b2, c2, 'a'
        return 'acute'

    raise Exception ('impossible')


def lengths2(x1, y1, x2, y2, x3, y3):
    a2 = abs(x1 - x2)**2 + abs(y1 - y2)**2
    b2 = abs(x2 - x3)**2 + abs(y2 - y3)**2
    c2 = abs(x3 - x1)**2 + abs(y3 - y1)**2
    return sorted([a2, b2, c2])


def lengths(x1, y1, x2, y2, x3, y3):
    l1 = ((x1 - x2)**2 + (y1 - y2)**2).sqrt()
    l2 = ((x2 - x3)**2 + (y2 - y3)**2).sqrt()
    l3 = ((x3 - x1)**2 + (y3 - y1)**2).sqrt()
    # l1 = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    # l2 = math.sqrt(abs(x2 - x3)**2 + abs(y2 - y3)**2)
    # l3 = math.sqrt(abs(x3 - x1)**2 + abs(y3 - y1)**2)
    return sorted([l1, l2, l3])


main()
