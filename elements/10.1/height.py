#!/usr/bin/python


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def balanced(n):
    if n is None:
        return (True, -1)

    lb, lh = balanced(n.left)
    rb, rh = balanced(n.right)

    if not lb or not rb:
        return (False, max(lh, rh) + 1)

    balanced = abs(lh - rh) <= 1
    return (balanced, max(lh, rh) + 1)


def main():
    balanced(t)
