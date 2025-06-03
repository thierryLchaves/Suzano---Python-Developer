nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 48.435
dados = {"nome": "Guilherme", "idade":28}

print("Nome: %s idade: %d" %(nome,idade))

print("Nome: {} idade: {}".format(nome,idade)) 

print("Nome: {0} idade: {1}".format(nome,idade))
 
print("Nome: {0} idade: {1} nome {0} {0}".format(nome,idade))
 
print("Nome: {nome} idade: {idade}".format(nome=nome,idade=idade))
 
print("Nome: {name} idade: {age}".format(age=idade, name=nome))
 
print("Nome: {nome} idade: {idade}".format(**dados))

print(f"Nome {nome}, idade {idade}")
print(f"Nome {nome}, idade {idade}, Saldo: {saldo:.2f}")
print(f"Nome {nome}, idade {idade}, Saldo: {saldo:10.2f}")