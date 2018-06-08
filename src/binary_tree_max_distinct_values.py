# -*- coding: utf-8 -*-
import timeit
"""
Find the maximum number of distinct values that appear on a path starting at the root of the
Tree.
"""


class Tree:

    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r


def max_distinct_numbers_1(T, values):
    if T is None:
        return len(set(values))
    else:
        values.append(T.x)
        value = max(max_distinct_numbers_1(T.l, values), max_distinct_numbers_1(T.r, values))
        values.remove(T.x)
        return value


def solution_1(T):
    values = []
    return max_distinct_numbers_1(T, values)


def max_distinct_numbers_2(T, count, values):
    if T is None:
        return count
    else:
        c = count
        if T.x not in values:
            values.add(T.x)
            c += 1
        value = max(max_distinct_numbers_2(T.l, c, values), max_distinct_numbers_2(T.r, c, values))
        values.discard(T.x)
        return value


def solution_2(T):
    values = set()
    return max_distinct_numbers_2(T, 0, values)


def build_T1():
    G = Tree(5)
    D = Tree(4, G)
    B = Tree(5, D)

    E = Tree(1)
    F = Tree(6)
    C = Tree(6, E, F)

    A = Tree(4, B, C)
    return A


def build_T2():
    G = Tree(9)
    D = Tree(8, G)
    B = Tree(5, D)

    E = Tree(1)
    F = Tree(6)
    C = Tree(6, E, F)

    A = Tree(4, B, C)
    return A


if __name__ == '__main__':
    assert solution_1(build_T1()) == 3
    assert solution_1(None) == 0
    assert solution_1(build_T2()) == 4

    assert solution_2(build_T1()) == 3
    assert solution_2(None) == 0
    assert solution_2(build_T2()) == 4

    T = build_T1()
    g = {"solution_1": solution_1, "solution_2": solution_2, "T": T}
    n = 100000
    t = timeit.timeit("solution_1(T)", number=n, globals=g)
    print("Time for solution 1: ", t)

    t = timeit.timeit("solution_2(T)", number=n, globals=g)
    print("Time for solution 2: ", t)
