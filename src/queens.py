# -*- coding: utf-8 -*-

from ast import literal_eval


def queens_without_collisions(queens_positions=[]):
    queens_positions = [literal_eval(pos) for pos in queens_positions]
    for i in range(0, len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            i_pos = queens_positions[i]
            j_pos = queens_positions[j]
            if i_pos[0] == j_pos[0] or i_pos[1] == j_pos[1]:
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
