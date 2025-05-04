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