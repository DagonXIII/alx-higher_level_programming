#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            upper = chr(ord(c) - 32)
        else:
            upper = c
        print("{:s}".format(upper), end="")
    print()
