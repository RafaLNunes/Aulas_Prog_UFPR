import random as rd

def main():

    rede = []

    ids_search = [rd.randint(1000, 9000), rd.randint(1000, 9000), 3103, 3105]

    for node_id in ids_search:

        rede[node_id] = {
            "temp":24.0+ (node_id%10),
            "energia":100.0,
            "protocol":"RPL"
        }
    
    print(f"\nTemperatura do motor 3103: {rede[3103]['temp']} C")
    rede[3103]["energia"] = 85.5
    print(f"\n --- Status Atual da Rede ---")
    for mote, dados, in rede.items():
        print(f"ID: {mote}\nStatus: {dados["protocol"]}\nBateria: {dados['energia']}%")


if __name__ == "__main__":
    main()