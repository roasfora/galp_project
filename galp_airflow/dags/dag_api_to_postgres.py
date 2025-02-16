from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess
import os

# Caminhos dentro do Airflow (DENTRO do container Docker)
AIRFLOW_HOME = "/usr/local/airflow"
SRC_DIR = f"{AIRFLOW_HOME}/dags/src"

API_SCRIPT = f"{SRC_DIR}/api_extract.py"
DB_SCRIPT = f"{SRC_DIR}/load_to_postgres.py"

# Definição dos argumentos padrão da DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 16),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Criando a DAG
with DAG(
    "api_to_postgres_dag",
    default_args=default_args,
    schedule_interval="0 12 * * *",  # Executa todos os dias ao meio-dia
    catchup=False,
) as dag:

    def run_api_script():
        """Executa o script de extração da API."""
        if not os.path.exists(API_SCRIPT):
            raise FileNotFoundError(f"Arquivo não encontrado: {API_SCRIPT}")

        result = subprocess.run(["python", API_SCRIPT], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            raise Exception(f"Erro ao rodar o script API: {result.stderr}")

    def run_db_script():
        """Executa o script de carregamento para o PostgreSQL."""
        if not os.path.exists(DB_SCRIPT):
            raise FileNotFoundError(f"Arquivo não encontrado: {DB_SCRIPT}")

        result = subprocess.run(["python", DB_SCRIPT], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            raise Exception(f"Erro ao rodar o script DB: {result.stderr}")

    # Tarefa 1: Extrai dados da API
    extract_api_task = PythonOperator(
        task_id="extract_api_data",
        python_callable=run_api_script,
    )

    # Tarefa 2: Insere dados no PostgreSQL
    load_to_postgres_task = PythonOperator(
        task_id="load_to_postgres",
        python_callable=run_db_script,
    )

    # Define a ordem das tarefas
    extract_api_task >> load_to_postgres_task
