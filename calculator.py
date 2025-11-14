"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def add(a, b): a+b

def subtract(a, b): a - b

def multiply(a, b): a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a


def logarithm(a, b):
    if b <= 0:
        raise ValueError

    return math.log(b,base=a)# use math library/raise ValueError

def exponent(a, b): a ** b



