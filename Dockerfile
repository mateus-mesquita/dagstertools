# Usando uma imagem leve do Python
FROM python:3.11-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Variável de ambiente para que o Python sempre enxergue a pasta /app na hora de importar módulos
ENV PYTHONPATH=/app

# Instalar dependências necessárias para o SO (se precisar de algo do pandas/pyarrow)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar apenas o arquivo de requisitos primeiro (para otimizar o cache do Docker)
COPY requirements.txt .

# Instalar as bibliotecas Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código fonte para dentro do container
COPY . .

# Comando para iniciar o servidor MCP usando STDIO
# Isso permite que a IA converse com o container via Standard Input/Output
CMD ["python", "-m", "servidor_mcp.mcp_main"]
