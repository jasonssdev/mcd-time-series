# Inferencia estadística de los parámetros de un modelo ARMA

Bienvenidos y bienvenidas a este nuevo video tutorial, donde vamos a hablar sobre la inferencia estadística de los parámetros de un modelo ARMA.

Usted sabrá que, cuando hablamos de inferencia estadística con respecto a los parámetros, detrás de eso existen hipótesis planteadas sobre dichos parámetros.

En particular, tenemos:

- Una hipótesis nula.
- Una hipótesis alternativa.

Nuestro objetivo es tomar decisiones en base a estas dos hipótesis y, para ello, utilizamos un elemento muy importante en esta toma de decisiones: **el valor p**.

Buscamos tomar decisiones a partir de diferentes pruebas estadísticas (*tests*), pero siempre mirando todo esto con altura de miras, porque hay que tener ciertas consideraciones y precauciones cuando se realiza inferencia sobre los parámetros de un modelo ARMA. Justamente eso es lo que vamos a revisar aquí.

Para ello, vamos a considerar uno de los ejemplos que hemos visto en tutoriales anteriores: el modelamiento de la acción de Tesla.

Tenemos la instalación de la librería **Darts** e importamos las librerías correspondientes.

Luego descargamos la serie de la acción de Tesla. Vamos a utilizar el precio de cierre mensual, es decir, datos mensuales.

Aplicamos el logaritmo, posteriormente diferenciamos la serie y obtenemos nuestra serie diferenciada, ya que aquí estamos convirtiéndola en un objeto `TimeSeries` de la biblioteca Darts.

Después realizamos el análisis de la función de autocorrelación (ACF) y de la función de autocorrelación parcial (PACF).

Con esto aplicamos un **Auto ARIMA**, considerando valores de $p$ y $q$ entre 0 y 4.

El resultado fue que el mejor modelo era un **MA(4)**.

¿Y por qué?

Porque obtuvo el menor error cuadrático medio.

Aquí ocurren cosas bastante interesantes.

Por ejemplo, podemos observar los valores de los parámetros, pero estas corresponden únicamente a **estimaciones puntuales**.

Como son estimaciones puntuales, debemos considerar que también poseen variabilidad.

Y esto es muy importante, porque la variabilidad del estimador es precisamente la que respalda la toma de decisiones en las pruebas de hipótesis sobre estos parámetros.

Ahora, si mostramos un resumen del modelo ajustado automáticamente mediante Auto ARIMA, observamos un desglose completo de los coeficientes.

Tenemos:

- Los coeficientes estimados.
- La varianza del ruido ($\sigma^2$).
- La desviación estándar de cada estimador.
- El estadístico de prueba.
- El valor p.
- El intervalo de confianza.

Si observamos los valores p, siempre estaremos interesados en contrastar las siguientes hipótesis:

- **Hipótesis nula ($H_0$):** el parámetro es igual a 0.
- **Hipótesis alternativa ($H_1$):** el parámetro es distinto de 0.

Para tomar la decisión observamos el valor p.

Si el valor p es menor que el nivel de significancia elegido, entonces existe evidencia suficiente para rechazar la hipótesis nula.

En este ejemplo, si observamos los resultados, los tres primeros parámetros presentan valores p mayores que los niveles de significancia habituales del 1 %, 5 % e incluso del 10 %.

Por lo tanto, si tomáramos decisiones únicamente sobre estos parámetros —el MA del rezago 1, el MA del rezago 2 y el MA del rezago 3— deberíamos concluir que son **estadísticamente iguales a cero**.

Por otro lado, el parámetro correspondiente al rezago 4 presenta un valor p prácticamente igual a cero.

Por lo tanto, existe evidencia suficiente para concluir que dicho parámetro es distinto de cero.

Lo mismo ocurre con la estimación de la varianza del ruido blanco.

Aquí es donde uno podría verse tentado a hacer lo siguiente:

> Como estos tres parámetros son significativamente iguales a cero, simplemente los elimino de la ecuación.

Es decir, explicar la serie temporal únicamente mediante el coeficiente asociado al rezago 4, junto con el término de ruido blanco correspondiente.

Sin embargo, hacer eso constituye un error.

Nosotros ya sabemos que ese modelo fue seleccionado como **el mejor modelo**.

Cuando ejecutamos Auto ARIMA, realizamos una inspección de todos los modelos candidatos propuestos a partir del análisis de la ACF y la PACF.

Finalmente concluimos que ese era el modelo que mejor se ajustaba a los datos.

Por lo tanto, eliminar estos parámetros y asumir que son exactamente cero puede empeorar el modelo en lugar de mejorarlo.

Parte de esos parámetros contribuyen a que ese modelo sea precisamente el que presenta el mejor ajuste.

Por ello, esta práctica debe tomarse con mucha precaución.

Es necesario ir más allá y revisar otras pruebas.

## Test de Ljung-Box

Por ejemplo, tenemos el test de Ljung-Box.

Esta prueba entrega un valor p que, en este caso, es prácticamente igual a uno.

¿Y qué nos dice este test?

Principalmente nos indica si existe o no autocorrelación en los residuos.

Si obtenemos un valor p alto, concluimos que **no existe evidencia de autocorrelación en los residuos**, lo cual es una muy buena señal para el modelo.

## Test de Jarque-Bera

Otra prueba importante es la de Jarque-Bera.

Esta prueba evalúa la normalidad de los residuos.

En este ejemplo, el valor p es aproximadamente **0.59**.

Como este valor es alto, no rechazamos la hipótesis nula de normalidad.

Por lo tanto, concluimos que es razonable asumir que los residuos siguen una distribución normal.

## Prueba de heterocedasticidad

Sin embargo, aparece un problema con la heterocedasticidad.

Esta prueba verifica si la varianza de los residuos permanece constante.

En este caso, el valor p es muy pequeño, aproximadamente **0.01**.

Si utilizamos un nivel de significancia del 5 %, debemos rechazar la hipótesis nula.

Esto significa que la varianza **no es constante**, sino que cambia a lo largo del tiempo.

Y ahí encontramos un problema importante.

Por lo tanto, el modelo no está cumpliendo completamente uno de los supuestos esperados para los residuos.

## Reflexión sobre la selección del modelo

En consecuencia, aunque estamos frente a un buen modelo y algunos coeficientes sean estadísticamente iguales a cero, debemos ampliar la perspectiva con la que tomamos la decisión.

Por esta razón, personalmente no recomiendo eliminar automáticamente esos parámetros.

Nosotros ya decidimos previamente que este es un buen modelo.

Si una persona no conociera el procedimiento de Auto ARIMA y simplemente observara la función de autocorrelación, podría concluir que un MA(4) es un buen modelo y verse tentada a eliminar los coeficientes que no resultan significativos.

Sin embargo, yo no lo recomiendo.

Siempre recomiendo verificar primero que los supuestos sobre los residuos se cumplan y, recién después de ello, tomar decisiones.

En este caso, la conclusión sería que el modelo ARMA no es suficiente para capturar completamente los patrones presentes en esta serie temporal.

Hay que recordar que estamos trabajando con una serie financiera correspondiente a una acción bursátil.

Las series financieras suelen ser aplicaciones especialmente complejas.

En la literatura existen modelos mucho más sofisticados que permiten capturar de mejor manera la heterocedasticidad presente en los residuos.

Por ello, siempre debemos realizar una reflexión profunda respecto a los modelos que estamos seleccionando y evitar ciertas prácticas que podrían parecer razonables a primera vista.

Sabemos que algunos parámetros son estadísticamente iguales a cero.

Sin embargo, eliminarlos podría empeorar el desempeño general del modelo.

Este ha sido el video tutorial de hoy.

Espero que haya sido de su agrado y nos vemos en el siguiente.
