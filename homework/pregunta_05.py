"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    from collections import defaultdict

    # Abre el archivo data.csv en modo lectura
    with open('files/input/data.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lines = file.readlines()

    # Inicializa un diccionario para almacenar los valores maximos y minimos de cada letra
    letter_max_min = defaultdict((lambda: (0, float('inf'))))

    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la tabulación como separador
        columns = line.strip().split('\t')
        # Actualiza el maximo y minimo para cada letra
        letter_max_min[columns[0]] = (
            max(letter_max_min[columns[0]][0], int(columns[1])),
            min(letter_max_min[columns[0]][1], int(columns[1]))
        )
    
    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    sorted_counts = sorted((letter, max_val, min_val) for letter, (max_val, min_val) in letter_max_min.items())

    # Retorna la lista de tuplas
    return sorted_counts

if __name__ == '__main__':
    # Llama a la función pregunta_05 e imprime el resultado
    print(pregunta_05())