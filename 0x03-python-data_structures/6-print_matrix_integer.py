#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
   for i in matrix:
    for m in range(len(i)):
        print("{:d}".format(i[m]), end="")
        if m !=len(i) -1:
            print(" ", end="")

    print()

