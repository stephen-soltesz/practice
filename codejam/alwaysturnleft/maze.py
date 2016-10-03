#!/usr/bin/python


import pprint
import sys

def main():
    with open(sys.argv[1]) as f:
        N = f.readline().strip()
        for i, line in enumerate(f.readlines()):
            forward, reverse = line.strip().split()
            #print 'Case #%d:' % (i + 1)
            ((c, r), enter, exit) = dimensions(forward)
            print (c, r), enter, exit
            m = []
            for x in range(c):
                m.append([0xf for y in range(r)])

            pprint.pprint(m)
            o = walkmaze(m, forward, enter)
            walkmaze(m, reverse, exit, initial_orientation=o)
            print 'Case #%d:' % (i + 1)
            for y in range(r):
                for x in range(c):
                    print '%x' % (0xf & (~ m[x][y])),
                print ''

            #sys.exit(1)

            #o, maze = walk2(forward)
            #print forward
            #print ' '.join(map(hex, maze))

            #_, maze = walk2(reverse, o)
            #print reverse
            #print ' '.join(map(hex, maze))

            #o, maze = walk(forward)
            #print forward
            #print ' '.join(maze)
            #_, maze = walk(reverse, o)
            #print reverse
            #print ' '.join(maze)
            #sys.exit(1)

N = 0x1
E = 0x8
S = 0x2
W = 0x4


def clear(w, d):
    return w & (~ d)


class Position(object):

    def __init__(self, n, s, w, e):
        self.ns = M(n, s)
        self.we = M(w, e)

    def update(self, d):
        self.ns.update(d)
        self.we.update(d)

    def cols(self):
        return self.we.size()

    def rows(self):
        return self.ns.size()

    def entrance(self):
        return (abs(self.we.c) - 1, 0)

    def exit(self):
        return (0, abs(self.ns.c) - 1)


class M(object):

    def __init__(self, pos, neg):
        self.p = pos
        self.n = neg
        self.c = 0
        self.max = 0
        self.min = 0

    def update(self, d):
        if d == self.n:
            self.c -= 1
        if d == self.p:
            self.c += 1
        self.max = max(self.max, self.c)
        self.min = min(self.min, self.c)

    def size(self):
        return self.max - self.min


def update_position(x, y, d):
    if d == N:
        y = y - 1
    if d == S:
        y = y + 1
    if d == W:
        x = x - 1
    if d == E:
        x = x + 1
    return x, y


def walkmaze(m, forward, enter, initial_orientation=2):
    compass = [N, E, S, W]
    direction = initial_orientation
    first_pass = True
    x, y = enter
    # print forward
    for move in list(forward):
        # print move, x, y
        if move == 'W':
            if not first_pass:
                if x >= 0 and y >= 0:
                    m[x][y] = clear(m[x][y], compass[direction])
                x, y = update_position(x, y, compass[direction])
            else:
                first_pass = False
            if x >= 0 and y >= 0:
                m[x][y] = clear(m[x][y], compass[(direction + 2) % len(compass)])

        if move == 'L':
            direction -= 1
            if direction < 0:
                direction = len(compass) - 1

        if move == 'R':
            direction += 1
            if direction >= len(compass):
                direction = 0

    # print "%s %s: %s %s" % (p.rows(), p.cols(), p.entrance(), p.exit())
    return (direction + 2 ) % len(compass)


def walk2(forward, initial_orientation=2):
    compass = [N, E, S, W]
    direction = initial_orientation
    walls = []
    p = Position(N, S, W, E)
    for move in list(forward):
        w = 0xf
        if move == 'W':
            print direction, compass[direction]
            w = clear(w, compass[direction])
            w = clear(w, compass[(direction + 2) % len(compass)])
            p.update(compass[direction])

            walls.append(w)
        if move == 'L':
            direction -= 1
            if direction < 0:
                direction = len(compass) - 1
        if move == 'R':
            direction += 1
            if direction >= len(compass):
                direction = 0

    print "%s %s: %s %s" % (p.rows(), p.cols(), p.entrance(), p.exit())
    return direction, walls 


def walk(path, initial_orientation=2):
    compass = ['N', 'E', 'S', 'W']
    o = initial_orientation
    r, c = 0, 0
    directions = []
    p = Position('N', 'S', 'W', 'E')
    for move in list(path):
        if move == 'W':
            # nothing changes.
            print o, compass[o]
            directions.append(compass[o])
            p.update(compass[o])

        if move == 'L':
            o -= 1
            if o < 0:
                o = len(compass) - 1
        if move == 'R':
            o += 1
            if o >= len(compass):
                o = 0

    print "%s %s: %s %s" % ((p.rows(), p.cols()), p.entrance(), p.exit())
    return ((p.rows(), p.cols()), p.entrance(), p.exit())
    # return (o + 2) % len(compass), directions


def dimensions(path, initial_orientation=2):
    compass = ['N', 'E', 'S', 'W']
    o = initial_orientation
    r, c = 0, 0
    directions = []
    p = Position('N', 'S', 'W', 'E')
    for move in list(path):
        if move == 'W':
            # nothing changes.
            directions.append(compass[o])
            p.update(compass[o])

        if move == 'L':
            o -= 1
            if o < 0:
                o = len(compass) - 1
        if move == 'R':
            o += 1
            if o >= len(compass):
                o = 0

    return ((p.cols(), p.rows()), p.entrance(), p.exit())


main()
