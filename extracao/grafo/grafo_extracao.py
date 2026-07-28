import pandas as pd
import json
from dagster import op, Config
from servidor_mcp.server import mcp

class GraphConfig(Config):
    separador: str = ""

# Criando ferramenta/op de leitura de arquivo unificada
@mcp.tool()
@op
def read_file_graph(config: GraphConfig, caminho: str):
    """
    Ferramenta MCP (e op Dagster) unificada para orquestrar a leitura de arquivos de dados.
    
    Este op decide qual operação de leitura executar com base na extensão
    do arquivo fornecido no `caminho`.
    
    Parâmetros:
    - caminho (str): O caminho absoluto ou relativo para o arquivo de dados.
    
    Retorno:
    - string JSON estruturada contendo os dados do arquivo lido.
    """
    try:
        if caminho.endswith(".csv"):
            dados = pd.read_csv(caminho, sep=config.separador if config.separador else None, engine='python')
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