"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    from collections import defaultdict

    # Abre el archivo data.csv en modo lectura
    with open('files/input/data.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lines = file.readlines()

    # Inicializa un diccionario para contar las letras
    letter_count = defaultdict(int)

    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la tabulación como separador
        columns = line.strip().split('\t')
        # Incrementa en 1 el contador para la letra de la primera columna
        letter_count[columns[0]] += 1
    
    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    sorted_counts = sorted(letter_count.items())

    # Retorna la lista de tuplas
    return sorted_counts

if __name__ == '__main__':
    # Llama a la función pregunta_02 e imprime el resultado
    print(pregunta_02())
