import logging
logging.basicConfig(filename='sist_confg.log', level=logging.WARN)


try:
    print("Teste de divisão\n\n")
    raio = -1/0
    print(f"{raio}")
    assert raio >=0, "O raio não existe Negativo"
    print("\n\ndivisão concluida")
except ZeroDivisionError as e:
    print(f"Tipo: {type(e)}")
    print(f"Arg: {e.args}")
    print(f"Mensagem: {str(e)}")
    
    
    
    logging.exception("Falha critica de divisão")
    logging.fatal("fatal work")
    logging.error("Erro de trabalho")