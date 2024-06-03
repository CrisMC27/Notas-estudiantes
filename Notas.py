import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
import warnings

warnings.filterwarnings('ignore')

datos = 'C:\\Users\\crist\\OneDrive\\Documentos\\U\\Datos1.csv'

# Leer el archivo CSV con diferentes codificaciones
codificaciones = ["utf-8", "latin-1"]
for codificacion in codificaciones:
    try:
        df = pd.read_csv(datos, sep=';', encoding=codificacion)
        print(f"El archivo se ha leído exitosamente con la codificación {codificacion}.")
        break
    except UnicodeDecodeError:
        print(f"No se pudo leer el archivo con la codificación {codificacion}.")

pd.options.display.float_format = '{:,.1f}'.format

# Análisis de datos
print('-----------------------------------------------------------')
print()
print('      <<...Calificaciones de los estudiantes ...>>')
print()
print(df.head(7))
print()
print('    .......Últimos estudiantes de la lista........')
print()
print(df.tail(7))
print('-----------------------------------------------------------')
print()
print('...Total de datos del archivo...')
print()
all_datos = df.size
print('El archivo tiene', all_datos, 'datos')
print('-----------------------------------------------------------')
print()
print('...Total estudiantes de la asignatura...')
print()
total_est =df['Nota final'].value_counts()
total2 = (total_est.sum())
print('En el curso hay {:,.0f}'.format(total2),'estudiantes')
