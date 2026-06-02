# Funciones de autocorrelación muestral y test de blancura

Bienvenidos y bienvenidas a una nueva clase.

Las series de tiempo exhiben diferentes tipos de patrones. Algunas de ellas presentan una tendencia lineal y/o estacionalidad.

En estos casos, parece natural pensar que la información pasada sirve para predecir el futuro, es decir, cabe esperar que la correlación no debería ser despreciable.

Sin embargo, para las series que no presentan tendencia, debemos cuantificar la correlación a diferentes instantes de tiempo, y decidir si dicha dependencia es o no despreciable.

En esta clase, veremos cómo cuantificar la autocorrelación, así como también responder a la pregunta si dicha correlación es significativa.

En esta clase, se revisarán los siguientes temas:

1. Función de autocorrelación.
2. Función de autocorrelación parcial.
3. Test de blancura.

---

## Tema 1: Función de autocorrelación

Dada una serie de tiempo $X_1$ hasta $X_n$, la función de autocorrelación muestral cuantifica la correlación de la serie a diferentes *lag* de tiempo $h$.

Es decir, calcula la correlación entre $X_t$ y $X_{t+h}$.

¿Cómo?

$$
\hat{\\rho}(h) = \frac{\hat{\\Gamma}(h)}{\hat{\\Gamma}(0)}
$$

$\hat{\\Gamma}(h)$ está dada por la siguiente expresión, donde $\hat{\\Gamma}(h)$ se denomina **función de autocovarianza muestral**.

Evidentemente, $\hat{\\rho}(h)$ pertenece al intervalo $[-1, 1]$, donde $\hat{\\rho}(0) = 1$, pues es la correlación de un vector consigo mismo.

Además, $\hat{\\rho}(h) = 0$ implica que para ese *lag* $h$ la serie no presenta correlación.

Así, un ruido aleatorio debería tener autocorrelación 0 para todo $h$ distinto de 0.

Por lo que una serie de tiempo presentará estructura de dependencia temporal si la función de autocorrelación muestral presenta valores estadísticamente distintos de 0, para al menos un valor de $h$ distinto de 0.

Se tiene que las autocorrelaciones muestrales son estadísticamente diferentes de 0 si el valor absoluto de $\hat{\\rho}(h)$ es mayor a:

$$
\frac{1,96}{\sqrt{n}}
$$

Donde $n$ es la cantidad de datos de la serie.

Por ejemplo, la gráfica muestra la serie $X_t$ de tamaño 200, la cual no presenta tendencia y una variabilidad prácticamente constante, por lo que esta serie puede ser confundida con un ruido.

Sin embargo, al analizar la función de autocorrelación muestral, **ACF**, se observan varios valores fuera de los límites:

$$
\pm \frac{1,96}{\sqrt{200}}
$$

La primera barra corresponde a $h = 0$ y, por lo tanto, vale 1.

Para $h = 1$:

$$
\hat{\\rho}(1) = 0,6068
$$

Y para $h = 2$:

$$
\hat{\\rho}(2) = 0,2629
$$

Son los dos *lag* más importantes.

Aunque para $h = 4, 5, 6, 16, 17$ y $18$, los valores de la autocorrelación se escapan levemente de la banda de confianza en torno al 0.

Consideremos ahora la siguiente gráfica que contiene la serie de tiempo $Y_t$ y su ACF.

La serie $Y_t$ presenta una clara tendencia al alza y una varianza no constante. En este caso, la ACF decae lentamente y recién en el *lag* 20 el valor está dentro de los límites:

$$
\pm 0,1386
$$

Esta es una característica de las series con tendencia y en el modelado de serie de tiempo.

Dicha tendencia debe ser eliminada, ya sea de forma determinista o bien a través de diferenciaciones.

La siguiente figura muestra la serie diferenciada y su respectiva ACF.

La serie diferenciada muestra un patrón similar al primer ejemplo, es decir, sin tendencia y con varianza constante.

Del mismo modo, ahora la ACF tiene un comportamiento similar al primer ejemplo, solo con algunos *lag* estadísticamente diferentes de 0.

Prueba tu conocimiento respondiendo la siguiente pregunta.

---

## Tema 2: Función de autocorrelación parcial

Dada una serie de tiempo $X_1$ hasta $X_n$, la función de autocorrelación parcial muestral, **PACF**, cuantifica la correlación de la serie a diferente *lag* de tiempo $h$, quitando el efecto de las observaciones intermediarias.

Es decir, cuantifica la correlación entre $X_t$ y $X_{t+h}$, dado $X_{t+1}$ hasta $X_{t+h-1}$.

Para entregar una definición formal de la PACF, considere para $h \geq 2$ las siguientes regresiones para $X_{t+h}$ y $X_t$, respectivamente.

Es decir, $X_{t+h}$ y $X_t$ son explicados por $X_{t+1}$ hasta $X_{t+h-1}$, a través de una regresión lineal, donde los coeficientes de regresión por estacionalidad son los mismos.

Luego se define la PACF, denotada por $\hat{\\phi}_{h,h}$, como la correlación entre los residuos de las dos regresiones anteriores.

Detengámonos en algunas observaciones relevantes respecto a la autocorrelación parcial.

En primer lugar, notar que para $h = 1$ no hay intermediario, por lo que la autocorrelación parcial y la autocorrelación simple coinciden por definición.

Análogamente, el criterio para definir si una autocorrelación parcial es estadísticamente diferente de 0 es el mismo, es decir, si $\hat{\\phi}_{h,h}$ es mayor a:

$$
\frac{1,96}{\sqrt{n}}
$$

Por ejemplo, para la serie $X_t$, la gráfica muestra la serie junto a su PACF, donde se puede apreciar que los primeros tres *lag* están fuera de los límites.

Y para $h = 1$:

$$
\hat{\\phi}_{1,1} = 0,6068 = \hat{\\rho}(1)
$$

Mientras que para $h = 2$:

$$
\hat{\\phi}_{2,2} = -0,1667
$$

El cual es totalmente diferente a $\hat{\\rho}(2)$, que era igual a 0,2629. Incluso cambia el signo.

A partir de este ejemplo, es evidente que ambas funciones de autocorrelación capturan información diferente de la serie del tiempo, y para el modelado de dicha serie las dos son muy importantes.

En el caso de la serie $Y_t$ del segundo ejemplo, la gráfica muestra la serie original y su PACF.

Destaca que la tendencia de la serie no tiene el mismo efecto en comparación con la ACF.

Ahora bien, sí existe un efecto visual y es que $\hat{\\phi}_{1,1}$ es muy cercano a 1, que es el límite superior para las autocorrelaciones, y el resto está prácticamente contenido dentro de los límites.

Este es otro indicio de que la serie presenta algún tipo de tendencia, por lo que debemos diferenciarla.

Aunque más adelante veremos una prueba estadística que nos diga si es necesario o no diferenciarla.

La siguiente figura muestra la serie $\nabla Y_t$ y su respectiva PACF, donde se observa que solo los primeros dos *lag* son claramente diferentes de 0.

Note que la PACF de la serie diferenciada no es exactamente igual a la PACF de la serie original.

Prueba tu conocimiento respondiendo la siguiente pregunta.

---

## Tema 3: Test de blancura

Un test de blancura busca determinar si una serie de tiempo es o no un ruido blanco.

Este último se define como una secuencia independiente e idénticamente distribuida, de media 0 y varianza constante, denotada por:

$$
X_t \sim IID(0, \sigma^2)
$$

Y diremos que el ruido blanco es gaussiano si la distribución corresponde a la distribución normal.

Como los $X_t$ son independientes, en particular, tanto la autocorrelación simple como parcial deberían ser 0 para todo $h$ distinto de 0.

Así, un ruido blanco $\epsilon_t$ debe estar centrado en 0, con varianza constante y funciones de autocorrelación simple y parcial sin *lag* significativos, tal como se muestra en la figura.

No obstante, lo anterior es solo una representación visual, por lo que una prueba de hipótesis que nos asegure que una serie sea o no un ruido blanco es de vital importancia.

Este tipo de prueba se denominan **test de blancura** o **test de portmanteau**, de los cuales existen varias alternativas, tales como:

- La prueba de Breusch-Godfrey.
- La prueba de Durbin-Watson.
- La prueba de Box-Pierce-Ljung.

Todas enfocadas en los residuos de un modelo de serie de tiempo, pero se pueden aplicar a una serie directamente para determinar si vale la pena ajustar un modelo a los datos.

Específicamente, la prueba de Box-Pierce-Ljung considera como hipótesis nula $H_0$:

$$
H_0: \text{los residuos son no correlacionados}
$$

Contra la hipótesis alternativa $H_1$:

$$
H_1: \text{los residuos tienen correlación}
$$

El estadístico de prueba $Q$ depende de la función de autocorrelación $\hat{\\rho}_e(h)$, para $h = 1$ hasta $H$, y tiene una distribución asintótica chi-cuadrado.

En la práctica, se determina el p-valor de la prueba para diferentes valores de $H$, el cual varía desde 1 hasta, típicamente, 20, o bien $n/4$.

Si algún p-valor es menor a 0,05, nivel de significancia generalmente utilizado, se rechaza la hipótesis nula, evidenciando que los residuos o series presentan autocorrelación estadísticamente significativa.

Al aplicar la prueba de Box-Pierce-Ljung a la serie $X_t$, se obtiene que para todo $h$, el p-valor es prácticamente 0, por lo que se rechaza la hipótesis nula de ruido blanco.

Mientras que para la serie $\epsilon_t$, pasa justamente lo opuesto, ya que en todos los casos los p-valores son muy grandes.

Por lo que no existe suficiente evidencia para rechazar la hipótesis de ruido blanco.

Prueba tu aprendizaje respondiendo la siguiente pregunta.

---

## Cierre de la clase

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

Las funciones de autocorrelación muestral, simple y parcial son una herramienta que nos permiten visualizar la estructura de correlación presente en la serie de tiempo.

Si una serie de tiempo presenta tendencia, la función de autocorrelación decae muy lentamente a 0.

Antes de analizar la ACF y PACF, se debe quitar, si es que hubiere, la tendencia de la serie.

La prueba de blancura de Box-Pierce-Ljung nos permite chequear si la serie analizada presenta o no autocorrelación.