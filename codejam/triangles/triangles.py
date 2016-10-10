#!/usr/bin/python

import sys
import math
import decimal


lengths = ['isosceles', 'scalene']
angles = ['obtuse', 'acute', 'right']
triangle = ['triangle', 'not a triangle']


def main():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for i in xrange(n):
            line = f.readline().strip()
            # if i + 1 != 12:
            #     continue
            print 'Case #%d:' % (i + 1),
            # x1, y1, x2, y2, x3, y3 = map(decimal.Decimal, line.split())
            x1, y1, x2, y2, x3, y3 = map(float, line.split())
            l1, l2, l3 = lengths(x1, y1, x2, y2, x3, y3)
            # print l1, l2, l3
            if not is_valid(l1, l2, l3):
                print 'not a triangle'
            else:
                kind = get_kind(l1, l2, l3)
                angle = get_angle(kind, l1, l2, l3)
                print kind, angle, 'triangle'


def get_kind(l1, l2, l3):
    if l1 != l2 and l2 != l3 and l3 != l1:
        return 'scalene'

    if l1 == l2 or l2 == l3:
        return 'isosceles'

    raise Exception('uhoh')


def get_angle(kind, l1, l2, l3):
    if kind == 'isosceles':
        if l2 == l3:
            print >>sys.stderr, 'found acute isosceles', l1, l2, l3
            return 'acute'
    l = length(l1, l2)
    # print l3, l
    if l3 == l:
        return 'right'
    elif l3 > l:
        return 'obtuse'
    elif l3 < l:
        return 'acute'

    raise Exception ('impossible')

    # print ['obtuse', 'acute', 'right']
    # if isosceles: assume right angle calculate third length, if third length
    # is greater then obtuse, if less acute, else right.
    # if scalene: assume right and use smallest two to calculate third. if
    # equal then right. 
    # if isosceles:
    #     if l1 == l2, then l3 is larger.
    #     if l2 == l3, then l1 is smallest, and cannot be right or obtuse.
    # if scalene:
    #     l = length(l1, l2)
    #     if l == l3, then right.
    #     if 
    pass


def length(l1, l2):
    return math.sqrt(l1**2 + l2**2)
    # return (l1**2 + l2**2).sqrt()


def lengths(x1, y1, x2, y2, x3, y3):
    # l1 = ((x1 - x2)**2 + (y1 - y2)**2).sqrt()
    # l2 = ((x2 - x3)**2 + (y2 - y3)**2).sqrt()
    # l3 = ((x3 - x1)**2 + (y3 - y1)**2).sqrt()
    l1 = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    l2 = math.sqrt(abs(x2 - x3)**2 + abs(y2 - y3)**2)
    l3 = math.sqrt(abs(x3 - x1)**2 + abs(y3 - y1)**2)
    return sorted([l1, l2, l3])


def is_valid(l1, l2, l3):
    if not (l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2):
        return False
        
    return True


main()
