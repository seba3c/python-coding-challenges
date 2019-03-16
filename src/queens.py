# -*- coding: utf-8 -*-

from ast import literal_eval


def queens_without_collisions(queens_positions=[]):
    queens_positions = [literal_eval(pos) for pos in queens_positions]
    for i_pos in queens_positions:
        for j_pos in queens_positions:
            if i_pos[0] == j_pos[0] and i_pos[1] != j_pos[1] or i_pos[0] != j_pos[0] and i_pos[1] == j_pos[1]:
                return str(i_pos).replace(' ', '')
    return str(True)


if __name__ == '__main__':

    Input = []
    Output = "True"
    assert queens_without_collisions(Input) == Output

    Input = ["(2,1)", "(3,3)"]
    Output = "True"
    assert queens_without_collisions(Input) == Output

    Input = ["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]
    Output = "(5,3)"
    assert queens_without_collisions(Input) == Output

    Input = ["(4,1)", "(7,2)", "(3,3)", "(8,4)", "(2,5)", "(5,6)", "(1,7)", "(6,8)"]
    Output = "True"
    assert queens_without_collisions(Input) == Output

    print("OK!")
