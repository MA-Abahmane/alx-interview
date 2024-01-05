#!/usr/bin/python3

"""
Mission V: Write a method that determines if a given
 data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ UTF-8 validator """

    for x in data:
        if x > 255 or x < 0:
            return False
    return True
