# Databricks notebook source
import os
username = spark.sql("SELECT current_user()").first()[0]
path = f"file:/tmp/{username}/dbacademy/jepfs"
dbutils.fs.rm(path, True)

