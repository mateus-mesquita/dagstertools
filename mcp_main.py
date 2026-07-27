from server import mcp
import extracao_dados
import info
import transformacao
import dagster_pipeline

if __name__ == "__main__":
    print("Iniciando MCP...")
    mcp.run()

