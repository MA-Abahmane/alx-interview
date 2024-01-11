#!/usr/bin/python3

"""
N Queens problem solver
"""

import sys


def is_safe(board, row, col):
    """ Check if it's safe to place a queen in a given position """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, row, board, solutions):
    """ Recursive function to solve N Queens problem """
    if row == N:
        solutions.append(list(board))
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)

def print_solutions(solutions):
    """Print the solutions in the specified format."""
    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])

def nqueens(N):
    """ Main function to solve N Queens problem """
    try:
        N = int(N)
        if N < 4:
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [-1] * N
    solutions = []

    solve_nqueens(N, 0, board, solutions)

    print_solutions(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    nqueens(sys.argv[1])
