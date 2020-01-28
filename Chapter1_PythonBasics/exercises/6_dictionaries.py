# DICCIONARIOS
# Como hemos visto, los diccionarios son útiles. En el siguiente ejercicio tendremos dos listas, una con países y la
# otra con el nombre de su capital.

# Definición de 'countries' y 'capitals'
countries = ['españa', 'francia', 'alemania', 'noruega']
capitals = ['madrid', 'parís', 'berlín', 'oslo']

# Obtén el índice de 'alemania' y asígnalo a una variable llamada 'ind_ale'


# Utiliza 'ind_ale' para obtener la capital de Alemania de 'countries' e imprime el resultado


# CREA TU PRIMER DICCIONARIO
# Ahora añade como keys los 'countries' y como values las 'capitals', respetando el mismo orden. En total deben estar
# los cuatro pares key-value
europe = {'españa': 'madrid'}

# Imprime 'europe'


# ACCESO A ELEMENTOS DEL DICCIONARIO
# Aprovecha la variable 'europe' creado por ti para el siguiente ejercicio

# Obtén todas las keys llamando al método 'keys()' del diccionario 'europe'. Imprime el resultado.


# Imprime la salida de utilizar la key 'noruega' en el diccionario 'europe


# MANIPULACIÓN DE DICCIONARIOS
# Ahora que conoces cómo se accede o actualiza un diccionario, vamos a ponerlo en práctica. Añade el valor 'roma' a la
# clave 'italia' a la variable 'europe'


# Asegura que 'italia' pertenece al diccionario de 'europe' (el resultado tiene que ser de tipo 'bool')


# Añade ahora 'alemania' como clave y como valor 'bonn'


# Imprime 'europe'


# Anteriormente hemos introducido un valor incorrecto para el país 'alemania'. Actualiza su valor y establece 'berlín'


# Ahora imagina que hemos introducido un valor imposible como que 'viena' se encuentra en 'australia', dado que nos
# hemos confundido con Austria
europe['australia'] = 'viena'

# Elimina 'australia' de 'europe'


# Imprime 'europe'


# DICCIONARIOS ANIDADOS
# ¿Recuerdas que las listas podían contener listas? pues con los diccionarios sucede lo mismo. Para ello vamos a
# utilizar una versión de Europa que contenga la capital y la población.
# Dictionary of dictionaries
europe_v2 = {'españa': {'capital': 'madrid', 'poblacion': 46.77},
          'francia': {'capital': 'parís', 'poblacion': 66.03},
          'alemania': {'capital': 'berlín', 'poblacion': 80.62},
          'noruega': {'capital': 'oslo', 'poblacion': 5.084}}

# Utiliza los corchetes de forma anidada para obtener la capital de Francia sobre 'europe_v2'. Imprime el resultado.


# Crea un diccionario con el nombre de 'data', con las claves 'capital' y 'poblacion' y establece los valores 'roma' y
# '59.83', respectivamente.


# Añade 'data' a 'europe_v2' con la clave 'italia'


# Imprime 'europe_v2'


