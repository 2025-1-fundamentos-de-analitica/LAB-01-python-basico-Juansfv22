"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    from collections import defaultdict

    # Abre el archivo data.csv en modo lectura
    with open('files/input/data.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lines = file.readlines()

    # Inicializa un diccionario para almacenar la cantidad de registros por clave
    letters_sum = defaultdict(int)

    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la tabulación como separador
        columns = line.strip().split('\t')

        # Accede a la columna 4
        letters = columns[3].split(',')

        # Itera sobre cada letra en la columna 4
        for letter in letters:
            # Incrementa la suma para cada letra
            letters_sum[letter] += int(columns[1])

    # Ordena el diccionario alfabéticamente
    sorted_letters = {key: letters_sum[key] for key in sorted(letters_sum.keys())}

    # Retorna el diccionario
    return sorted_letters

if __name__ == '__main__':
    # Llama a la función pregunta_11 e imprime el resultado
    print(pregunta_11())