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
    file_path = 'clusters_report.txt'
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()[2:]
        for line in lines:
            if line[0].isdigit():
                columns = line.split()
                cluster = int(columns[0])
                cantidad_palabras = int(columns[1])
                porcentaje_palabras = float(columns[3].strip('%'))
                palabras_clave = ', '.join(columns[4:]).replace(',', ', ')
                data.append([cluster, cantidad_palabras, porcentaje_palabras, palabras_clave])
    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras', 'porcentaje_de_palabras', 'palabras_clave'])
    return df
df = ingest_data()
