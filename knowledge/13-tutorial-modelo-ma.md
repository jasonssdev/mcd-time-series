# Modelo MA o Moving Average

Bienvenidos y bienvenidas a este videotutorial.

En este videotutorial de hoy vamos a hablar sobre el modelo MA o Moving Average, que por su traducción en español vendría siendo un modelo de media móvil.

Este modelo de media móvil es un modelo bastante curioso porque es, primero, un modelo que es estacionario.

Y es un modelo que depende de los errores del pasado para generar una predicción a futuro.

Aquí lo que tenemos nosotros, principalmente en esta ecuación de aquí, es la ecuación de nuestro modelo MA.

## Ecuación del Modelo MA

¿Qué es lo que está diciendo este modelo?

Nos está diciendo que cuando yo quiero predecir una serie en el momento \(t\), esa predicción va a ser igual a una media, \(\mu\), porque es un proceso estacionario.

Pero va a ser una combinación lineal del error que tengo en el momento actual, en el momento \(t\).

Más una combinación lineal de todos los momentos del pasado, asumiendo que este \(\varepsilon_t\) es un ruido blanco.

Entonces, nuestro objetivo en el día de hoy, en este videotutorial, es:

- Simular un modelo MA.
- Calcular su función de autocorrelación.
- Compararla con su función de autocorrelación teórica.
- Sacar conclusiones relevantes.

## Librerías a Utilizar

Para esto vamos a ocupar la librería que hemos estado ocupando desde antes.

Particularmente hemos estado ocupando la librería `darts`, no olvide instalarla.

Y también otra de las librerías que hemos ocupado en su momento es `statsmodels`, que también tiene sus funciones para modelos de serie de tiempo.

## Modelo ARMA(p, q)

Para generalizar un poco, y son cosas que usted va a ver en las próximas semanas, nosotros también tenemos definido lo que llamamos un modelo ARMA(p, q), que es un modelo más general.

El modelo ARMA une dos modelos que nosotros tenemos interés:

- Un modelo autorregresivo.
- El modelo MA, que es modelo de media móvil.

Esta es su ecuación en general.

Entonces, si comparamos con la ecuación anterior, vemos que existe una constante que está relacionada con la media.

Tiene el \(\varepsilon_t\), pero tiene esta parte de aquí.

Fíjense que esta es una combinación lineal de todos los valores de la serie del pasado, más una combinación lineal de todos los errores del pasado.

Si nosotros eliminamos esto de aquí, justamente recuperamos lo que está arriba.

Pero, ¿cuándo pasa ese caso?

Cuando este \(p\) es igual a cero.

O sea, cuando el modelo ARMA es un ARMA(0, q), lo que es equivalente a un MA(q).

Entonces, este es el modelo general.

¿Por qué lo hemos definido ahora?

Porque para hacer la simulación de un modelo MA, tenemos que definirlo a partir de un modelo ARMA en sus parámetros.

## Parámetros para Simular un Modelo ARMA

Ahora, lo que tenemos aquí es equivalente a esta expresión de acá.

¿Cuál es la diferencia?

Que esta parte de aquí, estas sumas que están de los errores del pasado, las hemos pasado restando al otro lado de la ecuación.

Y ahora aparecen estos \(\phi\), aparecen con signo negativo.

Ahora, ¿cuáles vendrían siendo los coeficientes que necesita nuestro comando para generar un modelo ARMA simulado?

Nosotros vamos a ocupar este método que se llama `arma_generate_sample`.

Para esto necesitamos poner dos vectores.

El vector del modelo de la parte autorregresiva va a ser:

\[
[1, -\phi_1, -\phi_2, \ldots, -\phi_p]
\]

Motivado por esto.

Y los coeficientes del modelo MA tienen que ir como:

\[
[1, \theta_1, \theta_2, \ldots, \theta_q]
\]

Entonces, ¿por qué aparecen estos 1 acá?

Esos 1 aparecen porque aquí hay un 1 que no está expresado, pero existe.

Y lo mismo en este \(\varepsilon_t\), también hay un 1 aquí, que es el parámetro que está delante del \(\varepsilon_t\), que no aparece pero existe.

Entonces esos 1 los necesitamos para poder definir nuestro método simulado.

## Simulación de un Modelo MA(2)

Fíjense lo que tenemos acá.

Vamos a generar una semilla.

Esto es principalmente para que usted pueda replicar los resultados que obtenemos.

Vamos a generar el vector de la componente autorregresiva y solamente vamos a poner un 1.

¿Por qué?

Porque estamos asumiendo que no hay término autorregresivo, lo que es equivalente a decir un ARMA(0, q).

En este caso vamos a asumir \(q = 2\).

Entonces, estamos asumiendo ese 1.

Ahora, para la parte de media móvil, tenemos este vector de dimensión 3, que es justamente:

\[
[1, \theta_1, \theta_2]
\]

Y ahí vamos a asumir estos dos valores:

\[
\theta_1 = 0.5
\]

\[
\theta_2 = -0.3
\]

Usted puede modificarlos por si quiere hacer pruebas con otros valores.

Por lo tanto, vamos a ocupar el método que es de la librería `darts`, y le ponemos los input:

- El vector autorregresivo, que no existe una componente autorregresiva, pero lo necesita como input el método.
- El vector MA.
- Vamos a generar una serie temporal de 1000 registros.

Entonces, al hacer la simulación y graficar nuestra serie temporal, esta vendría siendo la forma de una serie que proviene de un modelo ARMA(0, 2).

Una serie estacionaria, una serie que tiene varianza controlada.

Y justamente son las series que nosotros buscamos en todos los tutoriales que hemos visto anteriormente cuando nosotros hacemos las transformaciones.

## Función de Autocorrelación

Perfecto, entonces, ¿qué hacemos ahora?

Vamos a asumir que esto es una serie que tenemos registrada a partir de algún fenómeno y nosotros la queremos analizar.

Entonces, uno de los análisis que nosotros hacemos usualmente es graficar su función de autocorrelación.

Para esto vamos a generar un índice que lo solicita la librería `darts` para ocupar el `plot_acf`.

Y vamos a convertir los datos que hemos simulado desde un objeto de serie de tiempos de `darts`.

Después vamos a hacer el gráfico de nuestra función de autocorrelación.

¿Qué es lo que pasa aquí?

Fíjense que tenemos que la autocorrelación en 0 es 1, como lo es por definición.

Pero tenemos estos dos lags aquí que sobresalen:

- El lag 1.
- El lag 2.

La autocorrelación en 1 y la autocorrelación en 2.

Y el resto está muy dentro de esta banda que podrían considerarse 0, a excepción de este valor de aquí.

Pero no sobresale tanto como estas dos barras que es bastante notorio.

## Autocorrelación Teórica de un MA(2)

Entonces, ¿qué es lo que pasa con lo que deberíamos obtener de forma teórica?

De forma teórica, la autocorrelación para un modelo MA(2) debe tener las siguientes características.

Una, que la autocorrelación en 0 debe ser 1 por definición.

Y la autocorrelación en 1 y en 2 dependen de los parámetros que nosotros le hemos puesto a nuestra serie simulada.

Entonces, fíjense que si nosotros reemplazamos estos dos valores que hemos puesto en la simulación, nosotros tenemos que:

\[
\rho_1
\]

teórico, la autocorrelación con lag 1 teórico, debe ser aproximadamente:

\[
0.26
\]

Y la autocorrelación con lag 2 debe ser aproximadamente:

\[
-0.2239
\]

Pero estos valores son los valores teóricos.

Si nosotros miramos la autocorrelación que tenemos acá, tenemos que en el lag 1 anda muy cercano a 0.26.

Y en el lag 2 anda muy cercano a -0.22, incluso es un poquito menos.

Pero estos dos valores son las partes de la autocorrelación muestral, no la autocorrelación poblacional, como se conoce la autocorrelación teórica.

Porque estos son los valores de la autocorrelación.

Ahora, se espera que nosotros tengamos estos valores cercanos.

¿Por qué?

Porque es una serie simulada.

Pero, ¿dónde se ocurre esta diferencia?

Obviamente ocurre la diferencia por la estimación que hemos obtenido para \(\theta_1\) y para \(\theta_2\).

## Estimación de Parámetros del Modelo MA

Entonces, ¿cuáles son los valores de \(\theta_1\) y \(\theta_2\) estimados para nuestra serie simulada?

Para eso, vamos a ocupar el método de `darts` que se llama `ARIMA`.

`ARIMA` es una extensión más del modelo ARMA, pero donde existe un nuevo parámetro que es el \(d\).

En el caso de un media móvil vendría siendo 0, al igual que en la parte autorregresiva también tiene un parámetro 0.

Pero en este caso vamos a poner que la componente media móvil tiene un retraso de hasta dos lags del pasado.

Entonces, ajustamos el modelo MA y a eso hacemos el ajuste a nuestra serie simulada.

Con esta parte de aquí podemos ver cuáles son los parámetros estimados para nuestra serie simulada.

Entonces, fíjense que tenemos un vector de cuatro componentes.

El primer componente representa la estimación de la media, que es justamente este \(\mu\) que aparece aquí, o la constante, porque es un proceso estacionario.

Y si nosotros miramos nuestra gráfica vemos que está centrado alrededor de 0.

Por lo tanto, tiene sentido el valor que nosotros obtenemos como esa estimación.

El otro valor que obtenemos es la estimación para \(\theta_1\), que nos da:

\[
0.4967
\]

Y el valor que nosotros habíamos dejado fijo en el inicio en la simulación era:

\[
0.5
\]

El más cercano.

Y el otro valor que tenemos aquí es \(\theta_2\), la estimación para \(\theta_2\), y que nos da:

\[
-0.33
\]

Que también anda muy cercano al:

\[
-0.3
\]

que nosotros habíamos definido en un inicio como un input en nuestra simulación.

La pregunta final para este tutorial es qué representa este valor de aquí:

\[
0.9712
\]

Y es justamente la estimación de \(\sigma^2\), que es la estimación de la varianza de nuestro ruido blanco.

## Conclusión

Por lo tanto, ahí tenemos todos los parámetros identificados para nuestra serie y que nos permite hacer predicciones a futuro.

Tenemos estimado cuánto es la media de la serie.

Tenemos estimado cuánto es \(\theta_1\).

Tenemos estimado cuánto es \(\theta_2\).

Y también tenemos estimado cuánto es la varianza de nuestro ruido blanco.

Con eso tenemos todo identificado para hacer predicciones a futuro.

Espero que este tutorial haya sido de su agrado y nos vemos en el siguiente.
