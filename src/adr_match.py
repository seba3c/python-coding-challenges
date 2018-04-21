# -*- coding: utf-8 -*-

"""
Given a string checks if it is balanced in relation to (){}[] symbols.
"""


def is_match(ss):
    symbol_stack = []
    for c in ss:
        if c in ['(', "[", "{"]:
            symbol_stack.insert(0, c)
        elif c in [')', "]", "}"]:
            if not symbol_stack:
                return False
            else:
                e = symbol_stack.pop(0)
                mismatch = (c == ')' and e != '(') or (c == ']' and e != '[') or (c == '}' and e != '{')
                if mismatch:
                    return False
    return len(symbol_stack) == 0


assert is_match("[[a]]")
assert not is_match("[[a]")
assert is_match("{aasd{a}dasdasd}")
assert is_match("")
assert is_match("a23131a")
assert is_match("(a)2{31}31a [[]]")
assert is_match("{{{[[((([])))]]}}}")
assert not is_match("{{{[[(((()))]]}}}")
assert not is_match("(a)2{31}31a [[)]")
print("All test passed!")
