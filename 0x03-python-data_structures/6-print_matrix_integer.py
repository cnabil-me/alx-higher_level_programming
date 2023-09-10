#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for el in list:
            if el == list[len(list)-1]:
                print("{:d}".format(el), end="")
            else:
                print("{:d}".format(el), end=" ")
        print()
