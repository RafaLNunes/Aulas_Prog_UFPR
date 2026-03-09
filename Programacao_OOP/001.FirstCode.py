def Principal():
    print("Hello World!!!")
    id = 3103
    temp = 25.456079

    print(f"Sensor ID: {id}")

    # Por Padrao, o py utiliza um /n antes de cada print
    # caso queira retira-lo, basta por end="" no final
    # print("Teste", end="")

    # for i in range(3):
        # print(i, end="-")
        # Saída: 0-1-2-
    # print("")


    # caso queira usar formatação na propria impressao, utilizar formatação padrao de C
    # no caso, formata para aparecer apenas 2 casas no decimal
    print(f"Temperatura: {temp:.2f} C")

    # Da para fazer operações dentro do print
    print(f"Dobro: {id*2}")

if __name__ =="__main__":
    Principal()