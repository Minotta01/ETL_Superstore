#I create funtions facilitate data analysis** (Creo funciones para facilitar el análisis de datos)
import pandas as pd
# I have created a function to know if the file has more than 1 sheet, so that
# it will create a data frame for each sheet named with the name of the
# corresponding sheet %% I count how data have each table

def create_Dataframe(data):
  if len(data.sheet_names) > 1:
        info_dataframe = []
        for sheet_name in data.sheet_names:
            df = pd.read_excel(data, sheet_name=sheet_name)
            info_dataframe.append((sheet_name, df))
        return info_dataframe

  else:
        return pd.read_excel(data, sheet_name=data.sheet_names[0])


#I create a function to get the data from any data frame created from its name
#(Creo una función para obtener los datos de cualquier marco de datos creado a partir de su nombre)

def get_data(data,name_df):
  for number, (name,df) in enumerate(data,1):
    if name_df == name:
        print(f"Dataframe information {name} obtained")
        print(f"\nYou have chocen the data frame number {number} your name is {name}\n-----------------------------------------------------------------------\n")
        print(f'The characteristics of the dataframe {name}\n-----------------------------------------------------------------------\n"')
        print(f'\nInfo about of {name}\n')
        print(f'{df.info()}\n-----------------------------------------------------------------------\n')
        print(f'Describe the DataFrame {name}\n\n',df.describe(),'\n-----------------------------------------------------------------------\n')
        print(f'Type of datas the DataFrame {name}\n\n',df.dtypes,'\n-----------------------------------------------------------------------\n')
        print(f'the first datas of {name}:\n\n',df.head(),'\n-----------------------------------------------------------------------\n')
        print(f'Last datas of {name}\n\n',df.tail(),'\n-----------------------------------------------------------------------\n')
        return df
  else:
         print(f"dataframe the name of {name} do not found.")