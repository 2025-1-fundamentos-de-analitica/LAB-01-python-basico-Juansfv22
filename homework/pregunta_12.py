"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    from collections import defaultdict

    # Abre el archivo data.csv en modo lectura
    with open('files/input/data.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lines = file.readlines()

    # Inicializa un diccionario para sumar los valores de la columna 5 en cada letra
    letters_sum = defaultdict(int)

    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la tabulación como separador
        columns = line.strip().split('\t')

        # Accede a la columna 5
        dict = columns[4].split(',')

        # Itera sobre cada elemento del diccionario
        for item in dict:
            # Extrae el valor de cada elemento
            value = item.split(':')[1]
            # Incrementa la suma para cada letra
            letters_sum[columns[0]] += int(value)

    # Ordena el diccionario numéricamente
    sorted_letters = {key: letters_sum[key] for key in sorted(letters_sum.keys())}

    # Retorna el diccionario
    return sorted_letters

if __name__ == '__main__':
    # Llama a la función pregunta_12 e imprime el resultado
    print(pregunta_12())