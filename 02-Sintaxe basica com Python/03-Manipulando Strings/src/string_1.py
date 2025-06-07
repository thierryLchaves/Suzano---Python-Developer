nome = "Thierry"

print(nome.lower())
print(nome.upper())
print(nome.title())

texto ="    olá mundo     "
print(texto)
print(texto.strip() + ".")
print(texto.lstrip()+ ".")
print(texto.rstrip()+ ".")

menu = "Python"

print("####Python####")
print(menu.center(14))
print(menu.center(14,"#"))
print("P-y-t-h-o-n")
print("-".join(menu))