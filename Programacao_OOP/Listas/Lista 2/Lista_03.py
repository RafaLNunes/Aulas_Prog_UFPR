from collections import UserList

# Ex 1
class Sensor_ex1:
    def __init__(self, id, tipo, leitura):
        self.id = id
        self.tipo = tipo
        self.leitura = leitura


class Estacao_ex1:
    def __init__(self):
        self.__list_sensores = []

    def ADD_estation(self, sensor):
        self.__list_sensores.append(sensor)

    def remover_por_id(self, id):
        for sens in self.__list_sensores:
            if sens.id == id:
                self.__list_sensores.remove(sens)
                return True
        return False

    def list_estacao(self):
        for sens in self.__list_sensores:
            print(f"ID: {sens.id} | Tipo: {sens.tipo} | Leitura: {sens.leitura}")

    def buscar(self, id):
        for sens in self.__list_sensores:
            if sens.id == id:
                return sens
        return None

# Busca linear possui custo O(n).

# Ex 2
class Produto_ex2:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class Inventario_ex2:
    def __init__(self):
        self.__list_produtos = []

    def ADD_invt(self, produto):
        self.__list_produtos.append(produto)

    def __getitem__(self, item):
        return self.__list_produtos[item]

    def __len__(self):
        return len(self.__list_produtos)

    def __iter__(self):
        return iter(self.__list_produtos)

    def mais_caros(self, n):
        lista_ordenada = sorted(self.__list_produtos, key=lambda item: item.preco, reverse=True)

        return lista_ordenada[:n]

# A estrutura list facilita slicing e ordenação de forma eficiente.
 
# Ex 3
class MapaRegistradores_ex3:
    def __init__(self):
        self.__dict_reg = {}

    def definir(self, nome, endereco):
        self.__dict_reg[nome] = endereco

    def ler(self, nome):
        return self.__dict_reg.get(nome, None)

    def existe(self, nome):
        return nome in self.__dict_reg

# Dict possui busca média O(1).
 
# Ex 4
class Contato_ex4:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email
class Agenda_ex4:
    def __init__(self):
        self.__dict_contatos = {}

    def ADD_agend(self, nome, contato):
        self.__dict_contatos[nome] = contato

    def remover(self, nome):
        if nome in self.__dict_contatos:
            del self.__dict_contatos[nome]

    def atualizar(self, nome, telefone=None, email=None):
        if nome in self.__dict_contatos:
            if telefone:
                self.__dict_contatos[nome].telefone = telefone

            if email:
                self.__dict_contatos[nome].email = email

    def __contains__(self, nome):
        return nome in self.__dict_contatos

    def list_dados(self):
        for nome, contato in self.__dict_contatos.items():
            print(f"{nome} | {contato.telefone} | {contato.email}")

# Dict melhora desempenho de busca em relação à list.
 
# Ex 5
class Artigo_ex5:
    def __init__(self, titulo):
        self.titulo = titulo
        self.cods = set()

    def marcar(self, cod):
        self.cods.add(cod)

    def desmarcar(self, cod):
        self.cods.discard(cod)

    def tem_cod(self, cod):
        return cod in self.cods


def cods_comuns(a, b):
    return a.cods & b.cods


def todas_cods(a, b):
    return a.cods | b.cods

# Set otimiza operações de união e interseção.
 
# Ex 6
class FiltroEmails_ex6:
    def __init__(self, list_emails):
        self.__list_emails = list_emails

    def unicos(self):
        return list(set(self.__list_emails))

    def duplicados(self):
        set_dup = set()
        set_aux = set()

        for email in self.__list_emails:
            if email in set_aux:
                set_dup.add(email)
            else:
                set_aux.add(email)

        return list(set_dup)

# Set remove duplicatas em média O(1).
 
# Ex 7
class Prato_ex7:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
class Cardapio_ex7:
    def __init__(self):
        self.__dict_cardapio = {}

    def ADD_prato(self, categoria, prato):
        if categoria not in self.__dict_cardapio:
            self.__dict_cardapio[categoria] = []

        self.__dict_cardapio[categoria].append(prato)

    def list_card(self, categoria):
        return self.__dict_cardapio.get(categoria, [])

    def total_por_categoria(self):
        dict_total = {}

        for categoria, pratos in self.__dict_cardapio.items():
            soma = 0

            for prato in pratos:
                soma += prato.preco

            dict_total[categoria] = soma

        return dict_total

# Dict organiza categorias e list armazena múltiplos pratos.
 
# Ex 8
class HistoricoLeituras_ex8(UserList):

    def __init__(self):
        super().__init__()

    def append(self, item):
        if item < 0:
            raise ValueError("Valor negativo")

        UserList.append(self, item)

    def insert(self, index, item):
        if item < 0:
            raise ValueError("Valor negativo")

        UserList.insert(self, index, item)

    def extend(self, other):
        for item in other:
            if item < 0:
                raise ValueError("Valor negativo")

        UserList.extend(self, other)

    def media(self):
        return sum(self.data) / len(self.data)

    def maximo(self):
        return max(self.data)

    def minimo(self):
        return min(self.data)

# UserList permite personalizar validações mantendo comportamento de lista.
 
# Ex 9
class ContadorPalavras_ex9:
    def __init__(self, texto):
        self.__dict_contagem = {}

        palavras = texto.split()

        for palavra in palavras:
            palavra = palavra.lower()

            if palavra in self.__dict_contagem:
                self.__dict_contagem[palavra] += 1
            else:
                self.__dict_contagem[palavra] = 1

    def frequencia(self, palavra):
        return self.__dict_contagem.get(palavra.lower(), 0)

    def top_n(self, n):
        lista_ordenada = sorted(self.__dict_contagem.items(), key=lambda item: item[1], reverse=True)

        return lista_ordenada[:n]

    def total_unico(self):
        return len(self.__dict_contagem)

# Dict é eficiente para contagem de frequência.

# Ex 10
class Usuario_ex10:
    def __init__(self, nome):
        self.nome = nome
        self.permissoes = set()

    def conceder(self, permissao):
        self.permissoes.add(permissao)

    def revogar(self, permissao):
        self.permissoes.discard(permissao)

    def pode(self, permissao):
        return permissao in self.permissoes


def  Permissoes_Padrao(u1, u2):
    return u1.permissoes & u2.permissoes


def permissoes_exclusivas(u1, u2):
    return u1.permissoes ^ u2.permissoes


def permissoes_combinadas(u1, u2):
    return u1.permissoes | u2.permissoes

# Set facilita operações matemáticas entre permissões.

# Main
def main():

    exercicio = 10

    match exercicio:

        case 1:
            print("Ex 1:\n")

            estacao = Estacao_ex1()

            sensor1 = Sensor_ex1(1, "Temperatura", 22.5)
            sensor2 = Sensor_ex1(2, "Pressao", 1.4)

            estacao.ADD_estation(sensor1)
            estacao.ADD_estation(sensor2)

            estacao.list_estacao()

            print()

            busca = estacao.buscar(1)
            print(f"Sensor Encontrado: {busca.tipo}")

         
        case 2:
            print("Ex 2:\n")

            inventario = Inventario_ex2()

            inventario.ADD_invt(Produto_ex2(1, "Mouse", 50))
            inventario.ADD_invt(Produto_ex2(2, "Monitor", 800))
            inventario.ADD_invt(Produto_ex2(3, "Teclado", 120))

            for item in inventario[:2]:
                print(item.nome)

            for item in inventario.mais_caros(2):
                print(f"{item.nome} | {item.preco}")

         
        case 3:
            print("Ex 3:\n")

            mapa = MapaRegistradores_ex3()

            mapa.definir("GPIO_IN", "0x4000")
            mapa.definir("ADC", "0x5000")

            print(mapa.ler("GPIO_IN"))
            print(mapa.existe("ADC"))
            print(mapa.existe("PWM"))

         
        case 4:
            print("Ex 4:\n")

            agenda = Agenda_ex4()

            agenda.ADD_agend("Maria", Contato_ex4("99999-9999", "maria@email.com"))
            agenda.ADD_agend("Joao", Contato_ex4("88888-8888", "joao@email.com"))
            agenda.list_dados()

            agenda.atualizar("Maria", telefone="77777-7777")
            agenda.list_dados()
            
            print("\n\nMaria" in agenda)

         
        case 5:
            print("Ex 5:\n")

            artigo1 = Artigo_ex5("Python")
            artigo2 = Artigo_ex5("POO")

            artigo1.marcar("python")
            artigo1.marcar("backend")

            artigo2.marcar("backend")
            artigo2.marcar("oop")

            print(cods_comuns(artigo1, artigo2))
            print(todas_cods(artigo1, artigo2))

         
        case 6:
            print("Ex 6:\n")

            lista_emails = [
                "a@email.com",
                "b@email.com",
                "a@email.com",
                "c@email.com"
            ]

            filtro = FiltroEmails_ex6(lista_emails)

            print(filtro.unicos())
            print(filtro.duplicados())

         
        case 7:
            print("Ex 7:\n")

            cardapio = Cardapio_ex7()

            cardapio.ADD_prato("Bebidas", Prato_ex7("Suco", 8))
            cardapio.ADD_prato("Bebidas", Prato_ex7("Refrigerante", 6))
            cardapio.ADD_prato("Pratos", Prato_ex7("Lasanha", 25))

            for item in cardapio.list_card("Bebidas"):
                print(item.nome)

            print(cardapio.total_por_categoria())

         
        case 8:
            print("Ex 8:\n")

            historico = HistoricoLeituras_ex8()

            historico.append(10.5)
            historico.append(20.3)
            historico.append(5.1)

            print(historico)
            print(historico.media())
            print(historico.maximo())
            print(historico.minimo())

         
        case 9:
            print("Ex 9:\n")

            texto = "python python dados estrutura python lista"

            contador = ContadorPalavras_ex9(texto)

            print(contador.frequencia("python"))
            print(contador.top_n(2))
            print(contador.total_unico())

         
        case 10:
            print("Ex 10:\n")

            user1 = Usuario_ex10("Rafa")
            user2 = Usuario_ex10("Maria")

            user1.conceder("admin")
            user1.conceder("editor")

            user2.conceder("editor")
            user2.conceder("viewer")

            print( Permissoes_Padrao(user1, user2))
            print(permissoes_exclusivas(user1, user2))
            print(permissoes_combinadas(user1, user2))

if __name__ == "__main__":
    main()
