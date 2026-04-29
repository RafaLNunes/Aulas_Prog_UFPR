class conta:
    def __init__(self, titular: str, saldo:float):
        self._titular = titular
        self._saldo = saldo
        
    @property
    def Saldo(self) -> float:
        return self._saldo
    
    @Saldo.setter
    def Saldo(self, val):
        if val < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo += val
        
    @property
    def titular(self) -> str:
        return self._titular
    
def main():
    
    cont_banc = conta("Marcos", 20.4)
    
    cont_banc.Saldo = 20.3
    val1 = cont_banc.Saldo
    print(val1)

if __name__ == "__main__":
    main()