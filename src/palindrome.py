# -*- coding: utf-8 -*-


def is_palindrome(ss):
    """
    Indicates if a string is a palindrome

    @see: https://en.wikipedia.org/wiki/Palindrome
    """
    if ss is None:
        return False
    return ss == ss[::-1]


assert not is_palindrome(None)
assert is_palindrome("")
assert not is_palindrome("hola")
assert not is_palindrome("hello world")
assert is_palindrome("ala")
assert is_palindrome("wow wow")
print("All tests passed!")
