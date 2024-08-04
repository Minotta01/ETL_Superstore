import psycopg2
from psycopg2 import sql
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from contextlib import closing
from sqlalchemy.exc import SQLAlchemyError

load_dotenv(r'C:\Users\elrey\Documents\project_in_VSCode\ETL_Superstore\ConnectionData.env')

def crear_conexion():
    try:
        dbname=os.getenv('DB_NAME')
        user=os.getenv('DB_USER')
        password=os.getenv('DB_PASSWORD')
        host=os.getenv('DB_HOST')
        port=os.getenv('DB_PORT')
        # Reemplaza con tus detalles de conexión
        engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
        print("Motor de conexión a la base de datos creado exitosamente")
        return engine
    except SQLAlchemyError as e:
        print(f"Error al crear el motor de conexión: {e}")
        return None
    
def verificar_conexion(engine):
    if engine:
        try:
            with engine.connect() as conn:
                print("La conexión a la base de datos está activa y funcionando correctamente.")
            return True
        except SQLAlchemyError as e:
            print(f"Error al verificar la conexión: {e}")
            return False
    else:
        print("No se pudo establecer la conexión a la base de datos.")
        return False
    
def dataframe_a_tabla(df, nombre_tabla, engine):
    try:
        df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)
        print(f"DataFrame convertido exitosamente a la tabla '{nombre_tabla}'")
    except SQLAlchemyError as e:
        print(f"Error al convertir DataFrame a tabla: {e}")