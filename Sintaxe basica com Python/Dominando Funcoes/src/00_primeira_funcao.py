def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem2(nome = "Thierry")
exibir_mensagem2("Lucas")
exibir_mensagem3()
exibir_mensagem3(nome = "Chappie")