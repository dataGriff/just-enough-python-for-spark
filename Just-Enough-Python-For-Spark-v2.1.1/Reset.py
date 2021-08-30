# Databricks notebook source
username = spark.sql("SELECT current_user()").first()[0]
path = f"file:/tmp/dbacademy/{username}/jepfs"
dbutils.fs.rm(path, True)

