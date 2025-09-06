import logging
import os
import traceback
from datetime import date
from pathlib import Path

ROOT_PATH = Path(__file__).parent


def verifica_existencia(dir):
    """Verifica a extistência de um arquivo em um diretório
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


def exibite_lista(subdir, ie_opcao):
    """Essa função é utilizada para retornar em formato de lista, tanto os nomes dos subdiretórios
    existentes (pastas), quanto a sua posição em lista conforme estrutura padrão
    incializando da posição 0

    Args:
        subdir (list): Uma lista de strings contendo os caminhos completos das pastas.
        ie_opcao (number): Define o que será retornado. Pode ser 1 para "nomes",  2 para posições "posicoes"
        ou 0 para "ambos".

    Returns:
        list ou tuple: Dependendo do 'ie_opcao' especificado.
                       Retorna listas vazias se a lista de entrada estiver vazia.
    """
    lista_final = []
    numero_lista = []

    try:
        if not subdir:
            if ie_opcao == "1":
                return []
            elif ie_opcao == "2":
                return []
            elif ie_opcao == "0":
                logging.warning(
                    f"Tipo de retorno '{ie_opcao}' inválido. Retornando listas vazias."
                )
                return ([], [])

        for posicao, caminho_completo in enumerate(subdir):
            nome_final = os.path.basename(caminho_completo)
            lista_final.append(nome_final)
            numero_lista.append(posicao)

        if ie_opcao == "1":
            return sorted(lista_final)
        elif ie_opcao == "2":
            return sorted(numero_lista)
        elif ie_opcao == "0":
            return (lista_final, numero_lista)
        else:
            logging.error(
                f"Tipo de retorno '{ie_opcao}' não reconhecido. Retornando ambos por padrão."
            )
            return (lista_final, numero_lista)

    except Exception as e:
        logging.error(f"Erro ao processar detalhes das pastas: {e}")
        if ie_opcao == "1":
            return []
        elif ie_opcao == "2":
            return []
        else:
            return ([], [])


def list_diretorios(dir, pastas_ignoradas):
    """Listar as sub-pastas existentes dentro de um diretório
        passado no primeiro parâmetro, e como opção listar quais serão as subpastas ignoradas.
    Args:
        dir (str): deverá informar o aminho da pasta que contem sub-pastas
        pastas_ignoradas (str): deverá informar a lista das pastas que devem ser ignoradas.
        Essas deverão ser padrões pelo menos nessa versão

    Returns:
        list: Retorna a lista de diretórios encontrados.
    """
    if pastas_ignoradas is None:
        pastas_ignoradas = []

    sub_diretorios = []
    try:
        for item in os.listdir(dir):
            caminho_completo = os.path.join(dir, item)
            if os.path.isdir(caminho_completo) and item not in pastas_ignoradas:
                sub_diretorios.append(caminho_completo)
                sub_diretorios.extend(
                    list_diretorios(caminho_completo, pastas_ignoradas)
                )
    except Exception as e:
        logging.error(f"Aconteceu um erro pois {e}")
    return sub_diretorios


def cria_pasta(subdir, pastas_padroes):
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
                    caminho_novo_sub_diretorio = os.path.join(base_diretorio, nm_pasta)
                    arquivo_git = ".gitkeep"
                    if not os.path.exists(caminho_novo_sub_diretorio):
                        os.makedirs(caminho_novo_sub_diretorio)
                        if os.path.isdir(caminho_novo_sub_diretorio):
                            diretorio_arquivos_finais = os.path.join(
                                caminho_novo_sub_diretorio, arquivo_git
                            )
                            with open(diretorio_arquivos_finais, "w") as e:
                                e.write(arquivo_git)
    except Exception as e:
        logging.error(f"Não foi possível criar as pastas pois {e}")


def cria_arquivo(subdir, caminho_tamplate, nome_autor):
    """Essa função cria um arquivo no subdiretório existente na pasta raiz
       casso não queria utilizar a função de obtenção de lista devera passar o caminho da pasta absoluta
       o arquivo será criado em Markdown, com o nome da pasta passada no parâmetro, e o seu contéudo,
       terá como padrão o arquivo de template passado no segundo argumento.

    Args:
        subdir (str,list): deverá informar  o caminhos completos do diretórios a serem criados.
        caminho_tamplate (str): deverá informar  o caminho completo do arquivo de template.
        nome_autor (str): Será armazenado o nome inputado pelo usuário para substituição no arquivo base
    """
    with open(caminho_tamplate, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    try:
        if not subdir:
            return
        else:
            for nr_list, base_diretorio in enumerate(sorted(subdir)):
                nome_da_pasta = os.path.basename(base_diretorio)
                novo_numero = nr_list + 1
                nm_arquivo_pasta = f"{novo_numero} .{nome_da_pasta.split("-", 1)[1]}.md"

                diretorio_novo_arquivo = os.path.join(base_diretorio, nm_arquivo_pasta)
                dados_template = {
                    "titulo_arquivo": nm_arquivo_pasta.replace(".md", ""),
                    "nome_autor": nome_autor,
                    "x": novo_numero,
                    "data": date.today().strftime("%d/%m/%Y"),
                }
                conteudo_final = conteudo.format(**dados_template)
                with open(
                    diretorio_novo_arquivo, "w", encoding="utf-8"
                ) as novo_arquivo:
                    if dados_template and verifica_existencia(diretorio_novo_arquivo):
                        novo_arquivo.write(conteudo_final)
                        logging.info(
                            f"Foi criado um nove arquivo {nm_arquivo_pasta}, corretamente em {base_diretorio}"
                        )
                    else:
                        logging.error("Não foi possível criar o arquivo desejado")
    except Exception as e:
        logging.error(
            f"Não foi possível executar o código devido a um erro inesperado: {e}"
        )
        logging.error("Detalhes completos do erro (traceback):")
        traceback.print_exc()  # Isso imprimirá o traceback completo


def move_arquivo(subdir_alvo, subdir_destino):
    """Essa função tem como objetivo de cópiar os códigos que foram clonados
    para suas respectivas pastas dos módulos de uma trilha, deverá ser executado
    até o momento para realizar o "copy" de todos os arquivos da pasta quando necessário

    Args:
        subdir_alvo (str): Informa o caminho da pasta que contem os códigos
        subdir_destino (str): informa o caminho da pasta que recebera esses arquivos.
    """
    try:
        for iten_alvo in os.listdir(subdir_alvo):

            dir_alvo = os.path.join(subdir_alvo, iten_alvo)
            nome_dir = os.path.basename(dir_alvo)

            with open(dir_alvo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()

            dir_destino = os.path.join(subdir_destino, nome_dir)
            with open(dir_destino, "w", encoding="utf-8") as novo_arquivo:
                novo_arquivo.write(conteudo)

    except Exception as erro:
        logging.error(f"Erro de iteração devido {erro}")


if __name__ == "__main__":
    PASTAS_PADRAO = ["src", "imgs"]

    msg_sub_pasta = "informe o  nome do caminho absoluto onde será criado os arquivos: "
    nm_sub_pasta = input(msg_sub_pasta)
    path_template = ROOT_PATH / "template_padrao.md"
    nome_autor = input("informe o  nome do autor que ficara nos arquivos: ")
    sub_diretorios = list_diretorios(nm_sub_pasta, PASTAS_PADRAO)
    cria_arquivo(sub_diretorios, path_template, nome_autor)
    cria_pasta(sub_diretorios, PASTAS_PADRAO)
