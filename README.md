
# 📊 Dataform + DuckDB + BigQuery (Python Ready)

Este projeto demonstra como criar um pipeline de transformação de dados utilizando **GCP Dataform com BigQuery** para produção e **DuckDB com Python** para testes locais.

---

## 🧱 Estrutura do Projeto

```plaintext
my-dataform-project/
├── workflow_settings.yaml
├── definitions/
│   └── tables/
│       └── clientes.sqlx
├── includes/
├── package.json
├── python-helper/
│   ├── requirements.txt
│   ├── main.py
│   └── utils/
│       ├── generate_clients.py
│       └── test_transforms_duckdb.py
└── testdata/
    └── raw_clientes.csv
```

---

## 🚀 Instalação

### 📦 Pré-requisitos

- Python 3.8+
- Node.js 16+
- Conta no GCP com BigQuery habilitado
- Conta no [Dataform](https://console.cloud.google.com/dataform)
- Permissões no projeto GCP:
  - `BigQuery Data Editor`
  - `Dataform Admin`

### 📦 Inicializar projeto com Dataform

```bash
npm install -g @dataform/cli
dataform init my-dataform-project
cd my-dataform-project
```

---

## ⚙️ Configuração com `workflow_settings.yaml`

**`workflow_settings.yaml`**

```yaml
dataformCoreVersion: 3.0.0

defaultDatabaseConfig:
  database: seu-projeto-id
  schema: refined
  location: us

assertionSchema: tests
gcloudProjectId: seu-projeto-id
```

> Substitua `seu-projeto-id` pelo ID real do seu projeto GCP.

---

## 📄 Exemplo de Tabela em SQLX

**`definitions/tables/clientes.sqlx`**

```sql
config {
  type: "table",
  description: "Clientes ativos com dados formatados"
}

SELECT
  id,
  UPPER(nome) AS nome,
  DATE(data_criacao) AS data_criacao
FROM
  ${ref("raw.clientes")}
WHERE ativo = TRUE
```

---

## 🐍 Python para Geração e Testes Locais com DuckDB

### Instalar Dependências

```bash
cd python-helper
pip install -r requirements.txt
```

### `requirements.txt`

```txt
google-cloud-bigquery
pandas
duckdb
```

### Gerar Dados Mock

**`utils/generate_clients.py`**

```python
import pandas as pd

def save_mock_clients_csv(path="testdata/raw_clientes.csv"):
    rows = [
        {"id": 1, "nome": "Ana", "data_criacao": "2022-01-01", "ativo": True},
        {"id": 2, "nome": "Bruno", "data_criacao": "2022-06-10", "ativo": False},
        {"id": 3, "nome": "Carla", "data_criacao": "2023-03-15", "ativo": True},
    ]
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    print(f"Arquivo salvo em {path}")

if __name__ == "__main__":
    save_mock_clients_csv()
```

### Testar SQL Localmente com DuckDB

**`utils/test_transforms_duckdb.py`**

```python
import duckdb
import pandas as pd

def test_transform_sql():
    df = pd.read_csv("testdata/raw_clientes.csv")

    con = duckdb.connect()
    con.register("raw_clientes", df)

    query = '''
    SELECT
      id,
      UPPER(nome) AS nome,
      CAST(data_criacao AS DATE) AS data_criacao
    FROM raw_clientes
    WHERE ativo = TRUE
    '''

    result_df = con.execute(query).df()
    print(result_df)

if __name__ == "__main__":
    test_transform_sql()
```

---

## 🧪 Executando

### ✅ Gerar CSV para testes

```bash
python python-helper/utils/generate_clients.py
```

### ✅ Testar localmente com DuckDB

```bash
python python-helper/utils/test_transforms_duckdb.py
```

### ✅ Rodar Dataform local

```bash
dataform compile
dataform run
```

---

## ☁️ Executar no GCP

1. Navegue até `BigQuery > Dataform`
2. Crie um repositório Dataform apontando para seu GitHub
3. Configure a branch e execute

---

## 📌 Conclusão

Este repositório fornece:
- Transformações SQL com Dataform para BigQuery
- Geração de dados e testes locais com Python + DuckDB
- Configuração atualizada usando `workflow_settings.yaml`
- Integração moderna com GCP para ambientes de produção

---

## 🧠 Referências

- [Documentação oficial Dataform](https://cloud.google.com/dataform/docs)
- [Documentação DuckDB](https://duckdb.org/docs/)
