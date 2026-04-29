import math
from abc import ABC, abstractmethod

class Forma(ABC):
    
    def __init__(self, cor: str, type:str):
        self.color = cor
        self.type = type
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    
    @abstractmethod
    def perimetro(self) -> float:
        pass
    
    def descri(self) -> str:
        return self.color
    def tp(self):
        return self.type
    
class circulo(Forma):
    def __init__(self, cor:str, raio:float, type:str = "Circulo"):
        super().__init__(cor, type)
        self.raio = raio
    
    def area(self) -> float:
        return math.pi *self.raio ** 2
    
    def perimetro(self) -> float:
        return 2 * math.pi * self.raio

class Retangulo(Forma):
    def __init__(self, cor:str, largura:float, altura:float, type:str = "Retangulo"):
        super().__init__(cor, type)
        self.largura = largura
        self.altura = altura
        
    def area(self) -> float:
        return self.largura * self.altura
    
    def perimetro(self) -> float:
        return 2 * (self.largura + self.altura)
    
class Losango(Forma):
    def __init__(self, cor: str, Diagonal_Maior:float, Diagonal_Menor:float, type:str = "Losango"):
        super().__init__(cor, type)
        self.D_Maior = Diagonal_Maior
        self.D_Menor = Diagonal_Menor
    
    def area(self) -> float:
        return (self.D_Maior * self.D_Menor)/2
    
    def perimetro(self) -> float:
        return (math.sqrt(math.pow((self.D_Maior/2),2)+math.pow((self.D_Menor/2),2)))

    
def main():
    
    Formas: list[Forma] = {
        circulo("Azul", 3),
        Retangulo("Verde", 3, 20),
        circulo("Bordo", 20),
        Losango("Cinza", 10, 7)
    }
    
    for forma_um in Formas:
        print(f"\n-----{forma_um.tp()}-----")
        print(f"{forma_um.descri()}")
        print(f"Area: {forma_um.area():.2f}")
        print(f"Perimetro: {forma_um.perimetro():.2f}")
        
    print("\n\n\n")
    
    for f in Formas:
        
        print("\n-------Test--------")
        print(f"Forma: {f.tp()} / {f.descri()}")
        print(f"Para Forma: {isinstance(f, Forma)}")
        print(f"Para Circulo: {isinstance(f, circulo)}")
        
        if isinstance(f, circulo):
            print(f"Raio: {f.raio}")
    
if __name__ == "__main__":
    main()