class Estudate:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero 

    def __str__(self):
        return f"{self.nome} ({self.nome}) - {self.numero}"
    
thy = Estudate("Thierry",56451)
ty = Estudate("Tyara",17323)
