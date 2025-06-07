class Animal:
    
    def __init__(self,nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self,cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
       

class Ave(Animal):
    def __init__(self,cor_do_bico,**kw):
        self.cor_do_bico = cor_do_bico
        super().__init__(**kw) 
    
class Gato(Mamifero):
    pass


class FalarMixin:
    def falar(self):
        return ("Oi estou falando")

class Ornitorrinco(Mamifero,Ave,FalarMixin):
    def __init__(self, cor_do_bico,cor_pelo,nro_patas):
        # print(Ornitorrinco.__mro__)
        # print(Ornitorrinco.mro())

        super().__init__(cor_pelo = cor_pelo, cor_do_bico = cor_do_bico,nro_patas = nro_patas)

# gato = Gato(nro_patas=4,cor_pelo='preto')
# print(gato)

ornitorico = Ornitorrinco(nro_patas=2,cor_pelo='verde',cor_do_bico='laranja')
print(ornitorico.falar())