#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    av = sys.argv
    num = len(av) - 1

    if num > 1:
        print(num, 'arguments:')
        for i in range(1, num + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif num == 1:
        print(num, 'argument:')
        for i in range(1, num + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif num == 0:
        print(num, 'arguments.')
