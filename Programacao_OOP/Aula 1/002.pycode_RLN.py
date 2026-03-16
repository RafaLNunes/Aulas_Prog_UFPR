from time import sleep

def Principal():

    List_dados = ["12.5", "11.8", "13.2", "19.5", "12.1", "99.3"]

    for dado in List_dados:
        sleep(1)
        tensao_float = float(dado)
        
        print(f"\nTensão atual do calculo: {tensao_float:.1f} V")

        if tensao_float < 10 or tensao_float > 99.5:
            print(f"FALHA CRÍTICA: {tensao_float:.1f}")
            break

        else:
            print("Passou")

    else:
        print("Status Concluido em 100%")
        
    print("\n\nConcluido o processo de Verificação\n")



if __name__ == "__main__":
    Principal()