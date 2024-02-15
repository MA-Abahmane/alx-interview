#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(6, [2, 5, 4, 3, 5, 9])))
print("Winner: {}".format(isWinner(6, [2, 5, 4, 3, 5, 77])))
print("Winner: {}".format(isWinner(8, [2, 5, 4, 3, 5, 77])))
print("Winner: {}".format(isWinner(1, [1])))
print("Winner: {}".format(isWinner(1, [])))
print("Winner: {}".format(isWinner(1, None)))
