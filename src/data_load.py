import os
import pandas as pd
from sqlalchemy import create_engine, text  # Importando `text`
from dotenv import load_dotenv  # Importa dotenv

# Carregar variáveis do .env
load_dotenv()

# Configurações do PostgreSQL (agora carregadas do .env)
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Criando a conexão com o banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Caminhos dos arquivos CSV
csv_files = {
    "eur_to_usd_rates": r"C:\Users\isabe\Desktop\EDIT\EDIT\Data Ops\Galp_Project\data\eur_to_usd_rates.csv",
    "lusa_edp_news": r"C:\Users\isabe\Desktop\EDIT\EDIT\Data Ops\Galp_Project\data\lusa_edp_news.csv",
    "monthly_adjusted_data": r"C:\Users\isabe\Desktop\EDIT\EDIT\Data Ops\Galp_Project\data\monthly_adjusted_data.csv"
}

# Dicionário de schemas das tabelas
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

# Criando as tabelas no PostgreSQL
with engine.connect() as conn:
    for table, schema in table_schemas.items():
        conn.execute(text(schema))  # Usa `text()` para executar SQL
    conn.commit()
    print("Tabelas criadas com sucesso!")

# Carregando e inserindo os CSVs no banco de dados
for table_name, file_path in csv_files.items():
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        if table_name == "monthly_adjusted_data":
            df['date'] = pd.to_datetime(df['date'])  # Converte para datetime

        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Dados de {table_name} inseridos com sucesso!")
    else:
        print(f"Aviso: Arquivo {file_path} não encontrado.")

print("Processo concluído.")
