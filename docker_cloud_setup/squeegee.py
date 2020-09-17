import os
from dotenv import find_dotenv, load_dotenv
import pandas as pd
import psycopg2

# !pip install psycopg2-binary

load_dotenv(find_dotenv())

HOST = '138.197.145.169'
PORT = 5432
DB = 'postgres'
USER = 'postgres'
PASSWORD = 'squeegee1'

con = psycopg2.connect(
    database=DB,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)

pd.read_sql('SELECT * FROM pg_catalog.pg_tables;', con)
