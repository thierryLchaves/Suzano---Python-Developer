class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):

        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p2 = Pessoa.criar_de_data_nascimento(1996, 1, 26, "Thierry")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
