from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from pathlib import Path
import subprocess


def monitor_raw_data():

    raw_path = Path("/opt/airflow/dags/../../storage/raw")

    total_files = 0

    for path in raw_path.rglob("*.jsonl"):
        total_files += 1

    print(f"Total raw event files found: {total_files}")

def run_transformation():

    result = subprocess.run(
    ["python", "-m", "streaming.transform"],
    capture_output=True,
    text=True,
    cwd="/opt/airflow/project"
)

    print(result.stdout)

    if result.returncode != 0:
        raise Exception(result.stderr)

default_args = {
    "owner": "sahil",
    "start_date": datetime(2026, 5, 24)
}


with DAG(
    dag_id="raw_data_monitoring_pipeline",
    default_args=default_args,
    schedule="* * * * *",
    catchup=False,
    tags=["streaming", "monitoring"]
) as dag:

    monitor_task = PythonOperator(
        task_id="monitor_raw_storage",
        python_callable=monitor_raw_data
    )

    transform_task = PythonOperator(
        task_id="transform_raw_events",
        python_callable=run_transformation
    )

    monitor_task >> transform_task