# CORCHETES
# En la teoría se han visto diferentes formas de acceder a los datos de un DataFrame. La más simple es la utilización de
# corchetes.

# Importación de 'cars.csv' en un DataFrame
import pandas as pd
cars = pd.read_csv('./Chapter1_PythonBasics/resources/cars.csv', index_col=0)

# Imprime la columna 'country' de 'cars' como Series


# Imprime la columna 'country' de 'cars' como DataFrame


# Imprime las columnas 'country y 'drives_right' de 'cars' como DataFrame


# Ahora vamos a imprimir observaciones o filas, mediante slice.

# Imprime las tres pimeras filas


# Imprime de la cuarta a la sexta fila


# LOC e ILOC
# Usa 'loc' e 'iloc' (en dos líneas) para seleccionar la observación correspondiente con Japón. Imprime la salida como
# Series



# Usa 'loc' e 'iloc (en dos líneas) para seleccionar las observaciones de Australia y Egipto. Imprime la salida como
# DataFrame

# Imprime el valor de la columna 'drives_right' para la observación de 'Marruecos' con 'loc' o 'iloc'.


# Imprime un sub-DataFrame, que contenga las observaciones de 'Rusia' y 'Marruecos' y las columnas 'country' y
# 'drives_right' con 'loc' o 'iloc'


# Ahora vamos a seleccionar solamente columnas con 'loc' e 'iloc'.

# Imprime la columna 'drives_right' como Series con 'loc' o 'iloc'


# Imprime la columna 'drives_right' como DataFrame con 'loc' o 'iloc'


# Imprime las columnas 'cars_per_cap' y 'drives_right' como DataFrame con 'loc' o 'iloc'

