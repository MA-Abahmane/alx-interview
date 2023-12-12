#!/usr/bin/env python3

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
    if n <= 1:
        return 0

    # Initialize an array to store the minimum operations
    #  needed for each position
    dp = [float('inf')] * (n + 1)

    # Base case: 0 operations needed for position 1
    dp[1] = 0

    # Iterate from position 2 to n
    for i in range(2, n + 1):
        # Find factors of i
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n] if dp[n] != float('inf') else 0
