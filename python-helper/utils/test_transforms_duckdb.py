import duckdb
import pandas as pd

DUCKDB_FILE = "./data/data.duckdb"

def test_transform_sql():
    df = pd.read_csv("testdata/raw_clientes.csv")

    con = duckdb.connect(database = DUCKDB_FILE, read_only = False)
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