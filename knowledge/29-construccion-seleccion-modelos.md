# Construcción y selección de modelos

Bienvenidos y bienvenidas a una nueva clase.

Consideremos una serie de tiempo en la cual tiene sentido ajustar un modelo ARMA. Es decir, su gráfica luce estable en media y varianza, mientras que la ACF y la PACF muestran algunos *lags* significativos y, a largo plazo, decaen a cero.

Ya vimos en clases anteriores cómo realizar la estimación de parámetros de un modelo ARMA(p,q), con $p$ y $q$ fijos. El problema al que nos enfrentamos ahora es seleccionar los valores adecuados para los órdenes $p$ y $q$.

Ahora bien, hay que tener presente que, la mayoría de las veces, las series de tiempo no lucen estacionarias, ya sea porque presentan alguna tendencia o porque su varianza no es constante.

Recordemos que, en estos casos, los datos pueden ser transformados hasta conseguir una serie que luzca como un ARMA. Esto lo podemos conseguir, por ejemplo, mediante:

- Alguna combinación de transformaciones de Box-Cox y diferenciaciones.
- La eliminación de las componentes de tendencia y estacionales a través del método de descomposición.

En esta clase se revisarán los siguientes temas:

- **Tema 1:** Bondad de ajuste y criterios de información.
- **Tema 2:** Diagnóstico.

## Tema 1. Bondad de ajuste y criterios de información

Una vez realizada la estimación de parámetros del modelo, se requiere una medida para cuantificar si el ajuste del modelo a los datos es bueno o malo.

Desde el punto de vista de la calidad del ajuste, debemos tener presente que no es ventajoso elegir $p$ y $q$ arbitrariamente grandes, ya que, en estos casos, se suele sobreajustar la serie, obteniendo un estimador pequeño de la varianza del ruido.

Sin embargo, la varianza de las predicciones también depende de los parámetros del modelo. En consecuencia, las bandas de confianza de las predicciones podrían ser muy grandes si hay muchos parámetros estimados.

El problema mencionado es común en todos los modelos estadísticos paramétricos. Por ello, es usual aplicar el **principio de parsimonia**, el cual consiste en agregar parámetros al modelo solo si existe suficiente evidencia de que el modelo con una mayor cantidad de parámetros es significativamente mejor que el modelo con una menor cantidad de parámetros.

Para realizar lo anterior, se puede utilizar la inferencia sobre los parámetros del modelo a través de:

- Pruebas de hipótesis.
- Criterios de información.

Estos últimos consisten en evaluar la función objetivo, que, en la mayoría de los casos, corresponde a menos dos veces la log-verosimilitud o a la suma de cuadrados residuales, y penalizarla para evitar el sobreajuste y, en consecuencia, evitar modelos con órdenes muy grandes.

Si bien existen muchos criterios de información, en este curso nos limitaremos a discutir brevemente:

- El criterio de información de Akaike, AIC.
- El criterio de información de Schwarz, también conocido como criterio de información bayesiano, BIC.

### Criterios AIC y BIC

Como se mencionó, los criterios AIC y BIC toman como medida de ajuste la log-verosimilitud de los datos, mientras que la función penalizadora corresponde a una función de la cantidad de parámetros utilizados en el modelo.

Las expresiones matemáticas de estos criterios son las que se muestran a continuación:

$$
\operatorname{AIC}=-2\log L(\hat{\theta})+2k
$$

$$
\operatorname{BIC}=-2\log L(\hat{\theta})+k\log(n)
$$

También se define el AIC corregido:

$$
\operatorname{AICc}
=
\operatorname{AIC}
+
\frac{2k(k+1)}{n-k-1}
$$

donde:

- $n$ es la cantidad de datos de la serie.
- $\hat{\theta}$ corresponde al vector formado por $\hat{\beta}$ y $\hat{\sigma}_w^2$, es decir, el vector de parámetros estimados.
- $k$ es la cantidad de parámetros estimados.

En el caso de un ARMA(p,q), causal e invertible y con media igual a cero:

$$
k=p+q+1
$$

Esto se debe a que existen:

- $p$ parámetros autorregresivos.
- $q$ parámetros de media móvil.
- Un parámetro correspondiente a la varianza del ruido blanco.

Notar que el AICc es una corrección por sesgo del AIC, principalmente útil para tamaños de muestra pequeños. Sin embargo, no aporta cuando $n$ es grande, ya que el término de corrección tiende a cero a medida que $n$ tiende a infinito.

Además, el criterio BIC, en comparación con el AIC, penaliza con mayor fuerza la incorporación de un nuevo parámetro en el modelo, ya que, a partir de $n=8$, aproximadamente, el logaritmo natural de $n$ es mayor que dos.

Finalmente, se debe tener presente que la bondad de ajuste puede utilizarse para:

- Comparar diferentes métodos de estimación de un mismo modelo.
- Comparar diferentes modelos.

En este último punto, una herramienta útil consiste en utilizar las gráficas de la ACF y la PACF para proponer varios modelos y luego seleccionar el mejor a través de alguno de los criterios de información.

Por ejemplo, mediante el AIC seleccionaremos el modelo que tenga el menor valor de este criterio.

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

## Tema 2. Diagnóstico

Que el modelo propuesto se ajuste bien a los datos no solo se debe determinar a través de los criterios de bondad de ajuste.

También es necesario verificar que se cumplan los supuestos del modelo, es decir, que el modelo sea apropiado.

Una de las características más relevantes que se debe tener en cuenta es que los residuos deben ser aproximadamente un ruido blanco.

En términos prácticos, esto significa que los residuos no deberían contener información útil.

Los residuos calculados como se presenta a continuación deberían tener aproximadamente:

- Media igual a cero.
- Varianza igual a uno.
- Función de autocorrelación $\rho_e(h)$ nula para $h\neq0$.

Como vimos al inicio del curso, analizar las autocorrelaciones $\rho_e(h)$ de forma individual no es suficiente, ya que podría suceder que, globalmente, el modelo no sea bueno, a pesar de que todas las autocorrelaciones fueran no significativas.

Recordemos que las pruebas de Portmanteau permiten verificar si una serie es o no un ruido blanco.

Entre estas se encuentran:

- La prueba de Breusch-Godfrey.
- La prueba de Durbin-Watson.
- Las pruebas de Box-Pierce y Ljung-Box.

Todas tienen en común que la hipótesis nula establece que la serie es un ruido blanco. De este modo, las pruebas buscan evidencia que permita refutar dicha hipótesis.

En particular, la prueba de Ljung-Box la vimos de forma específica al comienzo del análisis de una serie de tiempo, para determinar si presenta una estructura de dependencia temporal y si tiene sentido ajustar un modelo.

Ahora que ya tenemos los modelos ARMA ajustados, podemos aplicar la misma prueba a los residuos de dicho modelo.

La prueba se vuelve a enunciar a continuación, destacando que la distribución asintótica del estadístico $Q$ es chi-cuadrado con:

$$
h-p-q
$$

grados de libertad, donde:

- $p$ corresponde a la cantidad de parámetros autorregresivos estimados.
- $q$ corresponde a la cantidad de parámetros de media móvil estimados.

En otras palabras, $p$ y $q$ corresponden a los órdenes del modelo ARMA(p,q).

### Normalidad de los residuos

Por otro lado, para la selección de modelos a partir de los criterios de información es importante contar con una distribución para el error, que, por lo general, se asume normal.

En ese sentido, también se debe poner a prueba la normalidad de los residuos ajustados.

Las pruebas de normalidad típicamente utilizadas para este propósito son:

- Shapiro-Wilk.
- Anderson-Darling.
- Lilliefors.

Estas pruebas deben acompañarse de la inspección gráfica que entrega el gráfico Q-Q normal.

### Homocedasticidad de los residuos

Finalmente, es parte de las hipótesis del modelo ARMA que este depende de un ruido blanco homocedástico, es decir, que su varianza sea constante.

En consecuencia, también se debe realizar una prueba de hipótesis de este tipo, como:

- Goldfeld-Quandt.
- Breusch-Pagan.

Las pruebas de normalidad y homocedasticidad solo se enuncian, ya que son pruebas estándar en los modelos de regresión lineal.

### Selección automática mediante Auto-ARIMA

Por último, programas como Python o R tienen una función denominada `auto.arima`, la cual busca el mejor modelo de la familia SARIMA.

En el caso de los modelos ARMA, esta función busca el mejor modelo ingresando valores relativamente altos de $p$ y $q$, y ajustando los modelos intermedios para tomar una decisión sobre el modelo que mejor se adapta a los datos.

Tiene como objetivo encontrar los órdenes del modelo que minimicen alguno de los siguientes criterios:

- AIC.
- BIC.
- AICc.

Cabe destacar que el modelo SARIMA lo veremos en las próximas clases, y que el modelo ARMA es un caso particular de este.

Si bien esta metodología entrega un modelo razonable, es posible que el modelo resultante tenga parámetros redundantes o que los residuos todavía contengan información útil.

Por eso, es importante tener muy claros los pasos del diagnóstico para obtener un modelo correcto cuando apliquemos la metodología de Box-Jenkins. Esta última la veremos en las próximas clases.

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

## Ideas más importantes

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

Para seleccionar los órdenes $p$ y $q$ de un modelo ARMA, es posible realizar una comparación de modelos mediante alguno de los criterios de información, o bien mediante inferencia sobre los parámetros de dicho modelo.

El modelo finalmente escogido debe ser adecuado, en el sentido de que satisfaga las hipótesis iniciales.

Un modelo ARMA tiene como hipótesis que el proceso es una combinación lineal de un ruido blanco. Por lo tanto, las hipótesis más importantes que se deben verificar sobre los residuos son:

- Que no presenten autocorrelación.
- Que su varianza sea constante.

La hipótesis de normalidad del ruido blanco es importante para la selección del modelo y para realizar inferencia sobre los parámetros.
