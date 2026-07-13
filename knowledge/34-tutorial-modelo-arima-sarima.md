# Aplicación de un modelo SARIMA

Bienvenidos y bienvenidas a este nuevo videotutorial, en el cual vamos a trabajar en la aplicación de un modelo SARIMA.

Para esto, vamos a utilizar una base de datos que trabajamos en la Ayudantía 3 del curso.

En esa ayudantía, principalmente, creamos una serie temporal a partir de una base de datos con registros de asistencia a distintos hoteles.

También propusimos un buen modelo ARMA.

Ahora, considerando que nuestro espectro de modelos ha aumentado y que tenemos disponibles los modelos ARIMA y SARIMA, el objetivo del día de hoy es aplicar un modelo SARIMA con la finalidad de mejorar el desempeño del modelo ARMA.

Buscaremos encontrar un modelo mejor utilizando como referencia el criterio AIC.

## Preparación del entorno

Para comenzar, vamos a instalar la librería Darts.

También vamos a cargar:

- Las librerías necesarias.
- Los métodos que necesitaremos utilizar.
- La base de datos de registros de hoteles.

Después realizaremos el procesamiento necesario para crear nuestra serie temporal.

## Construcción de la serie temporal

De la base de datos seleccionaremos únicamente los registros correspondientes a `Resort Hotel`.

También vamos a considerar solamente las reservas que no fueron canceladas.

Si la variable de cancelación es igual a cero, significa que la reserva no fue cancelada.

Para calcular la cantidad de asistentes, vamos a considerar:

- Los adultos.
- Los niños.

La base de datos también contiene una columna con la cantidad de bebés, pero en este análisis nos centraremos únicamente en adultos y niños.

La serie estará agregada a nivel diario.

## Visualización de la serie original

Después de realizar este procesamiento obtenemos nuestra serie original.

La serie tiene una frecuencia diaria y abarca desde 2015 hasta 2017.

Nuestro objetivo es ajustar un modelo SARIMA.

En la gráfica se observan ciertos movimientos que podrían considerarse cíclicos.

Como estamos trabajando con datos diarios, una posible periodicidad podría ser semanal, es decir, cada siete días.

## Aplicación del logaritmo

Vamos a aplicar el logaritmo a nuestra serie temporal.

En una primera instancia, ejecutaremos el comando `auto_arima` para que proponga el modelo que mejor se ajusta a los datos.

Sin embargo, vamos a indicar que queremos considerar modelos SARIMA.

Para ello, estableceremos una periodicidad igual a siete.

El resto de los parámetros se mantendrá sin restricciones particulares.

No vamos a establecer un orden máximo.

En otras palabras, le indicaremos a `auto_arima`:

> Busca el mejor modelo que puedas encontrar.

Vamos a realizar esta búsqueda sin proporcionarle información previa obtenida a partir de la función de autocorrelación o de la función de autocorrelación parcial.

Más adelante explicaremos por qué.

## Tiempo de ejecución de `auto_arima`

Este procedimiento puede demorar bastante.

Yo ya ejecuté este código y tardó mucho tiempo, principalmente porque no establecí un orden máximo para la búsqueda.

El algoritmo genera muchas combinaciones de modelos.

Algunos modelos tardan alrededor de 20 segundos en ajustarse y otros cerca de 10 segundos.

En promedio, podrían evaluarse entre cinco y diez modelos por minuto.

Como existe una gran cantidad de combinaciones, el proceso completo tarda bastante.

Por eso, simplemente ejecuté el código y esperé hasta que entregara el mejor modelo encontrado.

## Modelo seleccionado por `auto_arima`

El resultado indica que el mejor modelo es:

$$
\operatorname{SARIMA}(0,1,2)\times(1,0,1)_7
$$

La parte:

$$
(0,1,2)
$$

corresponde a la componente no estacional.

El valor central:

$$
d=1
$$

indica que la serie fue diferenciada una vez.

Esto ocurre porque la serie original no es estacionaria.

La parte:

$$
(1,0,1)_7
$$

corresponde a la componente estacional.

El valor:

$$
m=7
$$

indica que la periodicidad considerada es semanal.

El criterio AIC obtenido es cercano a:

$$
800
$$

## Comparación con el modelo anterior

En la ayudantía anterior, nuestro mejor modelo había obtenido un AIC de aproximadamente:

$$
800.28
$$

El modelo propuesto por `auto_arima` obtiene un AIC cercano a:

$$
800.64
$$

Por lo tanto, no representa una mejora respecto al modelo anterior, aunque los valores son bastante cercanos.

Aquí surge una pregunta:

> ¿Podemos encontrar un modelo mejor?

`auto_arima` evaluó una gran cantidad de modelos.

Realizar manualmente todas esas combinaciones podría tomar incluso más tiempo.

Sin embargo, aquí aparece la importancia de interpretar correctamente:

- La función de autocorrelación, ACF.
- La función de autocorrelación parcial, PACF.

Aunque `auto_arima` haya evaluado muchos modelos, una buena interpretación de estas gráficas puede permitirnos encontrar una mejor alternativa.

## Diferencias entre `auto_arima` y `SARIMAX`

Hay un aspecto importante que debemos considerar.

Cuando aplicamos `auto_arima` y posteriormente ajustamos el mismo modelo mediante `SARIMAX`, podemos obtener valores de AIC ligeramente diferentes.

Por ejemplo, al ajustar:

$$
\operatorname{SARIMA}(0,1,2)\times(1,0,1)_7
$$

mediante `SARIMAX`, el AIC obtenido es cercano a:

$$
798
$$

Esta diferencia puede deberse a la forma en que cada implementación estima la función de verosimilitud.

Por ello, algunos valores pueden cambiar ligeramente.

Debemos considerar estas diferencias al comparar modelos ajustados mediante comandos distintos.

## Recuperación del modelo ARIMA anterior

En la ayudantía anterior habíamos ajustado un modelo ARMA(6,7) sobre la serie diferenciada.

Eso equivale a considerar un modelo:

$$
\operatorname{ARIMA}(6,1,7)
$$

sobre la serie original.

Al ajustar este modelo, obtenemos un AIC cercano a:

$$
791
$$

Por lo tanto, este modelo es mejor que el propuesto por `auto_arima`.

Aunque todavía no incorpora una componente estacional, ya presenta un valor de AIC menor.

La pregunta ahora es:

> ¿Podemos mejorar todavía más este modelo incorporando la estructura estacional?

## Estacionariedad de la serie

Sabemos que al aplicar el logaritmo y diferenciar la serie obtenemos una serie aproximadamente estacionaria.

Esto puede observarse visualmente.

Además, podemos confirmarlo mediante la prueba Dickey-Fuller aumentada, ADF.

Al aplicar el test ADF a la serie logarítmica diferenciada, obtenemos un valor p bajo.

Por lo tanto, tenemos evidencia para considerar que la nueva serie es estacionaria.

Esto confirma que:

$$
d=1
$$

El parámetro $d$ indica cuántas veces debemos diferenciar la serie para lograr la estacionariedad.

La serie original no era estacionaria, pero después de una diferenciación obtenemos un comportamiento estacionario.

## Interpretación de la ACF

Volvamos a las gráficas de ACF y PACF.

La función de autocorrelación muestra que existen correlaciones altas aproximadamente cada siete días.

Se observan señales importantes en:

- El rezago 7.
- El rezago 14.
- El rezago 21.

Esto indica la presencia de un ciclo semanal.

Por esa razón, en el modelo SARIMA establecemos:

$$
m=7
$$

Este valor se mantendrá fijo, porque ya identificamos que la periodicidad de la serie puede ser semanal.

## Incorporación de la periodicidad

Si utilizamos el modelo:

$$
\operatorname{ARIMA}(6,1,7)
$$

y únicamente agregamos:

$$
m=7
$$

sin modificar los parámetros estacionales $P$, $D$ y $Q$, obtenemos prácticamente el mismo AIC:

$$
791
$$

Esto significa que indicar solamente la periodicidad no cambia el modelo.

Para que la componente estacional influya realmente, debemos modificar:

- $P$: componente autorregresiva estacional.
- $D$: diferenciación estacional.
- $Q$: componente de media móvil estacional.

## Propuesta de parámetros estacionales

¿Cómo podemos proponer valores para $P$, $D$ y $Q$?

Debemos volver a observar la ACF y la PACF.

Sabemos que la periodicidad ocurre cada siete días.

Además, observamos que los picos estacionales se repiten en varios ciclos.

La ACF nos ayuda principalmente a identificar posibles valores de $Q$, correspondientes a la componente de media móvil estacional.

La PACF nos ayuda a identificar posibles valores de $P$, correspondientes a la componente autorregresiva estacional.

La cantidad de picos significativos que se repiten en los múltiplos de la periodicidad puede orientarnos sobre los órdenes estacionales.

## Primer intento con una componente estacional

Comenzamos incorporando un parámetro estacional igual a uno.

Sin embargo, al ejecutar el modelo obtenemos un error.

¿Por qué ocurre esto?

Porque al incluir una componente estacional con periodo siete, algunos términos pueden superponerse con los rezagos que ya existen en la parte no estacional.

Por ejemplo, si tenemos un término no estacional en el rezago 7 y además un término estacional con periodicidad 7, podemos generar redundancia o problemas de especificación.

Por eso debemos reducir el orden no estacional.

Como la periodicidad es igual a siete, los parámetros no estacionales deberían ser menores que siete para evitar superposiciones directas.

Reducimos entonces el orden autorregresivo no estacional a seis.

## Evaluación de distintos valores de $Q$

Después de ajustar el modelo con esta nueva configuración, obtenemos un AIC cercano a:

$$
803
$$

Puede ser un modelo razonable, pero todavía no supera el valor de 791.

Como en la ACF se observan varios picos estacionales significativos, podemos aumentar el orden $Q$.

### Modelo con $Q=2$

Al establecer:

$$
Q=2
$$

obtenemos un AIC cercano a:

$$
793
$$

El modelo mejora, aunque todavía no supera al modelo ARIMA anterior.

### Modelo con $Q=3$

Después probamos:

$$
Q=3
$$

El ajuste tarda un poco más porque estamos incorporando más parámetros.

El AIC obtenido es cercano a:

$$
792
$$

Seguimos acercándonos al valor del modelo anterior.

### Modelo con $Q=4$

Finalmente, probamos:

$$
Q=4
$$

En este caso obtenemos un AIC cercano a:

$$
789
$$

Con esto logramos mejorar el modelo anterior.

Ahora tenemos un modelo que presenta un AIC menor que:

- El modelo propuesto por `auto_arima`.
- El modelo ARIMA(6,1,7) anterior.

La mejora fue posible gracias a la interpretación de la ACF y a la incorporación de una componente estacional de media móvil con cuatro términos.

## Evaluación de la PACF

Ahora observemos la PACF.

En la gráfica aparece una señal alrededor del rezago 6 y otra señal significativa cerca del rezago 13.

Podríamos pensar que existe una componente autorregresiva estacional que convendría incorporar.

Por eso probamos:

$$
P=1
$$

Sin embargo, el modelo no mejora.

Seguir aumentando $P$ podría mejorar el ajuste, pero también podría empeorarlo o incorporar parámetros innecesarios.

Por tanto, nos quedamos con el modelo anterior.

## Modelo seleccionado

El modelo final seleccionado presenta un AIC cercano a:

$$
789
$$

Este modelo es mejor que:

- El propuesto por `auto_arima`, con AIC cercano a 798 mediante `SARIMAX`.
- El modelo ARIMA anterior, con AIC cercano a 791.

La mejora se logró interpretando:

- La estructura periódica de la ACF.
- La estructura autorregresiva de la PACF.
- Los ciclos de siete días.
- La cantidad de picos estacionales significativos.

## Recomendación sobre `auto_arima`

Mi recomendación es que está bien utilizar `auto_arima`.

Es una herramienta útil porque permite evaluar muchos modelos con pocas líneas de código.

Sin embargo, no debemos depender únicamente de ella.

La atención principal debe estar en:

- La función de autocorrelación.
- La función de autocorrelación parcial.

La ACF ayuda a analizar la componente de media móvil.

La PACF ayuda a analizar la componente autorregresiva.

Cuando observamos ciclos recurrentes en los rezagos, podemos identificar la periodicidad.

Además, la cantidad de ciclos significativos puede ayudarnos a proponer los valores de $P$ y $Q$ de la componente estacional.

## Diagnóstico del modelo

Después de seleccionar el modelo, debemos revisar sus diagnósticos.

### Independencia de los errores

La prueba correspondiente indica que no rechazamos la hipótesis nula de independencia de los errores.

Esto significa que no existe evidencia suficiente de autocorrelación residual.

Por tanto, los residuos se comportan adecuadamente en términos de independencia.

### Heterocedasticidad

La prueba de heterocedasticidad indica que los residuos presentan varianza no constante.

Por lo tanto, existe heterocedasticidad.

### Normalidad de los residuos

La prueba de Jarque-Bera indica que los residuos no siguen una distribución normal.

El principal problema aparece en la curtosis.

Idealmente, la curtosis debería ser cercana a:

$$
3
$$

Sin embargo, los valores obtenidos son mayores.

A pesar de ello, observamos una mejora progresiva entre los distintos modelos.

Por ejemplo, la curtosis fue disminuyendo desde valores cercanos a:

$$
4.11
$$

hasta aproximadamente:

$$
3.95
$$

Aunque todavía no cumple completamente el supuesto de normalidad, el comportamiento mejora.

## Conclusión

El uso de `auto_arima` es una buena forma de comenzar la búsqueda de modelos.

Sin embargo, la interpretación de la ACF y la PACF permite proponer modelos potencialmente mejores.

En este caso, a pesar de que `auto_arima` evaluó una gran cantidad de combinaciones, logramos encontrar un modelo con menor AIC a partir del análisis manual de:

- La periodicidad semanal.
- Los picos recurrentes de la ACF.
- La información entregada por la PACF.
- Los órdenes estacionales $P$, $D$ y $Q$.

Espero que este tutorial sea de mucha utilidad para sus estudios.

Nos vemos en el siguiente.
