#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""


import sys

total_size = 0
status_codes = {}

try:
    for i, line in enumerate(sys.stdin, 1):
        data = line.split(" ")
        if len(data) >= 7:
            size = int(data[-1])
            code = int(data[-2])
            total_size += size

            if code in status_codes:
                status_codes[code] += 1
            else:
                status_codes[code] = 1

        if i % 10 == 0:
            print("File size: {:d}".format(total_size))
            for code in sorted(status_codes.keys()):
                print("{:d}: {:d}".format(code, status_codes[code]))

except KeyboardInterrupt:
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{:d}: {:d}".format(code, status_codes[code]))
