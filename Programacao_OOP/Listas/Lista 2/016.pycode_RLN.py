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
    def __init__(self):
        self.__list_np_test = [
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10),
            rd.uniform(-10,10)
        ]
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
    Exercicios = 7

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

            np_test_obj = analise_np()
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
    