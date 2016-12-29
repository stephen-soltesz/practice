#!/usr/bin/python


import sys


def convert(arg):
    i = 0
    l = len(arg)
    for c in range(l - 1, -1, -1):
        if arg[c] == '-':
            i *= -1
            break
        i += (ord(arg[c]) - ord('0')) * 10**(l - 1 - c)
    return i


def convert_fancy(arg):
    i = 0
    l = len(arg)
    start = 1 if arg[0] == '-' else 0
    for j, c in enumerate(arg[start:]):
        i += ord(c) - ord('0')
        if j != len(arg) - 1 - start:
            i *= 10

    if start:
        return -i
    else:
        return i



def itos(i):
    digits = []
    negative = i < 0
    if negative:
        i *= -1

    while i > 0:
        digits.append(chr(ord('0') + i % 10))
        i = i // 10

    if negative:
        digits.append('-')

    return ''.join(reversed(digits))


def main(args):
    for arg in args:
        i = int(arg)
        j = convert_fancy(arg)
        k = itos(j)
        if i != j:
            raise Exception('convert: %s != %s' % (i, j))

        if arg != k:
            raise Exception('itos: %s != %s' % (arg, k))

        print 'Converted %s to %s and back to %s' % (arg, j, k)


if __name__ == '__main__':
    main(sys.argv[1:])
