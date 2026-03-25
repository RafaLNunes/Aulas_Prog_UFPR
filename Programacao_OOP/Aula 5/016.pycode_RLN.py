import random as rd

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
        self.list_Parametros = []
    
    def Add_parametro(self, dado_parametro):
        self.list_Parametros.append(dado_parametro)


# Ex 4
def Get_List(lista_info_sensores, limite):
    
    Error_info = {
        "index_erro": int,
        "info_erro": float
    }
    
    for index, item in enumerate(lista_info_sensores):
        print(f"Dado {index+1}°: {item:.2f}")
    print()    
    for index, item in enumerate(lista_info_sensores):
        print(f"Dado {index+1}°: {item:.2f}")
        if item < limite:
            Error_info["index_erro"] = index
            Error_info["info_erro"] = item
            print("  ERROR")
            break
    
    
    
    return Error_info
    

def main():
    Exer = 5

    match Exer:
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
            for index, param in enumerate(Telemetria_dados.list_Parametros):
                print(f"Parametro {index+1}°: {param:.2f} V") 
            print("-+-+-+-+-+-+-+-+-+-")
            
            # ------------------------------------------------------------------------------
            print("\n\n\n")
        
        case 4:    
            # Ex 4
            list_sens = [
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
            
            entrega = float(input("Aqui virá o float tido como limite crítico (xx.x): "))
            ficha_tec = Get_List(list_sens, entrega)

            print(f"Index do Erro: {ficha_tec['index_erro']}\nValor do Erro: {ficha_tec['info_erro']:.2f}\nLimite de Valores: {entrega:.2f}")
    

        case 5:
            # teste
            # print("Hello")

#-----------------------------------

if __name__ == "__main__":
    main()