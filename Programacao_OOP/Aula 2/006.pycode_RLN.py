def main():
    name = input("Digite o nome do sensor: ")
    leitura = int(input("N° de Mensagens enviadas: "))
    energy = float(input("Consumo de energia  (mJ): "))

    print("\n ...... Relatório ...... ")
    print(f"Mensagens: {leitura}")
    print(f"Média de energia por mensagem: {energy/leitura:.2f} mJ")

    print("\n\n\n")
    print(f"{type(name)}\n{type(energy)}\n{type(leitura)}")


if __name__ == "__main__":
    main()
