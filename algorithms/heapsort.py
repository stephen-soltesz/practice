#!/usr/bin/python


def parent(i):
	return (i - 1) // 2

def left(i):
	# 0 - 1
	# 1 - 3
	# 2 - 5
	return i * 2 + 1

def right(i):
	# 0 - 2
	# 1 - 4
	# 2 - 6
	return (i + 1) * 2

# 0, 1, 2, 3, 4, 5, 6
# 0 - l1, r2
# 1 - l3, r4
# 2 - l5, r6

def max_heapify(a, i, m):
	l = left(i)
	r = right(i)

    largest = i
	if l < m and a[l] > a[i]:
		largest = l

	if r < m and a[r] > a[largest]:
		largest = r

	if largest != i:
		exchange(a, largest, i)
		max_heapify(a, largest, m)


def build_heap(a):
	for i in range(len(a)//2, -1, -1):
		print a
		max_heapify(a, i, len(a))
	print a


def exchange(a, i, j):
	t = a[i]
	a[i] = a[j]
	a[j] = t


def heap_sort(a):
	build_heap(a)
	end = len(a)
	for i in range(len(a) - 1, 0, -1):
		print i, a[i], a
		exchange(a, 0, i)
		end -= 1
		max_heapify(a, 0, end)


def main():
	a = [1, 10, 5, 3, 6, 7, 2]
	print a
	# build_heap(a)
	heap_sort(a)
	print a
	pass

main()
