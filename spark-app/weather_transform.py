from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import requests, json, os
from datetime import datetime
import os
import sys
API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    sys.exit("❌  WEATHER_API_KEY missing inside Spark driver")
CITY    = "Sakarya"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

spark = SparkSession.builder.appName("WeatherETL") \
        .config("spark.jars.packages",
                "org.postgresql:postgresql:42.7.3") \
        .getOrCreate()

try:
    data = requests.get(url, timeout=10).json()
    record = {
        "city": CITY,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "condition": data["weather"][0]["main"],
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = spark.read.json(spark.sparkContext.parallelize([json.dumps(record)]))

    df.write \
      .format("jdbc") \
      .option("url", "jdbc:postgresql://postgres:5432/airflow") \
      .option("dbtable", "weather_data") \
      .option("user", "airflow") \
      .option("password", "airflow") \
      .option("driver", "org.postgresql.Driver") \
      .mode("append") \
      .save()

    print("✅ Data written to PostgreSQL")

except Exception as e:
    print("❌ Error:", e)
    spark.stop()
    raise   

spark.stop()
