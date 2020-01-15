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
