# Tipos de Dados 
## Sumário 
  - [Tipos de dados](#1-tipos-de-dados)
  - [Modo Interativo](#2-modo-interativo)
  - [Variáveis e constantes](#3-variáveis-e-constantes)
  - [Conversão de tipos ](#4-conversão-de-tipos)
  - [Funções de entrada e saída](#5-funções-de-entrada-e-saída)

## 1. Tipos de dados  

### O que são tipos?
#### Por que usamos tipos?
Os tipos servem para definir as caracteristicas e comportamentos de um valor (objeto) para o interpretador.  
por exemplo:
Com esse tipo eu sou capaz de realizar operações matemáticas. Esse tipo para ser armazenado em memória irá consumir 24 bytes.

**Tipos em python**  
Os tipos built-in são:
| | |
| --- | --- |
| **`Texto`**| **`str`** |
| `Númerico` | int, floar, complex |
| `Sequencia` | list, tuple, range |
| `Mapa` | dict |
| `Coleção` | set, fronzenset |
| `Boleano` | bool |
| `Binário` | bytes, bytearray, memoryview |
---
### Tipos Númericos
**Números Inteiros**  
Números inteiros são representados pela classe int e possuem precisão ilimitada. São exemplos válidos de números inteiros:  
1,10,100, -1, -10, -100 .... 99001823  

**Números de ponto flutuante**  
Os números de ponto flutuante são usados para representar os números racionais e sua implementação é feita pela classe ***float***. São exemplos válidos de números de ponto flutuante:   
1.5, -10.543,0.76 .... 999278.002  

--- 
### Booleanos s String  
**Booleanos**  
é usado para representar verdadeiro ou falso, e é implementado pela classe bool. Em Python o tipo booleano é uma subclasse de int, uma vez que qualquer número diferente de 0 representa verdadeiro e 0 representa falso. São exemplos válidos de booleanos:  
True e False

**Strings**
Strings ou cadeia de caracteres são usadas para representar valores alganúmericos, em Python as strings são definidas utilizando a classe ***str***. São exemplos válidos de string:  
"Python", 'Python', """python""", '''Python''', "p"

--- 

## 2. Modo Interativo
### Objetivo Geral 
Como usar o modo interativo do interpretador Python  

#### Usando o modo interativo  
O interpretador Python pode executar em modo que possibilite o desenvolvedor a escrever código, e ver o resultado na hora. 
Para iniciar o modo interativo existem duas formas de iniciar o modo interativo, chamando apenas o interpretador `(python)` ou executando o script com a flag -i
```
(python -i app.py)
```  
#### Funções dir e help
**dir**  
Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto. Exemplo:  
```
dir()
dir(100)
```
**help**
Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável. Exemplo: 
```
help()
help(100)
```
#### Links Uteis
- [Trilha git](https://github.com/digitalinnovationone/trilha-python-dio)
- [Referências](https://wiki.python.org.br/ModoInterativo)

--- 

## 3. Variáveis e constantes  
### Objetivo Geral 
Entender o que são e como utilizar variáveis e constantes.  
#### O que são variáveis e constantes 
**Variáveis**  
Em lingaguem de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer como o mesmo durante a execução do programa.  
```
age = 29 
name = 'Thierry'
print(F'Meu nome é {name} e eu tenho {age} ano(s) de idade')
>> Meu nome é Thierry e eu tenho 23 anos de idade. 

age,name = (23,'thierry')
print(F'Meu nome é {name} e eu tenho {age} ano(s) de idade')
>> Meu nome é Thierry e eu tenho 23 anos de idade. 
```
**Alterando os valores**  
Perceba que não precisamos definir o tipo de dados da variável, o python faz isso automaticamente para nós. Por isso não podemos simplesmente criar uma variável sem atribuir um valor. Para alterar o valor da variável basta fazer um atribuição de um novo valor:

**Constantes**
Assim como variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce como um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.  
`Python não tem constantes`  
Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens por exemplo: *Java* *e* *C* utilizamos final e const, respectivamente para declarar uma constante. 
Em python usamos a convenção que diz ao progrmador que a variável é uma constante. Para fazer isso, você dever criar a variável com o nome todo em letras maíusculas:
```
ABS_PATH = '/home/tlchaves/Documents/python_course/'
DEBUG = True
STATES = [
  'MG', 
  'RJ', 
  'SP',
]
AMOUNT = 29.5
```  

#### Boas práticas. 
- Padrão de nomes deve ser *snake case*
- Escolher nomes sugestivos. 
- Nome de constantes todo em maiúsculo.

--- 

## 4. Conversão de tipos 
### Objetivos Geral 
Aprender a converter os tipos das variáveis.  

#### Convertendo tipos
Em alguns momentos é necessário ou será necessário converter o tipo de variável para manipular de forma diferente. Por exemplo:  
Variáveis do tipo *string*, que armazenam números e precisamos fazer alguma operação matemática com esse valor. 
**INTEIRO PARA FLOAT**  
```
preco = 100
print(preco) 
>> 100
preco = float(preco)
print(preco)
>> 100.0
preco = 10 /2 
print(preco)
>> 5.0
```  
**FLOAT PARA INTEIRO**  
```
preco = 10.30
print(preco)
>> 10.3
preco = int(preco)
print(preco)
>>10
```
**Conversão Por Divisão**  
```
preco = 10
print(preco)
>> 10
print(preco/2)
>>5.0
print(preco // 2) # Utilizando a divisão de um número inteiro utilizando 2 / ele preserva como inteiro 
>> 5
```
**Numérico Para String**  
```  
preco = 10.50
idade = 28

print(str(preco))
>> 10.50

print(str(idade))
>>28

texto = f"idade {idade} preço {preco}"
print(texto)
>> idade 28 preço 10.5
```
**String Para Numéro**  
```  
preco = "10.50"
idade = "28"
print(float(preco))
>>10.50
print(int(idade))
>> 28
```  
**Erro de conversão**  
```
preco = "python"
print(float(preco))  
>> Traceback (most recent call last):
  File "main.py", line 3, in <module>
  print(float(preco))  
ValueError: cloud not convert string to float: 'python'

```
---

## 5. Funções de entrada e saída
### Objetivo Geral  
Aprender como recber e exibir informações para o usuário.  

#### Lendo valores com a função input
A função builtin input é utilizada quando queremos ler dados da entrada padrão *(teclado)*. Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão *(tela)*. A função lê a entrada, converte para string e retorna o valor. 
```
nome = input("Informe o seu nome: ")
>>> informe o seu nome : |
```
#### Exibindo valores com a função print
A função builtin print é utilizada quando queremos exibir dados na saída padrão *(tela)*. Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais *(sep, end, file e flush)*, Todos os objetos são convertidos para string, separados por sep e terminados po end. A string final é exibida para o usuário. 
```
nome = "Thierry"
sobrenome = "Chaves"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")
>>Thierry Chaves
>>Thierry Chaves ...
>>Thierry#Chaves
```
### Links Uteis
- [Trilha no git](https://github.com/digitalinnovationone/trilha-python-dio)
- [Documentação input](https://doc.python.org/3/library/functions.html#input)
- [Documentação print](https://doc.python.org/3/library/functions.html#print) 
---
As respostas da aula 2 estão [aqui](IMGS)

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
Titulo: Tipos de dados 

Autor: Thierry Lucas Chaves  

Data criacao: 2025-05-23  

Data modificacao: 2025-05-24  

Versao: 1.0  
---
