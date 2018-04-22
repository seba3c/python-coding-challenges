# -*- coding: utf-8 -*-
import timeit
import random

from concurrent.futures.thread import ThreadPoolExecutor

"""
Returns the minimun number of lines required to reach all points (represented crystal statues)
from position 0,0. A line represent a laser shot, so it can pass throught the statues.
If two or more statues are in the same line from position 0,0 only one shot is needed
to reach all of them.
"""


class Point2D:

    def __init__(self, t):
        self.x = t[0]
        self.y = t[1]

    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __str__(self):
        return self.__repr__()


def verify_points(p1, p2, p3):
    return quadrant(p2) == quadrant(p3) and are_collinear(p1, p2, p3)


def are_collinear(p1, p2, p3):
    return (p1.y - p2.y) * (p1.x - p3.x) == (p1.y - p3.y) * (p1.x - p2.x)


def quadrant(p):
    if p.x > 0 and p.y > 0:
        return "first"
    elif p.x < 0 and p.y > 0:
        return "second"
    elif p.x < 0 and p.y < 0:
        return "third"
    elif p.x > 0 and p.y < 0:
        return "fourth"
    elif p.x == 0 and p.y == 0:
        return "center"


def solution_1(A):
    if not A:
        return 0
    center = Point2D((0, 0))
    points = []
    for p1 in A:
        ok = False
        for p2 in points:
            ok = verify_points(center, p1, p2)
            if ok:
                break
        if not ok:
            points.append(p1)
    return len(points)


def split_by_quadrant(A):
    first = []
    second = []
    third = []
    fourth = []
    for p in A:
        if p.x > 0 and p.y > 0:
            first.append(p)
        elif p.x < 0 and p.y > 0:
            second.append(p)
        elif p.x < 0 and p.y < 0:
            third.append(p)
        elif p.x > 0 and p.y < 0:
            fourth.append(p)
        elif p.x == 0 and p.y == 0:
            pass
    return (first, second, third, fourth)


def number_of_lines(A):
    center = Point2D((0, 0))
    points = []
    for p1 in A:
        ok = False
        for p2 in points:
            ok = are_collinear(center, p1, p2)
            if ok:
                break
        if not ok:
            points.append(p1)
    return len(points)


def solution_2(A):
    count = 0
    if not A:
        return count
    A1, A2, A3, A4 = split_by_quadrant(A)
    count += number_of_lines(A1)
    count += number_of_lines(A2)
    count += number_of_lines(A3)
    count += number_of_lines(A4)
    return count


def solution_3(A):
    count = 0
    if not A:
        return count
    A1, A2, A3, A4 = split_by_quadrant(A)
    t = ThreadPoolExecutor(4)
    f1 = t.submit(number_of_lines, (A1,))
    f2 = t.submit(number_of_lines, (A2,))
    f3 = t.submit(number_of_lines, (A3,))
    f4 = t.submit(number_of_lines, (A4,))
    count = f1.result() + f2.result() + f3.result() + f4.result()
    return count


def solution_4(A):
    count = 0
    if not A:
        return count
    t = ThreadPoolExecutor(4)
    f1 = t.submit(number_of_lines, (filter(lambda p: p.x > 0 and p.y > 0, A),))
    f2 = t.submit(number_of_lines, (filter(lambda p: p.x < 0 and p.y > 0, A),))
    f3 = t.submit(number_of_lines, (filter(lambda p: p.x < 0 and p.y < 0, A),))
    f4 = t.submit(number_of_lines, (filter(lambda p: p.x > 0 and p.y < 0, A),))
    count = f1.result() + f2.result() + f3.result() + f4.result()
    return count


def are_collinear_v2(p2, p3):
    return (0 - p2.y) * (0 - p3.x) == (0 - p3.y) * (0 - p2.x)


def number_of_lines_v2(A):
    points = []
    for p1 in A:
        if not next((p2 for p2 in points if are_collinear_v2(p1, p2)), None):
            points.append(p1)
    return len(points)


def number_of_lines_v3(A):
    points = []
    for p1 in A:
        ok = False
        for p2 in points:
            ok = p1.y * p2.x == p2.y * p1.x
            if ok:
                break
        if not ok:
            points.append(p1)
    return len(points)


def solution_5(A):
    count = 0
    if not A:
        return count
    t = ThreadPoolExecutor(4)
    f1 = t.submit(number_of_lines_v3, (filter(lambda p: p.x > 0 and p.y > 0, A),))
    f2 = t.submit(number_of_lines_v3, (filter(lambda p: p.x < 0 and p.y > 0, A),))
    f3 = t.submit(number_of_lines_v3, (filter(lambda p: p.x < 0 and p.y < 0, A),))
    f4 = t.submit(number_of_lines_v3, (filter(lambda p: p.x > 0 and p.y < 0, A),))
    count = f1.result() + f2.result() + f3.result() + f4.result()
    return count


def build_input(AA):
    A = []
    for t in AA:
        A.append(Point2D(t))
    return A


def build_random_input(N=10000):
    A = []
    for _ in range(0, N):
        x = random.randint(0, 40000)
        y = random.randint(0, 40000)
        A.append(Point2D((x, y)))
    return A


if __name__ == '__main__':
    A = build_input([(-1, -2), (1, 2), (2, 4), (-3, 2), (2, -2)])
    assert(solution_1(A) == 4)
    assert(solution_2(A) == 4)
    assert(solution_3(A) == 4)
    assert(solution_4(A) == 4)
    assert(solution_5(A) == 4)

    A = build_input([(-1, -2), (1, 2), (2, 4), (-3, 2), (2, -2), (3, 6)])
    assert(solution_1(A) == 4)
    assert(solution_2(A) == 4)
    assert(solution_3(A) == 4)
    assert(solution_4(A) == 4)
    assert(solution_5(A) == 4)

    assert(solution_1([]) == 0)
    assert(solution_2([]) == 0)
    assert(solution_3([]) == 0)
    assert(solution_4([]) == 0)
    assert(solution_5([]) == 0)

    assert(solution_1(None) == 0)
    assert(solution_2(None) == 0)
    assert(solution_3(None) == 0)
    assert(solution_4(None) == 0)
    assert(solution_5(None) == 0)

    A = build_random_input()
    g = {"solution_1": solution_1, "solution_2": solution_2,
         "solution_3": solution_3, "solution_4": solution_4, "solution_5": solution_5,
         "A": A}
    ans3 = solution_3(A)
    ans4 = solution_4(A)
    ans5 = solution_5(A)
    assert(ans3 == ans4 and ans4 == ans5)
    n = 10000
    #     t = timeit.timeit("solution_1(A)", number=n, globals=g)
    #     print("Time for solution 1: ", t)
    #     t = timeit.timeit("solution_2(A)", number=n, globals=g)
    #     print("Time for solution 2: ", t)
    t = timeit.timeit("solution_3(A)", number=n, globals=g)
    print("Time for solution 3: ", t)
    t = timeit.timeit("solution_4(A)", number=n, globals=g)
    print("Time for solution 4: ", t)
    t = timeit.timeit("solution_5(A)", number=n, globals=g)
    print("Time for solution 5: ", t)
