"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():
    # Definir el nombre del archivo
    file_path = 'clusters_report.txt'

    # Lista para almacenar los datos procesados
    data = []

    # Leer el archivo y procesar los datos
    with open(file_path, 'r') as file:
        # Saltar las primeras dos líneas y la línea del separador de guiones
        next(file)
        next(file)
        next(file)
        for line in file:
            # Dividir la línea en columnas
            columns = line.split(maxsplit=3)
            # Obtener los datos de las columnas
            cluster = columns[0]
            cantidad_palabras = columns[1]
            porcentaje_palabras = columns[2].replace(',', '.').strip('%')
            palabras_clave = ', '.join(columns[3].split())
            # Agregar los datos procesados a la lista
            data.append([cluster, cantidad_palabras, porcentaje_palabras, palabras_clave])

    # Crear el DataFrame de Pandas
    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras', 'porcentaje_de_palabras', 'palabras_clave'])

    # Devolver el DataFrame
    return df
