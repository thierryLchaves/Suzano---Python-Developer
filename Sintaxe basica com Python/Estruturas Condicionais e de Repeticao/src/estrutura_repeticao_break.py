while  True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

for numero in range(100):

    if numero == 10:
        break

    print(numero)


for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero,end=" 10")

while True:

    numero = int(input("Informe um novo número: "))

    if numero % 2  == 0:
        continue

    if numero == 10:
        break

    print(numero)