class Sensor:
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor

    def __str__(self):
        
        return f"Sensor {self.id}: {self.valor}V"
    
    def __repr__(self):
        
        return f"Sensor(id='{self.id}'. Valor={self.valor})"
    
    def __eq__(self, value):
        
        return self.id == value.id and self.valor == value.valor
    
    def __lt__(self, other):
        return self.valor <other.valor
    
    
class DriveIC2:
    _instancia = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            
            cls._instancia = super().__new__(cls)
        return cls._instancia

class ArquivoTemporario:
    def __init__(self, nome):
        self.nome = nome
        print(f"arquivo {nome} aberto.")
    
    def __del__(self):
        print(f"Limpando {self.nome} da RAM")

class BombaAgua:
    def __enter__(self):
        print("Ligando Bomba....")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Desligando Bomba")
        return False

class ContadorHardware:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.atual < self.limite:
            res = self.atual
            self.atual += 1
            return res
        raise StopIteration
        
class Multiplicador:
    def __init__(self, fator):
        self.fac = fator
        
    def __call__(self, valor):
        return valor * self.fac
        
class Leitura:
    def __init__(self,valor):
        self.valor = valor
        
    def __add__(self, other):
        return Leitura(self.valor + other.valor)
    
    def __repr__(self):
        return f"Leitura ({self.valor})"

class Contador:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        if  isinstance(other, Contador):
            return Contador(self.n + other.n)
        if isinstance(other, (int, float)):
            return Contador(self.n + other)
        return NotImplemented

    def __str__(self):
        return f"Erro de Implementação, tipo de variavel invalido"

    
def main():
    sens1 = Sensor("A1", 3.3)
    sens2 = Sensor("B1", 5.0)
    print(str(sens1))
    print(repr(sens1))
    print(f"\n{sens1}")
    
    d1 = DriveIC2()
    d2 = DriveIC2()
    
    print(d1 is d2)
    
    print("\n\n")
    
    temp = ArquivoTemporario("data_info.bin")
    del temp
    
    print("\n\n")
    
    with BombaAgua() as boma:
        print("Irrigando plantação")
        
    print("\n\n")
    
    for n in ContadorHardware(3):
        print(n)    
    
    print("\n\n")
    
    dobrar = Multiplicador(2)
    print(dobrar(10))
    
    print("\n\n")
    
    s1 = Leitura(10)
    s2 = Leitura(20)
    s3 = s1+s2
    print(s3)
    
    print("\n\n")
    
    print(sens1<sens2)
    
    print("\n\n")
    
    c = Contador(10)
    print(c+5)
    print(c+"2")
    
    
    
if __name__ == "__main__":
    main()