from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Caminho do projeto dbt dentro do contêiner
DBT_PROJECT_DIR = "/usr/local/airflow/dbt/Galp_Project"

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "retries": 1,
}

dag = DAG(
    "dbt_transformation_pipeline",
    default_args=default_args,
    description="Executa dbt para transformar dados",
    schedule_interval="@daily",
    catchup=False,
)

dbt_run = BashOperator(
    task_id="dbt_run",
    bash_command=f"dbt run --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROJECT_DIR}",
    dag=dag,
)

dbt_test = BashOperator(
    task_id="dbt_test",
    bash_command=f"dbt test --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROJECT_DIR}",
    dag=dag,
)

dbt_run >> dbt_test
