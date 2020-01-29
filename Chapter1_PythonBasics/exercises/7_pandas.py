# DATAFRAMES

# Listas pre-definidas.
# Contiene el país para los datos disponibles
names = ['Estados Unidos', 'Australia', 'Japón', 'India', 'Rusia', 'Marruecos', 'Egipto']
# Indica por que lado conduce la población del país. 'True' indica que conduce por la derecha
dr = [True, False, False, False, True, True, True]
# Número de vehículos por cada 1000 habitantes en el país correspondiente
cpc = [809, 731, 588, 18, 200, 70, 45]

# Importa el package 'pandas' con el alias como 'pd'. Instala previamente Pandas si no lo has realizado ya.


# Usa las listas para crear un diccionario con el nombre 'my_dict'. Las keys serán 'country', 'drives_right' y
# 'cars_per_cap', que se asocian a los values de las listas 'names', 'dr' y 'cpc'.


# Construye el DataFrame a partir del diccionario mediante el objeto 'DataFrame' de pandas y almacena el resultado en la
# variable con el nombre 'cars'


# Imprime 'cars'


# Definición de las etiquetas de los países
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Especifica las etiquetas de las filas estableciendo al atributo 'index' del DataFrame 'cars' la lista 'row_labels'


# Imprime 'cars'


# LEER DE CSV
# Utiliza la función 'read_csv' para importar el archivo 'cars.csv' a un DataFrame. Almacenalo en 'cars_v2'. Se
# encuentra en la ruta 'Chapter1_PythonBasic/resources'


# Imprime 'cars_v2'. ¿Está correctamente?


# Arregla la obtención de datos añadiendo el parámetro de entrada 'index_col' igualando a '0'


# Imprime 'cars_v2'


