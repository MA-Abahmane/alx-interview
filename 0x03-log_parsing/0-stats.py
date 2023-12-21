#!/usr/bin/python3

"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
 <status code> <file size> (if the format is not this one, the
 line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>
    (see input format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405
          and 500
        if a status code doesn’t appear or is not an integer, don’t
          print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal
 to not have the same output as this one.
"""

import sys


def function():
    """ Process function """
    # Initialize variables for file size and line count
    filesize, count = 0, 0
    # List of status codes to track
    stat_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Dictionary to store count for each status code
    stats = {k: 0 for k in stat_codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """ Function to print statistics """
        print("File size: {:d}".format(filesize))

        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        # Iterate through each line from stdin
        for line in sys.stdin:
            # Increment line count
            count += 1

            # Split the line into a list of words
            data = line.split()

            try:
                # Attempt to extract the status code from the line
                status_code = data[-2]

                # If the status code is in the list; update count
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass

            try:
                # Attempt to extract the file size from the line and
                # update total file size
                filesize += int(data[-1])
            except BaseException:
                pass

            # Print statistics every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)

        # Print final statistics
        print_stats(stats, filesize)

    except KeyboardInterrupt:
        # Handle keyboard interruption and print final statistics
        print_stats(stats, filesize)
        raise


if __name__ == '__main__':
    """ Import control """
    # Call the function when the script is executed
    function()
