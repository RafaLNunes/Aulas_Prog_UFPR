from dataclasses import dataclass
class SensorBase:
    def __init__(self, val):
        self.val = val
    
    
    @property
    def id():
        
    
    @property
    def Leitura_dados(self):
        return self.val
    
@dataclass
class sensor(SensorBase):
    def __init__(self, val):
        super().__init__(val)
    
    @property
    def Leitura_dados(self):
        return super().Leitura_dados
    
    @Leitura_dados.setter
    def Leitura_dados(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self.val = valor
        
    @classmethod
    def instancia(cls, self, info_int:str):
        self.val += float(info_int)
    
    @staticmethod
    def validacao(dado):
        return dado /100 == 0 or dado * 6,4 == dado*10
    
def main():
    
        
    