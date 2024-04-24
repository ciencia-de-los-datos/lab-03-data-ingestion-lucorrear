"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    # Lee el archivo 'clusters_report.txt' y ajusta el formato de la columna 'porcentaje_de_palabras_clave'
    df = pd.read_fwf('clusters_report.txt', 
                    colspecs="infer", 
                    widths=[9, 16, 16, 80], 
                    header=None, 
                    names=["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"])

    # Elimina las filas de encabezado y las filas vacías
    df = df.drop(index=[0, 1, 2])

    # Rellena los valores faltantes hacia adelante (ffill)
    df = df.ffill()

    # Reemplaza los espacios en los nombres de las columnas por guiones bajos y convierte a minúsculas
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Ajusta el formato de la columna 'porcentaje_de_palabras_clave'
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace('%', '').str.replace(',', '.').astype(float)
    
    # Asegura que las palabras clave estén separadas por coma y con un solo espacio entre palabra y palabra
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: re.sub(r'\s*,\s*', ', ', x))

    return df