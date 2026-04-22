class Animal:
    def __init__(self, nome: str, idade: int):
        self.name = nome
    def comer(self):
        print(f"{self.name} está comendo")
    
    def dormir(self):
        print(f"{self.name} está dormindo")

class Dog(Animal):
    def __init__(self, nome:str, raca:str, idade: int):
        super().__init__(nome, idade)
        self.raca = raca

    def latir(self):
        print(f"{self.name} está latindo")
    
    def comer(self):
        print(f"{self.name} está devorando a ração")
        
def main():
    Dog1 = Dog("TEO", "Golden", 12)
    Dog1.dormir()
    Dog1.latir()
    Dog1.comer()
    
if __name__ == "__main__":
    main()