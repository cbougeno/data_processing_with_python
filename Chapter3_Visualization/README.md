# Visualización de datos con Python
En este módulo vamos a aprender a visualizar datos con Python y a ***almacenar datos en nuevas estructuras de datos***, además de conocer cómo controlar el flujo de tus scripts.

La visualización de datos se utiliza continuamente para explorar los datasets para entender mejor el comportamiento de los datos y poder obtener información de los insights, o incluso para poder reportarlos.

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_global_visualization.png)

Existen multitud de packages encaminados a realizar visualización de datos en Python, y uno de los más populares es ```Matplotlib```.

## Matplotlib
Con ```matplotlib``` se pueden crear multitud de visualiaciones. La más común es la representación mediante líneas.
 
Para visualizar hay que llamar a un subpackage llamado ```pyplot```.

Vamos a crear un par de listas que contendrán las poblaciones mundiales a lo largo de los años y lo visualizaremos mediante la función ```plot()```.

El primer argumento de la función ```plot()``` corresponde con el eje de abcisas o eje x, mientras que el segundo argumento corresponde con el eje de ordenadas o eje y.

Finalmente, hacer que el package visualize los datos se realiza la llamada a la función ```show()```.

```python
import matplotlib.pyplot as plt
year = [1950, 1979, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
#         x    y
plt.show()
```

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_year_pop.png)

Si visualizamos la imagen, tenemos 4 puntos representados por una línea. Si únicamente queremos representar los puntos y no unirlos mediante líneas, usaremos la función ```scatter()```.

```python
import matplotlib.pyplot as plt
year = [1950, 1979, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.scatter(year, pop)
#            x    y
plt.show()
```

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_year_pop_scatter.png)

***Ejercicios 1_plot_scatter.py***

## Histograma
El histograma es un tipo de visualización muy útil para la exploración de datos. Te puede dar una idea de la distribución de tus variables.

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_distribution.png)

En esta imagen vemos primero doce puntos distribuidos. Hemos decidico separarlo en 3 conjuntos, con anchura de 2. El resultado del histograma es contar cuantos puntos pertenecen a cada conjunto, 4 en el primero, 6 en el segundo y 2 en el último. Esta visuaización sirve a modo de resumen de los 12 puntos del conjunto de datos, y nos dice que la mayoria de valores están en el medio, pero que también hay más valores por debajo del valor 2 que por encima del valor 4.

```python
import matplotlib.pyplot as plt
help(plt.hist())
```

```
Help on function hist in module matplotlib.pyplot:

hist(x, bins=None, range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, *, data=None, **kwargs)
    Plot a histogram.
    
    Compute and draw the histogram of *x*.  The return value is a tuple
    (*n*, *bins*, *patches*) or ([*n0*, *n1*, ...], *bins*, [*patches0*,
    *patches1*,...]) if the input contains multiple data.  See the
    documentation of the *weights* parameter to draw a histogram of
    already-binned data.
    
    Multiple data can be provided via *x* as a list of datasets
    of potentially different length ([*x0*, *x1*, ...]), or as
    a 2-D ndarray in which each column is a dataset.  Note that
    the ndarray form is transposed relative to the list form.
    
    Masked arrays are not supported at present.
   
    Parameters
    ----------
    x : (n,) array or sequence of (n,) arrays
        Input values, this takes either a single array or a sequence of
        arrays which are not required to be of the same length.
    
    bins : int or sequence or str, optional
        If an integer is given, ``bins + 1`` bin edges are calculated and
        returned, consistent with `numpy.histogram`.
    
        If `bins` is a sequence, gives bin edges, including left edge of
        first bin and right edge of last bin.  In this case, `bins` is
        returned unmodified.
    
        All but the last (righthand-most) bin is half-open.  In other
        words, if `bins` is::
    
            [1, 2, 3, 4]
    
        then the first bin is ``[1, 2)`` (including 1, but excluding 2) and
        the second ``[2, 3)``.  The last bin, however, is ``[3, 4]``, which
        *includes* 4.
    
        Unequally spaced bins are supported if *bins* is a sequence.
    
        With Numpy 1.11 or newer, you can alternatively provide a string
        describing a binning strategy, such as 'auto', 'sturges', 'fd',
        'doane', 'scott', 'rice' or 'sqrt', see
        `numpy.histogram`.
    
        The default is taken from :rc:`hist.bins`.
    
    range: ...
```

Como puedes suponer, ```matplotlib``` tiene una manera de crear histogramas. Para ello deberás importar el subpackage ```pyplot``` y usar la 
función ```hist()```. Esta tiene muchísimos argumentos de entrada, pero los dos primeros son quizá los más importantes. ```x``` será la lista de valores sobre la que quieres construir el histograma y ```bins``` es el número de conjuntos por los que va a dividir el dataset (por defecto divide en 10 conjuntos).

Así pues, para hacer un ejemplo de histograma, se crea una lista con 12 valores, y se selecciona que se forme el histograma con 3 conjuntos:
```
import matplotlib.pyplot as plt
values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins=3)
plt.show()
```

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_histogram.png)

El número de conjuntos es importante ya que si se establecen pocos puede no mostrar suficientes detalles, mientras que si se excede puede complicarlo.

Cuando realizas varias gráficas, puedes llamar a la función ```plt.clf()``` para reiniciar las características de la gráfica

***Ejercicios 2_histogram.py***

## Personalizar visualizaciones
Crear un gráfico es una cosa. Hay que dar con el gráfico correcto, que haga que el mensaje sea claro a primera vista, ese es el reto.

Hay multiples formas, existen distintos tipos de gráficos (como hemos visto), y por cada uno de ellos existe un número infinito de personalizaciones, como el poder cambiar colores, forma, etiquetas.

La elección depende de los datos y de lo que se desee.

Volviendo al ejercicio de las poblaciones, si solo lo hacemos como hasta ahora el resultado queda un poco pobre:

```python
import matplotlib.pyplot as plt
years = [1950, 1951, 1952, ... , 2100]
pop = [2.53, 2.57, 2.62, ... , 10.85]

plt.plot(years, pop)

plt.show()
```

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_years_pop_1.png)

Siendo claros, no se sabe que datos se están mostrando, especialmente para aquellos que lo ven por primera vez. Para solucionar esto debemos **etiquetar** el gráfico, añadiendo el nombre de los ejes ```x``` e ```y```. Esto lo consequimos de la siguiente manera:

```python
import matplotlib.pyplot as plt
years = [1950, 1951, 1952, ... , 2100]
pop = [2.53, 2.57, 2.62, ... , 10.85]

plt.plot(years, pop)

plt.xlaber('Año')
plt.ylaber('Población')

plt.show()
```

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_years_pop_2.png)

De esta forma queda mucho más claro que nos indica cada eje. 

A continuación vamos a indicar el título de la gráfica. 

```python
import matplotlib.pyplot as plt
years = [1950, 1951, 1952, ... , 2100]
pop = [2.53, 2.57, 2.62, ... , 10.85]

plt.plot(years, pop)

plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Proyecciones de Población Muncial')

plt.show()
```

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_years_pop_3.png)

Lo siguiente es dar perspectiva a la gráfica, para ello vamos a hacer que el eje y comience por 0 y que crezca en intervalos de 2 hasta el valor 10. Esto podemos hacerlo con la función ```yticks```:

```python
import matplotlib.pyplot as plt
years = [1950, 1951, 1952, ... , 2100]
pop = [2.53, 2.57, 2.62, ... , 10.85]

plt.plot(years, pop)

plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Proyecciones de Población Mundial')
plt.yticks([0, 2, 4, 6, 8, 10])
plt.show()
```

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_years_pop_3.png)

Y ahora podemos añadir otro argumento para darle el valor que deseemos a los marcadores, poniendo los valores en *miles de millón*:

```python
import matplotlib.pyplot as plt
years = [1950, 1951, 1952, ... , 2100]
pop = [2.53, 2.57, 2.62, ... , 10.85]

plt.plot(years, pop)

plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Proyecciones de Población Mundial')
plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2MM', '4MM', '6MM', '8MM', '10MM'])
plt.show()
```

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_years_pop_4.png)

Para finalizar, vamos a añadir más datos que añadan valor de los últimos años. En wikipedia se ha extraido la información de los años 1800, 1850 y 1900, así que vamos a añadirlos:

```python
import matplotlib.pyplot as plt
years = [1950, 1951, 1952, ... , 2100]
pop = [2.53, 2.57, 2.62, ... , 10.85]

# Añadimos datos anteriores
years = [1800, 1850, 1900] + years 
pop = [1.0, 1.262, 1.650] + pop

plt.plot(years, pop)

plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Proyecciones de Población Mundial')
plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2MM', '4MM', '6MM', '8MM', '10MM'])
plt.show()
```

![Imagen](https://github.com/cbougeno/data_processing_with_python/blob/master/Chapter3_Visualization/resources/images/im_years_pop_5.png)
