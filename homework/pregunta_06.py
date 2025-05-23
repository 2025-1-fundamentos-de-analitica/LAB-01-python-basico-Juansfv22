"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    from collections import defaultdict

    # Abre el archivo data.csv en modo lectura
    with open('files/input/data.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lines = file.readlines()

    # Inicializa un diccionario para almacenar los valores maximos y minimos de cada cadena
    letter_max_min = defaultdict((lambda: (float('inf'), 0)))

    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la tabulación como separador
        columns = line.strip().split('\t')

        # Accede a la columna 5
        dict = columns[4].split(',')

        # Itera sobre cada elemento del diccionario
        for item in dict:
            # Divide el elemento en clave y valor
            key, value = item.split(':')
            # Actualiza el maximo y minimo para cada cadena
            letter_max_min[key] = (
                min(letter_max_min[key][0], int(value)),
                max(letter_max_min[key][1], int(value))
            )
    
    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    sorted_counts = sorted((letter, max_val, min_val) for letter, (max_val, min_val) in letter_max_min.items())

    # Retorna la lista de tuplas
    return sorted_counts

if __name__ == '__main__':
    # Llama a la función pregunta_06 e imprime el resultado
    print(pregunta_06())