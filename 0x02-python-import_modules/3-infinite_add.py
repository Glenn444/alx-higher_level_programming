#!/usr/bin/python3
import sys

if __name__ == '__main__':
    av = sys.argv
    num = len(av)
    sum = 0

    if num > 1:
        for i in range(1, num):
            sum += int(av[i])

    print(sum)
