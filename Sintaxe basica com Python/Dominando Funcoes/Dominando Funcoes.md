# Dominando Funcoes
## Sumário 
- [Funções - Parte 1](#1-funções-pate-1)
- [Funções - Parte 2](#2-funções-pate-2)
---
## 1. Funções Pate 1 
### Objetivo Geral 
Entender como funcionam as funções em Python. 
#### Estudo aprofundado sobre funções 
**O que são funções?**  
Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada.  
```
def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem2(nome = "Guilherme")
exibir_mensagem3()
exibir_mensagem3(nome = "Chappie")
```  
**Retornando valores**  
Para retornar um valor, utilizamos a palavra reservada *return*. Toda função Python retorna *None* por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor. 
```
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1

    return antecessor, sucessor 

calcular_total([10,20,34]) #64
retorna_antecessor_e_sucessor(10) # (9,11 )
```  
**Argumentos nomeados**  
Funções tambpem podem ser chamadas usando argumentos nomeados da forma chave=valor.
```
def salvar_carro(marca,modelo, ano, placa):
    #  salava carro no banco de dados..
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"})

# Carro inserido com sucesso ! Fiat / Palio / 19999/ ABC-1234
```  
**Args e kwargs**  
Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.  
```
def exibir_poema(data_externo, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n\{meta_dados}"
    print(mensagem )

exibir_poema("Sexta-feira, 26 de agosto de 2025"","Zen of Python","Beautiful is better than ugly.",autor="Tim paters",ano=1999)
```
---
## 2. Funções Pate 2 
### Parâmetros Especiais
Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. Para melhor legibilidade e desempenho, faz sentido restriir a maneira pelo qual argumentos posasam ser passados, assim um desenvolvedor precisa apenas olhar para definição da função para determinar se os itens são passados **por posição, por posição e nome, ou por nome.**  

| | | | | |
| -- | -- | -- | -- | -- |
| def f | (pos1, pos2, /,| pos_or_kwd, | *, | kwd1, kwd2): |
| | ! | Posistional or keyword | | ! |
| | ! | | | --Keyword only |
| | --Positional only |  

<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: center;">
    <img src="imgs\image.png">
    </td>
</tr>
</table>


**Positional only**
```
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC -1234", marca="Fiat", 
motor="1.0", combustivel="Gasolina") # inválido

```

**Keyword only**
```
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC -1234", marca="Fiat", 
motor="1.0", combustivel="Gasolina") # válido

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

```

**Keyword and positional only**
```
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

```  
### Objetos de primeira classe 
Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados (lista, tuplas, dicionários, etc) e usar como valor de retorno para uma função(closures).

```
def somar(a,b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20
```
### Escopo local e escopo global 
Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais utilizamos a palavra-chave **global**, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global. Essa **Não é uma boa prática e deve ser evitada**  
```
salario = 2000

def salario_bonus(bonus):
    global salario 
    salario += bonus
    return salario 

salario_bonus(500) # 2500
``` 
--- 

### Links Uteis
- [Trilha no git](https://github.com/digitalinnovationone/trilha-python-dio)

---
As respostas da aula 6 estão [aqui](IMGS)

<table style="text-align: center; width: 100%;"> l
<caption><b>Skls do projeto </b></caption>
<tr>
    <td style="text-align: center;">
    <img alt="Markdown" src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"/>
    </td>
    <td style="text-align: center;">
    <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    </td>
    <td style="text-align: center;">
    <img alt="VSCode" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </td>
<tr> 
</table>

---
Titulo: Dominando Funcoes 

Autor: Thierry Lucas chaves

Data criacao: 26/05/2025

Data modificacao: 28/05/2025

Versao: 1.0  
---