class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor
        self.marcha = 1


    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruummm...")

    def trocar_marcha(self,nro_marchar):
        print("Trocando marcha")

        def  _trocar_marcha(nro_marcha):
            if nro_marcha > self.marcha:
                print("Marcha trocada..")
            else:
                print("Não foi possível trocar de marchar..")

    # def __str__(self):
    #     return f"Bicicle: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"

# b1 = Bicicleta("Vermelha","Caloi",2002,600)

# b1.buzinar()
# b1.correr()
# b1.parar()

# print(b1.cor, b1.modelo,b1.ano, b1.valor)

b2 =  Bicicleta("Verde","Monark",2000,189)
b2.trocar_marcha()

# b2.buzinar() # Bicicleta.buzinar(b2)
# b2.get_cor()
print(b2)