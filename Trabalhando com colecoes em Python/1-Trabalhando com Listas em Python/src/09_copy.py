lista = [1, "Python", [40, 30, 20]]

ls = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(ls),id(lista))

ls[0] = 2 
print(ls)
print(lista)