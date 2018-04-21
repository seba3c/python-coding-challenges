# -*- coding: utf-8 -*-

"""
Happy Number
============
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the
squares of its digits, and repeat the process until the number either equals 1
(where it will stay), or it loops endlessly in a cycle which does not include 1.

For example:

7*7 -> 49, 4*4 + 9*9 -> 97
7 => 49 => 97 => 130 => 10 => 1 => Happy!
2 => 4 => 16 => 37 => 58 => 89 => 145 => 42 => 20 => 4 => Loop encountered => Not Happy!

(Full description at https://en.wikipedia.org/wiki/Happy_number.)

Write a method that takes a positive integer and that returns True if the
number is happy, False otherwise.
"""


def sum_of_squares(n):
    r = sum(list(map(lambda x: x * x, [int(i) for i in str(n)])))
    return r


def is_happy(n):
    ni = n
    if (ni > 1):
        squares = set()
        ni = sum_of_squares(n)
        while (ni != 1 and ni not in squares):
            if (ni == 1):
                return True
            if ni in squares:
                return False
            squares.add(ni)
            ni = sum_of_squares(ni)
    if (ni == 1):
        return True
    return False


# Test Cases
if __name__ == '__main__':
    # Happy numbers from 1 to 100, inclusive
    happy_numbers = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82,
                     86, 91, 94, 97, 100]

    is_happy(7)

    for n in range(1, 101):
        expected = n in happy_numbers
        assert is_happy(n) is expected
    print("Done!")
