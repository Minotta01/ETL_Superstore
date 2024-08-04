import psycopg2
from psycopg2 import sql
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from contextlib import closing

load_dotenv(r'C:\Users\elrey\Documents\project_in_VSCode\ETL_Superstore\ConnectionData.env')

def database_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            #dbname='superstore',
            user=os.getenv('DB_USER'),
            #user='postgres',
            password=os.getenv('DB_PASSWORD'),
            #password='@_titerito',
            host=os.getenv('DB_HOST'),
            #host='localhost',
            port=os.getenv('DB_PORT')
            #port='5432'

        )
        connection.close()
        print("Conexión a la base de datos establecida.")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None

def check_connetion(connetion):
    if connetion:
        print("\nLa conexión a la base de datos está activa y funcionando correctamente.\n")
        return True
    else:
        print("\nNo se pudo establecer la conexión a la base de datos.\n")
        return False

def dataframe_to_table(df, name_tabla, connection):
    try:
         with closing(connection):
            engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)
            df.to_sql(name_tabla, engine, if_exists='replace', index=False)
            print(f"\nDataFrame convertido exitosamente a la tabla\n '{name_tabla}'")
    except Exception as e:
        print("\nError al convertir DataFrame a tabla:",'\n', e)