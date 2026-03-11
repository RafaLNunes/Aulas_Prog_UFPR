def calc_Med(val):
    if not val:
        return 0.0
    
    somar = sum(val)
    med = somar / len(val)
    return med

def main():
    ler_list = []
    n = int(input("QTD de sensores: "))
    for i in range(n):
        val = float(input(f"Temperatura acessada no sensor {i}: "))
        ler_list.append(val)
    med_fiunal = calc_Med(ler_list)
    print(f"Média das {n} leitura: {med_fiunal:.2f} C")

if __name__ == "__main__":
    main()