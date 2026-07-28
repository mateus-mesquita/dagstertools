# Regras de Commits do Projeto

Este documento estabelece as regras obrigatórias de versionamento e commits para manter a organização das ramificações (branches) do nosso repositório.

## 📌 Fluxo de Trabalho (Branching)

Para garantir que o histórico do Git reflita corretamente a estrutura do projeto, siga rigorosamente o mapeamento entre pastas e branches detalhado abaixo.

### 1. Pasta Geral de Extração de Dados
Qualquer alteração, criação ou deleção de arquivos que ocorra dentro da pasta `extracao` (exceto subpastas com regras específicas) deve **obrigatoriamente** ser commitada na branch:
👉 **`extracao-de-dados`**

**Exemplo de fluxo:**
```bash
git switch extracao-de-dados
git add extracao/novo_script.py
git commit -m "feat: Adicionado novo script de extração geral"
```

### 2. Subpasta Pandas
Todas as alterações que envolvam arquivos especificamente dentro da subpasta `extracao/ops/pandas/` devem **obrigatoriamente** ser commitadas na branch:
👉 **`pandas`**

*(Lembrando que a branch `pandas` é uma ramificação direta da branch `extracao-de-dados`).*

**Exemplo de fluxo:**
```bash
git switch pandas
git add extracao/ops/pandas/extracao_dados.py
git commit -m "fix: Corrigido formato de saída no pandas"
```

### 3. Pasta do Servidor MCP e Dockerfile
Qualquer alteração, criação ou deleção de arquivos dentro da pasta `servidor_mcp/` (como `mcp_main.py` ou `server.py`), bem como qualquer alteração no arquivo `Dockerfile`, deve ser **obrigatoriamente** commitada na branch:
👉 **`servidor`**

**Exemplo de fluxo:**
```bash
git switch servidor
git add servidor_mcp/ Dockerfile
git commit -m "fix: Ajustes na inicialização do servidor MCP e Dockerfile"
```

### 4. Pasta Geral de Tratamento de Dados
Qualquer alteração, criação ou deleção de arquivos que ocorra dentro da pasta `tratamento` (exceto subpastas com regras específicas) deve **obrigatoriamente** ser commitada na branch:
👉 **`tratamento-de-dados`**

**Exemplo de fluxo:**
```bash
git switch tratamento-de-dados
git add tratamento/ops/novo_script.py
git commit -m "feat: Adicionado novo script de tratamento geral"
```

### 5. Subpasta Pandas em Tratamento
Todas as alterações que envolvam arquivos especificamente dentro da subpasta `tratamento/ops/pandas/` devem **obrigatoriamente** ser commitadas na branch:
👉 **`tratamento-lib-pandas`**

*(Lembrando que a branch `tratamento-lib-pandas` é uma ramificação direta da branch `tratamento-de-dados`).*

**Exemplo de fluxo:**
```bash
git switch tratamento-lib-pandas
git add tratamento/ops/pandas/numericos.py
git commit -m "feat: Tratamento numérico usando pandas"
```

---

## 🔀 Regras de Merge

A integração (merge) das alterações entre as ramificações não é feita de forma automática; **deve ser expressamente solicitada ou realizada manualmente de forma intencional**.

Quando o merge for solicitado, ele deve respeitar estritamente a seguinte ordem hierárquica (de baixo para cima):

1. **`pandas` -> `extracao-de-dados`**
   *(Primeiro as alterações locais de tratamento no pandas sobem para a pasta geral de extração)*
2. **`tratamento-lib-pandas` -> `tratamento-de-dados`**
   *(As alterações da subpasta pandas sobem para a pasta geral de tratamento)*
3. **`extracao-de-dados` -> `master`**
   *(Por fim, a extração de dados consolidada sobe para a branch principal)*
4. **`tratamento-de-dados` -> `master`**
   *(Por fim, o tratamento de dados consolidado sobe para a branch principal)*
5. **`servidor` -> `master`**
   *(As alterações nos arquivos principais do servidor MCP vão direto para a master, sem passar pelas branches de dados)*

---

## ⚠️ O que NÃO Fazer
- **Nunca** commite arquivos da pasta `pandas` ou `tratamento/ops/pandas` enquanto estiver nas branches gerais (`extracao-de-dados` ou `tratamento-de-dados`). 
- **Nunca** misture, no mesmo commit, alterações das pastas gerais com as pastas específicas do pandas. Elas devem ser commitadas em suas respectivas branches.
