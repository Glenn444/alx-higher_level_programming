#!/usr/bin/python3
"""
This program imports the add function from add_0.py and prints the result of 1+2.
"""

from add_0 import add

a = 1
b = 2
result = add(a, b)

print("{} + {} = {}".format(a, b, result))

