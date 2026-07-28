import pandas as pd
import json
from dagster import op
from server import mcp

# Criando ferramenta/op de leitura de arquivo unificada
@mcp.tool()
@op
def read_file_graph(caminho: str, separador: str = ""):
    """
    Ferramenta MCP (e op Dagster) unificada para orquestrar a leitura de arquivos de dados.
    
    Este op decide qual operação de leitura executar com base na extensão
    do arquivo fornecido no `caminho`.
    
    Parâmetros:
    - caminho (str): O caminho absoluto ou relativo para o arquivo de dados.
    - separador (str, opcional): Delimitador a ser usado caso o arquivo seja um CSV.
    
    Retorno:
    - string JSON estruturada contendo os dados do arquivo lido.
    """
    try:
        if caminho.endswith(".csv"):
            dados = pd.read_csv(caminho, sep=separador if separador else None, engine='python')
        elif caminho.endswith(".xlsx"):
            dados = pd.read_excel(caminho)
        elif caminho.endswith(".parquet"):
            dados = pd.read_parquet(caminho)
        elif caminho.endswith(".json"):
            dados = pd.read_json(caminho)
        else:
            return json.dumps({"erro": "Formato de arquivo não suportado"})
            
        return dados.to_json(orient="records")
    except Exception as e:
        return json.dumps({"erro": f"Erro ao ler arquivo: {str(e)}"})