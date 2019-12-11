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

Para ver el tipo de una variable basta con utilizar la ```función type```.

Los tipos en Python son:
+ String
    + Los strings se represetan con comilla doble ```"``` o simple ```'```
```python
type("Hello Python")
```
```
str
```
+ Entero
```python
type(34)
```
```
int
```
+ Flotante
```python
type(0.05)
```
```
float
```
+ Boleano
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