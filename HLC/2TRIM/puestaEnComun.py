#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
import pandas as pd
import sqlite3

# 1. Módulo CSV (Estándar de Python)

# Leer un archivo CSV
def leer_csv():
    with open('archivo.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  # Cada fila es una lista

# Leer un archivo CSV con encabezados
def leer_csv_con_encabezados():
    with open('archivo.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)  # Cada fila es un diccionario

# Escribir un archivo CSV
def escribir_csv():
    data = [
        ['Nombre', 'Edad', 'Ciudad'],
        ['Alice', 25, 'Madrid'],
        ['Bob', 30, 'Barcelona'],
    ]
    with open('archivo.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Escribir un archivo CSV con encabezados
def escribir_csv_con_encabezados():
    data = [
        {'Nombre': 'Alice', 'Edad': 25, 'Ciudad': 'Madrid'},
        {'Nombre': 'Bob', 'Edad': 30, 'Ciudad': 'Barcelona'},
    ]
    with open('archivo.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Nombre', 'Edad', 'Ciudad'])
        writer.writeheader()  # Escribir encabezados
        writer.writerows(data)


# 2. Uso de pandas para CSV
# Leer un archivo CSV con pandas
def leer_csv_pandas():
    df = pd.read_csv('archivo.csv')
    print(df.head())  # Mostrar las primeras filas

# Escribir un archivo CSV con pandas
def escribir_csv_pandas():
    data = {'Nombre': ['Alice', 'Bob'], 'Edad': [25, 30], 'Ciudad': ['Madrid', 'Barcelona']}
    df = pd.DataFrame(data)
    df.to_csv('archivo.csv', index=False)

# Manipulación de datos con pandas
def manipular_datos_pandas():
    data = {'Nombre': ['Alice', 'Bob'], 'Edad': [25, 30], 'Ciudad': ['Madrid', 'Barcelona']}
    df = pd.DataFrame(data)

    # Filtrar datos
    filtrado = df[df['Edad'] > 25]
    print(filtrado)

    # Agrupar datos
    agrupado = df.groupby('Ciudad').mean()
    print(agrupado)

    # Agregar una nueva columna
    df['Nueva_Columna'] = df['Edad'] * 2
    print(df)

# 3. Trabajar con archivos CSV grandes

# Leer un archivo CSV grande en trozos
def leer_csv_grande():
    chunksize = 10000  # Número de filas por trozo
    for chunk in pd.read_csv('archivo.csv', chunksize=chunksize):
        print(chunk.head())


# 4. Validación de datos en CSV

# Verificar si un archivo CSV está vacío
def verificar_archivo_vacio():
    if os.stat('archivo.csv').st_size == 0:
        print('El archivo CSV está vacío.')

# Verificar encabezados
def verificar_encabezados():
    with open('archivo.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        if headers != ['Nombre', 'Edad', 'Ciudad']:
            print('Los encabezados no son válidos.')


# 5. Conversión de CSV a otros formatos

# Convertir CSV a JSON
def convertir_csv_a_json():
    df = pd.read_csv('archivo.csv')
    df.to_json('archivo.json', orient='records')

# Convertir CSV a Excel
def convertir_csv_a_excel():
    df = pd.read_csv('archivo.csv')
    df.to_excel('archivo.xlsx', index=False)


# 6. Limpieza de datos en CSV

# Eliminar filas con valores faltantes
def eliminar_filas_con_valores_faltantes():
    df = pd.read_csv('archivo.csv')
    df_limpio = df.dropna()
    print(df_limpio)

# Rellenar valores faltantes
def rellenar_valores_faltantes():
    df = pd.read_csv('archivo.csv')
    df_limpio = df.fillna(0)
    print(df_limpio)

# Eliminar duplicados
def eliminar_duplicados():
    df = pd.read_csv('archivo.csv')
    df_limpio = df.drop_duplicates()
    print(df_limpio)


# 7. Integración con bases de datos

# Cargar datos desde CSV a SQLite
def cargar_csv_a_sqlite():
    df = pd.read_csv('archivo.csv')
    conn = sqlite3.connect('base_de_datos.db')
    df.to_sql('tabla', conn, if_exists='replace', index=False)
    print("Datos cargados en SQLite.")

# Exportar datos desde SQLite a CSV
def exportar_sqlite_a_csv():
    conn = sqlite3.connect('base_de_datos.db')
    df = pd.read_sql('SELECT * FROM tabla', conn)
    df.to_csv('archivo.csv', index=False)
    print("Datos exportados a CSV.")


if __name__ == "__main__":
    # Llamar a las funciones necesarias
    # Ejemplo: leer_csv(), escribir_csv(), etc.
    leer_csv();
    escribir_csv();
    pass
