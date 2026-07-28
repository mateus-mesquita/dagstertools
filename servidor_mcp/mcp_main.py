import pandas as pd
from servidor_mcp.server import mcp

# Importando os módulos para registrar as ferramentas (@mcp.tool) no servidor
import extracao.ops.pandas.extracao_dados
import extracao.grafo.grafo_extracao

if __name__ == "__main__":
    mcp.run()
