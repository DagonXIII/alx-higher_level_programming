#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    try:
        if b > a:
            raise Exception("Too far")
        else:
            result = (a ** b) / b
    except Exception as ex:
        result = 0
    return result
