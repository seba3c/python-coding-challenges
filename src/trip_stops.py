# -*- coding: utf-8 -*-
import random
import math
import itertools

from concurrent.futures.thread import ThreadPoolExecutor

"""
Return the number of possible combinations of three kind of stops during a trip, before
a previous combination must be repeated.

Each list represent the distance from the trip origin where the stop is placed.
Each list can be disordered.

Example:

    A = [29, 50]
    B = [61, 37]
    C = [37, 70]

(29, 37, 70), (29, 61, 70), (50, 61, 70)

Should return 3.
"""


def solution_v1(A, B, C):

    def countt(it):
        itt = filter(lambda t: t[0] < t[1] and t[1] < t[2], it[0])
        return sum(1 for _ in itt)

    N = len(A)
    NN = N * N * N

    prod = itertools.product(A, B, C)
    t = ThreadPoolExecutor(4)
    chunk = math.ceil(NN / 4)

    f1 = t.submit(countt, (itertools.islice(prod, chunk),))
    f2 = t.submit(countt, (itertools.islice(prod, chunk),))
    f3 = t.submit(countt, (itertools.islice(prod, chunk),))
    f4 = t.submit(countt, (itertools.islice(prod, chunk),))
    count = f1.result() + f2.result() + f3.result() + f4.result()
    return count if count < 1000000000 else -1


if __name__ == '__main__':

    A = [29, 50]
    B = [61, 37]
    C = [37, 70]

    ans = solution_v1(A, B, C)
    assert(ans == 3)

    A = [5]
    B = [5]
    C = [5]

    ans = solution_v1(A, B, C)
    assert(ans == 0)

    A = [5]
    B = [6]
    C = [7]

    ans = solution_v1(A, B, C)
    assert(ans == 1)

    A = [5, 6]
    B = [5, 7]
    C = [5, 8]

    ans = solution_v1(A, B, C)
    assert(ans == 2)

    N = 100
    A = [random.randint(1, 500) for x in range(N)]
    B = [random.randint(501, 1000) for x in range(N)]
    C = [random.randint(1001, 1500) for x in range(N)]
    ans = solution_v1(A, B, C)
    assert(ans == N * N * N)

    N = 100
    A = [random.randint(1, 500) for x in range(N)]
    B = [random.randint(501, 1000) for x in range(N)]
    C = [x for x in range(N - 1)] + [1001]
    ans = solution_v1(A, B, C)
    assert(ans == N * N * 1)
