# Notações gerais 

Neste repositório será adotada toda documentação em Markdown, sendo asssim seguirei algumas diretrizes e comportamentos padrões

## Diretrizes
- ### 1. Do repositório
    O repositório está estruturado em pastas, onde cada uma das aulas acessadas/aprendidas, estão em suas respectiva pasta. 
- ### 2. Do documento 
    O documento contendo a estrutura geral da aula será em formato `.Md(Markdown)`, e seguira a premissa de CamelCase em seu nome.  
    - #### 2.1. Das pastas
         As pasta com os nomes da Materias serão iguais as aprensentadas no curso, porém sem acentuação 
    - #### 2.2. Do Readme
        Ao ser concluida uma nova aula deverá ser preenchido o [Check Box de conclusão](#3-lista-de-conclusão-de-aulas) informando que a aulas foi realizada.
    - ### 2.3.  Estrutura padrão de sub-diretório
        Em toda pasta deverão conter no mínimo **3**(três) outros sub-diretórios  
        - #### 2.3.1. Diretório de Imagens
            `**Diretório de Imagens**`: Este diretório sempre será nomeado de `imgs`, e nele será armazenado os prints utilizados no documento.   
        - #### 2.3.2. Diretório de Códigos
            `**Diretório de código**`:  Este diretório sempre será nomeado de `src`, neste diretório será armazenado os exemplos de códigos feitos nas aulas e seguira a recomendação as boas práticas de  nomeação (sem upper case, com _ entre os nomes, e descrição curta do objetivo do código) 
        - #### 2.3.3. Diretório de Dados
            `**Diretório de dados*`: Este diretório sempre será nomeado de `db`, e nele será armazenado os dados complementares a serem usados (arquivos pdf etc..)  
### 2.4 Estrutura de rodapé
    Em todo arquivo deverá conter em seu rodapé a seguinte estrutura 
   ```
    <table style="text-align: center; width: 100%;"> 
    <caption><b>Skls do projeto </b></caption>
    <tr>
        <td style="text-align: center;">
        <img alt="Skil utilizada" src="buscar estilo em: https://github.com/Ileriayo/markdown-badges"/>
        </td>
    </tr>
    <tr> 
       <td style="text-align: center; width: 100%;">
       <b>Metadados</b>
       </td>
    </tr>
    </table>
    ---
    titulo: "Nome do documentos"
    autor: "Thierry Lucas Chaves"
    data_criacao: "DD-MM-AAAA"
    data_modificacao: "DD-MM-AAAA"
    versao: "1.0"
    ---
```
### 3. Lista de conclusão de aulas
- [X]  <b> Introdução ao Ambiente Python e Projetos colaborativos  </b>
    - [X] Introdução ao Python com a Suzano 
    - [X] Ambiente de Desenvolvimento e Primeiros Passos com Python 
    - [X] Conhecendo a Linguagem de Programação Python 
    - [X] Versionamento de Código com Git e Github
    - [X] Desafios de Projetos: Crie um Portfólio Vencedor 
    - [x] Contribuindo em um projeto Open Source no GitHUB
- [ ] <b> Sintaxe Básico com Python </b>
    - [X] Tipos de Operadores com Python 
    - [X] Estrutura condicionais e de repetição em Python 
    - [X] Manipulando Strings com Python 
    - [x] Dominando Funções Python 
    - [ ] Criando um Sistema Bancário com Python 
- [ ] <b>Trabalhando com Coleções em Python </b>
    - [ ] Trabalhando com Listas em Python 
    - [ ] Conhecendo tuplas em Python 
    - [ ] Exemplorando conjuntos em Python 
    - [ ] Aprendendo a utilizar Dicionários em Python 
    - [ ] Lidando com Data, Hora e Fuso Horário em Python 
    - [ ] Otimizando Sistema Báncário com funções Python 
    - [X] Desafios de código: Aperfeiçoe sua lógica e Pensamento computacional 
    - [ ] Gestão e Controle de transações Bancárias. 
- [ ] <b>Programação Orientada a Objetos com Python </b>
    - [ ] Introdução à Porgramação Orientada a Objetos (POO) com Python 
    - [ ] Aprenda o conceito de Herança com Python 
    - [ ] Aplicando Encapsulamento em Python 
    - [ ] Conhecendo Polimorfismo em Python 
    - [ ] Interfaces e Classes Abstratas com Python 
    - [ ] Modelando o Sistema Báncário em POO com Python 
    - [ ] Criando um Pacote de Processamento de Imagens com Python 
    - [ ] Fundamentos de POO em sistemas bancários 
- [ ] <b>Produtividade com Microsoft Copilot Studio </b>
    - [ ] Conhecendo o Microfost Copilot Studio 
    - [ ] Trabalhando com Ambientes no Microfost Copilot Studio
    - [ ] Criando seu primeiro copiloto no Microfost Copilot Studio
    - [ ] Introdução aos tópicos no Microfost Copilot Studio
    - [ ] Ramificando um tópico no Microfost Copilot Studio 
    - [ ] Trabalhando com tópicos de Fallback do sistema no Microfost Copilot Studio
    - [ ] Introdução a Entidades e variáveis no Microfost Copilot Studio
    - [ ] Criando respostas generativas com IA no Microfost Copilot Studio
    - [ ] Criando um copiloto com fluxo de conversa personalizado no Microfost Copilot Studio
- [ ] <b>Integrando com Serviços de IA</b>
    - [ ] Fundamentos da IA Generativa
    - [ ] Conceitos Fundamentais de IA
    - [ ] Fundamentos do Aprendizado de Máquina
    - [ ] Conceitos de Processamento de Linguagem Natural 
    - [ ] Análise de Sentimentos com Language Studio no Azure IA
    - [ ] Trabalhando com Serviços Azure OpenAI


## Observações:
Para esse projeto foi criado o [arquivo de automação](automacao_estrutura_pasta/cria_lista.py), para facilitar a criação dos arquivos de notações que serão adotados nas aulas, bem como a estrutura padrão mencionada em [Estruturas de diretórios](#23--estrutura-padrão-de-sub-diretório) seguindo o mesmo padrão
ao executar o código o usuário deverá inserir os caminho absolutos da pasta que corresponde ao módulo caso necessário modificar o arquivo de [template](automacao_estrutura_pasta/template_padrao.md)

<table style="text-align: center; width: 100%;"> 
<caption><b>Skls do projeto </b></caption>
<tr>
    <td style="text-align: center;">
    <img alt="Markdown" src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"/>
    </td>
<tr> 
</table>
---
Titulo: Readme
Autor: Thierry Lucas Chaves  
Data criacao: 08-05-2025
Data modificacao: 28-05-2025
Versao: 1.0  
---
