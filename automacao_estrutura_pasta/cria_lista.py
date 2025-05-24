import os
import logging
from datetime import date 

def verifica_existencia(dir):
    """ Verifica a extistência de um arquivo em um diretório
        específico
    Args:
        dir (str): deverá informar o diretório completo do arquivo 
    Returns:
        Boleano: Retorna  true se existe o arquivo especifico no diretório se não retorna false
    """
    try:
        return os.path.exists(dir)
    except Exception as e:
        logging.error(f"Ocorreu um erro ao verificar o diretório devido ao erro \n {e}")

def list_diretorios(dir,pastas_ignoradas):
    """ Listar as sub-pastas existentes dentro de um diretório
        passado no primeiro parâmetro, e como opção listar quais serão as subpastas ignoradas. 
    Args:
        dir (str): deverá informar o aminho da pasta que contem sub-pastas
        pastas_ignoradas (str): deverá informar a lista das pastas que devem ser ignoradas, essas deverão ser padrões pelo menos nessa versão

    Returns:
        list: Retorna a lista de diretórios encontrados. 
    """
    if pastas_ignoradas is None:
        pastas_ignoradas = []

    sub_diretorios = []
    try:
        for item in os.listdir(dir):
            caminho_completo = os.path.join(dir,item)
            if os.path.isdir(caminho_completo) and item not in pastas_ignoradas:
                sub_diretorios.append(caminho_completo)
                sub_diretorios.extend(list_diretorios(caminho_completo,pastas_ignoradas))
    except Exception as e:
        logging.error(f"Aconteceu um erro pois {e}")
    return sub_diretorios

def cria_arquivo(subdir,caminho_tamplate,nome_autor):
    """Essa função cria um arquivo no subdiretório existente na pasta raiz
       casso não queria utilizar a função de obtenção de lista devera passar o caminho da pasta absoluta
       o arquivo será criado em Markdown, com o nome da pasta passada no parâmetro, e o seu contéudo, 
       terá como padrão o arquivo de template passado no segundo argumento. 

    Args:
        subdir (str,list): deverá informar  o caminhos completos do diretórios a serem criados. 
        caminho_tamplate (str): deverá informar  o caminho completo do arquivo de template.
        nome_autor (str): Será armazenado o nome inputado pelo usuário para substituição no arquivo base
    """
    with open(caminho_tamplate,'r',encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    try:
        if not subdir:
            return
        else:
            for base_diretorio in subdir:
                nm_arquivo_pasta = f"{os.path.basename(base_diretorio)}.md"
                diretorio_novo_arquivo = os.path.join(base_diretorio,nm_arquivo_pasta)
                dados_temlate = {
                    "titulo_arquivo" : nm_arquivo_pasta.replace(".md",""),
                    "nome_autor" : nome_autor,
                    "data" : date.today().strftime("%d/%m/%Y")
                }
                conteudo_final = conteudo.format(**dados_temlate)
                with open(diretorio_novo_arquivo,'w',encoding='utf-8') as novo_arquivo:
                    if dados_temlate and verifica_existencia(diretorio_novo_arquivo):
                        novo_arquivo.write(conteudo_final)
                        logging.info(f"Foi criado um nove arquivo {nm_arquivo_pasta}, corretamente em {base_diretorio}")
                    else:
                        logging.error(f"Não foi possível criar o arquivo desejado")     
    except Exception as e:
        logging.error(f"Não foi possivél executar o código pois {e}")

def cria_pasta(subdir,pastas_padroes):
    """Cria uma lista de subdiretórios no dentro do diretório passado no argumento, 
    devera conter uma lista de nomes de pastas que serão criadas no diretório em questão. 
    e também criar um arquivo gitkeep para manter a estruturação das pastas no git/github

    Args:
        subdir (str,list): deverá informar  o caminho da pasta raiz, subdiretórios a serem acessados
        pastas_padroes (list): deverá informar a lista com os nomes das pastas que serão criados
    """
    try:
        if not subdir:
            return
        else:
            for base_diretorio in subdir:
                for nm_pasta in pastas_padroes:
                    caminho_novo_sub_diretorio = os.path.join(base_diretorio,nm_pasta)
                    arquivo_git = ".gitkeep"
                    if not os.path.exists(caminho_novo_sub_diretorio):
                        os.makedirs(caminho_novo_sub_diretorio)
                        if os.path.isdir(caminho_novo_sub_diretorio):
                            diretorio_arquivos_finais = os.path.join(caminho_novo_sub_diretorio,arquivo_git)
                            with open(diretorio_arquivos_finais,'w') as e:
                                e.write(arquivo_git)
          

                 

    except Exception as e:
        logging.error(f"Não foi possível criar as pastas pois {e}")
    
if __name__ == '__main__':
    PASTAS_PADRAO = [
             "db",
             "src",
             "imgs"
    ]

    nm_sub_pasta = input("Digite o caminho completo do diretório/subdiretório: ")
    path_template = input("Digite o caminho completo do arquivo padrão: ")
    nome_autor = input("Digite o nome a ficar no arquivo: ")
    sub_diretorios = list_diretorios(nm_sub_pasta,PASTAS_PADRAO)
    cria_arquivo(sub_diretorios, path_template,nome_autor)
    cria_pasta(sub_diretorios,PASTAS_PADRAO)

#r'/home/tlchaves/Documentos/Estudos/DIO/Suzado_Bootcamp/Suzano---Python-Developer/Sintaxe basica com Python'
#r'/home/tlchaves/Documentos/Estudos/DIO/Suzado_Bootcamp/Suzano---Python-Developer/automacao_estrutura_pasta/template_padrao.md'