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
    + Un número que tiene parte entera y parte decimal.
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

