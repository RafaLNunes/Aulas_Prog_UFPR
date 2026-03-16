import random as rd

def main():
    leitura = [rd.randint(1,300), rd.randint(1,300), rd.randint(1,300), rd.randint(1,300)]
    fases = ["A", "B", "C", "D"]
    for f, v in zip(fases, leitura):
        print(f"Fases {f}: {v} V")
    print("\n\n\n")
    for i, v in enumerate(leitura):
        print(f"Sensor {i+1}: {v}")

if __name__ == "__main__":
    main()