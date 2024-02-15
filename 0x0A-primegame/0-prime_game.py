#!/usr/bin/python3
"""
    > Prime Game <
    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a prime
    number from the set and removing that number and its multiples from the
    set. The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """ Determine the winner, Maria or Ben. """
    players = {'Ben': 0, 'Maria': 0}

    if nums == []:
        return None

    for rnd in range(x):
        n = nums[rnd]

        if n == 1:
            players['Ben'] += 1
            continue

        lst = []
        for i in range(n):
            lst.append(i + 1)

        turn = 0
        while True:
            played = False
            for i in range(len(lst)):

                if isPrime(lst[i]):
                    prime = lst[i]
                    clearMultiples(lst, prime)
                    played = True
                    turn += 1
                    break

            if (not played):
                break

        if (turn % 2 == 0):
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Ben'] < players['Maria']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return None


def clearMultiples(lst, n):
    """ removing that number and its multiples from the list """
    try:
        while True:
            lst.remove(n)
            n += n
    except ValueError:
        return 1


def isPrime(n):
    """ check if number prime """
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False
