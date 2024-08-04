
#I import the necessary resources from installed libraries
#(Importo los recursos necesarios de las bibliotecas instaladas)

import pandas as pd
from funtions import create_Dataframe,get_data # <--- Here I import the created functions that I will use
from connect import crear_conexion, verificar_conexion, dataframe_a_tabla
from sqlalchemy import create_engine
from contextlib import closing
from sqlalchemy.exc import SQLAlchemyError

def main():
    import_data = r'C:\Users\elrey\Documents\project_in_VSCode\ETL_Superstore\Superstore.xlsx'

    # Load the Excel file
    data = pd.ExcelFile(import_data, engine='openpyxl')

    # I call the create_frame function to create the dataframes and save them in a list
    dataframe_created = create_Dataframe(data)

    print(f'Were created {len(dataframe_created)} dataframes\n')  # <- Here show the amount the data frame were created

    # I show the name and the order of each data frame that was created
    for index, (name, df) in enumerate(dataframe_created, 0):
        print(f"The name of the dataframe created in step {index} which is equivalent to data frame number {index + 1} is: {name}")

    print('\n', '----------------------------------------------------------------------', '\n')

    # I display the information in the data frame of my choice.
    Orders = get_data(dataframe_created, 'Orders')  # <- Here I've chosen the data frame Orders
    Returns = get_data(dataframe_created, 'Returns')  # <- Here I've chosen the data frame Returns
    People = get_data(dataframe_created, 'People')  # <- Here I've chosen the data frame People


    engine = crear_conexion()
        
        # Verificar que la conexión fue exitosa
    if verificar_conexion(engine):
            try:
                # Convertir el DataFrame a una tabla en la base de datos
                dataframe_a_tabla(Returns, 'Returns', engine)
                dataframe_a_tabla(Orders, 'Orders', engine)
                dataframe_a_tabla(People, 'People', engine)
            except Exception as e:
                 print(f"Error al crear las tablas: {e}")
            finally:
                 engine.dispose()
                 print("Conexión cerrada.")
    else:
        print("No se pudo proceder con la operación en la base de datos debido a un error en la conexión.")
        
    print("El DataFrame sigue disponible para otras operaciones si es necesario.")


if __name__ == "__main__":
    main()