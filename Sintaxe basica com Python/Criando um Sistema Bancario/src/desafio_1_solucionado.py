# menu = """

# [d] Depositar 
# [s] Sacar 
# [e] Extrato
# [q] Sair

# => """

# saldo = 1500
# limite = 500
# extrato = ""
# numero_saques = 0
# LIMITE_SAQUE = 3



# while True:
#     opcao = input(menu)

#     if opcao == "d":
        
#         valor = float(input("Informe o valor do depósito: "))

#         if valor > 0:
#             saldo += valor
#             extrato += f"Depísto: R$ {valor:.2F}\n"

#         else:
#             print("Operação falhou! o valor informado é invalido")

#     elif opcao == "s":

#         valor = float(input("Informe o valor do saque: "))

#         excedeu_saldo = valor > saldo
        
#         excedeu_limite = valor > limite

#         excedeu_saques = numero_saques >= LIMITE_SAQUE

#         if excedeu_saldo:
            
#             print("Operação falhou! você não tem saldo suficiente. ")

#         elif excedeu_limite:
            
#             print("Operação falhou! o valor do saque excede o limite.  ")

#         elif excedeu_saques:

#             print("Operação falhou! Número máximo de saque excedido. ")

#         elif valor >0:
#             saldo -= valor
#             extrato += f"Saque: R$ {valor:.2f}\n"
#             numero_saques += 1

#         else:
#             print("Operação falhou! O valor informado é inválido. ")
    

#     elif opcao == "e":
#         print("EXTRATO".center(18,"#"))
#         print("Não foram realizadas movimentações." if not extrato else extrato)
#         print(f"\nSaldo: R$ {saldo:.2f}")
#         print("#".center(18,"#"))

#     elif opcao == "q":
#         break
#     else:
#         print("Opção inválida, por favor selecione novamente a operação.")



def criar_usuario(nome, dt_nascimento, cpf, endereco_lista):

    if len(endereco_lista) == 5:
        logradouro, numero, bairro, cidade, estado = endereco_lista
    else:
        print("Aviso: A lista de endereço não contém o número esperado de elementos. Usando valores vazios.")
        logradouro, numero, bairro, cidade, estado = "", "", "", "", ""


    usuario = {
        "nome": nome,
        "data_nascimento": dt_nascimento,
        "cpf": cpf,
        "endereco": { # Dicionário aninhado para o endereço
            "logradouro": logradouro,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }
    }
    return usuario

def verifica_cpf (cpf,usuarios):
    for usuario in usuarios:
        if usuarios["cpf"] == cpf:
            return True
    return False 
#
usuarios = []
contador = 0

# O loop continuará enquanto o contador for menor que 1 (ou seja, uma vez).
# Se você quiser cadastrar mais de um usuário, altere '1' para o número desejado.
while contador < 1:
    print(f"\n--- Cadastro do Usuário {contador + 1} ---")
    nm_usario = input("Digite o nome do usuário: ")
    dt_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
    cpf = input("Digite o CPF: ")

    # Coleta os componentes do endereço separadamente e os armazena em uma lista
    print("\n--- Digite os componentes do endereço ---")
    logradouro_input = input("Logradouro (rua, avenida, etc.): ")
    numero_input = input("Número: ")
    bairro_input = input("Bairro: ")
    cidade_input = input("Cidade: ")
    estado_input = input("Estado (UF): ")

    # Cria a lista de endereço para passar para a função
    endereco_para_funcao = [
        logradouro_input,
        numero_input,
        bairro_input,
        cidade_input,
        estado_input
    ]

    # Chama a função criar_usuario passando a lista de endereço
    novo_usuario = criar_usuario(
        nome=nm_usario,
        dt_nascimento=dt_nascimento,
        cpf=cpf,
        endereco_lista=endereco_para_funcao # Passando a lista como parâmetro
    )
    
    # Adiciona o dicionário do novo usuário à lista de usuários.
    usuarios.append(novo_usuario)
    
    # Incrementa o contador para controlar o número de usuários cadastrados.
    contador += 1

# Após o loop, imprime a lista completa de usuários cadastrados.
# Cada item na lista é um dicionário contendo as informações de um usuário.
print("\n--- Usuários Cadastrados ---")
for i, usuario in enumerate(usuarios):
    print(f"Usuário {i + 1}:")
    print(f"  Nome: {usuario['nome']}")
    print(f"  Data de Nascimento: {usuario['data_nascimento']}")
    print(f"  CPF: {usuario['cpf']}")
    # Acessando os componentes do endereço aninhado
    print(f"  Endereço:")
    print(f"    Logradouro: {usuario['endereco']['logradouro']}")
    print(f"    Número: {usuario['endereco']['numero']}")
    print(f"    Bairro: {usuario['endereco']['bairro']}")
    print(f"    Cidade: {usuario['endereco']['cidade']}")
    print(f"    Estado: {usuario['endereco']['estado']}")
    print("-" * 30)