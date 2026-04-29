class date:
    def __init__(self, dia:int, mes:int, ano:int):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    @classmethod
    def hoje(cls):
        from datetime import date
        d = date.today()
        return cls(d.day, d.month, d.year)
    
    @classmethod
    def from_string(cls, data_str:str):
        dia, mes, ano = map(int, data_str.split('/'))
        return cls(dia, mes, ano)
    
    @staticmethod
    def eh_bi(ano:int) -> bool:
        
        return ano % 4 == 0 and (ano %100 != 0 or ano % 400 ==0)

def main():
    dia = date(20, 10, 2001)
    
    d = dia.hoje()
    e = dia.eh_bi(2025)
    f = dia.from_string("01/02/2019")
    
    print(f"{d}\n{e}\n{f}")    
    
if __name__ == "__main__":
    main()    
        