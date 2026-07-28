import pandas as pd
import json
from dagster import op
from server import mcp


@mcp.tool()
@op 
def read_csv(caminho: str, separador: str = "") -> str:
    """Lê um arquivo CSV e retorna os dados em formato JSON"""
    try:
        if separador:
            dados = pd.read_csv(caminho, sep=separador)
        else:
            try:
                dados = pd.read_csv(caminho, sep=None, engine='python')
            except Exception:
                dados = pd.read_csv(caminho, sep=',')
        return dados.to_json(orient="records")
    except FileNotFoundError:
        return json.dumps({"erro": f"Arquivo não encontrado: {caminho}"})
    except pd.errors.EmptyDataError:
        return json.dumps({"erro": "O arquivo CSV está vazio."})
    except pd.errors.ParserError:
        return json.dumps({"erro": "Erro de parse: Não foi possível estruturar o CSV."})
    except Exception as e:
        return json.dumps({"erro": f"Erro inesperado ao ler CSV: {str(e)}"})


@mcp.tool()
@op
def read_excel(caminho: str) -> str:
    """Lê um arquivo Excel e retorna os dados em formato JSON"""
    try:
        dados = pd.read_excel(caminho)
        return dados.to_json(orient="records")
    except FileNotFoundError:
        return json.dumps({"erro": f"Arquivo não encontrado: {caminho}"})
    except Exception as e:
        return json.dumps({"erro": f"Erro ao ler Excel: {str(e)}"})


@mcp.tool()
@op 
def read_parquet(caminho: str) -> str:
    """Lê um arquivo Parquet e retorna os dados em formato JSON"""
    try:
        dados = pd.read_parquet(caminho)
        return dados.to_json(orient="records")
    except FileNotFoundError:
        return json.dumps({"erro": f"Arquivo não encontrado: {caminho}"})
    except Exception as e:
        return json.dumps({"erro": f"Erro ao ler Parquet: {str(e)}"})


@mcp.tool()
@op
def read_json(caminho: str) -> str:
    """Lê um arquivo JSON e retorna os dados estruturados"""
    try:
        dados = pd.read_json(caminho)
        return dados.to_json(orient="records")
    except FileNotFoundError:
        return json.dumps({"erro": f"Arquivo não encontrado: {caminho}"})
    except ValueError as e:
        return json.dumps({"erro": f"Erro no formato do JSON: {str(e)}"})
    except Exception as e:
        return json.dumps({"erro": f"Erro inesperado ao ler JSON: {str(e)}"})
