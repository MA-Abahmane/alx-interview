#!/usr/bin/python3

"""
Write a script that reads stdin line by line and computes metrics:
"""

import sys

if __name__ == '__main__':
    # Initialize variables
    Fsize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def stats_print(stats: dict, file_size: int) -> None:
        """ Function to print statistics """
        print("File size: {:d}".format(Fsize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        # Iterate through each line from stdin
        for line in sys.stdin:
            count += 1
            data = line.split()

            # Extract and update status code count
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass

            # Extract and update total file size
            try:
                Fsize += int(data[-1])
            except BaseException:
                pass

            # Print statistics every 10 lines
            if count % 10 == 0:
                stats_print(stats, Fsize)

        # Print final statistics
        stats_print(stats, Fsize)

    except KeyboardInterrupt:
        # Handle keyboard interruption and print final statistics
        stats_print(stats, Fsize)
        raise
