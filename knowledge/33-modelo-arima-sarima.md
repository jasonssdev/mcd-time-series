# Modelos ARIMA y SARIMA

Bienvenidos y bienvenidas a una nueva clase.

Los modelos ARMA son una buena alternativa para modelar series estacionarias. Sin embargo, en la práctica, muchas series de la vida real no son estacionarias, ya que incluyen tendencia y/o componentes periódicos.

Desde la perspectiva de análisis vista hasta este momento, es necesario remover las posibles tendencias y/o componentes periódicos, y ajustar un modelo ARMA a la serie resultante, sin tendencia y sin componente periódica.

No obstante, dicho procedimiento no es único, ya que también vimos que es posible eliminar la tendencia y/o la componente periódica aplicando diferenciaciones.

Ahora revisaremos cómo integrar las diferenciaciones en los modelos ARMA.

En esta clase se revisarán los siguientes temas:

- **Tema 1:** Modelos ARIMA y SARIMA.
- **Tema 2:** Estimación y predicción en modelos SARIMA.
- **Tema 3:** Pruebas de no estacionariedad.

## Tema 1. Modelos ARIMA y SARIMA

Para comprender el modelo ARIMA, consideremos, en primer lugar, una serie estacionaria $Y_t$, a la cual se le agrega una tendencia lineal:

$$
T_t=\beta_0+\beta_1t
$$

obteniendo la serie resultante $X_t$.

Si asumimos que $Y_t$ sigue un modelo AR(1), es decir:

$$
Y_t=\phi Y_{t-1}+\varepsilon_t
$$

entonces la diferencia de $X_t$ está dada como se muestra en pantalla.

Es decir, la serie $X_t$ diferenciada es una serie estacionaria, ya que su media es constante y su covarianza es una función que depende exclusivamente de la separación temporal $h$, tal como se muestra en pantalla.

Esto ocurre porque:

$$
\operatorname{Cov}(\varepsilon_t,\varepsilon_{t+h})=0
$$

si $h$ es positivo.

Además, a partir de la representación causal de $Y_t$, es posible calcular la covarianza entre el ruido y el proceso $Y_t$ en diferentes instantes de tiempo, tal como se muestra en pantalla.

Por otro lado, como mencionamos en clases pasadas, el modelo AR(1) con:

$$
\phi=1
$$

no es estacionario.

Como:

$$
X_t=X_{t-1}+\varepsilon_t
$$

es claro que la diferencia de $X_t$ es estacionaria.

Los dos casos de no estacionariedad son diferentes, ya que en el primero falla la media, mientras que en el segundo falla la autocovarianza.

Aunque en ambos casos se logra recuperar una serie estacionaria mediante la diferenciación, en el primer caso, si la no estacionariedad es provocada por una tendencia determinista, siempre es conveniente intentar remover directamente dicha tendencia.

En el segundo caso, el polinomio característico tiene una raíz en el círculo unitario. Este es el caso más conveniente para modelar mediante diferenciación.

### Series no estacionarias homogéneas

En general, tendremos la siguiente definición para series no estacionarias homogéneas.

El grado de diferenciación $d$ es fijo y corresponde al primer valor para el cual se logra la estacionariedad.

Esto nos permite definir los modelos ARIMA.

La sigla ARIMA significa:

> **Autorregresivo integrado de media móvil**

También puede interpretarse como un modelo ARMA integrado.

Los polinomios característicos $\phi(B)$ y $\theta(B)$ tienen raíces fuera del círculo unitario, de manera que el proceso definido por:

$$
\nabla^d X_t
$$

sea causal e invertible.

## Ejemplo: modelo ARIMA(1,1,1)

Para comprender la estructura de un modelo ARIMA, consideremos un modelo:

$$
\operatorname{ARIMA}(1,1,1)
$$

Sus polinomios característicos son:

$$
\phi(B)=1-\phi B
$$

y

$$
\theta(B)=1+\theta B
$$

La ecuación final se muestra en pantalla.

Se puede apreciar que un ARIMA(1,1,1) es equivalente a un ARMA(2,1).

De manera general, un modelo:

$$
\operatorname{ARIMA}(p,d,q)
$$

corresponde a un:

$$
\operatorname{ARMA}(p+d,q)
$$

donde este último presenta $d$ raíces unitarias.

Es decir, el modelo ARIMA separa las raíces del polinomio característico autorregresivo de un modelo ARMA en:

- Las raíces que están sobre el círculo unitario.
- Las raíces que no se encuentran sobre el círculo unitario.

## Significado del término integrado

El término **integrado** proviene del hecho de que es necesario sumar los elementos del proceso diferenciado para recuperar la serie original.

Esta operación corresponde al proceso inverso de la diferenciación discreta.

Por ejemplo, si:

$$
d=1
$$

y definimos:

$$
Y_t=\nabla X_t
$$

entonces:

$$
X_t=X_0+\sum_{i=1}^{t}Y_i
$$

Es decir, para recuperar la serie original, debemos acumular o integrar las diferencias.

## Diferenciación estacional

También es posible modelar series temporales periódicas de periodo $s$.

La componente periódica puede removerse mediante la diferenciación estacional:

$$
\nabla_s X_t=X_t-X_{t-s}
$$

Luego, es posible incorporar en un mismo modelo:

- Efectos autorregresivos no estacionales.
- Efectos de media móvil no estacionales.
- Diferenciación no estacional.
- Efectos autorregresivos estacionales.
- Efectos de media móvil estacionales.
- Diferenciación estacional.

Este modelo se denomina **SARIMA**, o bien **ARIMA estacional**.

## Estructura de un modelo SARIMA

Un modelo SARIMA queda determinado por:

$$
\operatorname{SARIMA}(p,d,q)\times(P,D,Q)_s
$$

donde:

- $(p,d,q)$ representan la estructura ARIMA no estacional.
- $(P,D,Q)$ representan la estructura ARIMA estacional.
- $s$ corresponde al periodo fijo de la componente periódica.

Los parámetros en minúscula representan la parte no estacional:

- $p$: orden autorregresivo.
- $d$: grado de diferenciación.
- $q$: orden de media móvil.

Los parámetros en mayúscula representan la parte estacional:

- $P$: orden autorregresivo estacional.
- $D$: grado de diferenciación estacional.
- $Q$: orden de media móvil estacional.

La palabra **multiplicativo** se debe a que los respectivos polinomios característicos deben multiplicarse, tal como se muestra en la definición.

Es posible agregar otra componente periódica si fuese necesario, incorporando otros polinomios a la estructura anterior.

No obstante, no es habitual añadir más de una componente periódica a un modelo SARIMA.

Esto ocurre porque la diferenciación de orden $s$ provoca la pérdida de los primeros $s$ datos observados, que deben utilizarse como condiciones iniciales.

## Identificación de los órdenes estacionales

En general, reconocer los órdenes de la componente estacional suele ser complejo utilizando solamente las gráficas ACF y PACF de la serie original.

Sin embargo, recurriendo a la definición, si:

$$
X_t\sim\operatorname{SARIMA}(p,d,q)\times(P,D,Q)_s
$$

entonces la serie:

$$
Y_t=\nabla_s^D\nabla^dX_t
$$

será estacionaria y podrá representarse mediante un modelo ARMA.

De forma general, este proceso tendrá órdenes relacionados con:

$$
p+sP
$$

para la parte autorregresiva y:

$$
q+sQ
$$

para la parte de media móvil.

Por lo tanto, deberíamos observar algunos rezagos significativos en la ACF y la PACF, dependiendo de los valores de $p$, $q$, $P$, $Q$ y $s$.

## Ejemplo de modelo SARIMA

Por ejemplo, si:

$$
X_t\sim\operatorname{SARIMA}(1,0,1)\times(1,1,0)_{12}
$$

el modelo satisface la ecuación que se muestra en pantalla, la cual es bastante extensa.

El resultado corresponde a una relación en términos de:

- El proceso $X_t$.
- Sus valores pasados.
- El ruido actual.
- Los valores pasados del ruido.

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

## Tema 2. Estimación y predicción en modelos SARIMA

Comenzando con la predicción, para un proceso:

$$
X_t\sim\operatorname{ARIMA}(p,d,q)
$$

existe un proceso:

$$
Y_t=\nabla^dX_t
$$

que sigue un modelo:

$$
\operatorname{ARMA}(p,q)
$$

Por lo tanto, podemos predecir:

$$
\widehat{Y}_{n+m\mid n}
$$

mediante cualquiera de los métodos vistos anteriormente para los modelos ARMA.

Por ejemplo:

- El mejor predictor lineal.
- El mejor predictor suponiendo pasado infinito y truncando los datos observados.

## Predicción para $d=1$

Para comprender cómo obtener:

$$
\widehat{X}_{n+m\mid n}
$$

consideremos el caso:

$$
d=1
$$

y asumamos que disponemos de:

$$
\widehat{Y}_{n+m\mid n}
$$

A partir de la definición:

$$
Y_t=X_t-X_{t-1}
$$

se tiene que:

$$
\widehat{Y}_{n+m\mid n}
=
\widehat{X}_{n+m\mid n}
-
\widehat{X}_{n+m-1\mid n}
$$

Por lo tanto:

$$
\widehat{X}_{n+m\mid n}
=
\widehat{Y}_{n+m\mid n}
+
\widehat{X}_{n+m-1\mid n}
$$

Esta es una ecuación recursiva.

La recurrencia comienza para:

$$
m=1
$$

ya que:

$$
\widehat{X}_{n\mid n}=X_n
$$

es decir, el último dato observado.

## Predicción para $d=2$

En el caso:

$$
d=2
$$

se tiene:

$$
Y_t=X_t-2X_{t-1}+X_{t-2}
$$

Luego, el predictor de $X_{n+m}$ satisface la ecuación recursiva que se muestra en pantalla.

En el caso particular de:

$$
m=1
$$

el primer predictor depende directamente de los dos últimos datos observados.

Esto constituye una diferencia importante respecto al caso $d=1$.

Naturalmente, este procedimiento puede extenderse a cualquier valor de $d$.

## Error cuadrático medio de la predicción

Finalmente, el error cuadrático medio puede aproximarse mediante la expresión que se muestra en pantalla.

En ella, los coeficientes:

$$
\psi_j^*
$$

corresponden a los coeficientes de $z^j$ en el polinomio $\psi^*$, obtenido según la expresión mostrada en pantalla.

## Estimación de parámetros

La estimación de parámetros se realiza de forma similar al caso de los modelos ARMA.

Es decir, los parámetros del modelo se estiman utilizando la información de:

$$
Y_t
$$

en lugar de utilizar directamente:

$$
X_t
$$

Para estimar los parámetros de la parte ARMA se puede utilizar máxima verosimilitud.

Cuando el modelo contiene parámetros estacionales, pero no presenta raíces unitarias en la parte autorregresiva o de media móvil, el procedimiento de estimación es el mismo.

Por ejemplo, un modelo:

$$
\operatorname{SARIMA}(p,0,q)\times(P,0,Q)_s
$$

puede representarse como un modelo ARMA con órdenes extendidos.

De manera simplificada:

$$
\operatorname{ARMA}(p+sP,q+sQ)
$$

Por tanto, solo aumenta la cantidad de parámetros que deben estimarse.

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

## Tema 3. Pruebas de no estacionariedad

El problema de la no estacionariedad en series temporales lineales surge cuando el polinomio autorregresivo de un modelo ARMA presenta:

- Una raíz unitaria.
- Una raíz cercana al círculo unitario.

Adicionalmente, el polinomio de media móvil también podría contener una raíz sobre el círculo unitario o cerca de él.

Una raíz unitaria en cualquiera de estos polinomios tiene implicaciones importantes para la modelación.

Por ejemplo:

- Una raíz cercana a 1 en el polinomio autorregresivo sugiere que los datos deberían diferenciarse antes de ajustar un modelo ARMA.
- Una raíz cercana a 1 en el polinomio de media móvil puede indicar que los datos fueron sobrediferenciados.

## Pruebas de raíz unitaria

Los procedimientos estándar de inferencia utilizados para detectar la presencia de una raíz unitaria son:

- Prueba de Dickey-Fuller, DF.
- Prueba de Dickey-Fuller aumentada, ADF.
- Prueba de Phillips-Perron, PP.

No entraremos en los detalles técnicos de cada prueba, ya que el objetivo principal es saber cómo utilizarlas e interpretarlas.

En todos los casos, la hipótesis nula es:

$$
H_0:\text{existe una raíz unitaria}
$$

Mientras que la hipótesis alternativa es:

$$
H_1:\text{no existe una raíz unitaria}
$$

Esto significa que inicialmente se asume que existe una raíz unitaria, a menos que se demuestre lo contrario.

Por tanto, si el objetivo es descartar la presencia de una raíz unitaria, el resultado del test debería entregar un valor p pequeño.

Por ejemplo:

$$
p<0.05
$$

que corresponde a uno de los niveles de significancia más utilizados.

## Ejemplo: índice de oscilación del sur

Consideremos la serie correspondiente al índice de oscilación del sur, SOI, para un periodo de 453 meses comprendido entre 1950 y 1987.

El SOI mide cambios en la presión atmosférica relacionados con las temperaturas de la superficie del mar en el océano Pacífico central.

La medición comienza en enero de 1950 y finaliza en septiembre de 1987.

Se dejan como conjunto de prueba:

- El año 1986 completo.
- Los primeros nueve meses de 1987.

El resto de los datos se utilizan como conjunto de entrenamiento para ajustar un modelo de la familia SARIMA.

La división se muestra en la figura presentada en pantalla.

## Modelo propuesto por Auto-ARIMA

Al aplicar la función `auto_arima`, seleccionando el mejor modelo mediante el AIC, se obtiene:

$$
\operatorname{SARIMA}(0,1,4)\times(0,0,2)_{12}
$$

con:

$$
\operatorname{AIC}=194.14
$$

Los coeficientes estimados y sus respectivas desviaciones estándar se muestran en pantalla.

Como el tamaño de muestra es relativamente grande, podemos utilizar como referencia la distribución asintótica de los coeficientes estimados.

La significancia se evalúa mediante un test $Z$, cuya hipótesis nula es:

$$
H_0:\text{el coeficiente es igual a cero}
$$

El estadístico de prueba puede aproximarse mediante:

$$
Z=
\frac{|\text{coeficiente estimado}|}
{\text{desviación estándar}}
$$

Para una significancia del 5 %, el valor debería ser aproximadamente mayor que 2 para considerar que el parámetro es significativo.

Bajo este criterio, todos los coeficientes del modelo entregado por `auto_arima` son significativos, salvo el coeficiente MA(3).

## Diagnóstico del modelo Auto-ARIMA

Al realizar el diagnóstico del modelo, los residuos parecen comportarse casi como ruido blanco según su ACF.

Sin embargo, la prueba de Ljung-Box indica que esta hipótesis no se cumple.

En pantalla se muestran las gráficas correspondientes.

Para:

$$
h\geq4
$$

el valor p es menor que:

$$
0.05
$$

Por tanto, existe autocorrelación residual y el modelo no captura toda la estructura temporal de la serie.

Además, `auto_arima` seleccionó un modelo no estacionario, ya que:

$$
d=1
$$

No obstante, al aplicar las pruebas de raíz unitaria ADF y PP, se obtienen valores p menores que:

$$
0.01
$$

Esto ocurre tanto al aplicar las pruebas a la serie original $X_t$ como a la serie desestacionalizada $Y_t$, definida mediante una diferenciación de rezago 12.

Por lo tanto, se concluye que no existe una raíz unitaria.

Este resultado es opuesto a lo reportado por `auto_arima`.

## Análisis exploratorio de la serie

El análisis exploratorio de la serie original y de la serie desestacionalizada se muestra en la siguiente figura.

Se identifica que el periodo de frecuencia 12 es importante.

Esto se observa porque la oscilación regular presente en las gráficas ACF y PACF de $X_t$ desaparece o disminuye al analizar la serie diferenciada estacionalmente.

Esto sugiere que:

$$
D=1
$$

Adicionalmente:

- La PACF de $X_t$ sugiere $p=1$.
- La ACF de $X_t$ sugiere un valor de $q$ entre 0 y 3, seleccionándose $q=2$.
- La PACF de la serie diferenciada estacionalmente sugiere un valor de $P$ entre 1 y 3.
- Aunque el valor $P=2$ posiblemente no sea significativo, se escoge $P=3$.
- La ACF de la serie diferenciada estacionalmente sugiere un valor de $Q$ entre 0 y 3, seleccionándose $Q=2$.

En conclusión, a partir del análisis exploratorio y de las pruebas de raíz unitaria, se propone el siguiente modelo:

$$
\operatorname{SARIMA}(1,0,2)\times(3,1,2)_{12}
$$

Sin embargo, el análisis exploratorio muestra una fuerte dependencia en la serie diferenciada cada 12 periodos.

Posiblemente podría aumentarse el orden de diferenciación estacional $D$ para proponer otro modelo.

## Ajuste del modelo propuesto

Al ajustar el modelo propuesto, se obtienen los coeficientes estimados y sus respectivas desviaciones estándar, tal como se muestra en pantalla.

El AIC obtenido es:

$$
102.55
$$

Este valor es considerablemente menor que el correspondiente al modelo propuesto por `auto_arima`.

Los residuos muestran un comportamiento similar al ruido blanco según:

- La gráfica ACF.
- El valor p de la prueba de Ljung-Box.

Además, el valor p de la prueba de normalidad de Shapiro-Wilk es:

$$
0.2025
$$

Por tanto, no se rechaza la hipótesis de normalidad.

El valor p de la prueba de Breusch-Pagan es:

$$
0.1368
$$

Por tanto, no se rechaza la hipótesis de homocedasticidad.

En consecuencia, podríamos decir que el modelo es apropiado.

## Simplificación del modelo

Sin embargo, al observar el cociente entre el valor absoluto del parámetro estimado y su desviación estándar, algunos valores son considerablemente menores que dos.

Por ello, se puede proponer un modelo más simple:

$$
\operatorname{SARIMA}(1,0,1)\times(1,1,2)_{12}
$$

En este modelo, el parámetro SMA(1) se fija en cero para no incorporarlo.

Los parámetros estimados y sus respectivas desviaciones estándar se muestran en pantalla.

El modelo disminuye su AIC a:

$$
96.27
$$

al eliminar los parámetros no significativos.

Por tanto, este sería un modelo mejor.

Los residuos continúan satisfaciendo las propiedades de ruido blanco según la gráfica mostrada en pantalla.

Además:

- La prueba de normalidad entrega un valor p de $0.2803$.
- La prueba de homocedasticidad entrega un valor p de $0.0865$.

Por tanto, tampoco se rechazan las hipótesis de normalidad y homocedasticidad.

Este modelo también puede considerarse apropiado.

## Comparación predictiva

Finalmente, para comparar los modelos en términos predictivos, la tabla mostrada en pantalla presenta:

- El AIC del ajuste.
- El RMSE obtenido a partir de la muestra de prueba.

Entre los modelos ajustados mediante el análisis exploratorio existe una mejora clara respecto al modelo propuesto por `auto_arima`.

Entre los modelos construidos manualmente, la diferencia es mínima.

Esto también puede observarse en las gráficas de predicción, donde se muestra solamente el periodo final de la serie.

Es importante notar que las predicciones generadas por `auto_arima` no siguen adecuadamente la forma de la serie de prueba.

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

## Ideas más importantes

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

Los modelos no estacionarios:

$$
\operatorname{ARIMA}(p,d,q)
$$

se caracterizan por presentar al menos una raíz unitaria en el polinomio autorregresivo.

Desde este punto de vista, un modelo:

$$
\operatorname{ARIMA}(p,d,q)
$$

puede considerarse equivalente a un:

$$
\operatorname{ARMA}(p+d,q)
$$

que presenta $d$ raíces unitarias.

Para incorporar componentes periódicas en los modelos ARIMA, estas se agregan de forma multiplicativa desde el punto de vista de los polinomios característicos.

La forma multiplicativa con que se incorporan los efectos no estacionarios y estacionales permite construir una variable auxiliar que puede modelarse mediante un ARMA.

Esto permite extender de manera sencilla los procedimientos de:

- Predicción.
- Estimación de parámetros.
- Diagnóstico.

desde los modelos ARMA hacia los modelos SARIMA.

Los criterios de información:

- AIC.
- BIC.
- AICc.

siguen siendo válidos para los modelos SARIMA y pueden compararse con los valores obtenidos en modelos ARMA.

Esto significa que podemos utilizar estos criterios para seleccionar el mejor modelo posible dentro de esta familia.
