def Sensor_Status(id_sensor, limiar=25.0, intervalo=10):
    print(f"\n[CONFIG] Sensor ID: {id_sensor}")
    print(f"         limiar de Alerta: {limiar:.2f} C")
    print(f"         Intervalo de leitura: {intervalo} S")

def main():
    Sensor_Status(325064)
    print("\n\n")
    Sensor_Status(439057, 37.542, 23)
    print("\n\n")
    Sensor_Status(458767, 25.0, 2)
    print("\n\n")

if __name__ == "__main__":
    main()