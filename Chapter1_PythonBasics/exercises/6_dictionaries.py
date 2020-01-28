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

