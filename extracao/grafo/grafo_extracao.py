from extracao.ops.pandas.extracao_dados import read_csv, read_excel, read_parquet, read_json
from dagster import graph
from mcp_main import mcp

# Criando grafo de leitura de arquivo
@mcp.tool()
@graph
def read_file_graph(caminho: str, separador: str = ""):
    """
    Grafo Dagster (e ferramenta MCP) para orquestrar a leitura de arquivos de dados.
    
    Este grafo tenta decidir qual operação de leitura executar com base na extensão
    do arquivo fornecido no `caminho`.
    
    Parâmetros:
    - caminho (str): O caminho absoluto ou relativo para o arquivo de dados.
    - separador (str, opcional): Delimitador a ser usado caso o arquivo seja um CSV.
    
    Retorno:
    - string JSON estruturada contendo os dados do arquivo lido.
    """
    if caminho.endswith(".csv"):
        dados = read_csv(caminho, separador)
        return dados
    elif caminho.endswith(".xlsx"):
        dados = read_excel(caminho)
        return dados
    elif caminho.endswith(".parquet"):
        dados = read_parquet(caminho)
        return dados
    elif caminho.endswith(".json"):
        dados = read_json(caminho)
        return dados
    else:
        raise ValueError("Formato de arquivo não suportado")
        return None