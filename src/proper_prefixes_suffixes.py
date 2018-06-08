# -*- coding: utf-8 -*-
import random
import string
import timeit

from concurrent.futures.thread import ThreadPoolExecutor

"""
Get a proper suffix and prefix with the maximum length
"""


def proper_prefixes(S):
    prefixs = set([""])
    cc = ""
    for c in S[0:len(S) - 1]:
        cc += c
        prefixs.add(cc)
    return prefixs


def proper_suffixes(S):
    prefixs = set([""])
    cc = ""
    for c in S[::-1][0:len(S) - 1]:
        cc = c + cc
        prefixs.add(cc)
    return prefixs


def solution_1(S):
    """
    Submitted
    """
    s1 = proper_prefixes(S)         # O(len(S))
    s2 = proper_suffixes(S)         # O(len(S))
    s1.intersection_update(s2)      # O(len(s1) * len(s2))
    s1 = sorted(s1, reverse=True)   # O(len(s1) log len(s1))
    return len(s1[0])               # O(1)


def solution_2(S):
    """
    Using threads
    """
    t = ThreadPoolExecutor(2)
    t1 = t.submit(proper_prefixes, S)
    t2 = t.submit(proper_suffixes, S)
    s1 = t1.result()
    s2 = t2.result()
    s1.intersection_update(s2)
    s1 = sorted(s1, reverse=True)
    return len(s1[0])


def solution_3(S):
    current = ""
    start = 0
    end = len(S) - 1
    prefix = ""
    suffix = ""
    for i in range(start, end):         # O(N - 1)
        prefix += S[i]                  # ##
        suffix = S[end - i] + suffix       # O(1)
        if prefix == suffix:               #
            current = prefix            # ##
    return len(current)                 # O(1)


def build_input(N):
    return ''.join(random.choices(string.ascii_lowercase, k=N))


if __name__ == '__main__':

    assert solution_1("codibility") == 0
    assert solution_1("abbabba") == 4

    assert solution_2("codibility") == 0
    assert solution_2("abbabba") == 4

    assert solution_3("codibility") == 0
    assert solution_3("abbabba") == 4

    S = build_input(1000)
    assert solution_1(S) == solution_3(S)

    S = build_input(10000)
    g = {"solution_1": solution_1, "solution_2": solution_2, "solution_3": solution_3, "S": S}
    n = 100
    t = timeit.timeit("solution_1(S)", number=n, globals=g)
    print("Time for solution 1: ", t)

    t = timeit.timeit("solution_2(S)", number=n, globals=g)
    print("Time for solution 2: ", t)

    t = timeit.timeit("solution_3(S)", number=n, globals=g)
    print("Time for solution 3: ", t)
