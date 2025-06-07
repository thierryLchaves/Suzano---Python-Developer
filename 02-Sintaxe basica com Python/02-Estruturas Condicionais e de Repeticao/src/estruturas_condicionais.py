MAIOR_IDADE = 18
IDADE_ESPECIAL = 1717

idade = int(input("Informe sua idade "))

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CHN")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CHN")
else:
    print("Ainda não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CHN")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Ainda não pode tirar a CNH")