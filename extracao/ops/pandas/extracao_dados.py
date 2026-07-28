import pandas as pd
import json
from dagster import op
from server import mcp


@mcp.tool()
@op 
def read_csv(caminho: str, separador: str = "") -> str:
    """
    Ferramenta MCP (e op Dagster) para carregar arquivos CSV.
    
    Extrai os dados de um arquivo CSV (Comma-Separated Values) usando a biblioteca Pandas.
    Caso um separador específico não seja fornecido, tenta inferir automaticamente o delimitador correto.
    Ideal para ler arquivos de texto estruturados em colunas.
    
    Retorno:
    - Sucesso: Uma string JSON contendo uma lista de dicionários (orient="records") com os dados.
    - Falha: Uma string JSON informando o erro (ex: arquivo não encontrado ou vazio).
    """
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
    """
    Ferramenta MCP (e op Dagster) para carregar planilhas Excel.
    
    Extrai os dados de um arquivo Excel (.xls ou .xlsx) usando a biblioteca Pandas.
    Útil para ingestão de dados que foram salvos de planilhas.
    
    Retorno:
    - Sucesso: Uma string JSON contendo uma lista de dicionários (orient="records") com os dados.
    - Falha: Uma string JSON informando o erro.
    """
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
    """
    Ferramenta MCP (e op Dagster) para carregar arquivos Parquet.
    
    Lê o conteúdo de um arquivo colunar no formato Parquet usando a biblioteca Pandas.
    Este formato é muito utilizado em Big Data por sua compactação e eficiência de leitura.
    
    Retorno:
    - Sucesso: Uma string JSON contendo uma lista de dicionários (orient="records") com os dados.
    - Falha: Uma string JSON informando o erro.
    """
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
    """
    Ferramenta MCP (e op Dagster) para estruturar arquivos JSON brutos.
    
    Lê o conteúdo de um arquivo .json e o carrega usando Pandas. 
    Serve para validar se a estrutura do arquivo original pode ser convertida corretamente 
    em formato colunar (DataFrame) antes de devolvê-la de forma padronizada.
    
    Retorno:
    - Sucesso: Uma string JSON padronizada (orient="records").
    - Falha: Uma string JSON informando erros de parsing (ValueError) ou ausência de arquivo.
    """
    try:
        dados = pd.read_json(caminho)
        return dados.to_json(orient="records")
    except FileNotFoundError:
        return json.dumps({"erro": f"Arquivo não encontrado: {caminho}"})
    except ValueError as e:
        return json.dumps({"erro": f"Erro no formato do JSON: {str(e)}"})
    except Exception as e:
        return json.dumps({"erro": f"Erro inesperado ao ler JSON: {str(e)}"})
