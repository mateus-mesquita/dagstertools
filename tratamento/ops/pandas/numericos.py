from dagster import op
from servidor_mcp.server import MCP
import pandas as pd

@MCP.tool()
@op
def trocar_virgula(df):
    """
    Substitui todas as ocorrências de vírgula (',') por ponto ('.') em um DataFrame do Pandas.
    Esta ferramenta é essencial para tratar dados numéricos extraídos no formato brasileiro 
    (que utilizam vírgula como separador decimal), preparando-os para cálculos ou 
    conversão para tipos numéricos apropriados.
    
    Args:
        df (pandas.DataFrame): DataFrame contendo os dados a serem tratados.
        
    Returns:
        pandas.DataFrame: Novo DataFrame com as vírgulas substituídas por pontos.
    """
    try:
        return df.replace({',': '.'})
    except Exception as e:
        raise RuntimeError(f"Erro ao trocar vírgula: {e}")

@MCP.tool()
@op
def converter_para_numerico(df, coluna):
    """
    Converte os valores de uma coluna específica de um DataFrame do Pandas para o tipo numérico.
    Qualquer valor que não puder ser convertido (como texto inválido) será forçado para NaN 
    (Not a Number), preservando a consistência numérica da coluna. Ideal para limpar dados 
    após a remoção de caracteres indesejados.
    
    Args:
        df (pandas.DataFrame): DataFrame contendo a coluna a ser convertida.
        coluna (str): Nome da coluna que sofrerá a conversão.
        
    Returns:
        pandas.DataFrame: DataFrame com a coluna especificada tipada como numérica.
    """
    try:
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
        return df
    except Exception as e:
        raise RuntimeError(f"Erro ao converter a coluna '{coluna}' para numérico: {e}")