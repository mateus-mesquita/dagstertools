import os
from dagster import job, op
from extracao.grafo.grafo_extracao import read_file_graph

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(BASE_DIR, "insurance.csv")

@op
def get_csv_path() -> str:
    """Retorna o caminho absoluto do arquivo insurance.csv"""
    return CSV_PATH

@job
def insurance_job():
    """Pipeline principal para o processamento do dataset de seguros."""
    caminho = get_csv_path()
    
    # Utilizando a op Dagster (que também está registrada no MCP)
    dados = read_file_graph(caminho)
