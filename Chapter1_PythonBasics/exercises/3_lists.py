# LISTAS

# ¿Podrías decir cuál de las siguientes es una manera correcta de construir una lista? Puede haber várias respuestas:

a = [1, 3, 4, 2]
b = [[1, 2, 3], [4, 5, 7]]
c = [1 + 2, "a" * 5, 3]

# Variable de área (en metros cuadrados)
f_entr = 11.25
f_coci = 18.0
f_salo = 20.0
f_dorm = 10.75
f_bany = 9.50

s_entr = "entrada"
s_coci = "cocina"
s_salo = "salón"
s_dorm = "dormitorio"
s_bany = "baño"

# Adapta la lista de 'areas' para que se intercale el nombre de la estancia con su correspondiente área. Puedes usar las
# variables anteriores o escribirlas a mano, tú decides.
areas = ["entrada", None, None, f_coci, None, f_salo, None, f_dorm, "baño", None]

# Imprime 'areas'

# Información de 'casa' como una lista de listas. Complétala con el resto de estancias, dormitorio y baño, en ese orden.
casa = [["entrada", f_entr],
        ["cocina", f_coci],
        ["salón", f_salo]]

# Imprime la 'casa' y su 'type()'

# SUBSETTING LISTS
# Imprime el segundo elemento de la lista 'area'. Deberá coincidir con 11.25
print()

# Imprime el último elemento (tail) de la lista 'area'. Deberá coincidir con 9.50
print()

# Imprime el área de la lista 'area' asociada al 'salón'. Deberá coincidir con 20
print()

# Subset
# Utilizando una combinación de subselecciones crea una nueva variable, llamada 'cocina_dormitorio_area' que contenga la
# suma del área de la 'cocina' y del 'dormitorio'.
cocina_dormitorio_area = None
print(cocina_dormitorio_area)

# Slicing
# Utiliza las técnicas para crear intervalos vistas para crear dos variables, 'planta_baja' y 'planta_alta' que
# contengan los 6 primeros elementos y los 4 últimos, respectivamente.
planta_baja = areas
planta_alta = areas
print(planta_baja)
print(planta_alta)

# SUBSETTING LISTA DE LISTAS
# Como has podido ver las listas de Python pueden almacenar cualquier cosa, incluso listas. Ahora piensa (sin ejecutar
# nada inicialmente) en cual puede ser el resultado de:
result = casa[-1][1]

# REEMPLAZAR ELEMENTOS DE UNA LISTA
# Actualiza el valor del area del 'baño', de la variable 'areas', para que sea de '10.50' metros cuadrados en lugar de
# '9.50'

# Vamos a hace qué el 'salón' se convierta en un 'spa'. Modifica el valor en la variable 'areas'. Imprime el resultado
# de 'areas'.

print(areas)

# EXTENDER DE UNA LISTA
# Utiliza el operador + para añadir ['piscina', 25.0] al final de la lista de 'areas'. Almacénalo en una variable con el
# nombre de 'areas_1' e imprime el resultado.
areas_1 = None
print(areas_1)
# Ahora extiende 'areas_1' añadiendo un 'garaje' con el valor 15.45 y nómbralo como 'areas_2' e imprime el resultado.
areas_2 = None
print(areas_2)

# ELIMINAR DE UNA LISTA
# Queremos eliminar de la lista 'areas_2' la 'piscina' y el valor asociado a su área. Recuerda utilizar la función del()
# e imprime el resultado.
print(areas)

# TRABAJO INTERNO DE LISTAS
# En este ejercicio deberás modificar el segundo comando, que crea la variable 'areas_copy' como una variable que apunta
# al mismo espacio de memoria que 'areas_only'. Edita el segundo comando para copiar únicamente los valores a otra
# variable.

# Lista de áreas
areas_only = [11.25, 18.0, 20.0, 10.75, 9.50]

# Crear 'areas_copy'
areas_copy = areas_only

# Modificar el índice 0 de 'areas_copy'
areas_copy[0] = 5.0

# Imprimir 'areas_only' y 'areas_copy'
print(areas_only)