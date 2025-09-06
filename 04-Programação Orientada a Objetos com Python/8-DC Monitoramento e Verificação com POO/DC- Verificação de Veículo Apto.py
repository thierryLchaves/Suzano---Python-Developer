class Carro:
    @staticmethod
    def verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual):

        idade_carro = ano_atual - ano_fabricacao
        if idade_carro <= 10:
            return f"{modelo}: Apto"
        else:
            return f"{modelo}: Nao apto"


def main():

    modelo = input()
    ano_fabricacao = int(input())
    ano_atual = int(input())

    resultado = Carro.verificar_aptidao_carro(
        modelo=modelo, ano_fabricacao=ano_fabricacao, ano_atual=ano_atual
    )

    print(resultado)


if __name__ == "__main__":
    main()
