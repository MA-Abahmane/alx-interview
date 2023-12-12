#!/usr/bin/python3

"""
    In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste =>
HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """ Minimum Operations """
    cnt = 0
    nxt = 'H'
    body = 'H'

    while (len(body) < n):
        if (n % len(body) == 0):
            cnt += 2
            nxt = body
            body += body
        else:
            cnt += 1
            body += nxt

    return 0 if len(body) != n else cnt
