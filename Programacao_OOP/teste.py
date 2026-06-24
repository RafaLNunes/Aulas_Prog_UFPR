def Principal():
    print("Hello World!!!")
    id = 3103
    temp = 25.456079

    print(f"Sensor ID: {id}")

    # Por Padrao, o py utiliza um /n antes de cada print
    # caso queira retira-lo, basta por end="" no final
    # print("Teste", end="")

    # for i in range(3):
        # print(i, end="-")
        # Saída: 0-1-2-
    # print("")


    # caso queira usar formatação na propria impressao, utilizar formatação padrao de C
    # no caso, formata para aparecer apenas 2 casas no decimal
    print(f"Temperatura: {temp:.2f} C")

    # Da para fazer operações dentro do print
    print(f"Dobro: {id*2}")

if __name__ =="__main__":
    Principal()
    
    
import numpy as np
import random as rd

def exibir_matrix(matrix):
    print("\n\n --------------- MATRIX ESTRUCTURE ---------------")
    for line in matrix:

        for colun in line:
            print(f"{colun:^5}", end = " ")
        print()

def rand_texture():
    #aqui vem outra

    line = rd.randint(0,1050)
    colu = rd.randint(0,1050)

    matrix = []
    for i in range(line):
        new_line = []
        for j in range(colu):
            val = rd.randint(-150,250)
            print(f" Valor para [{i}][{j}]:[{val}]")
            new_line.append(val)
        matrix.append(new_line)
    # exibir_matrix(matrix)

def main():
    # aqui vem a central
    rand_texture()

if __name__ == "__main__":
    main()



from time import sleep

def Principal():

    List_dados = ["12.5", "11.8", "13.2", "19.5", "12.1", "99.3"]

    for dado in List_dados:
        sleep(1)
        tensao_float = float(dado)
        
        print(f"\nTensão atual do calculo: {tensao_float:.1f} V")

        if tensao_float < 10 or tensao_float > 99.5:
            print(f"FALHA CRÍTICA: {tensao_float:.1f}")
            break

        else:
            print("Passou")

    else:
        print("Status Concluido em 100%")
        
    print("\n\nConcluido o processo de Verificação\n")



if __name__ == "__main__":
    Principal()
    
    
    
    
    # FUNÇÕES E ?RECURSIVIDADE?
# o interessante das funções é a reutilização em qualquer ponto do codigo, após sua criação
# no caso do py:
"""
def Nome_da_def(valor):
    informações
    ...
    ...
    ...
    return valor_ou_qualquer_outra_coisa
"""

def sum(a,b):
    return a+b
def Saudar(name, campus):
    print(f"Hello {name}, bem vindo a {campus}")
    print(f"You are number: {sum(3,10)}")

if __name__ == "__main__":
    Saudar("rafael", "UFPR Poli")


def fact(n):
    if n<= 1:
        return 1
    return n * fact(n - 1)

def main():
    numb = 998
    result = fact(numb)
    # A partir do numb2 == 999, gera um exception
    numb2 = 998
    print(f"Fatorial de {numb} é {result}")
    print(f"Fatorial de {numb2} é {fact(numb2)}")

if __name__ == "__main__":
    main()
    
    
    
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
    
    
    def main():
    name = input("Digite o nome do sensor: ")
    leitura = int(input("N° de Mensagens enviadas: "))
    energy = float(input("Consumo de energia  (mJ): "))

    print("\n ...... Relatório ...... ")
    print(f"Mensagens: {leitura}")
    print(f"Média de energia por mensagem: {energy/leitura:.2f} mJ")

    print("\n\n\n")
    print(f"{type(name)}\n{type(energy)}\n{type(leitura)}")


if __name__ == "__main__":
    main()



# imports no py, servem para trazer biblioteca
# se você usar from, consegue até importar funções expecificas de uma biblio
# sem pesar demais puxando toda a biblio

import random as rnd
import ath

def main():
    Rand_import_test()

def Math_import_test():
    print("Teste")

def Rand_import_test():
    ruido = rnd.random()

    porta = rnd.randint(10000,655402)

    fases = ["A", "B", "C"]
    sortear = rnd.choice(fases)
    print(f"Ruido: {ruido}")
    print(f"Porta: {porta}")
    print(f"Fase: {sortear}")

if __name__ == "__main__":
    main()



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
    
    
    
    def calc_Med(val):
    if not val:
        return 0.0
    
    somar = sum(val)
    med = somar / len(val)
    return med

def main():
    ler_list = []
    n = int(input("QTD de sensores: "))
    for i in range(n):
        val = float(input(f"Temperatura acessada no sensor {i}: "))
        ler_list.append(val)
    med_fiunal = calc_Med(ler_list)
    print(f"Média das {n} leitura: {med_fiunal:.2f} C")

if __name__ == "__main__":
    main()
    
    
    
    
    import random as rd

def exibir_matrix(matrix):
    print("\n\n --------------- MATRIX ESTRUCTURE ---------------")
    for line in matrix:

        for colun in line:
            print(f"{colun:^5}", end = " ")
        print()

def main():
    line = int(input("N° de Linhas: "))
    colu = int(input("N° de Colunas: "))

    matrix = []
    for i in range(line):
        new_line = []
        for j in range(colu):
            val = rd.randint(-150,250)
            print(f" Valor para [{i}][{j}]:[{val}]")
            new_line.append(val)
        matrix.append(new_line)
    exibir_matrix(matrix)

if __name__ == "__main__":
    main()


import numpy as np
import random as rd

def main():
    ler = np.array([25.4,26.1,24.8,25.9,27.2])

    ajust = ler + 2.0

    print(f"Temperatura: {ajust}")
    print(f"Média: {ler}") # :.2f nãoi ta funcionando aqui
    print(f"Desvio Padrão: {np.std(ler):.2f}")

    matrix = np.array([
        [rd.randint(-150,250), rd.randint(-150,250), rd.randint(-150,250)],
        [rd.randint(-150,250), rd.randint(-150,250), rd.randint(-150,250)],
        [rd.randint(-150,250), rd.randint(-150,250), rd.randint(-150,250)]
    ])

    print("\nMatriz Transposta: ")
    print(matrix.T)

if __name__ == "__main__":
    main()
    
    
    
    
    
    def main():

    sensor = {
        "id":310,
        "tipo": "RPL_Node",
        "valor":25.5,
        "Unidade":"Celsius",
        "bateria": 30
    }

    print(f"--- Telemetria do sensor {sensor['id']} ---")
    print(f"Leitura: {sensor['valor']} {sensor['Unidade']}")

    sensor["status"] = "Ativo"
    if "bateria" in sensor:
        print(f"Bateria: {sensor['bateria']}%")
    else:
        print("Não encontrado")

if __name__ == "__main__":
    main()
    
    
    
    
    import random as rd

def main():

    rede = {}

    ids_search = [3103, 3105]

    for node_id in ids_search:

        rede[node_id] = {
            "temp":24.0+ (node_id%10),
            "energia":100.0,
            "protocol":"RPL"
        }
    
    print(f"\nTemperatura do motor 3103: {rede[3103]['temp']} C")
    rede[3103]["energia"] = 85.5
    print(f"\n --- Status Atual da Rede ---")
    for mote, dados, in rede.items():
        print(f"ID: {mote}\nStatus: {dados["protocol"]}\nBateria: {dados['energia']}%")


if __name__ == "__main__":
    main()
    
    
    import math
import random as rd


def Gerar_leitura(nominal):
    return nominal + rd.uniform(-5.0, 5.0)
def Calc_Pot(V, I, cos_phi=0.95):
    return V * I * cos_phi
def main():
    Fases = ["A", "B", "C"]
    nominais = [127.0, 127.0, 127.0]
    corrente = 10.5
    F_val = "Fases"
    v_real_val = "Volts"
    p_Ativa_val = "Potencia"
    print(f"{F_val:<6} | {v_real_val:<11} | {p_Ativa_val:<11}")
    for F,N in zip(Fases,nominais):
        v_real = Gerar_leitura(N)
        p_Ativa = Calc_Pot(v_real, corrente)

        print(f"{F:<6} | {v_real:>11.2f} | {p_Ativa:>11.2f}")

if __name__ == "__main__":
    main()


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
    
    
    def main():
    
    print("Hello")

if __name__ == "__main__":
    print("\n\n\nINICIADO O COD\n\n\n")
    main()
    
    
    
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
    
    
    import traceback
import logging
logging.basicConfig(filename='sist_confg.log', level=logging.WARN)


try:
    print("Teste de divisão\n\n")
    raio = -1/0
    print(f"{raio}")
    assert raio >=0, "O raio não existe Negativo"
    rainse RuntimeError("falha de Barramento")
    print("\n\ndivisão concluida")
except ZeroDivisionError as e:
    print(f"Tipo: {type(e)}")
    print(f"Arg: {e.args}")
    print(f"Mensagem: {str(e)}")
    
    
    
    logging.exception("Falha critica de divisão")
    logging.fatal("fatal work")
    logging.error("Erro de trabalho")
    
    traceback.print_exc()


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


class A:
    def Metodo(self):
        print("\nA.Metodo")
class B(A):
    def Metodo(self):
        print("\nB.Metodo")
        super().Metodo()
class C(A):
    def Metodo(self):
        print("\nC.Metodo")
        super().Metodo()
class D(B, C):
    def Metodo(self):
        print("\nD.Metodo")
        super().Metodo()

def main():
    Objs_A = A()
    Objs_B = B()
    Objs_C = C()
    Objs_D = D()
    
    Objs_A.Metodo()
    Objs_B.Metodo()
    Objs_C.Metodo()
    Objs_D.Metodo()
    
    
if __name__=="__main__":
    main()
    
    
    
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
    print("")
    
        
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
    
    from collections import UserList
import numpy as np

class Lista_Sensor(UserList):
    def append(self, item):
        if item <0:
            raise ValueError("Erro de QTD")
        super().append(item)




def main():
    l = [12,2,3,4,5,1,6,7,17,8,9,10,11,13,14,15,16,18,19,20]
    s = set(l)
    print(s)
    s.add(44)
    s.remove(1)
    print(s)
    
    a = {1,2,3}
    b = {3,4,5}
    
    print(a | b)
    print(a & b)
    print(a - b)

    print("\n\n\n\n")
    
    let = Lista_Sensor()
    let.append(10.5)

    
if __name__ == "__main__":
    main()
    
    
    import multiprocessing as mp
import time

def calc_Q(x):
    tempo_I =time.time()
    while(time.time()-tempo_I)<180:
        _ = x * x
    return x*x

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9,10]
    lista_Resu = []
    
    
    '''
    for i in lista:
        lista_Resu.append(calc_Q(i))
    '''
    
    
    with mp.Pool(processes=3) as pool:
        resultados = pool.map(calc_Q, lista)
        
    
    print(resultados)
    
    import random as rd
import math
import numpy as np
from dataclasses import dataclass

#Ex 1
class Processador:
    ## Passo 1.B    
    def __init__(self, data_info):
        self.__info_Project = data_info
    
    ## Passo 1.C
    def Dobrar(self):
        print(f"Dobro de {self.__info_Project} é {self.__info_Project*2}")

# Ex 2
class Mascara:
    ## Passo 2.A
    def __init__(self, Valor):
        self.Valor_Entregue = Valor
        self.Valor_Gerado = rd.randint(1,50)
    
    ## Passo 2.B
    def Operacao_OR(self):
        print(f"Val interno: {self.Valor_Gerado} / {self.Valor_Gerado:0b}")
        print(f"Val Entregue: {self.Valor_Entregue} / {self.Valor_Entregue:0b}\n")
        return self.Valor_Entregue | self.Valor_Gerado

# Ex 3
class Telemetria:
    def __init__(self, comp_name):
        self.__Componente_Nome = comp_name
        self.__list_Parametros = []
    
    def Add_parametro(self, dado_parametro):
        self.__list_Parametros.append(dado_parametro)
    
    def Leitura_Lista(self):
        return self.__list_Parametros    
    
# Ex 4
class Sensor_critico:
    def __init__(self, limit):
        self.__limite = limit
        self.__list_sens = [
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10),        
            rd.uniform(1,10)        
        ]
        
    def Get_List(self):
        
        list_info = {
            "index_erro": int,
            "info_erro": float
        }
        
        for index, item in enumerate(self.__list_sens):
            print(f"Dado {index+1}°: {item:.2f}")
        print()    
        for index, item in enumerate(self.__list_sens):
            print(f"Dado {index+1}°: {item:.2f}")
            if item < self.__limite:
                list_info["index_erro"] = index
                list_info["info_erro"] = item
                print("  ERROR")
                break
        
        
        
        return list_info
    
# Ex 5
class Raio_secao:
    def __init__(self):
        self.__pi = math.pi
    def Calc_Raio(self, raio):
        return self.__pi * pow(raio,2)

# Ex 6
class ruido:
    
    def __init__(self):
        self.__ruido = rd.uniform(-0.5,0.5)
    
    def Capta_Ruido(self, val_parametro):
        return self.__ruido+val_parametro

# Ex 7
class somatoria:
    def __init__(self, n_vindo):
        self.__atual_val = 0
        self.__n = n_vindo
    def Recursiva_Sum(self, valor):
        
        if self.__n == 0:
            return self.__atual_val
        self.__atual_val = self.__atual_val + valor
        self.__n = self.__n-1
        return self.Recursiva_Sum(self.__atual_val)
        
    def somat_leitura(self, valor):
        resultado = self.Recursiva_Sum(valor)
        return resultado
        
# Ex 8
class IDdispositivo:
    def __init__(self, disc_ID):
        # Dicionário privado (__ indica que é privado)
        self.__ID_dispositivos = disc_ID

    def buscar_ID(self, id):

        resultado = self.__ID_dispositivos.get(id, "ID não encontrado")
        return resultado

# Ex 9
class analise_np:
    def __init__(self, list_data):
        self.__list_np_test = list_data   
        self.__mascara_controle = []
        
    def analise(self):
        array_list_np = np.array(self.__list_np_test)
        self.__mascara_controle = array_list_np > 0
            
        
        analise_result = array_list_np[self.__mascara_controle]
        resultado = np.sum(analise_result)
        return resultado

# Ex 10
@dataclass
class Evento:
    id: str
    gravidade: str

def main():
    Exercicios = 9

    match Exercicios:
        case 1:
            # Ex 1
            
            ## Passo A
            data_process = float(input("Aqui virá um valor Float (xx.x): "))
            print(data_process,"\n")
            
            ## Passo B
            Dados_Projeto = Processador(data_process)
            
            ## Passo C
            Dados_Projeto.Dobrar()
            
            # ------------------------------------------------------------------------------
            print("\n\n\n")
        
        case 2:
            # Ex 2
            
            ## Passo A
            val_entrada = int(input("Aqui virá um valor inteiro: "))
            controle = Mascara(val_entrada)
            
            ## Passo C
            Or_Result = controle.Operacao_OR()
            print(f"Resultado do OR bit a bit: {Or_Result} / {Or_Result:0b}")
            
            # ------------------------------------------------------------------------------
            print("\n\n\n")
        
        case 3:
            #Ex 3
            
            ## Passo A
            nome_comp = str(input("Aqui virá o nome de um componente: "))
            Telemetria_dados = Telemetria(nome_comp)
            
            ## Passo B
            check = 1
            while check:
                parametro_info = float(input("Aqui virá um valor float: "))
                check = int(input("Gostaria de continuar?\n(0 => Não)\n(1 => Sim)\nEscolha: "))
                if not check:
                    # print("saindo")
                    break
                Telemetria_dados.Add_parametro(parametro_info)
            
            ## Passo C
            print("\n")
            print("-+-+-+-+-+-+-+-+-+-")
            for index, param in enumerate(Telemetria_dados.Leitura_Lista()):
                print(f"Parametro {index+1}°: {param:.2f} V") 
            print("-+-+-+-+-+-+-+-+-+-")
            
            # ------------------------------------------------------------------------------
            print("\n\n\n")
        
        case 4:    
            # Ex 4

            
            entrega = float(input("Aqui virá o float tido como limite crítico (xx.x): "))
            sensor_crit = Sensor_critico(entrega)
            ficha_tec = sensor_crit.Get_List()

            print(f"Index do Erro: {ficha_tec['index_erro']}\nValor do Erro: {ficha_tec['info_erro']:.2f}\nLimite de Valores: {entrega:.2f}")
    

            # ------------------------------------------------------------------------------
            print("\n\n\n")
            
        case 5:
            # Ex 5
            
            ## Passo B
            raio_info = float(input("Aqui virá  o raio do seu condutor: "))
            ## Passo C
            info_raio = Raio_secao()
            Area_transversal = info_raio.Calc_Raio(raio_info)
            print(f"A aseção transversal desse condutor é de {Area_transversal}")
        
            # ------------------------------------------------------------------------------
            print("\n\n\n")
            
        case 6:
            # Ex 6
            ruido_inicial = float(input("Aqui, virá o parâmetro base para o ruido: "))
            info_ruido = ruido()
            ruido_final = info_ruido.Capta_Ruido(ruido_inicial)
            
            print(f"Esse é o Resultado do ruido: {ruido_final:.2f}")
            
            # ------------------------------------------------------------------------------
            print("\n\n\n")
            
        case 7:
            # Ex 7
            n_recursivo = int(input("Digite o numero de repetições: "))
            val_inicial_sum = float(input("Digite o valor inicial do calculo: "))
            sum_calc = somatoria(n_recursivo)
            print(f"Somatória: {sum_calc.somat_leitura(val_inicial_sum)}")
            
            # ------------------------------------------------------------------------------
            print("\n\n\n")
            
        case 8:
            #ex 8
            
            dados_iniciais = {
                "Sala1": "001",
                "Sala2": "001",
                "Sala3": "003"
            }
            
            gerenciador = IDdispositivo(dados_iniciais)
            
            print(f"IP Encontrado: {gerenciador.buscar_ID('Sala1')}")
            print(f"IP Encontrado: {gerenciador.buscar_ID('sala10')}")
            
            # ------------------------------------------------------------------------------
            print("\n\n\n")
            
        case 9:
            # Ex 9
            list_dt = []   
            
            x = 5
            for i in range(x):
                dt = float(input("Entre com o item da list: "))
                list_dt.append(dt)
            
  

            np_test_obj = analise_np(list_dt)
            resultado = np_test_obj.analise()
            
            print(f"\n Somatória: {resultado:.2f}")
            
            # ------------------------------------------------------------------------------
            print("\n\n\n")
            
        case 10:
            # Ex 10
            
            valor_analise = float(input("Digite o valor numerico da gravidade: "))
            Evnt = Evento(id="001",gravidade = "ALTA" if valor_analise > 10 else "BAIXA") 
            print(f"ID: {Evnt.id}\nGravidade: {Evnt.gravidade}")
            
#-----------------------------------

if __name__ == "__main__":
    main()
    