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



