from dataclasses import dataclass

@dataclass
class Veiculo:
    modelo: str
    capacidade: float
    carga_atual:float

@dataclass
class Estacao:
    nome: str
    pot: float
    preco_kwh: float

def temp_Preciso(v,e):

    temp = v.capacidade * (1 - v.carga_atual /100)
    temp_carga_total = temp / e.pot

    return temp_carga_total


def custo_recarga(v,e):

    energia_falt = v.capacidade * (1 - v.carga_atual/100)
    custo_total_bater = energia_falt * e.preco_kwh

    return custo_total_bater

def main():
    
    Tesla = Veiculo("Tesla Model3", ((50+82)/2), 0.10)
    BYD = Veiculo("BYD Dolphin", 44.9, 0.10)

    estacao = Estacao("Eletroposto UFPR", ((50+60+120+150+300)/5), 3.5)
    
    temp_tesla = temp_Preciso(Tesla, estacao)
    temp_byd = temp_Preciso(BYD, estacao)

    # esta dando e hora, 1.3 seria 1 hora e 30% de outra = 1h e +-20 min
    # multiplica por 60 para converter em mins

    temp_tesla *= 60
    temp_byd *= 60

    custo_tesla = custo_recarga(Tesla, estacao)
    custo_byd = custo_recarga(BYD, estacao)

    print(f"\n\nTempo do {Tesla.modelo}: {temp_tesla:.0f} Minutos")
    print(f"custo do {Tesla.modelo}: R$ {custo_tesla:.2f}")

    print(f"\n\nTempo do {BYD.modelo}: {temp_byd:.0f} Minutos")
    print(f"custo do {BYD.modelo}: R$ {custo_byd:.2f}\n\n")


if __name__ == "__main__":
    main()