FROM apache/airflow:2.8.0-python3.9

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir -p /opt/airflow/logs && chmod -R 777 /opt/airflow/logs