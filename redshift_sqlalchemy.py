from sqlalchemy import create_engine,select,Table,Text
import psycopg2
dest_schema='Dummy'
dest_table='table_test'
sql =f"""Truncate table {dest_schema}.{dest_table};"""
engine= create_engine('redshift+psycopg2://username@host.amazonaws.com:5439/database')
with engine.connect() as connection, connection,begin():
    connection.execute(sql)
    print('Table Truncated Sucessfully')
