 
# EXERCÍCIO 1
class Sensor_ex1():
    def __init__(self, id, tipo, leitura):
        self.id = id
        self.tipo = tipo
        self.leitura = leitura

class Estacao_ex1:
    def __init__(self):
        self.sensores = []

    def adicionar(self, sensor):
        self.sensores.append(sensor)

    def remover_por_id(self, id):
        for s in self.sensores:
            if s.id == id:
                self.sensores.remove(s)
                return True
        return False

    def listar(self):
        for s in self.sensores:
            print(f"ID: {s.id} | Tipo: {s.tipo} | Leitura: {s.leitura}")

    def buscar(self, id):
        for s in self.sensores:
            if s.id == id:
                return s
        return None


 
# EXERCÍCIO 2
class Produto_ex2:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class Inventario_ex2:
    def __init__(self):
        self.lista = []

    def adicionar(self, produto):
        self.lista.append(produto)

    # protocolo []
    def __getitem__(self, index):
        return self.lista[index]

    # len()
    def __len__(self):
        return len(self.lista)

    # iterador
    def __iter__(self):
        return iter(self.lista)

    def mais_caros(self, n):
        lista_ordenada = sorted(self.lista, key=lambda x: x.preco, reverse=True)
        return lista_ordenada[:n]


 
# EXERCÍCIO 3
 class MapaRegistradores_ex3:
    def __init__(self):
        self._mapa = {}

    def definir(self, nome, endereco):
        self._mapa[nome] = endereco

    def ler(self, nome):
        return self._mapa.get(nome, None)

    def existe(self, nome):
        return nome in self._mapa


 
# EXERCÍCIO 4
 class Contato_ex4:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email

class Agenda_ex4:
    def __init__(self):
        self._contatos = {}

    def adicionar(self, nome, contato):
        self._contatos[nome] = contato

    def remover(self, nome):
        if nome in self._contatos:
            del self._contatos[nome]

    def atualizar(self, nome, telefone=None, email=None):
        if nome in self._contatos:
            if telefone:
                self._contatos[nome].telefone = telefone
            if email:
                self._contatos[nome].email = email

    def __contains__(self, nome):
        return nome in self._contatos

    def listar(self):
        for nome, c in self._contatos.items():
            print(f"{nome} -> Tel: {c.telefone} | Email: {c.email}")


def main():
    exercicio = 1

    match exercicio:

         
        case 1:
            print("EX 1:\n")

            est = Estacao_ex1()

            s1 = Sensor_ex1(1, "Temp", 25.5)
            s2 = Sensor_ex1(2, "Press", 1.2)

            est.adicionar(s1)
            est.adicionar(s2)

            est.listar()

            print("\nBuscando ID 1:")
            print(est.buscar(1).tipo)

            print("\nRemovendo ID 1")
            est.remover_por_id(1)

            est.listar()

            print("====================================================")
         
        case 2:
            print("EX 2:\n")

            inv = Inventario_ex2()

            inv.adicionar(Produto_ex2(1, "Mouse", 50))
            inv.adicionar(Produto_ex2(2, "Teclado", 120))
            inv.adicionar(Produto_ex2(3, "Monitor", 900))

            print("Primeiros 2 (slicing):")
            for p in inv[:2]:
                print(p.nome)

            print("\nMais caros:")
            for p in inv.mais_caros(2):
                print(p.nome, p.preco)

            print("====================================================")
         
        case 3:
            print("EX 3:\n")

            mapa = MapaRegistradores_ex3()

            mapa.definir("GPIO_IN", "0x4000")
            mapa.definir("ADC", "0x5000")

            print("Leitura:", mapa.ler("GPIO_IN"))
            print("Existe ADC?", mapa.existe("ADC"))
            print("Existe PWM?", mapa.existe("PWM"))

            print("====================================================")
         
        case 4:
            print("EX 4:\n")

            agenda = Agenda_ex4()

            agenda.adicionar("Maria", Contato_ex4("9999-9999", "maria@email.com"))
            agenda.adicionar("João", Contato_ex4("8888-8888", "joao@email.com"))

            agenda.listar()

            print("\nAtualizando Maria")
            agenda.atualizar("Maria", telefone="7777-7777")

            print("\n'Maria' está na agenda?", "Maria" in agenda)

            agenda.listar()

            print("\nRemovendo João")
            agenda.remover("João")

            agenda.listar()

            print("====================================================")

 

if __name__ == "__main__":
    main()