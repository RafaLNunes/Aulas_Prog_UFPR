import math
import random as rd


def Gerar_leitura(nominal):
    return nominal + rd.uniform(-5.0, 5.0)
def Calc_Pot(V, I, cos_phi=0.95):
    return V * I * cos_phi
def main():
    Fases = ["A", "B", "C"]
    nominais = [127.0, 127.0, 127.0]
    corrente = 10.5

    for F,N in zip(Fases,nominais):
        v_real = Gerar_leitura(N)
        p_Ativa = Calc_Pot(v_real, corrente)

        print(f"{F:<5} | {v_real:>12.2f} | {p_Ativa:>12.2f}")

if __name__ == "__main__":
    main()
