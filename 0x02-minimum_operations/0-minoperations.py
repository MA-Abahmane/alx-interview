#!/usr/bin/python3

"""
    In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
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
