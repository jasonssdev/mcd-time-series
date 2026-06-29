# Predicción de series de tiempo

Bienvenidos y bienvenidas a una nueva clase.

La predicción de series de tiempo a través de procesos estocásticos no solo nos entrega el valor puntual de la predicción, sino que también nos entrega una cuantificación del error, lo cual nos permite construir intervalos de confianza para las predicciones, obteniendo así una herramienta que cuantifica el nivel de incertidumbre.

Para llevar esto a cabo, vamos a suponer que \(X_t\) es un proceso estocástico estacionario, cuya realización es la serie de tiempo de largo \(n\):

- \(x_1, x_2, \ldots, x_n\)

El objetivo será predecir el instante \(n+m\), para \(m = 1, 2, 3,\) en adelante, utilizando la información de las \(n\) observaciones.

Si bien no tenemos una cota superior para \(m\), el horizonte de predicción, en la práctica, este valor no puede ser muy grande para procesos estacionarios. De hecho, veremos que en algunos modelos solo podemos predecir un paso y luego el predictor queda pegado en la media.

También veremos que es la estructura de autocorrelación quien controlará el alcance de las predicciones.

En esta clase se revisarán los siguientes temas:

1. Mejor predictor lineal.
2. Predicción a un paso.
3. Predicción a \(m\) pasos.

---

## Tema 1. Mejor predictor lineal

Si denotamos por \(\hat{x}_{n+m|n}\) al predictor de \(x_{n+m}\), quizás la notación puede ser extraña.

Pero cuando \(n\) y \(m\) son valores fijos, por ejemplo:

- \(n = 100\)
- \(m = 1\)

se tiene que:

- \(\hat{x}_{101|100}\)

indicando que es el predictor del dato 101 utilizando la información de los primeros 100 datos.

Así,

- \(\hat{x}_{102|100}\)

representa al predictor del dato 102 utilizando la información de los primeros 100 datos.

Para determinar \(\hat{x}_{n+m|n}\) existen varias estrategias, tales como:

- El mejor predictor lineal.
- El mejor predictor en general.

Se sabe que, si el proceso estocástico es gaussiano, ambos coinciden bajo pérdida cuadrática.

El mejor predictor lineal asume la forma que aparece en pantalla, mientras que el mejor predictor tiene la forma de la esperanza condicional de \(x_{n+m}\) dado \(x_1, \ldots, x_n\).

En primera instancia fijemos nuestra atención en el mejor predictor lineal, donde los pesos óptimos \(\alpha_j\) son aquellos que minimizan el error cuadrático medio esperado, tal como aparece en pantalla.

Para encontrar los pesos óptimos:

- \(\alpha_0\)
- \(\alpha_1\)
- ...
- \(\alpha_n\)

se calcula el gradiente de \(Q(\alpha)\) y se iguala a cero.

Asumiendo que \(x_0 = 0\), se tiene la proposición que aparece en pantalla.

Además, al imponer la condición de insesgamiento, es decir, que la esperanza del predictor es igual a la esperanza del verdadero valor, y asumiendo que la media \(\mu = 0\), entonces:

- \(\alpha_0 = 0\)

Una vez obtenidos los coeficientes óptimos, la función objetivo, es decir, el error cuadrático medio de predicción, se expresa como sigue:

\[
P_{n+m|n}
\]

corresponde a la esperanza de la diferencia al cuadrado entre el predictor y el verdadero valor.

Esta cantidad la utilizaremos posteriormente para construir intervalos de confianza.

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

---

## Tema 2. Predicción a un paso

En primer lugar describamos las ecuaciones que nos permiten encontrar el predictor un instante al futuro.

Es decir, el predictor de:

\[
x_{n+1}
\]

conocido como **predicción a un paso**.

Asumiendo que la esperanza del proceso es cero y utilizando la notación para:

\[
\hat{x}_{n+1|n}
\]

los coeficientes \(\alpha_j\) pasan a denominarse:

\[
\phi_{n,n+1-j}
\]

Como punto al margen, esta notación explica la utilizada para la autocorrelación parcial y el algoritmo de Durbin-Levinson.

Continuando con el objetivo de hallar los coeficientes \(\alpha_j\), al aplicar la proposición anterior y considerando que:

\[
\gamma(h)
\]

es la esperanza del producto entre el proceso en el instante \(t\) y el instante \(t+h\), es decir, la función de autocovarianza del proceso \(X_t\), se obtiene un sistema de ecuaciones lineales en los coeficientes \(\phi_{nj}\).

Su forma matricial es:

\[
\Gamma_n \Phi_n = \Gamma_n
\]

donde:

- \(\Phi_n\) contiene los coeficientes \(\phi_{n1}, \phi_{n2}, \ldots, \phi_{nn}\).
- El vector \(\Gamma_n\) contiene las autocovarianzas \(\gamma_1, \gamma_2, \ldots, \gamma_n\).
- La matriz \(\Gamma_n\) está formada por las autocovarianzas evaluadas en los primeros \(n\) rezagos.

Adicionalmente, el error cuadrático medio de predicción adopta la forma:

\[
\gamma_0 - \Gamma_n^T \Gamma_n^{-1}\Gamma_n
\]

Así, tanto para determinar los coeficientes \(\Phi_n\) como para calcular \(P_{n+1|n}\), basta invertir la matriz \(\Gamma_n\), lo cual puede ser complejo cuando \(n\) es muy grande.

### Ejemplo: proceso AR(2)

Para un proceso AR(2) causal:

Si \(x_1\) es la primera observación, entonces el predictor de \(x_2\) es:

\[
\hat{x}_{2|1}
\]

y está dado por:

\[
\phi_{11}x_1
\]

que es igual a:

\[
\rho_1x_1
\]

Ahora, si disponemos de \(x_1\) y \(x_2\), el predictor de \(x_3\) es:

\[
\hat{x}_{3|2}
\]

dado por:

\[
\phi_{21}x_2 + \phi_{22}x_1
\]

Los coeficientes \(\phi_{21}\) y \(\phi_{22}\) se obtienen resolviendo el sistema de ecuaciones estudiado anteriormente.

Concluyendo que:

\[
\hat{x}_{3|2} = \phi_1x_2 + \phi_2x_1
\]

Siguiendo este camino se puede verificar que para:

\[
n \ge 2
\]

se tiene:

\[
\hat{x}_{n+1|n}
=
\phi_1x_n+\phi_2x_{n-1}
\]

Es decir:

- \(\phi_{n1}=\phi_1\)
- \(\phi_{n2}=\phi_2\)
- \(\phi_{nj}=0\) para \(j=3,4,\ldots\)

En términos generales, para resolver el sistema es posible particionar la matriz \(\Gamma_n\) y, utilizando las propiedades de la matriz inversa particionada, se obtiene el algoritmo de **Durbin-Levinson**.

Continuando con el ejemplo del AR(2), podemos calcular de forma iterativa el error cuadrático medio de predicción.

En este caso:

- \(P_{1|0}=\gamma_0\)
- \(P_{2|1}=P_{1|0}(1-\phi_{11}^2)\)

Y finalmente:

\[
P_{n+1|n}=P_{n|n-1}
\]

para:

\[
n=2,3,4,\ldots
\]

A partir de \(P_{3|2}\) el error permanece constante.

Esto ocurre porque estamos trabajando con un proceso AR(2), cuyos únicos coeficientes distintos de cero son los dos primeros.

El algoritmo de Durbin-Levinson puede aplicarse a todos los procesos lineales, particularmente:

- AR(p)
- MA(q)
- ARMA(p,q)

Sin embargo, resulta más complejo para los modelos MA(q) y ARMA(p,q), debido a que la correlación parcial nunca se anula y, en consecuencia, los coeficientes óptimos \(\phi_{jn}\) no serán cero.

Por otro lado, Brockwell y Davis propusieron otro algoritmo que permite encontrar directamente el mejor predictor lineal y su error cuadrático medio.

### Ejemplo: proceso MA(1)

Consideremos un proceso MA(1) invertible, donde el ruido blanco tiene varianza \(\sigma^2\).

Recordemos que la función de autocovarianza es:

- \(\gamma_0=(1+\theta^2)\sigma^2\)
- \(\gamma_1=\theta\sigma^2\)
- \(\gamma_h=0\), para \(h\ge2\)

En este caso:

- \(\theta_{nj}=0\) para \(j\ge2\)
- \(\theta_{n1}=\dfrac{\theta\sigma^2}{P_{n|n-1}}\)

donde:

- \(P_{1|0}\)
- \(P_{2|1}\)
- ...
- \(P_{n+1|n}\)

son los valores mostrados en pantalla.

Por lo tanto,

\[
\hat{x}_{n+1|n}
\]

adquiere la expresión correspondiente.

Esto significa que, para predecir \(x_{n+1}\), necesitamos de forma recursiva todos los predictores a un paso de:

\[
x_t,\quad t=1,\ldots,n-1
\]

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

---

## Tema 3. Predicción a \(m\) pasos

La predicción a un paso es muy útil para ir midiendo el ajuste del modelo a medida que se incorporan nuevos datos.

Sin embargo, muchas veces nos interesa no solo predecir un paso al futuro, sino \(m\) pasos, utilizando siempre la información de la muestra:

\[
x_1,\ldots,x_n
\]

Es decir, queremos determinar valores factibles para:

- \(x_{n+1}\)
- \(x_{n+2}\)
- ...
- \(x_{n+m}\)

donde:

\[
m=1,2,3,\ldots
\]

En principio, \(m\) podría ser cualquier número natural, teniendo claro que, en la práctica, no debe ser muy grande cuando trabajamos con procesos estacionarios.

Obsérvese además que:

\[
m=1
\]

corresponde al caso particular estudiado anteriormente.

Nuevamente, los coeficientes óptimos se obtienen minimizando el error cuadrático medio de predicción.

Para un \(m\ge1\) fijo, el predictor lineal de \(x_{n+m}\) adquiere la forma mostrada en pantalla.

Los coeficientes óptimos deben satisfacer las ecuaciones normales, que pueden escribirse utilizando la función de autocovarianza.

Su representación matricial y su solución aparecen a continuación.

Finalmente, el error cuadrático medio de predicción mantiene exactamente la misma estructura que en el caso \(m=1\).

La única diferencia es el vector:

\[
\Gamma_n^{(m)}
\]

lo que produce un cambio en la solución:

\[
\Phi_n^{(m)}
\]

Por lo tanto, para obtener predicciones a \(m\) pasos es posible aplicar el algoritmo innovativo.

### Ejemplo: MA(1)

Del ejemplo anterior obtuvimos que:

\[
P_{n+1|n}
\]

está dado por la expresión correspondiente.

Luego,

\[
\hat{x}_{n+2|n}=0
\]

y

\[
P_{n+2|n}=\gamma_0
\]

ya que:

\[
\theta_{n+1,j}=0
\]

para todo:

\[
j\ge2
\]

Esto significa que todos los predictores siguientes son cero y la varianza del predictor coincide con la varianza del proceso para \(j\ge2\).

Esto ocurre porque la función de autocovarianza es distinta de cero únicamente cuando:

\[
h=1
\]

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

---

## Resumen

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes:

- Bajo pérdida cuadrática, el mejor estimador lineal y el mejor estimador general, dado por la esperanza condicional, coinciden.
- La predicción a un paso es importante porque permite ajustar la serie a medida que avanza el tiempo.
- La predicción a \(m\) pasos se utiliza para predecir hacia el futuro desde el presente, por lo que, en general, no se predicen \(m\) pasos desde un valor pasado.
