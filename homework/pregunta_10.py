"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    # Abre el archivo data.csv en modo lectura
    with open('files/input/data.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lines = file.readlines()

    # Inicializa una lista para almacenar los resultados
    tuples = []

    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la tabulación como separador
        columns = line.strip().split('\t')
        # Extrae la letra de la columna 1
        letter = columns[0]
        # Extrae las columnas 4 y 5 y cuenta los elementos
        column_4_count = len(columns[3].split(','))
        column_5_count = len(columns[4].split(','))
        # Agrega la tupla a la lista
        tuples.append((letter, column_4_count, column_5_count))

    # Retorna la lista de tuplas
    return tuples

if __name__ == '__main__':
    # Llama a la función pregunta_10 e imprime el resultado
    print(pregunta_10())