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

```
mydir/
      module1.py
      module2.py
      __init.py__
```

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

Puedes importar todo un paquete, con lo que deberás repetir el nombre del paquete para poder utilizar una función
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

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter1_PythonBasics/resources/images/im_variables.png)

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
(type(casa1))
```
```
list
```

```python
casa2 = [["David", 45],
         ["Maria", 42],
         ["Cristina", 27],
         ["Roberto", 19]]
print(type(casa2))
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
print(casa1[3])
```
```python
42
```

En el caso que queramos escoger el elemento 7 "Roberto", habrá que espeficicar el índice ```6```
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
print(casa1[6])
```
```python
"Roberto"
```
O también es posible realizarlo mediante índices negativos. Esto es útil cuando quieres obtener elementos al final de tu lista.
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
print(casa1[-1])
```
```python
19
```
### Intervalos
Es posible obtener una sublista especificando un intervalo de índices mediante el uso de la siguiente sintaxis ```[3:5]```. En el ejemplo anterior tendríamos:
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
print(casa1[3:5])
```
```
[42, "Cristina"]
```
Como podemos observar, empieza por el 4º elemento hasta el 5º. Esto quiere decir que el índice final, el 5, es excluido. En general la sintaxis es la siguiente ```[ start(inclusive) : end(exclusive) ]```

Por otro lado, si vamos a hacer una subselección desde el índice 0 de la lista, es posible hacerlo mediante la siguiente sintaxis ```[:end]```, como podemos ver en el ejemplo.

```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
print(casa1[:4])
```
```
["David", 45, "María", 42]
```

Se puede hacer también desde un índice hasta el último de la cola mediante ```[start:]```, como:
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
print(casa1[5:])
```
```
[ 27, "Roberto", 19 ]
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
[ "David", 45, "María", 42, "Cristina", 27, "Roberto", 19 ]
[ "David", 45, "María", 42, "Cristina", 27, "Roberto", 20 ]
```
También es posible modificar varios elementos al mismo tiempo
```
casa1[0:2] = ["Raúl", 39]
print(casa1)
```
```
[ "David", 45, "María", 42, "Cristina", 27, "Roberto", 20 ]
```
Ahora queremos incluirnos en la lista. Para ello tendremos que utilizar el simbolo más ```+``` para concatenar la lista con una nueva con mi edad, de la siguiente forma:
```
casa1 + ["yo", 29]
```
```
[ "David", 45, "María", 42, "Cristina", 27, "Roberto", 20, "yo", 29 ]
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
[ "David", 45, 42, "Cristina", 27, "Roberto", 20 ]
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
[ 'a', 'z', 'c' ]
[ 'a', 'z', 'c' ]
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
[ 'a', 'b', 'c' ]
[ 'a', 'z', 'c' ]
```

# FUNCIONES
Una función es una **parte de código reutilizable**, desarrollada para **solucionar una tarea particular**. Puedes crear una función para evitar tener que **escribir varias veces una parte del código**.
En lo que llevamos de curso hemos utilizado algunas, como ```del``` o ```type```.

## max
Un ejemplo es la función ```max()```, una de las funciones build-in de Python. Si lo utilizamos con la lista de edades tenemos lo siguiente:
```python
edades = [45, 42, 27, 20]
print(max(edades))
```
```
45
```
El resultado es ```45```, el valor más alto de la lista. ```max()``` funciona como una caja negra. No sabemos cómo lo hace pero funciona, pero como actua ```max()``` no es importante. Lo importante es que te puede ayudar a crear tus propias líneas de código.

Otra cosa importante es que puedes asignar el resultado de la función ```max()``` a una nueva variable:
```
mayor = max(edades)
mayor
```
```
45
```

## round
```round()``` es una función que se utiliza para redondear valores a una precisión concreta. Tiene dos argumentos de entrada, el primero es el valor numeríco sobre el que se quiere redondear y el segundo será la precisión decimal con la que quieres redondear.

Imaginad que quiero redondear mi altura a un solo decimal. Sería así:
```python
print(round(1.69, 1))
```
```
1.7
```
Es posible llamar a la función ```round()``` sin especificar la parte decimal:
```python
print(round(1.79))
```
```
2
```
Automáticamente busca cual es el valor Entero más cercano.

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter1_PythonBasics/resources/images/im_help_round_ndigits.png)

## help
Si quieres conocer más acerca de las funciones build-in de Python puedes llamar a la función ```help()```

````python
help(round)
````

## Funciones utilizadas
Existen muchas funciones built-in en Python, y de ellas nosotros hemos estado utilizando algunas, como ```type()``` o ```print()```; incluso las que castean una tipo de dato a otro, como ```str()```, ```int()```, ```float()``` y ```bool()```.

## Back 2 Basic
Volviendo con los tipos de datos, las variables como ```str```, ```int``` o ```list``` son ```Object``` con los tipos mencionados anterriormente. Cada uno de estos tipos de datos contiene funciones llamadas ```metodos```, como
+ ```str```
    + ```capitalize()```
    + ```replace()```
+ ```int```
    + ```bit_lenght()```
    + ```conjugate()```
+ ```list```
    + ```index()```
    + ```count()```

En Python, TODO es un ```Object``` y cada objeto tiene métodos específicos. Es posible que distintos Objects compartan métodos, como es el caso de ```index()``` que se encuentra tanto en ```str``` como en ```list```

### list methods
 Volviendo con el ejemplo de las edades, si utilizamos el método ```index()``` del elemento ```'Cristina'```, el resultlado será:
 ```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
print(casa1.index("Cristina"))
```
```
4
```
Dado que 4 es el índice del string ```"Cristina"```

También se puede utilizar el método ```count()``` para contar el número de ocurrencias para un valor determinado en la lista.
```python
casa1 = ["David", 45, "María", 42, "Cristina", 27, "Roberto", 19]
print(casa1.count(45))
```
```
1
```
Y esto tiene sentido, dado que ```"David"``` es el único que tiene la edad de ```45```.

### str methods
Continuando con los ejemplos, ahora es el turno de strings:
```python
"cristina".capitalize()
```
```
"Cristina"
```
El método ```capitalize()``` devuelve el string con la primera letra en mayusculas.

Tambien es posible reemplazar caracteres por otros, como:
```python
"Cristina".replace("na", "an")
```
```
"Cristian"
```

## Cambios en métodos
Existen algunos métodos que no devuelven una respuesta, como es el caso de ```append()``` para las listas:
```python
casa1 = [ "David", 45, "María", 42, "Cristina", 27, "Roberto", 19 ]
casa1.append("Pepe")
print(casa1)
```
```
[ "David", 45, "María", 42, "Cristina", 27, "Roberto", 19, "Pepe" ]
```
```python
casa1.append(35)
print(casa1)
```
```
[ "David", 45, "María", 42, "Cristina", 27, "Roberto", 19, "Pepe", 35 ]
```

## Packages
Ahora que conoces el funcionamiento de las funciones, puedes darte cuenta que es posible utilizar funciones creadas por terceros para tu propio beneficio.

Es necesario que conozcas que todo el código escrito no tiene porque ir en un mismo script .py.
Esto es debido que puede ser un inconveniente tener cantidades ingentes de lineas de código, ya que es posible que no utilices algunas líneas de código y puede ser un problema de mantener.

Un ```package``` es el directorio o carpeta donde está alojado el script, y cada script recibe el nombre de módulo. Se pueden encontrar miles de packages opem source en internet. ```numpy```es un package para que los data scientist trabajen de forma eficiente con arrays y/o vectores numéricos, ```matlibplot``` es utilizado para visualización de datos y ```scikit-learn``` para machine learning.

Estos packages no se encuentran por defecto en Python. Para poder instalarlo es necesario hacerlo con herramientas como ```pip``` o ```conda```.

Ve a la URL http://pip.readthedocs.org/en/stable/installing y descarga ```get-pip.py``` y en el terminal escribe.

```shell script
python3 get-pip.py
``` 

Una vez instalado ```pip``` podrás instalar numpy de la siguiente forma:

```shell script
pip3 install numpy
```

### Import package
Después de hacer la instalación, deberías ser capaz de importar el package o un módulo específico de dicho packete.

Para importar un package entero en python puedes hacer lo siguiente:
```python
import numpy
array([ 1, 2, 3 ])
```
```
NameError: name 'array' is not defined.
```

Se ha producido el error ya que debemos especificar la función de la siguiente manera:
```python
import numpy
numpy.array([1, 2, 3])
```
```
array([ 1, 2, 3 ])
```

Aunque esta notación puede ser un tanto larga y tediosa. Es posible importar numpy con un alias:
```python
import numpy as np
np.array([ 1, 2, 3 ])
```
```
array([ 1, 2, 3 ])
```

Ahora supón que solamente queremos importar la función ```array()``` del package numpy, en lugar de todas las funciones:
```python
from numpy import array
array([ 1, 2, 3 ])
```
```
array([ 1, 2, 3 ])
```

Ahora sí que es posible llamar al método de esta forma, y no dará el error visto anteriormente.

El problema de utilizar esta forma es que no queda del todo claro la función a qué método pertenece.

## Numpy
Es un package que permite a los desarrolladores trabajar con vectores numéricos. Permite realizar operaciones matemáticas sobre colecciones, con buen rendimiento.

Supón que tenemos el siguiente listado de alturas, donde cada índice está asociado al índice de otra lista con los pesos:
```python
heights = [1.73, 1.68, 1.71, 1.89, 1.79]
weights = [65.4, 59.2, 63.6, 88.4, 68.7]
```
Si ahora intentamos calcular el IMC, obtendremos el siguiente error:
```python
weights / heights ** 2
```
```
TypeError: unsupported operand type(s) for **: 'list' and 'int'
```
La mejor manera de solucionar esto sería utilizando Numpy. Numpy proporciona una solución a las listas comunes, los ```array```. Estas son similares a las listas, pero con características añadidas: puedes realizar operaciones entre arrays

Ahora es posible asociar las listas anteriores a arrays de la siguiente forma:
```python
import numpy as np

np_heights = np.array(heights)
np_weights = np.array(weights)
```
Una vez transformadas las listas en arrays ya es posible calcular el IMC:
```python
imc = np_weights / np_heights ** 2
print(imc)
```
```
array([ 21.852, 20.975, 21.75, 24.747, 21.441 ])
```
Con esto se consigue que se realicen las operaciones elemento a elemento.

### Características
+ Las arrays de Numpy solamente aceptan un único tipo, ya sea enteros, decimales, boleanos, o cualquiera. Si se trata de crear una array con diferentes tipos de datos, estos se transformarán a strings ```str```.
+ Comportamientos diferentes:
```python
import numpy as np
python_list = [ 1, 2, 3 ]
np_array = np.array([ 1, 2, 3 ])

print(python_list + python_list)
print(np_array + np_array)
```
```
[ 1, 2, 3, 1, 2, 3 ]
[ 2, 4, 6 ]
```

### Numpy Subseting
Volviendo con los valores del IMC vamos a explicar esto.

Para seleccionar un elemento hay que acceder mediante corchetes y el valor del índice que necesitemos vía zero-index.

Por otro lado, es posible escoger valores mayores y/o menores a cierto valor, por medio de ```<, <=, >, >=```. Esto devolverá una array de booleans.

Si lo que queremos es obtener solamente los valores numéricos, basta con introducir esta array de booleans sobre corchetes. A continuación un ejemplo:

```python
import numpy as np
imc = np.array([ 21.852, 20.975, 21.75, 24.747, 21.441 ])

print(imc[1])

print(imc < 23)

print(imc[imc < 23])
```
```
20.975
array([ False, False, False, True, False ])
array([24.747])
```

### Numpy Type
Si obtenemos el ```type()``` de una array obtenemos:
```python
import numpy as np
np_heights = np.array([ 1.73, 1.68, 1.71, 1.89, 1.79 ])
np_weights = np.array([ 65.4, 59.2, 63.6, 88.4, 68.7 ])

print(type(np_heights))
print(type(np_weights))
```
```
numpy.ndarray
numpy.ndarray
```
Diciendonos que se trana de una array de n-dimensiones. Esta array específicamente es de una sola dimensión, pero es posible crear arrays de 2, 3 o 7. Vamos a trabajar ahora con 2 dimensiones.

### 2D Numpy Arrays
Creamos una array de 2-dimensiones con las alturas y pesos:
```python
import numpy as np
np_2d = np.array([[ 1.73, 1.68, 1.71, 1.89, 1.79 ],
                  [ 65.4, 59.2, 63.6, 88.4, 68.7 ]])
print(np_2d)
```
```
array([[ 1.73, 1.68, 1.71, 1.89, 1.79 ],
       [ 65.4, 59.2, 63.6, 88.4, 68.7 ]]
```
Obtenemos un par de sublistas dentro de un array. Cada sublista corresponde con una columna en la array de 2-dimensiones.

Ahora vamos a hablar del atributo ```shape()``` del objeto array. ```shape()``` nos aporta información acerca de la estructura de datos de la array, e indica el número de dimensiones (o filas) y columnas que tiene la array:
```python
print(np_2d.shape)
```
```
(2, 5)
```
Donde el primer valor corresponde al número de filas y el segundo al número de columnas (de ahora en adelante **row** y **columns**), para una array de 2-dimensiones. En este caso tenemos 2 filas y 5 columnas.

Los índices ahora quedan de la siguiente manera:
```
             #0      #1      #2      #3      #4
array([[    1.73,   1.68,   1.71,   1.89,   1.79    ],      #0
       [    65.4,   59.2,   63.6,   88.4,   68.7    ]]      #1

```
Para seleccionar una *row* basta con usar corchetes:
```python
print(np_2d[0])
```
```
array([ 1.73, 1.68, 1.71, 1.89, 1.79 ])
```
Y si queremos obtener el tercer elemento de la primera row haremos así:
```python
print(np_2d[0][2])
```
```
1.71
```
Básicamente es como seleccionar la *row* y de esta hacer otra selección. Sin embargo se puede simplificar a:

```python
print(np_2d[0, 2])
```
```
1.71
```
Obteniendo el mismo resultado pero de una manera más intuitiva.

Supón ahora que queremos obtener el segundo y tercer elemento de cada *row*, lo haríamos con la siguiente sintaxis:
```python
print(np_2d[:, 1:3])
```
```
array([[ 1.68, 1.71 ],
       [ 59.2, 63.6 ]])
```
Los primeros dos puntos quiere decir que escoja todas las *rows*, y la sintaxis de las *columns* es lo que ya vimos en las listas. Recuerda que el primer valor es inclusivo y el último exclusivo.

De forma parecida puedes escoger unicamente los elementos de la segunda *row*:
```python
print(np_2d[1, :])
```
```
array([ 65.4,   59.2,   63.6,   88.4,   68.7 ]
```
## Generar Datos
Vamos a utilizar una función de numpy, llamada ```np.random.normal()```. Con ello generaremos datos para nuestro ejemplo de baseball.

```python
import pandas as np
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
``` 

## Estadistica Básica
Numpy es comunmente utilizada para tareas relacionadas con estadística. Es por ello que el package contiene funciones, tales como:
+ ```mean()```
    + Promedio de sumar todos los valores del conjunto y dividirlo entre el número de valores.
+ ```median()```
    + Valor medio cuando el conjunto de datos es ordenado de mayor a menor.
+ ```std()```
    + Se utiliza para cuantificar la dispersión del conjunto de datos
+ ```corrcoef()```
    + Indica cómo de correlacionadas están dos variables entre si.

----
# Python Intermedio
Parte en la que avanzaremos en más contenido ya visto, como nuevos tipos de datos, entre otras cosas.

## Diccionarios
Los diccionarios son colecciones de datos no ordenados, modificables e indexados. Se escriben mediante llaves ```{}``` y contienen claves (keys) y valores (values).

Imagina, como ya hemos visto en otros ejercicios, que tienes un par de listas. Una destinada a la población, que contiene valores numéricos de población mundial, y otra lista de países, asociadas entre ellas por los índices de sendas listas.

```python
pop = [30.5, 2.77, 39.21]
countries = ['afganistán', 'albania', 'algeria']
```

Pretendes obtener la población de Algeria, por lo que deberás identificarla mediante la función ```index()```, y una vez tienes este índice buscar en la lista ```pop```.
```python
ind_alg = countries.index('algeria')
ind_alg
```
```
2
```
```python
pop[ind_alg]
```
```
39.21
```

Como se puede ver, es posible realizar esto con listas, pero se trata de un verdadero dolor de cabeza. No es algo para lo que esté pensado el uso de listas.

La solución a esto es el uso de diccionarios. La **key** del diccionario que vamos a crear serán los países, mientras que los **values** serán las poblaciones de dichos países:
```python
world = {'afganistán': 30.5, 'albania': 2.77, 'algeria': 39.21}
```

Es practicamente igual a un objero JSON. Ahora podemos obtener un valor utilizando los corchetes con un valor de un país como **key**
```python
world['afganistan']
```
```
30.5
```

La sintaxis será la siguiente:
```
dict_name[key]
result: value
```

Es importante saber que las ```keys``` serán únicas, y si tratas de almacenar un valor en una clave existente únicamente se almacenará el último valor añadido. Se puede decir que se actualiza el valor en la ```key``` de la siguiente forma:

```python
world['algeria'] = 39.31
world
```
```
{'afganistán': 30.5, 'albania': 2.77, 'algeria': 39.21}
```

Asimismo, las ```claves``` son objetos inmutables, no pudiendo modificar su valor en ningún caso, y estas pueden ser de tipos:
+ Strings
+ Integers
+ Booleans
```python
{0: "hola", True: "querido", "dos": "mundo"}
``` 

Nota adicional, los diccionarios no son solamente fáciles a la hora de trabajar, sino muy eficientes ya que Python realiza la búsqueda de las **keys** de forma muy rápida, incluso en diccionarios enormes.

Se puede validar si un diccionario contiene una ```key``` de la siguiente forma:

```python
'afganistan' in world
```
```
True
```

O incluso borrarlo (se va a añadir un nuevo registro):
````python
world['sealand'] = 0.000027
world
````
```
{'afganistán': 30.5, 'albania': 2.77, 'algeria': 39.21, 'sealand': 0.000027}
```
```python
del(world['sealand'])
world
```
```
{'afganistán': 30.5, 'albania': 2.77, 'algeria': 39.21}
```
Al volver a imprimir el resultado vemos que ```sealand``` se ha borrado del diccionario.

### Listas vs Diccionarios
Como hemos visto, los dos objetos son muy similares. Entre ellas:
+ Ambos objetos pueden ser seleccionados, actualizados y borrados con corchetes ```[]```.

Entre las diferencias, tenemos que:
+ **listas** indexan por un rango numérico
+ **diccionarios** lo hacen por clave, siendo esta de tipo inmutable.

Entonces, ¿cuándo utilizarlas?:
+ **listas** cuando el orden de la coleccion de valores importa
+ **diccionarios** cuando tienes que hacer consultas rápidas por claves únicas

***Ejercicios 6_diccionarios.py***

## Pandas
Como científico de datos se trabaja con grandes cantidades de datos. La forma de estos puede ser muy diferente, pero la podemos llevar a una estructura tabular.

Cuando trabajamos con tablas los datos los obtenermos por filas o ```rows```. Cada fila es una observación, y por cada observación tenemos diferentes columnas ````columns```` o variables.

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter1_PythonBasics/resources/images/im_tabular_table.png)

Para ello la librería más comunmente utilizada ens ```Pandas```. Se trata de una herramienta de alto nivel para la manipulación y el procesamiento de datos, construida con Numpy

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter1_PythonBasics/resources/images/im_tabular_table_python.png)

A parte de variables y observaciones, estas últimas tienen también lo que se conoce como etiquetas.

### Como construir una tabla con Pandas
Para construir uno mismo una tabla podemos utilizar los diccionarios.
````python
dict = {
    "country": ["Brasil", "Rusia", "India", "China", "Sudafrica"],
    "capital": ["Brasilia", "Moscú", "Nueva Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}
````

Las claves serán las columnas mientras que los valores se convierten en los datos, columans por columnas.

A continuación hay que importar el package de la siguiente y convertir el diccionario a un ```DataFrame``:

```python
import pandas as pd
df = pd.DataFrame(dict)
```

Si visualizamos estos datos, vemos que los índices se autoenumeran desde 0 en adelante. Podemos modificar el atributo ```index```:

```python
df.index["BR", "RU", "IN", "CH", "SU"]
```


Ahora imagina que tenemos los datos en un fichero externo, como un csv. Podemos leer directamente los datos desde ficheros, tablas en DDBB y muchos otros inputs.

```text
,country,capital,area,population
BR,Brasil,Brasilia,8.516,200.4
RU,Rusia,Moscú,17.10,143.5
IN,India,Nueva Delhi,3.286,1252
CH,China,Beijing,9.597,1357
SU,Sudafrica,Pretoria,1.221,52.98
```
Vamos a tratar de importar estos datos en Python utilizando la función ```read_csv()``` de Pandas.

```python
df = pd.read_csv('path/to/bricks.csv')
```
```
  Unnamed: 0    country      capital    area  population
0         BR     Brasil     Brasilia   8.516      200.40
1         RU      Rusia        Moscú  17.100      143.50
2         IN      India  Nueva Delhi   3.286     1252.00
3         CH      China      Beijing   9.597     1357.00
4         SU  Sudafrica     Pretoria   1.221       52.98
```

Lo primero es obtener los datos del csv que se encuentran en un directorio. Vemos que no ha procesado bien la primera columna de los índices. Para ello realizamos la lectura estableciendo el parámetro ````index_col````:
```
      country      capital    area  population
BR     Brasil     Brasilia   8.516      200.40
RU      Rusia        Moscú  17.100      143.50
IN      India  Nueva Delhi   3.286     1252.00
CH      China      Beijing   9.597     1357.00
SU  Sudafrica     Pretoria   1.221       52.98
```

***Ejercicios 7_pandas.py***

## Índices y selección de datos

Existen muchas maneras de indexar y seleccionar datosde un DataFrame. La primera es mediante corchetes ```[]```, la siguiente es por medio de acceso de datos a partir de los métodos ```loc``` y ```iloc```, que hacen que Pandas sea realmente útil.

### Acceso a columnas
Imagina que quieres acceder solamente a la primera columna del conjunto de datos de coches, ```country```. Simplemente puedes hacerlo escribiendo a la derecha del DataFrame el nombre de la columna mediante **corchetes**, como se muestra a continuación:

```python
df['country']
```
```
BR       Brasil
RU        Rusia
IN        India
CH        China
SU    Sudafrica
Name: country, dtype: object
```

Vemos que el resultado son los valores para dicha columna, enlazados con las correspondientes etiquetas. Destaca también la última línea, que informa del tipo de datos y el nombre de la columna. 

Al hacer esto la salida deja de ser un DataFrame, y se conoce como ```Serie```:

````python
print(type(df['country']))
````
```
<class 'pandas.core.series.Series'>
```

La Serie consiste en una array de 1-dimensión, que puede ser etiquetada como el DataFrame. Un conjunto de series forma un DataFrame.

Si haces una seleccion sobre el DataFrame con dobles corchetes obtienes un DataFrame:

```python
df[['country']]
```
```
      country
BR     Brasil
RU      Rusia
IN      India
CH      China
SU  Sudafrica
```
Si comprobamos ahora el tipo, veremos que se trata de un DataFrame con una sola columna.
```python
print(type(df[['country']]))
```
```
<class 'pandas.core.frame.DataFrame'>
```

De una forma parecida se pueden extraer dos columnas:
```python
df[['country', 'capital']]
```
```
      country      capital
BR     Brasil     Brasilia
RU      Rusia        Moscú
IN      India  Nueva Delhi
CH      China      Beijing
SU  Sudafrica     Pretoria
```
Siendo claros, lo que estamos haciendo aquí es acceder con una lista de cabeceras. Podemos acceder también con una variable lista:
```python
headers = ['country', 'capital']
df[headers]
```
```
      country      capital
BR     Brasil     Brasilia
RU      Rusia        Moscú
IN      India  Nueva Delhi
CH      China      Beijing
SU  Sudafrica     Pretoria
```

### Acceso a filas
La única forma de acceder a las rows es mediante ```slice``` ```[a:b]```. Para el caso que vamos a poner vamos a acceder a los índices del 1 al 3, basándonos en **zero.index** (recuerda que el primer valor es inclusivo y el último es exclusivo):
````python
df[1:4]
````
```
   country      capital    area  population
RU   Rusia        Moscú  17.100       143.5
IN   India  Nueva Delhi   3.286      1252.0
CH   China      Beijing   9.597      1357.0
```

#### Notas
+ Los corchetes funcionan, pero de forma limitada.
+ Idealmente buscamos algo parecido a las numpy arrays de 2-dimensiones -> ```slice```
+ En Pandas se usa ```loc``` ```label-based``` e ```iloc``` ```integer-position-based```

#### loc
```loc``` es un método de DataFrame en el que tienes que indicar el índice. El resultado es una Serie que contiene toda la información de la row.
```python
df.loc['RU']
```
```
country       Rusia
capital       Moscú
area           17.1
population    143.5
Name: RU, dtype: object
```
Del mismo modo que antes, si quieres obtener el DataFrame debes hacerlo con doble corchete:
```python
df.loc[['RU']]
```
```
   country capital  area  population
RU   Rusia   Moscú  17.1       143.5
```
La visualización cambia en fundios de si utilizas DataFrame o Series.

De esta forma puedes seleccionar varias rows mediante las etiquetas:
```python
df.loc[['RU', 'IN', 'CH']]
```
```
   country      capital    area  population
RU   Rusia        Moscú  17.100       143.5
IN   India  Nueva Delhi   3.286      1252.0
CH   China      Beijing   9.597      1357.0
```

Hasta ahora solo hemos escogido o filas o columnas. Podemos hacer una selección combinando ambas:
```python
df.loc[['RU', 'IN', 'CH'], ['country', 'capital']]
```
```
   country      capital
RU   Rusia        Moscú
IN   India  Nueva Delhi
CH   China      Beijing
```

Puedes utilizar ```loc``` para devolver todas las rows (utilizando dobles puntos) y algunas columnas:

```python
df.loc[:, ['country', 'capital']]
```
```
      country      capital
BR     Brasil     Brasilia
RU      Rusia        Moscú
IN      India  Nueva Delhi
CH      China      Beijing
SU  Sudafrica     Pretoria
```

#### iloc
Esta forma de acceder por índice es mediante su valor númerico por orden. De forma que podemos acceder al primer row tanto con ````loc```` como con ```iloc```
```python
df.loc[['RU']]
```
```
   country capital  area  population
RU   Rusia   Moscú  17.1       143.5
```
```python
df.iloc[[1]]
```
```
   country capital  area  population
RU   Rusia   Moscú  17.1       143.5
```
Para equiparar la seleccion de filas y columnas de antes podemos hacerla por valores enteros de la siguiente forma:
```python
df.iloc[[1,2,3], [0,1]]
```
```
   country      capital
RU   Rusia        Moscú
IN   India  Nueva Delhi
CH   China      Beijing
```
***Ejercicios 8_pandas_2.py***
