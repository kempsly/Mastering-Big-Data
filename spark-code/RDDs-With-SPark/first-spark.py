# Databricks notebook source
from pyspark import SparkConf, SparkContext

# COMMAND ----------

conf = SparkConf().setAppName("Read File")

# COMMAND ----------

sc = SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

#text = sc.textFile('sample.txt')
text = sc.textFile('sample_columned.txt')

# COMMAND ----------

print('\n\n\n')
print(text.collect())
print('\n\n\n')
