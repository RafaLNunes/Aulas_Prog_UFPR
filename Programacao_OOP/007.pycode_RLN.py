# imports no py, servem para trazer biblioteca
# se você usar from, consegue até importar funções expecificas de uma biblio
# sem pesar demais puxando toda a biblio

import random as rnd

def main():
    ruido = rnd.random()

    porta = rnd.randint(10000,655402)

    fases = ["A", "B", "C"]
    sortear = rnd.choice(fases)
    print(f"Ruido: {ruido}")
    print(f"Porta: {porta}")
    print(f"Fase: {sortear}")

if __name__ == "__main__":
    main()
