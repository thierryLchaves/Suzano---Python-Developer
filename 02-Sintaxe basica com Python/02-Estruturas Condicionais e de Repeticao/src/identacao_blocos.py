
def sacar(valor: float):
    saldo = 500
    if saldo >= valor:
        print("valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500

    saldo += valor


sacar(1000)
depositar(100)