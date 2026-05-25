# Modelos Ingenuos Aplicados con Python

## Introducción

Bienvenidos y bienvenidas a este nuevo video tutorial en el cual vamos a hablar sobre los modelos ingenuos, y nuevamente aplicado con Python.

Recordar que deben instalar la librería en la que estamos trabajando, en este caso **Darts**, como lo hicimos en el tutorial anterior.

Además, vamos a considerar mayoritariamente las mismas librerías del tutorial anterior.

En este caso en particular vamos a agregar un par de comandos más, que son principalmente tres de los modelos que vamos a ver en este tutorial:

- `NaiveDrift`
- `NaiveSeasonal`
- `ExponentialSmoothing`

Estos tres modelos son considerados parte de los modelos ingenuos.

---

## Modelos Utilizados

### NaiveDrift

Tenemos el `NaiveDrift`, que la predicción que genera a futuro es un valor del último que tenemos, más una consideración de la tendencia de todos los datos que tenemos en el pasado.

### NaiveSeasonal

El `NaiveSeasonal` está considerado cuando tenemos una serie temporal que tiene estacionalidad.

Por ejemplo, la predicción del futuro, si consideramos una estacionalidad anual, el valor que tenemos para noviembre siguiente sería ese mismo valor del noviembre pasado.

### ExponentialSmoothing

Luego tenemos el `ExponentialSmoothing`, que considera para hacer predicciones tanto la tendencia como la estacionalidad.

---

## Métrica de Evaluación

Vamos a considerar una métrica porque queremos hacer validación cruzada para ver qué tan bien predicen estos modelos.

En este caso vamos a considerar el **MAPE**, que es el error porcentual absoluto medio.

---

## Base de Datos

Vamos a utilizar también la misma base de datos de los pasajeros de una aerolínea a través del tiempo.

Entonces, recordemos que esta es nuestra serie original.

No la vamos a transformar, sino que vamos a considerar nuestros modelos ingenuos con la serie original.

---

## Entrenamiento de los Modelos

Creamos nuestros tres modelos:

- `NaiveDrift`
- `NaiveSeasonal`
- `ExponentialSmoothing`

Ahora vamos a generar un entrenamiento y una validación.

¿Qué vamos a considerar?

Vamos a considerar nuestra serie original hasta el primero de enero de 1960 y vamos a generar una predicción a 12 meses a futuro.

Entonces, ¿qué pasa aquí?

Vamos a hacer el `fit` de nuestro modelo.