def main():

    sensor = {
        "id":310,
        "tipo": "RPL_Node",
        "valor":25.5,
        "Unidade":"Celsius",
        "bateria": 30
    }

    print(f"--- Telemetria do sensor {sensor['id']} ---")
    print(f"Leitura: {sensor['valor']} {sensor['Unidade']}")

    sensor["status"] = "Ativo"
    if "bateria" in sensor:
        print(f"Bateria: {sensor['bateria']}%")
    else:
        print("Não encontrado")

if __name__ == "__main__":
    main()