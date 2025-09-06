class BicicletaInterna:
    def __init__(self, modelo, nivel_bateria):

        self.modelo = modelo
        self.nivel_bateria = nivel_bateria

    def calcular_distancia(self):
        dist = self.nivel_bateria * 0.5
        return dist

    def obter_mensagem(self):
        distancia = self.calcular_distancia()
        return f"{self.modelo}: Distancia estimada = {distancia} km"


def main():

    modelo = input()

    nivel_str = input()
    nivel_bateria = int(nivel_str)

    bicicleta = BicicletaInterna(modelo=modelo, nivel_bateria=nivel_bateria)
    print(bicicleta.obter_mensagem())


if __name__ == "__main__":
    main()
