#!/usr/bin/python3

"""
Mission V: Write a method that determines if a given
 data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ UTF-8 validator """
    # Initialize a variable to keep track of the
    # number of trailing bytes
    trailing_bytes = 0

    # Iterate through each integer in the data
    for num in data:
        # Check if the most significant bit is set
        if num & 0x80 == 0:
            # If it's the start of a new character,
            # reset trailing_bytes
            if trailing_bytes != 0:
                return False
        elif num & 0xC0 == 0x80:
            # If it's a trailing byte, decrement trailing_bytes
            trailing_bytes -= 1
            if trailing_bytes < 0:
                return False
        elif num & 0xE0 == 0xC0:
            # If it's the start of a 2-byte character,
            # set trailing_bytes to 1
            trailing_bytes = 1
        elif num & 0xF0 == 0xE0:
            # If it's the start of a 3-byte character,
            # set trailing_bytes to 2
            trailing_bytes = 2
        elif num & 0xF8 == 0xF0:
            # If it's the start of a 4-byte character,
            # set trailing_bytes to 3
            trailing_bytes = 3
        else:
            # If none of the conditions are met,
            # it's an invalid start byte
            return False

    # After iterating through all bytes, check if there
    # are any incomplete characters
    return trailing_bytes == 0
