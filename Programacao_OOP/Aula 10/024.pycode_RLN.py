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
    
    