#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print("0")
    else:
        sum = 0
        for arg in args:
            sum += int(arg)
        print(sum)
