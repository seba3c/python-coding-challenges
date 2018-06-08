# -*- coding: utf-8 -*-
import random
import timeit
import itertools


def solution_1(N):
    n = str(N)
    # https://docs.python.org/2/library/itertools.html#itertools.permutations
    p = itertools.permutations(n, len(n))
    p = set(p)
    p = list(itertools.filterfalse(lambda x: len(x) > 1 and x[0] == '0', p))
    return len(p)


def solution_2(N):
    """
    Submitted
    """
    n = str(N)
    ps = itertools.permutations(n, len(n))
    result = set()
    for p in ps:
        if (len(p) > 1 and p[0] != '0' or len(p) == 1) and p not in result:
            result.add(p)
    return len(result)


def solution_3(N):
    n = str(N)
    p = itertools.permutations(n, len(n))
    p = set(p)
    p = list(itertools.filterfalse(lambda x: x[0] == '0' and len(x) > 1, p))
    return len(p)


if __name__ == '__main__':

    assert solution_1(0) == 1
    assert solution_1(1213) == 12
    assert solution_1(123) == 6
    assert solution_1(100) == 1

    assert solution_2(0) == 1
    assert solution_2(1213) == 12
    assert solution_2(123) == 6
    assert solution_2(100) == 1

    assert solution_3(0) == 1
    assert solution_3(1213) == 12
    assert solution_3(123) == 6
    assert solution_3(100) == 1

    N = random.randint(100000000, 999999999)
    g = {"solution_1": solution_1, "solution_2": solution_2, "solution_3": solution_3, "N": N}
    n = 1000
    t = timeit.timeit("solution_1(N)", number=n, globals=g)
    print("Time for solution 1: ", t)

    t = timeit.timeit("solution_2(N)", number=n, globals=g)
    print("Time for solution 2: ", t)

    t = timeit.timeit("solution_3(N)", number=n, globals=g)
    print("Time for solution 3: ", t)
