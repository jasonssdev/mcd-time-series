# Ayudantía 3: modelado de los residuos y comparación de modelos ARMA

## Análisis de los residuos

Vamos ahora con la parte de los residuos.

En muchas ocasiones, la estructura de correlación todavía permanece en la parte aleatoria de la serie.

Voy a graficar los residuos.

Normalmente, lo que uno espera es que estos residuos se comporten como ruido blanco.

## ¿Qué es el ruido blanco?

Seguramente este concepto ya lo han visto, pero voy a realizar un repaso general.

Una serie o un proceso de ruido blanco no presenta un patrón temporal y no contiene una estructura de correlación.

Sus valores son, básicamente, aleatorios.

En el contexto de los residuos, queremos que estos se comporten como ruido blanco, porque eso significaría que el modelo ya capturó la estructura importante de la serie.

Formalmente, un proceso de ruido blanco cumple las siguientes condiciones:

$$
E(\varepsilon_t)=0
$$

$$
\operatorname{Var}(\varepsilon_t)=\sigma^2
$$

$$
\operatorname{Cov}(\varepsilon_t,\varepsilon_{t-k})=0
\qquad \text{para } k\neq 0
$$

Es decir:

- La esperanza de los residuos en el tiempo debe ser igual a cero.
- La varianza debe ser constante.
- La covarianza entre un residuo en el tiempo $t$ y otro residuo en el tiempo $t-k$ debe ser igual a cero.

En otras palabras, no debe existir correlación entre los residuos de distintos periodos.

Al observar la gráfica, uno podría pensar que la esperanza es cercana a cero y que la varianza parece relativamente constante.

Sin embargo, necesitamos evaluar formalmente si estos datos presentan o no una estructura de correlación.

## Test de Ljung-Box

Para eso podemos aplicar el test de Ljung-Box.

Este test nos permitirá determinar si los datos y, en este caso particular, los residuos, se comportan como ruido blanco.

Estoy utilizando la función de Ljung-Box e ingresando los residuos.

Voy a evaluar diez rezagos.

Este valor puede modificarse. Por ejemplo, podríamos considerar:

- 10 rezagos.
- 12 rezagos.
- 24 rezagos.

Como la serie es mensual, también tendría sentido analizar 12 o 24 rezagos.

En este caso, el estadístico obtenido es aproximadamente:

$$
75.62
$$

y el valor p es muy cercano a cero.

La hipótesis nula del test establece que los residuos no presentan autocorrelación, es decir, que se comportan como ruido blanco.

Como el valor p es menor que un nivel de significancia del 5 %, rechazamos la hipótesis nula.

Por lo tanto, existe evidencia estadística para concluir que la serie de residuos no es ruido blanco.

Si no hay ruido blanco, significa que los residuos todavía contienen alguna estructura de correlación.

Entonces podemos continuar con el análisis mediante las gráficas de:

- La función de autocorrelación, ACF.
- La función de autocorrelación parcial, PACF.

## Interpretación de la ACF

Veamos primero la función de autocorrelación.

El valor en el rezago cero siempre será igual a uno, porque corresponde a la correlación de la serie consigo misma.

La función de autocorrelación muestra el grado de correlación que existe entre un dato en el tiempo $t$ y los valores anteriores de la serie.

Por ejemplo, en el primer rezago se analiza la relación entre:

$$
X_t
\quad \text{y} \quad
X_{t-1}
$$

En la gráfica, el primer rezago no parece ser claramente significativo.

Esto podría indicar que el valor en $t-1$ no está aportando demasiada correlación a los datos.

Sin embargo, habría que estudiarlo con cuidado, porque está cerca del límite de significancia.

El segundo rezago tampoco parece contener una correlación importante.

En cambio, los rezagos 3, 4, 5 y 6 sí parecen significativos.

Esto indica que el valor en el tiempo $t$ tiene cierto grado de correlación con los valores observados en:

$$
t-3,\quad t-4,\quad t-5,\quad t-6
$$

Eso es importante.

Visualmente, podemos observar que los residuos todavía contienen una estructura de correlación.

Por lo tanto, esto coincide con el resultado del test de Ljung-Box, que indicaba que los residuos no se comportaban como ruido blanco.

También podemos prestar atención al rezago 12.

A pesar de que intentamos eliminar la estructura estacional, todavía aparece una señal en torno al mes 12.

Esto podría indicar que todavía permanece algún patrón estacional en los residuos.

## Interpretación de la PACF

Ahora vamos a analizar la función de autocorrelación parcial.

El primer rezago de la ACF y de la PACF siempre será el mismo.

A partir del segundo rezago empiezan a diferenciarse.

La PACF mide la correlación directa entre dos observaciones, eliminando el efecto de los rezagos intermedios.

Por ejemplo, para el rezago 2 se analiza la relación entre:

$$
X_t
\quad \text{y} \quad
X_{t-2}
$$

eliminando el efecto correspondiente a:

$$
X_{t-1}
$$

Para el rezago 3 se analiza la relación entre:

$$
X_t
\quad \text{y} \quad
X_{t-3}
$$

eliminando la estructura de correlación asociada a:

$$
X_{t-1}
\quad \text{y} \quad
X_{t-2}
$$

Y así sucesivamente.

En esta gráfica se observa que los rezagos 3, 4, 5, 6, 7 y 8 parecen significativos para la función de autocorrelación parcial.

## Propuesta de órdenes para un modelo ARMA

Ahora vamos a realizar algunos ejercicios.

Recuerden que, de manera general:

- La PACF nos ayuda a proponer el componente autorregresivo.
- La ACF nos ayuda a proponer el componente de media móvil.

A partir de la PACF, podríamos pensar en un componente autorregresivo con hasta ocho rezagos.

Es decir, podríamos considerar:

$$
p=8
$$

Para el componente de media móvil podríamos considerar, por ejemplo, hasta seis o siete rezagos.

Es decir:

$$
q=6
$$

o

$$
q=7
$$

Voy a utilizar distintos ejemplos para observar cómo se comportan los modelos a medida que aumentamos sus órdenes.

## Ajuste de un modelo ARMA(8,6)

Voy a considerar ocho parámetros para la parte autorregresiva.

Como no utilicé diferenciación en este procedimiento, el valor de $d$ será igual a cero.

Para la parte de media móvil utilizaré seis parámetros.

Por tanto, estoy ajustando los residuos mediante un modelo ARMA, aunque la función utilizada corresponde a ARIMA.

El modelo puede escribirse como:

$$
\operatorname{ARIMA}(8,0,6)
$$

Voy a ajustarlo y después voy a obtener el resumen del modelo.

Como tenemos ocho parámetros autorregresivos y seis parámetros de media móvil, el proceso de estimación puede ser más complejo.

## Resultados del modelo

En el resumen podemos observar:

- El modelo ajustado.
- El número de observaciones.
- La log-verosimilitud.
- Los coeficientes estimados.
- Los valores p.
- Los criterios de información.
- Las pruebas de diagnóstico.

El número de observaciones es 396.

Los modelos de Box-Jenkins se ajustan bajo determinados supuestos y tienen asociada una función de verosimilitud.

A partir de la log-verosimilitud podemos obtener métricas como:

- AIC.
- BIC.
- HQIC.

También aparece una constante, que actúa de manera similar a un intercepto.

## Significancia de los parámetros autorregresivos

La constante no resulta significativa.

El parámetro AR(1) tampoco es significativo.

El parámetro AR(2) tampoco es significativo.

En general, varios de los primeros parámetros autorregresivos presentan valores p altos.

Esto significa que, bajo las pruebas individuales, no tenemos evidencia estadística suficiente para afirmar que esos parámetros son distintos de cero.

Por ejemplo, algunos parámetros empiezan a presentar valores p menores a medida que aumentan los rezagos.

Uno de ellos podría llegar a ser significativo utilizando un nivel de significancia del 10 %.

Sin embargo, varios valores siguen siendo relativamente altos.

En términos generales, los componentes autorregresivos no permiten rechazar la hipótesis nula de que sus coeficientes sean iguales a cero.

## Significancia de los parámetros de media móvil

En el componente de media móvil ocurre algo similar.

Varios parámetros no resultan significativos.

Uno de los parámetros, alrededor del quinto rezago, sí parece ser significativo.

La estimación de la varianza del ruido, $\sigma^2$, también resulta significativa.

## Diagnóstico de ruido blanco

En el resumen también aparece el test de Ljung-Box.

Inicialmente parecía que el test seguía rechazando la hipótesis nula, pero debemos observar correctamente el valor p.

El valor p es mayor que:

$$
0.05
$$

Por tanto, ya no rechazamos la hipótesis nula.

Esto indica que, después de ajustar este modelo, los residuos sí pueden considerarse aproximadamente ruido blanco.

El modelo está eliminando la estructura de correlación que permanecía en los residuos.

Esto es importante.

## Diagnóstico de normalidad

También aparece el test de Jarque-Bera, que evalúa la normalidad de los residuos.

En este caso, el resultado indica que los residuos no cumplen completamente el supuesto de normalidad.

El coeficiente de asimetría es aproximadamente:

$$
0.58
$$

Idealmente, debería ser cercano a cero.

La curtosis debería ser cercana a:

$$
3
$$

Sin embargo, esto tampoco se cumple completamente.

Estas características pueden explicar el rechazo de la hipótesis nula de normalidad en el test de Jarque-Bera.

## Criterio AIC

El valor del AIC para este modelo es aproximadamente:

$$
2191
$$

Este criterio puede utilizarse para comparar el modelo con otras alternativas.

Mientras menor sea el AIC, mejor será el equilibrio entre:

- La calidad del ajuste.
- La cantidad de parámetros utilizados.

## Ajuste de un modelo ARMA(2,2)

Ahora, solamente como ejercicio, voy a ajustar un modelo ARMA(2,2).

Este modelo puede escribirse como:

$$
\operatorname{ARIMA}(2,0,2)
$$

En este caso, los dos parámetros autorregresivos resultan significativos.

Los parámetros del componente de media móvil también resultan significativos.

Los residuos pueden considerarse ruido blanco.

Sin embargo, todavía no se cumple completamente el supuesto de normalidad.

El AIC obtenido es aproximadamente:

$$
2194
$$

Este valor es ligeramente mayor que el del modelo anterior.

## Ajuste de un modelo ARMA(3,3)

Ahora voy a ajustar un modelo ARMA(3,3):

$$
\operatorname{ARIMA}(3,0,3)
$$

En este modelo, algunos estimadores empiezan a perder significancia.

Esto ocurre tanto en la parte autorregresiva como en la parte de media móvil.

La estimación de $\sigma^2$ sigue siendo significativa.

Los residuos todavía pueden considerarse ruido blanco.

Sin embargo, el AIC aumenta considerablemente.

El valor obtenido es aproximadamente:

$$
2305
$$

Este resultado es peor que los anteriores.

## Ajuste de un modelo ARMA(4,4)

También podemos probar un modelo ARMA(4,4):

$$
\operatorname{ARIMA}(4,0,4)
$$

El AIC obtenido es aproximadamente:

$$
2184
$$

Los parámetros del componente autorregresivo resultan significativos.

En cambio, los parámetros del componente de media móvil no resultan significativos utilizando un nivel del 5 %.

Esto es interesante.

A pesar de ello, el valor del AIC indica que, entre los modelos comparados, este podría ser uno de los mejores.

## Modelo sin estructura de correlación

Finalmente, podríamos ajustar un modelo que solamente utilice una media constante y no incorpore ningún grado de correlación.

Sin embargo, este modelo probablemente no será competitivo.

La razón es que ya sabemos que la estructura inicial de los residuos contiene correlación.

Por tanto, un modelo que ignore completamente esa dependencia temporal no capturará adecuadamente la dinámica de los datos.

## Selección del modelo

En conclusión, yo me quedaría con el modelo que presenta el mejor equilibrio entre:

- Un valor bajo de AIC.
- Residuos que se comporten como ruido blanco.
- Una estructura razonable de parámetros.
- Una adecuada representación de la dependencia temporal.

Con este modelo estamos intentando capturar:

- La estructura autorregresiva.
- La estructura de media móvil.
- La correlación presente en los residuos.

Una vez ajustado el modelo, tendríamos que generar la predicción correspondiente al componente residual.

Después, esta predicción se podría sumar a:

- La predicción de la tendencia.
- La predicción de la estacionalidad.

De esta manera obtendríamos la predicción final:

$$
\widehat{Y}_t
=
\widehat{T}_t
+
\widehat{S}_t
+
\widehat{R}_t
$$

Esto también se revisó en la Ayudantía 2 y es un procedimiento que ya se puede implementar.

En conclusión, las ayudantías 2 y 3 presentan diferentes herramientas y enfoques para modelar una serie temporal.

## Pregunta sobre diferenciación

—Consulta. En vez de descomponer la serie en tendencia, estacionalidad y residuo, ¿la tendencia la podríamos haber eliminado diferenciando una vez?

—Exacto, sí.

—Y ahí iríamos por otro camino. ¿No tendríamos que ajustar un polinomio?

—Exactamente. Ese es otro camino.

En ese caso, toda la parte de la tendencia se incorpora mediante la diferenciación y el modelado se carga directamente al modelo ARIMA.

Claramente, el orden del modelo ARIMA también cambiaría, porque diferenciar la serie no es equivalente a eliminar por separado:

- La tendencia.
- La estacionalidad.

Por tanto, existen diferentes estrategias.

Una estrategia consiste en modelar los datos de manera estructural desde el inicio:

1. Modelar la tendencia.
2. Modelar la estacionalidad.
3. Modelar los residuos.

Otra estrategia consiste en diferenciar la serie y cargar toda la estructura restante a un modelo ARIMA.

También podría existir una tercera estrategia:

- Modelar la tendencia.
- Modelar la estacionalidad.
- Incorporar la parte autorregresiva directamente en otro tipo de modelo.

Eso lo veremos en la siguiente clase.

—¿Ahí quedó claro, Emilio?

—Sí, sí, claro.

—Súper.

## Consulta sobre los grupos

—¿Alguna otra consulta?

Voy a dejar de compartir.

—¿Emilio?

—¿Se me escucha?

—Sí, te escucho.

—Tengo una pregunta sobre los grupos. En la semana 6 creo que hay una actividad que dice “Conoce tu grupo”, pero me aparece un error. No sé si será porque no tengo grupo o si ya debería tener uno.

—Gracias, Diego, por la consulta.

Como mencioné al inicio de la clase, los grupos ya están creados y asignados.

Las personas que se inscribieron mediante el enlace con su grupo ya tienen su grupo asignado.

Quienes no se inscribieron también tienen grupo, pero fueron distribuidos de manera aleatoria.

El problema corresponde únicamente a la configuración de la actividad en la plataforma.

## Discusión sobre una serie temporal de vuelos

—Tengo unos datos en minutos. El negocio sabe que esto tiene una tendencia y una estacionalidad.

La estacionalidad es clara durante los doce meses del año.

También existe una tendencia porque la puntualidad ha ido aumentando a lo largo del tiempo, debido a que aumenta el tráfico aéreo.

Cuando modelo la puntualidad o el atraso de un vuelo particular, sé que existe un componente de serie temporal por estas razones.

Actualmente lo estoy modelando mediante XGBoost.

Yo sé que ese modelo no captura bien la estacionalidad y la tendencia.

¿Cómo podría aprovechar esta estructura temporal en los datos y después aplicar cualquier otro modelo a los residuos?

—¿Tus datos son diarios o mensuales?

—Son vuelo a vuelo. En un día tengo muchos vuelos.

—Entonces podrías generar un dato diario de puntualidad.

—Sí, también podría ser mensual o semanal. Puedo agregarlo según lo que necesite.

—¿Has graficado la ACF o la PACF de la serie?

—No. Todavía no. Está todo en una etapa exploratoria.

—Perfecto. Lo primero que tendrías que hacer es graficar la ACF y la PACF de la serie original, sin diferenciar.

Probablemente observarás que la serie no es estacionaria.

A partir de ahí tienes dos caminos.

### Camino 1: diferenciación

Puedes diferenciar la serie.

Después de diferenciarla, puedes volver a graficar:

- La ACF.
- La PACF.

A partir de estas gráficas podrías intentar ajustar un modelo ARIMA.

### Camino 2: descomposición estructural

También puedes aplicar el procedimiento que utilizamos hoy:

1. Modelar la tendencia.
2. Modelar la estacionalidad.
3. Modelar los residuos con un ARMA.

Si la tendencia es creciente, tal vez podrías utilizar:

- Una regresión lineal simple.
- Una regresión polinomial de grado 2 como máximo.

Para la parte estacional, podrías utilizar un procedimiento sencillo, como calcular promedios mensuales.

Finalmente, la parte residual podría modelarse mediante un modelo ARMA.

Este podría ser un enfoque conveniente para tu problema.

## Pregunta sobre la agregación de los vuelos

—Para la parte de *feature engineering*, ¿recomiendas calcular el promedio diario o la mediana?

—Eso depende de la distribución de tus datos.

Si los datos diarios son muy asimétricos o existen valores extremos, probablemente sea mejor utilizar la mediana.

La media es muy sensible a los valores extremos.

Por tanto, primero tendrías que explorar la distribución de los datos.

## Frecuencia temporal y unidad de análisis

—Permiso. Respecto a la idea del compañero, ¿no podría utilizar como índice la fecha completa, incluyendo día, mes, año y hora?

Así podría mantener todos los vuelos sin calcular un promedio diario.

—Creo que primero hay que definir qué se quiere modelar y cuál será la unidad de análisis.

Modelar cada vuelo de manera individual podría ser demasiado complejo, porque hay muchos vuelos diarios.

Probablemente sea más práctico generar una medida representativa diaria.

También hay que considerar la recurrencia de los vuelos.

Por ejemplo, si un vuelo:

- Tiene el mismo origen.
- Tiene el mismo destino.
- Sale todos los lunes.
- Sale siempre alrededor de las 7 de la mañana.

Entonces existe un comportamiento repetitivo que permite identificar ese vuelo en particular.

En ese caso, la componente estacional podría ser semanal.

—Yo también pensaría que, para los vuelos, el comportamiento puede ser más semanal que diario.

Por ejemplo, un vuelo que sale los viernes a las 7 u 8 de la noche podría repetirse de manera similar una semana después.

Por tanto, los datos podrían presentar una estacionalidad semanal.

—Eso es muy importante.

La frecuencia de los datos determina cómo debemos interpretar la ACF y la PACF.

En una serie mensual, una estacionalidad anual aparece cada doce meses.

Por eso, un patrón importante alrededor del rezago 12 puede indicar comportamiento estacional.

Si los datos son diarios y el patrón es semanal, entonces deberíamos observar señales alrededor del rezago 7.

Eso significaría que el comportamiento de un lunes podría relacionarse con el lunes anterior.

Por tanto, la unidad de medida y la frecuencia determinan cómo se interpreta la estacionalidad.

## Diferentes tipos de estacionalidad

Cada serie puede presentar una periodicidad distinta.

Por ejemplo:

- Una serie diaria puede tener estacionalidad semanal.
- Una serie semanal puede tener estacionalidad mensual o anual.
- Una serie mensual puede tener estacionalidad anual.
- Una serie quincenal puede presentar patrones cada quince días.

Por eso, el primer paso consiste en identificar las frecuencias presentes en los vuelos y agruparlos de una manera coherente.

Eso podría simplificar considerablemente el modelado de la serie temporal.

—Muchas gracias.

Es un problema difícil porque existen muchas frecuencias de vuelos.

Además, en mi caso, la predicción es a largo plazo.

Por eso, quizá una agregación mensual por aeropuerto podría ser útil.

Estoy pensando y explorando ideas.

—Podrías probar también otro tipo de modelo. Creo que podría funcionar bastante bien.

—No conozco ese modelo.

## Cierre de la ayudantía

—Bien, ¿existe alguna otra consulta?

—De mi parte, nada. Muchas gracias, profesor, por la ayudantía.

—Perfecto. Gracias a ti por participar.

Nos vemos de aquí a dos semanas.

Respecto de los grupos, como les mencioné, espero que el problema se solucione pronto.

Si hay algún anuncio importante, se les comunicará mediante la plataforma.

Que estén bien.

Nos vemos en dos semanas y no se olviden de que tienen un laboratorio que ya está cerca.

Nos vemos.

Gracias.

Chau.