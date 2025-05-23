"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    from collections import defaultdict

    # Abre el archivo data.csv en modo lectura
    with open('files/input/data.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lines = file.readlines()

    # Inicializa un diccionario para sumar los valores de las letras
    letter_sum = defaultdict(int)

    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la tabulación como separador
        columns = line.strip().split('\t')
        # Incrementa la suma para la letra de la primera columna
        letter_sum[columns[0]] += int(columns[1])
    
    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    sorted_sum = sorted(letter_sum.items())

    # Retorna la lista de tuplas
    return sorted_sum

if __name__ == '__main__':
    # Llama a la función pregunta_03 e imprime el resultado
    print(pregunta_03())