from sqlalchemy import create_engine,select,Table,Text
import pandas as pd
import psycopg2

sql ="select * from dummy_table"
engine= create_engine('redshift+psycopg2://username@host.amazonaws.com:5439/database')
with engine.connect() as connection, connection,begin():
    df = pandas.read_sql(sql,connection)

