# Introducción a Series de Tiempo con Python

## Introducción

Bienvenidos y bienvenidas a este videotutorial.

En este tutorial vamos a dar una introducción a series de tiempo ocupando el lenguaje de programación Python.

En esta oportunidad vamos a utilizar una librería muy ocupada en la actualidad llamada **Darts**, que permite trabajar mucho con series de tiempo.

Sin embargo, no es la única librería que vamos a utilizar para hacer el manejo de series de tiempo.

Es clásico ocupar:

- Pandas
- NumPy

También vamos a ocupar **Matplotlib**, que es para hacer gráficos.

Y esta en particular, que es **SciPy**, para hacer una transformación muy usual también en series de tiempo, que es la transformación **Box-Cox**.

---

## Base de Datos

También vamos a ocupar un conjunto de datos que está dentro de la librería Darts.

En esta oportunidad muestra la cantidad de pasajeros que tiene una aerolínea en particular a través del tiempo.

Entonces, cargamos la base de datos en nuestra memoria de Python.

La guardamos en nuestra variable llamada `series` y con Matplotlib la graficamos.

¿Qué es lo que vemos?

Vemos que a través del tiempo esta serie temporal de pasajeros de una aerolínea tiene una tendencia alcista.

Sin embargo, también tiene ciclos crecientes y bajistas que, a medida que pasa el tiempo, aumentan su amplitud.

---

## Transformación de la Serie Temporal

Entonces, ¿qué es lo clásico que uno hace en series de tiempo?

Lo clásico es transformar la serie temporal.

¿Por qué?

Porque es muy usual que en los modelos que usted va a ver más adelante se tengan que cumplir ciertos supuestos.

Y algunos de los supuestos, para que se cumplan, tendríamos que transformar nuestra serie original.

Para después aplicar el modelo y hacer la devolución en la transformación inversa para hacer nuestras futuras proyecciones.

---

## Transformación Logarítmica

Entonces tenemos distintas transformaciones.

Una es el logaritmo.

Logaritmo natural puede ser en particular.

En este caso ocupamos NumPy para transformar nuestra serie.

Y ocupamos `TimeSeries` para volver a considerarla como un elemento de serie de tiempo.

Graficamos con Matplotlib y esto es lo que vemos.

¿Cuál es la gran diferencia con nuestra serie anterior?

Donde teníamos que las amplitudes eran más bajas y, a medida que pasaba el tiempo, los ciclos tenían una mayor amplitud.

¿Qué pasó ahora?

Los ciclos tienden a tener una amplitud más constante.

Y eso es lo que ayuda la transformación del logaritmo.

Trata de controlar la varianza de nuestra serie temporal, y eso es un punto muy bueno.

---

## Diferenciación

¿Cuál es otra transformación usual que podemos utilizar en series temporales?

Otra es la diferenciación.

¿Qué es la diferenciación?

Es principalmente considerar la diferencia entre el dato del futuro con su momento anterior.

Por lo tanto, tenemos la serie de los incrementos de esta serie temporal.

Al aplicar a nuestra serie original el comando `diff`, que hace la diferenciación, tenemos que esta es nuestra serie temporal.

Vemos que, con respecto a nuestra serie original, esta serie ha perdido la tendencia que tenía en la serie original, que era creciente.

En este caso no tenemos tendencia principalmente.

¿Y qué es lo que vemos?

Se trata de conservar un poco la serie de los ciclos, dado que en nuestra serie original tenemos grandes subidas, pero también grandes bajadas que, a medida que pasa el tiempo, estas subidas y bajadas cada vez son mayores.

Y se ve aquí en nuestra serie de los incrementos.

Por lo tanto, esta transformación es una transformación muy ocupada en series temporales y la vamos a ocupar mucho en el futuro.

---

## Transformación Box-Cox

Para finalizar, vamos a ver una transformación más, que es la transformación de **Box-Cox**.

Box-Cox es una función donde nosotros tenemos que utilizar un lambda para hacer esta transformación.

Con SciPy buscamos este valor de lambda que, en este caso particular para nuestra serie, nuestro valor óptimo vendría siendo aproximadamente `0.148`.

Con ese lambda nosotros aplicamos la transformación a nuestra serie temporal.

Y notemos que se parece mucho a la transformación del logaritmo natural.

O sea, que tiene el mismo beneficio que el logaritmo natural, que nos permite controlar la varianza.

Ahora, si controlamos la varianza, también podríamos hacer Box-Cox y luego una diferenciación.

¿Para qué?

Para quitarle la tendencia.

Eso se lo dejo como ejercicio propuesto para que ustedes vean cómo luce esa serie temporal sin tendencia y con una varianza más controlada.

---

## Cierre

Espero que este tutorial haya sido de su agrado y nos vemos en el siguiente.