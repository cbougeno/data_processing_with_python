# Módulo 1: Conceptos básicos de Python
Python es un lenguaje de programación muy versatil, que es ampliamente utilizado a día de hoy para:
+ Si quieres hacer rápidos cálculos
+ Para desarrollo web
+ Para realizar limpieza, procesamiento y análisis de datos


## Código
Aquí todo lo relacionado con código
### Script
Un script es un fichero con el código y sintaxis de python, y debe acabar con la extensión ***.py***
### Comentarios
Los comentarios son importantes para asegurar que tanto tu como otros puedan entender sobre que trata el código.
Se representa con el símbolo ***#***

## Introducción
Lore ipsum ...
### ¿Qué es \_\_init\__.py?
Los ficheros con el nombre **\_\_init\_\_.py** se utilizan para marcar en disco aquellos *paquetes de directorios Python*. Por ejemplo, podemos tener:
````shell script
Chapter1_PythonBasics/exercises/__init__.py
Chapter1_PythonBasics/exercises/1_introduction.py
````
**mydir** se trata del paquete que contiene el proyecto, por lo que es posible importar el código de *module.py* así:
```python
import Chapter1_PythonBasics.exercises
```
o incluso
```python
from Chapter1_PythonBasics import exercises
```

### Importar paquetes
```import``` es el comando que se utiliza en Python para importar paquetes de tu propio proyecto o de dependencias externas.

Puesdes importar todo un paquete, con lo que deberás repetir el nombre del paquete para poder utilizar una función
```python
import os
os.getcwd()
```
o puedes importar una función o clase dentro de un paquete:
```python
from os import getcwd
getcwd()
```
también es posible renombrar paquetes como desees:
```python
import os as custom
custom.getcwd()
```

### Python como calculaora
Python está perfectamente diseñada para realizar operaciones básicas, tales como suma, resta, multiplicación y división. A parte de estas es posible realizar otras como:

+ Suma ```+```
+ Resta ```-```
+ Muliplicación ```*```
+ División ```/```
+ Exponentes ```**```
+ Módulo ```%```

## Variables y Tipos
Cuando queramos almacenar valores utilizamos las *variables*. Las características de una variable en Python son:
+ específica: no es posible invocar una misma variable con dos valores *case-sensitive*
+ posibilidad de llamar al valor de una variable a posteriori
![Imagen](https://github.com/cbougeno/data_processing_with_python/Chapter1_PythonBasics/resources/images/im_variables.png)

De tal modo que si una variable es modificada es el código contunuaría funcionando, siempre y cuando el cambio sea por el mismo tipo.

Para asignar un valor a una variable se hace uso del caracter ```=```, como en el siguiente ejemplo:
```python
n = 5
```

Para ver el tipo de una variable basta con utilizar la ```función type()```.

Los tipos en Python son:
+ String
    + Los strings se represetan con comilla doble ```"``` o simple ```'```, y representan texto.
```python
type("Hello Python")
```
```
str
```
+ Entero
    + Un número sin parte decimal.
```python
type(34)
```
```
int
```
+ Flotante
    + Representa un número real con parte entera y parte decimal.
```python
type(0.05)
```
```
float
```
+ Boleano
    + Representan valores lógicos. Solo aceptan ```True``` o ```False``` *capitalizado*
```python
type(True)
```
```
bool
```
## Operadores
Un mismo operador puede tener distinto comportamiento cuando trabaja para según qué tipo de dato. P.E:
```Python
2 + 5
```
```
7
```
```python
'ab' + 'cd'
```
```
'abcd'
```

### Conversión de tipos
Utilizando el operador ```+``` se pueden concatenar dos strings, haciendo posible construir mensajes personalizados.
Sin embargo, no es posible 'sumar' strings con otros tipos, como enteros, booleanos, etc... Para ello deberás utilizar la función ```str()```, que convertirá el valor del atributo en string. Existen funciónes similares para los otros tipos, como ```int()```, ```float()``` y ```bool()```.

## Python Lists
Hemos visto tipos de datos, ¿pero que sucede cuando tienes multiples puntos de datos y quieres almacenarlos en una misma variable? (P.E: edad de todos los alumnos de la clase).

Se podría crear una variable por cada uno de la clase, pero esto sería un inconveniente. Para ello existen las listas, y se pueden almacenar con los brackets, de la siguiente forma ```[a, b, c]```.

La ventaja de las listas en Python son las siguentes:
+ Agrupas una colección de valores a un nombre
+ Pueden contener cualquier tipo, incluso otras listas
+ Pueden contener distintos tipos al mismo tiempo (no suele ser común)

```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
type(casa1)
```
```
list
```

```python
casa2 = [["David", 45],
         ["Maria", 42],
         ["Cristina", 27],
         ["Roberto", 19]]
type(casa2)
```
```
list
```

Como hemos visto anteriormente, en Python cada tipo tiene funcionalidades específicas y distintos comportamientos específicos, y esto también sucede con las listas.

## Subsetting Lists
Python usa indices para acceder a los elementos de una lista. Si volvemos al ejemplo de ```casa1```, el primer elemento tiene el índoce ```0```, el siguiente tiene el ```1```, y así sucesivamente.

Supón que queremos escoger la edad de María, que es el cuarto elemento, con lo que escogeríamos el índice ```3``` (conocido como 'zero index') de la siguiente forma:
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
casa1[3]
```
```python
42
```

En el caso que queramos escoger el elemento 7 "Roberto", habrá que espeficicar el índice ```6```
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
casa1[6]
```
```python
"Roberto"
```
O también es posible realizarlo mediante índices negativos. Esto es útil cuando quieres obtener elementos al final de tu lista.
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
casa1[-1]
```
```python
19
```
### Intervalos
Es posible obtener una sublista especificando un intervalo de índices mediante el uso de la siguiente sintaxis ```[3:5]```. En el ejemplo anterior tendríamos:
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
casa1[3:5]
```
```
[42, "Cristina"]
```
Como podemos observar, empieza por el 4º elemento hasta el 5º. Esto quiere decir que el índice final, el 5, es excluido. En general la sintaxis es la siguiente ```[ start(inclusive) : end(exclusive) ]```

Por otro lado, si vamos a hacer una subselección desde el índice 0 de la lista, es posible hacerlo mediante la siguiente sintaxis ```[:end]```, como podemos ver en el ejemplo.

```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
casa1[:4]
```
```
["David", 45, "María", 42]
```

Se puede hacer también desde un índice hasta el último de la cola mediante ```[start:]```, como:
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
casa1[5:]
```
```
[27, "Roberto", 19]
```

## List Manipulation
Acciones que se pueden hacer con las listas.
+ Cambiar elementos de la lista
+ Añadir elementos a la lista
+ Eliminar elementos de la lista

Todas estas manipulaciones son sencillas mediante Python. Volviendo con el ejercicio de las edades, imagina que Roberto ha cumplido un año y queremos modificarlo. Bastará con asociar el valor al índice que queramos actualizar:
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
print(casa1)
casa1[7] = 20
print(casa1)
```
```
["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
["David", 45, "María", 42, "Cristina", 27, "Roberto", 20]
```
También es posible modificar varios elementos al mismo tiempo
```
casa1[0:2] = ["Raúl", 39]
print(casa1)
```
```
["David", 45, "María", 42, "Cristina", 27, "Roberto", 20]
```
Ahora queremos incluirnos en la lista. Para ello tendremos que utilizar el simbolo más ```+``` para concatenar la lista con una nueva con mi edad, de la siguiente forma:
```
casa1 + ["yo", 29]
```
```
["David", 45, "María", 42, "Cristina", 27, "Roberto", 20, "yo", 29]
```
Pudiendo crear una nueva lista para almacenarlo:
```
casa1_ext = casa1 + ["yo", 29]
```
Eliminar de una lista también es sencillo, basta con usar la función ```del```
```
del casa1[2]
print(casa1)
```
```
["David", 45, 42, "Cristina", 27, "Roberto", 20]
```
A causa de haber eliminado un elemento de la lista, todos los sucesivos a este elemento han reducido su índice en uno. De modo que si volviesemos a ejecutar la misma línea se eliminaria el valor ```42``` de la lista.

### Behind Scenes
Comentar lo que sucede cuando modificamos listas. Cuando creamos una lista cualquiera ```x``` y creamos una copia de esta ```y```, si modificamos un elemento de la copia también se modifica en la original.
```python
x = ['a', 'b', 'c']
y = x
y[1] = 'z'
print(x)
print(y)
```
```
['a', 'z', 'c']
['a', 'z', 'c']
```
Esto es debido que cuando copias un elemento de una lista a otra mediante el simbolo igual ```=```, se copia la referencia de la lista no el valor actual. De modo que las dos variables apuntan a la misma direción de memoria del ordenador.
Cuando modificas una lista, se modifica el valor de la dirección de memoria. Por eso ```x``` e ```y``` se modifican.

Si lo que quieres es hacer una copia de los valores de una lista, lo puedes hacer de la siguiente forma
```python
x = ['a', 'b', 'c']
y = list(x)
y = x[:]
y[1] = 'z'
print(x)
print(y)
```
```
['a', 'b', 'c']
['a', 'z', 'c']
```