# Estruturas Condicionais e de Repeticao
## Sumário 
- [Identação e blocos](#1-identação-e-blocos)
- [Estruturas condicionais](#2-estruturas-condicionais)
- [Estruturas de Repetição](#3-estruturas-de-repetição)
---
## 1. Identação e blocos
### Objetivo Geral 
Aprender como o interpretador Python utiliza a identação do código para delimitar os blocos de comandos. 
#### Identação e os blocos de comandos
Identar código é uma forma de mantar o código fonte mais legível e manutenível. Ms em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.  
**Bloco de comando**  
As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o início e fim do bloco. Em Java e C por exemplo, utilizamos chaves:  
```
void sacar(double valor) { // início do bloco do método 
  if (this.saldo >= valor){ // início do bloco do if
    this.saldo -= valor; 
  } // fim do bloco do if
} // fim do bloco do método
```
**Bloco em Java sem formatar**
```
void sacar(double valor) { // início do bloco do método
if (this.saldo >= valor){ // início do bloco do if
this.saldo -= valor; 
} // fim do bloco do if
} // fim do bloco do método
```
**Utilizando Espaços**  
Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco. 

```
def sacar(self,valor: float) -> Nome: # Início do bloco do método
    if self.saldo >= valor:
        self.saldo -= valor
    # fim do bloco do if 
# fim do bloco do método 
```
**Isso não funciona em Python**  
```
def sacar(self,valor: float) -> Nome: # Início do bloco do método
if self.saldo >= valor:
self.saldo -= valor
# fim do bloco do if 
# fim do bloco do método 
```
## 2. Estruturas condicionais
### Objetivo Geral 
O que são as estruturas condicionais e como utilizá-las 
#### if / if-else / elif 
A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.  
**IF**  
Para criar um estrutura condicional simples, composta por um único desvio, podemos utilizar a palavras reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.  
```
saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
  print("Realizando saque!")

if saldo < saque:
  print("Saldo insuficiente!")
```
**IF/ELSE**  
Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do else será executado.  
```
saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
  print("Realizando saque!")
else:
  print("Saldo insuficiente!")

```
**IF/ELIF/ELSE**  
Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavras reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código. 
```
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if  opcao == 1:
  valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
  print("Exibindo o extrato...")
else:
  sys.exit("Opção inválida!")
```

#### if aninhado 
#### if ternário
## 3. Estruturas de Repetição

tabela exemplo 
| | |
| -- | -- |
| nome | valor |

<div style="border-left: 4px solid red; background-color:rgb(22, 23, 24); padding: 10px;">
  <strong style="color: red;">Exemplo de alerta</strong>
  <p> Somente um exemplo.</p>
</div>

exemplo código 
```
print("Hello World!")
```
---

---
### Links Uteis
- [Trilha no git](https://github.com/digitalinnovationone/trilha-python-dio)
---
As respostas da aula 4 estão [aqui](IMGS)

<table style="text-align: center; width: 100%;"> 
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
Titulo: Estruturas Condicionais e de Repeticao 

Autor: Thierry Lucas chaves

Data criacao: 26/05/2025

Data modificacao: 26/05/2025

Versao: 1.0  
---