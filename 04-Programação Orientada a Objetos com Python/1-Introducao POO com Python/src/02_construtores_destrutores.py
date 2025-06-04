class Cachorro:
    def __init__(self,nome,cor,acordado = True):
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("Aauauauau")
    
    def __del__(self):
        print("removendo a instância da classe ")



     
# def criar_cachorro():
#     c = Cachorro("Chappie","amarelo")
#     print(c.nome)

# criar_cachorro()

 
c = Cachorro("Chappie","amarelo")
c.falar()
print("Olá mundo!")
del c
print("Olá mundo!")
print("Olá mundo!")
print("Olá mundo!")

