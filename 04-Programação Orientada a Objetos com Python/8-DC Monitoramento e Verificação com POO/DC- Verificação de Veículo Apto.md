# DC-Verificação de Veículo Apto

## Princípios Básicos 
__Descrição__   
Um aplicativo de monitoramento de carros precisa verificar se um carro está apto para rodar com base no ano de fabricação e no ano atual.Um carro é considerado apto se tiver até 10 anos de uso.  
Para resolver este desafio, você deve utilizar conceitos de Programação Orientada a Objetos (POO), como a definição de métodos estáticos, para realizar a verificação da aptidão do carro sem a necessidade de instanciar objetos.  
A aplicação de POO deve ser utilizada para organizar a lógica de verificação do carro e para retornar o resultado da aptidão de forma estruturada.

__Entrada__  
A entrada deve conter:  
- O modelo do carro (String).
- O ano de fabricação (int).
- O ano atual (int).

__Saída__  
Deverá retornar uma mensagem indicando se o carro está apto ou não.
- Retorno em formato de mensagem.

__Exemplos__  
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

<table style="text-align: center; width: 100%;"> 
<caption><b>Exemplos de Saída & Entrada </b></caption>
<tr> 
    <td style="text-align: center;">
        Entrada
    </td>
     <td style="text-align: center;">
        Saída
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        Civic </br>
        2015 </br>
        2015
    </td>
    <td style="text-align: center;">
        Civic: Apto
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        Gol </br>
        2012 </br>
        2025
    </td>
    <td style="text-align: center;">
        Gol: Nao apto
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        Corolla </br>
        2018 </br>
        2025
    </td>
    <td style="text-align: center;">
        Corolla: Apto
    </td>
<tr> 
</table>

__Atenção:__  É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

[Código](DC-Sistema%20de%20Pedidos%20de%20Restaurante.py)