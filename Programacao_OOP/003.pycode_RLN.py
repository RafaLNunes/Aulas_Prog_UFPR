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
