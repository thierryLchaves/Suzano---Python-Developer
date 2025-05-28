menu = """

[d] Depositar 
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

def sacar_dinheiro(valor_saque, saldo,limite, limite_qt_saque = LIMITE_SAQUE):
    qt_saque = 0 
    dinheiro_conta = 0 

    if qt_saque <= limite_qt_saque:
        qt_saque += 1

        if valor_saque > saldo:
            dinheiro_conta = f"Não foi possível sacar o dinheiro informado pois não tem saldo suficiente em conta"
        elif valor_saque <= dinheiro_conta  and valor_saque > limite:
            dinheiro_conta = f"Não foi possivel sacar a quantidade solicitada pois o valor exede o limite de {limite}"
        elif valor_saque <= saldo and valor_saque <= limite:
             dinheiro_conta = (saldo - valor_saque)

    else:
        print(f"Valor de {LIMITE_SAQUE} saque diarios excedidos")
    
    return dinheiro_conta        

for limiter  in range(3):
    result = sacar_dinheiro(valor_saque=500,saldo=saldo,limite=limite)
    print(result)
    limiter += 1
