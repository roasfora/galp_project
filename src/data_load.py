import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv  # Importa dotenv

# ✅ Carregar variáveis do ambiente
load_dotenv()

# ✅ Configurações do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")  # Default para 5432 se não for especificado
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# ✅ Conectando ao banco de dados PostgreSQL
try:
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()
    print("✅ Conexão bem-sucedida ao PostgreSQL!")
except Exception as e:
    print(f"❌ Erro ao conectar ao PostgreSQL: {e}")
    exit()

# ✅ Caminhos dos arquivos CSV (SEM _v2)
csv_files = {
    "eur_to_usd_rates": r"C:\Users\isabe\Desktop\EDIT\EDIT\Data Ops\Galp_Project\data\eur_to_usd_rates.csv",
    "lusa_edp_news": r"C:\Users\isabe\Desktop\EDIT\EDIT\Data Ops\Galp_Project\data\lusa_edp_news.csv",
    "monthly_adjusted_data": r"C:\Users\isabe\Desktop\EDIT\EDIT\Data Ops\Galp_Project\data\monthly_adjusted_data.csv"
}

# ✅ Definição do esquema das tabelas (SEM _v2)
table_schemas = {
    "eur_to_usd_rates": """
        CREATE TABLE IF NOT EXISTS eur_to_usd_rates (
            timestamp TIMESTAMP PRIMARY KEY,
            eur_to_usd_rate FLOAT
        );
    """,
    "lusa_edp_news": """
        CREATE TABLE IF NOT EXISTS lusa_edp_news (
            title TEXT,
            link TEXT PRIMARY KEY
        );
    """,
    "monthly_adjusted_data": """
        CREATE TABLE IF NOT EXISTS monthly_adjusted_data (
            date DATE PRIMARY KEY,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            adjusted_close FLOAT,
            volume BIGINT,
            dividend_amount FLOAT
        );
    """
}

# ✅ Criando as tabelas no PostgreSQL (SEM _v2)
for table, schema in table_schemas.items():
    try:
        cursor.execute(schema)
        conn.commit()
        print(f"✅ Tabela '{table}' criada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao criar a tabela '{table}': {e}")

# ✅ Carregando e inserindo os CSVs no banco de dados 
for table_name, file_path in csv_files.items():
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        if table_name == "monthly_adjusted_data":
            df['date'] = pd.to_datetime(df['date'])  # Converte para datetime

        # ✅ Gerando query para inserir dados
        columns = ', '.join(df.columns)
        placeholders = ', '.join(['%s'] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders}) ON CONFLICT DO NOTHING"

        # ✅ Convertendo DataFrame para lista de tuplas
        data_tuples = [tuple(row) for row in df.to_numpy()]

        try:
            cursor.executemany(insert_query, data_tuples)
            conn.commit()
            print(f"✅ Dados de '{table_name}' inseridos com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao inserir dados na tabela '{table_name}': {e}")

    else:
        print(f"⚠️ Aviso: Arquivo '{file_path}' não encontrado.")

# ✅ Consulta `SELECT * FROM monthly_adjusted_data` 
try:
    cursor.execute("SELECT * FROM monthly_adjusted_data LIMIT 5;")  # Agora SEM `_v2`
    results = cursor.fetchall()
    print("\n🔍 Resultados da tabela 'monthly_adjusted_data':")
    for row in results:
        print(row)
except Exception as e:
    print(f"❌ Erro ao consultar 'monthly_adjusted_data': {e}")

# ✅ Fechando conexão com o banco de dados
cursor.close()
conn.close()
print("\n🎉 Processo concluído com sucesso!")
