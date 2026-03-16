import random as rd

def exibir_matrix(matrix):
    print("\n\n --------------- MATRIX ESTRUCTURE ---------------")
    for line in matrix:

        for colun in line:
            print(f"{colun:^5}", end = " ")
        print()

def main():
    line = int(input("N° de Linhas: "))
    colu = int(input("N° de Colunas: "))

    matrix = []
    for i in range(line):
        new_line = []
        for j in range(colu):
            val = rd.randint(-150,250)
            print(f" Valor para [{i}][{j}]:[{val}]")
            new_line.append(val)
        matrix.append(new_line)
    exibir_matrix(matrix)

if __name__ == "__main__":
    main()
