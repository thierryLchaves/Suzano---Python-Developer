salario = 2000

def salario_bonus(bonus):
    global salario 
    salario += bonus
    return salario 

salario_bonus(500) # 2500



def lista_exemplo_errado(lista):
    lista_aux = lista.copy(2)
    lista_aux.append(2)
    print(f"Lista aux = {lista_aux}")


lista = [1]

lista_exemplo_errado(lista)
print(lista)