# -*- coding: utf-8 -*-


def solution(A):
    # write your code in Python 3.6
    smallest_positive_int = 1
    number_set = set(A)
    while smallest_positive_int in number_set:
        smallest_positive_int += 1
    return smallest_positive_int


if __name__ == '__main__':

    A = [1, 3, 6, 4, 1, 2]
    ans = solution(A)
    print(ans)
