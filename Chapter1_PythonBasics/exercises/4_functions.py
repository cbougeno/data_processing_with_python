# HELP

# Utiliza la función 'help()' para obtener la documentación de la función 'complex()'

# Pregunta: Cual de las siguientes opciones es verdadera:
# a) 'complex()' recibe dos argumentos; 'real' y '[, imag]'.
# b) 'complex()' recibe dos argumentos; 'real' y 'imag'. Ambos son requeridos.
# c) 'complex()' recibe dos argumentos; 'real' y 'imag'. 'real' es requerido, 'imag' es un argumento opcional.
# d) 'complex()' recibe dos argumentos; 'real' y 'imag'. Si 'imag' no se especifica, su valor es 1.

# Ahora obtén la documentación de 'sorted()':

# Cómo has podido comprobar, tiene varios argumentos, entre ellos 'iterable', 'key' y 'reverse'. Iterable es una
# colección de objetos, como List.

# Cuando un argumento se iguala a un valor quiere decir que este es su valor por defecto, como 'key=None' o
# 'reverse=False'. De momento NO utilizaremos 'key'.

# Vamos a utilizar las siguientes variables en un ejercicio:
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Concatena el contenido de las listas 'first' y 'second', y nombra la variale como 'full':

# Ordena la variable 'full' en orden descendente, e imprime el resultado:

## STRING METHODS
# Los strings tienes candidad de métodos útiles, si quieres conocerlos puedes usar la función `help()`.

# Variable 'hortaliza':
hortaliza = "alcachofa"

# Utiliza el método 'upper()' sobre la variable 'hortaliza' y almacénala en la variable 'hortaliza_up':

# Imprime 'hortaliza' y 'hortaliza_up':


# Imprime el número de vocales 'a' en la variable 'hortaliza' mediante el método 'count()':

## LIST METHODS
# Lista de áreas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Utiliza el método 'index()' para obtener el índice del elemento '20.0' en la variable 'areas', e imprime el resultado:

# Llama al método 'count()' de la variable 'areas' para obtener el número de ocurrencias del valor '9.50', e imprime el
# resultado:

# Utiliza el método 'append()' para añadir dos áreas nuevas con los valores: '24.5' y  '15.45' en ese mismo orden:


# Imprime la variable 'areas':

# Usa el método 'reverse()' para obtener el listado ordenado de forma inversa:

# Imprine nuevamente la variable 'areas':


## PACKAGE
# En el siguiente ejercicio se va a utilizar nociones de geometría.

# Definición del radio de la circunferencia:
r = 0.43

# Importa el package 'math' para poder acceder a la constante 'pi'


# Calcula la circunferencia 'C' del circulo descrito por el radio 'r':
C = 0

# Calcula el área 'A' del circulo descrito por el radio 'r':
A = 0

# Imprime la circunferencia y el área
print("Circumference: " + str(C))
print("Area: " + str(A))

## Import selectivo
# 'import math' obtiene todas las funcionalidades del package math. En este ejercicio solamente queremos obtener la
# funcionalidad 'radians' del package 'math'.

# Definicion del radio 'r', (distancia de la Luna a la Tierra):
r = 192500

# Importa la función 'radians' del package 'math':


# Calcula la distancia con la que se desplaza la Luna cuando realiza '12' grados (puedes calcularlo mediante la
# expresión:radio por phi, donde phi es el ángulo en radianes). Almacenalo en 'dist'.


# imprime 'dist'

# Pregunta:
# Supón que quieres usar la función 'inv()', que se encuentra en el subpackage 'linalg' del package 'scipy'. Quieres
# usar la siguiente línea:
# my_inv([[1, 2], [3, 4]])
# Cuál de las siguientes opciones escogerías para realizar el import:
# a) import scipy
# b) import scipy.linalg
# c) from scipy.linalg import my_inv
# d) from scipy.linalg import inv as my_inv

