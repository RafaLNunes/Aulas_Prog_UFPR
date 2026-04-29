import math
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo: str, capacidade: float, carga_atual:float):
        self.model = modelo
        self.capacidade = capacidade
        self.carga = carga_atual
        self.temp_carga_total:float

    @abstractmethod
    def temp_Preciso(self, E):

        return self.temp_carga_total
    
    def model_view(self):
        return self.model
    

class Estacao(ABC):
    
    def __init__(self, nome: str, pot: float, preco_kwh: float):
        self.name = nome
        self.potencia = pot
        self.RS_KWH = preco_kwh
        self.custo_total_bater:float
    
    @abstractmethod
    
    def custo_recarga(self, V):
        
        return self.custo_total_bater
    def estation_view(self):
        return self.name
    

class BYD(Veiculo):
    def __init__(self, modelo: str, capacidade: float, carga_atual:float):
        super().__init__(modelo, capacidade, carga_atual)
        
    def temp_Preciso(self, E):
        
        temp = (self.capacidade * (1 - self.carga /100))*1.5#Eficiencia
        temp_carga_total = temp / E
        return temp_carga_total

class TESLA(Veiculo):
    def __init__(self, modelo: str, capacidade: float, carga_atual:float):
        super().__init__(modelo, capacidade, carga_atual)
        
    def temp_Preciso(self, E):
        
        temp = (self.capacidade * (1 - self.carga /100))*1.2#Eficiencia
        temp_carga_total = temp / E
        return temp_carga_total

class Ipiranga(Estacao):
    def __init__(self, nome, pot, preco_kwh):
        super().__init__(nome, pot, preco_kwh)
    
    def custo_recarga(self, V_cap, V_carga):

        energia_falt = V_cap * (1 - V_carga/100)
        custo_total_bater = energia_falt * self.preco_kwh

        return custo_total_bater
class BR_Posto(Estacao):
    def __init__(self, nome, pot, preco_kwh):
        super().__init__(nome, pot, preco_kwh)
    
    def custo_recarga(self, V_cap, V_carga):

        energia_falt = V_cap * (1 - V_carga/100)
        custo_total_bater = energia_falt * self.preco_kwh

        return custo_total_bater

def main():
    
    Veiculos: list[Veiculo] = {
        BYD("BYD Dolphin", 44.9, 0.10),
        TESLA("Tesla Model3", ((50+82)/2), 0.10)
    }
    
    Estacoes: list[Estacao] = {
        Ipiranga("Eletroposto UFPR", ((50+60+120+150+300)/5), 3.5),
        BR_Posto("POSTO BR", ((50+60+1120+150+300)/5), 3.5)
    }
    

    for veic in Veiculos:
        for estation in Estacoes:
            print(f"-------Modelo {veic.model_view()}-------")
            print(f"Estação: {estation.estation_view()}")
            print(f"\n\nTempo do {veic.model_view()}: {veic.temp_Preciso(estation.potencia):.2f} Minutos")
            print(f"custo do {veic.model_view()}: R$ {estation.custo_recarga(veic.capacidade, veic.carga):.2f}")
        
if __name__ == "__main__":
    main()
