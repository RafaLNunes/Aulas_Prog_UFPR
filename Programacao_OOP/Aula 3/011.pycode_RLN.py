import numpy as np
import random as rd

def main():
    ler = np.array([25.4,26.1,24.8,25.9,27.2])

    ajust = ler + 2.0

    print(f"Temperatura: {ajust}")
    print(f"Média: {ler}") # :.2f nãoi ta funcionando aqui
    print(f"Desvio Padrão: {np.std(ler):.2f}")

    matrix = np.array([
        [rd.randint(-150,250), rd.randint(-150,250), rd.randint(-150,250)],
        [rd.randint(-150,250), rd.randint(-150,250), rd.randint(-150,250)],
        [rd.randint(-150,250), rd.randint(-150,250), rd.randint(-150,250)]
    ])

    print("\nMatriz Transposta: ")
    print(matrix.T)

if __name__ == "__main__":
    main()