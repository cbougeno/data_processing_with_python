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

# Subsetting lista de listas
# Como has podido ver las listas de Python pueden almacenar cualquier cosa, incluso listas. Ahora piensa (sin ejecutar
# nada inicialmente) en cual puede ser el resultado de
result = casa[-1][1]
