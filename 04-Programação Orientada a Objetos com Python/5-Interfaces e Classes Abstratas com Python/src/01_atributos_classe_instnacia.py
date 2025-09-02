class Estudate:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudate("Thierry", 1)
aluno_2 = Estudate("Tyara", 2)
mostrar_valores(aluno_1, aluno_2)


Estudate.escola = "Python"
aluno_3 = Estudate("Larissa", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
