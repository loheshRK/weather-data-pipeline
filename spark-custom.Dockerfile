FROM bitnami/spark:latest

# Root yetkisiyle paketleri kur
USER root
RUN apt-get update && apt-get install -y python3-pip

# Python bağımlılıkları (requests, pandas, …)
COPY requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt

# Log dizini
RUN mkdir -p /logs && chmod -R 777 /logs

# Bitnami imajındaki varsayılan non‑root kullanıcıya geri dön
USER 1001
