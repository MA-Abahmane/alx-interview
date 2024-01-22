#!/usr/bin/python3

"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """ rotate 2D Matrix 90 degrees clockwise
    """
    l = len(matrix)
    nm = []

    for col in range(0, l):
        p = []
        for lst in matrix:
            p.append(lst[col])
        p.reverse()
        nm.append(p)

    matrix.clear()
    for i in nm:
        matrix.append(i)
