#!/usr/bin/python

import pprint
import string
import sys


N = 0x1
E = 0x8
S = 0x2
W = 0x4


def main():
    with open(sys.argv[1]) as f:
        N = f.readline().strip()
        for i, line in enumerate(f.readlines()):
            forward, reverse = line.strip().split()

            # Check dimensions forward.
            _, _, min_x, max_x, min_y, max_y = dimensions(forward)

            # Use the 'reverse' path to walk through the maze again from the
            # entrance, but using an always-turn-right 'forward' path.
            # Change all 'lefts to rights, and rights to lefts, and reverse
            # the order of the sequence.
            backward = ''.join(reversed(reverse.translate(string.maketrans('LR', 'RL'))))

            # Check dimensions forward and the 'reversed' forward path.
            last_x, last_y, min_x, max_x, min_y, max_y = dimensions(backward, min_x, max_x, min_y, max_y)

            # Calculate dimensions of maze.
            X = max_x - min_x + 1
            Y = max_y - min_y + 1

            # Create an X by Y array.
            maze = []
            for x in range(X):
                maze.append([0 for y in range(Y)])

            entrance = (X - 1 - max_x, 0)
            exit = (abs(min_x - last_x), abs(last_y))

            o = walkmaze(maze, forward, entrance)
            walkmaze(maze, reverse, exit, initial_orientation=o)

            print 'Case #%d:' % (i + 1)
            for y in range(Y):
                print ''.join(['%x' % maze[x][y] for x in range(X)])

            
def mark_wall_clear(w, d):
    return w | d


def update_position(x, y, d):
    if d == N:
        y = y - 1
    elif d == S:
        y = y + 1
    elif d == W:
        x = x - 1
    elif d == E:
        x = x + 1
    return x, y


def walkmaze(m, forward, enter, initial_orientation=2):
    compass = [N, E, S, W]

    direction = initial_orientation

    x, y = enter

    # Clear the door at the entrance.
    m[x][y] = mark_wall_clear(m[x][y], compass[(direction + 2) % len(compass)])

    for move in list(forward[1:-1]):

        if move == 'W':
            if x >= 0 and y >= 0 and x < len(m) and y < len(m[0]):
                m[x][y] = mark_wall_clear(m[x][y], compass[direction])

            x, y = update_position(x, y, compass[direction])

            if x >= 0 and y >= 0 and x < len(m) and y < len(m[0]):
                m[x][y] = mark_wall_clear(m[x][y], compass[(direction + 2) % len(compass)])

        if move == 'L':
            direction -= 1
            if direction < 0:
                direction = len(compass) - 1

        if move == 'R':
            direction += 1
            if direction >= len(compass):
                direction = 0

    return (direction + 2 ) % len(compass)


def dimensions(path, min_x=0, max_x=0, min_y=0, max_y=0):
    # A clockwise representation of compass directions.
    compass = [N, E, S, W]
    # Entrance is always on the north side, so initial orientation is 'S'.
    direction = 2

    # Assume the initial start is 0, 0, but the position updates are
    # unconstrained, so we may get negative positions.
    x, y = 0, 0

    for move in list(path[1:-1]):
        if move == 'W':
            # Orientation does not change, but position does.
            x, y = update_position(x, y, compass[direction])

            min_x = x if x < min_x else min_x
            max_x = x if x > max_x else max_x
            
            min_y = y if y < min_y else min_y
            max_y = y if y > max_y else max_y

        if move == 'L':
            # Rotate counter-clockwise one position.
            direction -= 1
            if direction < 0:
                direction = len(compass) - 1

        if move == 'R':
            # Rotate clockwise one position.
            direction += 1
            if direction >= len(compass):
                direction = 0

    return x, y, min_x, max_x, min_y, max_y


if __name__ == '__main__':
    main()
