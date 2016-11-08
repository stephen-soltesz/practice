#!/usr/bin/python


def lookup():
    pass


def reverse(x):
    return x


def flip(x, size):
    maxvalue = 2**size - 1
    # print 'x = 0x%x' % x,
    x = maxvalue & x
    # print 'x = 0x%x' % x
    result = 0
    ebit = size - 1
    for sbit in range(size):
        bit = 1 << sbit
        value = x & bit
        shift = ebit - sbit
        if shift > 0:
            result = result | (value << shift)
        elif shift < 0:
            result = result | (value >> abs(shift))
        # print sbit, '0x%x' % bit, '0x%x' % value, '0x%x' % shift, '0x%x' % result
        ebit -= 1
    return result


for i in range(32):
    print i, '0x%x' % i, '0x%x' % flip(i, 16)
