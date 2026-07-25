import pandas as pd
from dagster import op
from mcp_main import mcp


@mcp.tool()
@op 
def read_csv(caminho: str, separador: str = ';') -> pd.DataFrame:
    dados = pd.read_csv(caminho, sep=separador)
    return dados

@mcp.tool()
@op
def read_excel(caminho: str) -> pd.DataFrame:
    dados = pd.read_excel(caminho)
    return dados


    