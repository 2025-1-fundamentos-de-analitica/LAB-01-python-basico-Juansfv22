"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    from collections import defaultdict

    # Abre el archivo data.csv en modo lectura
    with open('files/input/data.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lines = file.readlines()

    # Inicializa un diccionario para almacenar la cantidad de registros por clave
    keys_count = defaultdict(int)

    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la tabulación como separador
        columns = line.strip().split('\t')

        # Accede a la columna 5
        dict = columns[4].split(',')

        # Itera sobre cada elemento del diccionario
        for item in dict:
            # Extrae la clave del elemento
            key = item.split(':')[0]
            # Incrementa el contador para cada clave
            keys_count[key] += 1

    # Ordena el diccionario numéricamente
    sorted_keys = {key: keys_count[key] for key in sorted(keys_count.keys())}

    # Retorna el diccionario
    return sorted_keys

if __name__ == '__main__':
    # Llama a la función pregunta_09 e imprime el resultado
    print(pregunta_09())