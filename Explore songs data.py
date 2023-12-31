# Databricks notebook source
# MAGIC %fs head --maxBytes=10000 "/databricks-datasets/songs/README.md"

# COMMAND ----------

# MAGIC %fs ls "/databricks-datasets/songs/data-001"

# COMMAND ----------

# MAGIC %fs head --maxBytes=10000 "/databricks-datasets/songs/data-001/part-00000"

# COMMAND ----------

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()
df = spark.read.format('csv').option("sep", "\t").load('dbfs:/databricks-datasets/songs/data-001/part-00000')
df.display()
