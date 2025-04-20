from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {"owner": "airflow", "retries": 1, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="weather_api_spark_etl",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="* * * * *",
    catchup=False,
    tags=["weather", "spark", "postgres"]
) as dag:

    run_spark_weather_etl = BashOperator(
        task_id       = "run_spark_weather_etl",
        bash_command=(
            # env değişkenini docker exec’e enjekte ediyoruz
            "docker exec "
            "-e WEATHER_API_KEY='{{ var.value.WEATHER_API_KEY }}' "
            "spark-master bash /opt/spark-app/weather-submit"
        ),
    )
