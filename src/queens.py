# -*- coding: utf-8 -*-

from ast import literal_eval


def queens_without_collisions(queens_positions=[]):

    def have_collition(point_1, point_2):
        x1, y1 = point_1[0], point_1[1]
        x2, y2 = point_2[0], point_2[1]
        # check if the points are:
        # 1 - horizontally aligned
        # 2 - vertically aligned
        # 3 - form a 45 degree angle
        return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

    queens_positions = [literal_eval(pos) for pos in queens_positions]
    for i in range(0, len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            point_1 = queens_positions[i]
            point_2 = queens_positions[j]
            if have_collition(point_1, point_2):
                return str(point_1).replace(' ', '')
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

    Input = ["(4,1)", "(3,2)"]
    Output = "(4,1)"
    assert queens_without_collisions(Input) == Output

    print("OK!")
