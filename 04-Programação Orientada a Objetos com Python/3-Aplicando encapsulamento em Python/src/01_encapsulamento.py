class Conta:

    def __init__(self,nr_agencia,saldo=0):
      self._saldo = saldo 
      self.nr_agencia = nr_agencia

    def depositar(self,valor):
        #...
        self._saldo += valor


    def sacar(self,valor):
        #...
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
    
conta = Conta('0001',100)
# conta.depositar(100)
print(conta._saldo)
print(conta.nr_agencia)
print(conta.mostrar_saldo())