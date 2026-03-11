import numpy as np
import time
import random as rd
import panda as pd

def exibir_matrix(matrix):
    print("\n\n --------------- MATRIX ESTRUCTURE ---------------")
    for line in matrix:

        for colun in line:
            print(f"{colun:^5}", end = " ")
        print()

def rand_texture():
    #aqui vem outra

    line = rd.randint(0,1050)
    colu = rd.randint(0,1050)

    matrix = []
    for i in range(line):
        new_line = []
        for j in range(colu):
            val = rd.randint(-150,250)
            print(f" Valor para [{i}][{j}]:[{val}]")
            new_line.append(val)
        matrix.append(new_line)
    # exibir_matrix(matrix)

def main():
    # aqui vem a central

if __name__ == "__main__":
    main()
