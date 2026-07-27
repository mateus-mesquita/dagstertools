import pandas as pd
from dagster import op
from server import mcp


@mcp.tool()
@op 
def read_csv(caminho: str, separador: str = "") -> str:
    """Lê um arquivo CSV e retorna os dados em formato JSON"""
    if separador:
        dados = pd.read_csv(caminho, sep=separador)
    else:
        try:
            dados = pd.read_csv(caminho, sep=None, engine='python')
        except Exception:
            dados = pd.read_csv(caminho, sep=',')
    return dados.to_json(orient="records")


@mcp.tool()
@op
def read_excel(caminho: str) -> str:
    """Lê um arquivo Excel e retorna os dados em formato JSON"""
    dados = pd.read_excel(caminho)
    return dados.to_json(orient="records")


@mcp.tool()
@op 
def read_parquet(caminho: str) -> str:
    """Lê um arquivo Parquet e retorna os dados em formato JSON"""
    dados = pd.read_parquet(caminho)
    return dados.to_json(orient="records")



