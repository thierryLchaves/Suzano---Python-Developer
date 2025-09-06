# DC- Monitoramento de Bicicletas

## Princípios Básicos 
__Descrição__   
Um sistema de monitoramento de bicicletas compartilhadas precisa calcular a distância máxima que cada bicicleta pode percorrer, com base no nível atual de bateria.  
Cada 1% de bateria permite percorrer 0,5 km. Neste desafio, você deve utilizar os conceitos de Programação Orientada a Objetos (POO) para modelar a bicicleta.  
Crie uma classe que contenha os atributos necessários e um método para calcular a distância estimada.

__Entrada__  
A entrada deve conter:  
- O nome do modelo da bicicleta (String).
- O nível de bateria (int).

__Saída__  
Deverá retornar uma mensagem com o modelo da bicicleta e a distância máxima estimada, formatada com uma casa decimal.  
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
        BikeX </br>
        80
    </td>
    <td style="text-align: center;">
       BikeX: Distancia estimada = 40.0 km
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        UrbanRide </br>
        50
    </td>
    <td style="text-align: center;">
        UrbanRide: Distancia estimada = 25.0 km
    </td>
<tr> 
    <td style="text-align: center;">
        EcoBike </br>
        30
    </td>
    <td style="text-align: center;">
       EcoBike: Distancia estimada = 15.0 km
    </td>
    
<tr> 
</table>

__Atenção:__  É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

[Código](https://github.com/thierryLchaves/Suzano---Python-Developer/blob/fd9b021e6c898a1d1a61953e0c3a741a25a0f34d/04-Programa%C3%A7%C3%A3o%20Orientada%20a%20Objetos%20com%20Python/8-DC%20Monitoramento%20e%20Verifica%C3%A7%C3%A3o%20com%20POO/DC-%20Monitoramento%20de%20Bicicletas.py)