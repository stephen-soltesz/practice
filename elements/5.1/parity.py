#!/usr/bin/python

import math
import sys

print sys.maxint

def parity(v):
	result = 0
	while v > 0:
		result = result ^ (v & 0x1)
		v = v >> 1
	return result

def parity2(v):
	result = 0
	while v > 0:
		result = result ^ 1
		v = v & (v - 1)
	return result

for i in range(30):
	print i, '0x%x' % i, parity(i), parity2(i)
