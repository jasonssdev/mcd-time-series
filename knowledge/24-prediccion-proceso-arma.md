# Predicción en procesos ARMA

Bienvenidos y bienvenidas a una nueva clase.

Las ecuaciones generales de predicción, también denominadas ecuaciones normales, son las que determinan al mejor predictor lineal.

Sin embargo, proporcionan en general poca información sobre la predicción para los modelos ARMA.

Ahora veremos cómo aprovechar la estructura de los procesos ARMA para proponer predicciones que, en un principio, asumen un pasado infinito.

Es decir, usaremos la información desde menos infinito hasta:

\[
x_{-2}, x_{-1}, x_0, x_1, \ldots, x_n
\]

que luego aproximaremos para obtener predicciones usando el pasado realmente observado.

En esta clase se revisarán los siguientes temas:

1. Predicción con pasado infinito en modelos ARMA.
2. Predicción truncada de pasado infinito en modelos ARMA.

---

## Tema 1. Predicción con pasado infinito en modelos ARMA

Sabemos que el mejor predictor lineal coincide con la esperanza condicional cuando se asume normalidad en los residuos.

Esto significa que:

\[
\hat{x}_{n+m|n}
\]

está dado por la esperanza condicional de \(x_{n+m}\), dado todo el pasado desde \(n\) hacia atrás.

Aprovechándonos de la estructura de la esperanza condicional y asumiendo que se conoce todo el pasado remoto de la serie, podemos estimar \(x_{n+m}\) por:

\[
\tilde{x}_{n+m}
\]

el cual está dado por la esperanza condicional de \(x_{n+m}\), dado \(x_n\) hasta \(x_1, x_0\), y así todo el pasado infinito.

Es decir, sigue siendo la esperanza condicional de \(x_{n+m}\), pero los elementos que estamos condicionando contienen información de todo el pasado del proceso.

En general:

\[
\tilde{x}_{n+m}
\]

y

\[
\hat{x}_{n+m|n}
\]

son distintos.

Sin embargo, para muestras grandes:

\[
\tilde{x}_{n+m}
\]

es una buena aproximación de:

\[
\hat{x}_{n+m|n}
\]

Cabe resaltar que la nueva notación \(\tilde{x}_{n+m}\) significa que se quiere predecir el valor de \(x_{n+m}\) utilizando todo el pasado de la serie, desde \(x_n\) hasta el pasado remoto.

Quizás en este punto sería bueno preguntarse:

> ¿Por qué aproximar \(\hat{x}_{n+m|n}\) por \(\tilde{x}_{n+m}\)?

O mejor dicho:

> ¿Cuál es la ganancia de asumir que se conoce todo el pasado remoto?

Obviamente, al final de la clase podremos responder con fundamentos a estas preguntas.

Para poder entregar las ecuaciones de pronóstico, asumiremos que tenemos un proceso \(X_t\) ARMA causal e invertible, de media cero, y ruido blanco \(\varepsilon_t\), de media cero y varianza \(\sigma^2\).

Así, la representación MA infinito y AR infinito, escrita desde \(x_{n+m}\), el cual es el valor que queremos predecir, son las que aparecen en pantalla.

Al tomar esperanza condicional respecto a \(x_n\) y todo su pasado, se tiene el siguiente valor para la esperanza condicional de \(\varepsilon_t\), y el siguiente valor para la esperanza condicional de \(x_t\).

El ruido tiene esperanza cero cuando \(t > n\), y es exactamente igual a \(\varepsilon_t\) cuando \(t \le n\).

Esto se explica por la causalidad e invertibilidad de \(X_t\), ya que \(x_n\) depende del ruido del instante \(n\) y del pasado de ese instante.

En consecuencia, \(\varepsilon_t\) y \(x_n\), hasta todo el pasado, son independientes si \(t > n\).

Mientras que si \(t \le n\), entonces \(\varepsilon_t\) pertenece al conjunto generado por \(x_n\) y todo su pasado.

En consecuencia, \(\varepsilon_t\) es constante dado \(x_n\) y el pasado.

Del mismo modo, en el caso de \(x_t\), este es conocido dado \(x_n\) y todo su pasado cuando \(t \le n\).

Así, su valor esperado es el mismo valor y corresponde al predictor cuando \(t > n\).

Luego se tiene que el predictor satisface las siguientes dos ecuaciones.

Ambas expresiones son útiles para obtener las predicciones y su respectivo error cuadrático medio.

Por un lado, utilizando la representación causal, la diferencia entre \(x_{n+m}\) y \(\tilde{x}_{n+m}\) queda escrita como una combinación lineal finita de los errores, ya que los términos desde \(m\) en adelante coinciden tanto para \(x_{n+m}\) como para \(\tilde{x}_{n+m}\).

Es decir, obtenemos la siguiente expresión, donde los pesos son los coeficientes de \(\psi_j\), para:

\[
j = 0, \ldots, m-1
\]

De esta última expresión, tenemos que el error cuadrático medio de predicción esperado es como sigue.

Además, para un valor fijo de \(n\), los errores de predicción son correlacionados, tal como se muestra a continuación.

Por lo tanto, existe dependencia entre los términos predichos.

Por otro lado, la representación AR infinito nos permite obtener una ecuación de predicción recursiva.

Es decir, el predictor:

\[
\tilde{x}_{n+m}
\]

depende del predictor anterior:

\[
\tilde{x}_{n+m-1}
\]

y así sucesivamente.

Además, dado que en la práctica no disponemos de:

\[
x_0, x_{-1}, \ldots
\]

hasta todo el pasado remoto, debemos truncar \(\tilde{x}_{n+m}\), considerando la aproximación que aparece en pantalla.

La aproximación es calculada recursivamente para:

\[
m = 1, 2, 3, \ldots
\]

En el caso del error cuadrático medio de predicción, se aproximará por la expresión que ya habíamos calculado, la que se muestra nuevamente en pantalla.

Por ejemplo, para una serie de largo:

\[
n = 100
\]

el predictor de \(x_{101}\) se obtiene utilizando:

\[
m = 1
\]

Es decir:

\[
\tilde{x}_{101|100}
\]

está dado por la expresión mostrada en pantalla, y:

\[
P_{101|100} = \sigma^2
\]

Mientras que el predictor de \(x_{102}\) se obtiene utilizando:

\[
m = 2
\]

El cual nuevamente se muestra en pantalla junto con:

\[
P_{102|100}
\]

que es su error de predicción.

Y así continuamos con el predictor de \(x_{103}\), evaluando:

\[
m = 3
\]

Es decir:

\[
P_{103|100}
=
\sigma^2(1+\psi_1^2+\psi_2^2)
\]

Como se puede apreciar, la varianza del predictor crece a medida que \(m\) es mayor.

A su vez, converge a la varianza del proceso cuando \(m\) tiende a infinito.

Mientras tanto, el predictor depende de los coeficientes \(\pi_j\) de la representación AR infinito, los cuales tienden a cero a medida que \(m\) tiende a infinito.

Los coeficientes \(\pi_j\) se obtienen directamente para los procesos AR(p).

Sin embargo, para los procesos MA(q) y ARMA(p,q), estos se obtienen a partir de las respectivas ecuaciones en diferencia.

**Prueba tu aprendizaje respondiendo a la siguiente pregunta.**

---

## Tema 2. Predicción truncada de pasado infinito en modelos ARMA

Antes de realizar la predicción de los procesos ARMA estacionarios, debemos notar que es muy común que la media de dichos procesos sea diferente de cero.

Es decir, asumiendo que \(Y_t\) es un proceso ARMA causal e invertible con media \(\mu\), es posible definir:

\[
X_t = Y_t - \mu
\]

donde:

\[
E(X_t)=0
\]

En este caso, la función de autocovarianza de \(X_t\) e \(Y_t\) es la misma, tal como aparece en pantalla.

Adicionalmente, en términos del predictor, se tiene que:

\[
\tilde{y}_{n+m}
=
\tilde{x}_{n+m}+\mu
\]

Es decir, el predictor de \(y_{n+m}\) es el predictor de \(x_{n+m}\) más la media \(\mu\).

Y dado que la varianza no se ve afectada por un traslado, se tiene que el error cuadrático medio de predicción es el mismo para \(\tilde{x}\) e \(\tilde{y}\).

Esto quiere decir que los predictores coinciden con la media a largo plazo.

Además, basta con asumir que el proceso tiene media cero para los cálculos, y luego se puede agregar la media en caso de ser necesario.

Continuando con la predicción para los modelos ARMA, es posible obtener las predicciones sin encontrar directamente los coeficientes \(\pi_j\).

En el caso de los AR(p), esto es evidente.

### Ejemplo: AR(2)

En el AR(2), se tiene que el predictor de \(x_{n+1}\) está dado por:

\[
-\pi_1x_n-\pi_2x_{n-1}-\ldots-\pi_nx_1
\]

lo cual va a ser igual a:

\[
\phi_1x_n+\phi_2x_{n-1}
\]

ya que:

- \(\pi_1=-\phi_1\)
- \(\pi_2=-\phi_2\)
- \(\pi_j=0\), para \(j \ge 2\)

En el caso del predictor de \(x_{n+2}\), se tiene que es igual a:

\[
\phi_1\tilde{x}_{n+1|n}+\phi_2x_n
\]

Para el predictor de \(x_{n+3}\), tenemos que este será:

\[
\phi_1\tilde{x}_{n+2|n}+\phi_2\tilde{x}_{n+1|n}
\]

Continuando con la ecuación recursiva, se obtiene que el predictor de \(x_{n+m}\) va a ser igual a:

\[
\phi_1\tilde{x}_{n+m-1|n}
+
\phi_2\tilde{x}_{n+m-2|n}
\]

para:

\[
m \ge 3
\]

Como se puede apreciar, la recurrencia de los predictores es la misma que la recurrencia del modelo AR(2).

### Ejemplo: MA(1)

Como otro ejemplo, para un MA(1) invertible, se tiene que la representación AR infinito es la que se da a continuación.

Luego, el predictor de \(x_{n+1}\) es:

\[
-\pi_1x_n-\pi_2x_{n-1}-\ldots-\pi_nx_1
\]

lo cual corresponde a:

\[
\theta x_n-\theta^2x_{n-1}+\theta^3x_{n-2}
\]

y así hasta:

\[
-(-\theta)^n x_1
\]

Luego, el predictor de \(x_{n+2}\) se presenta a continuación.

Siguiendo la recurrencia se tiene que:

\[
\tilde{x}_{n+m|n}=0
\]

si:

\[
m \ge 2
\]

Por otro lado, en el caso de los modelos ARMA, la recurrencia podría complicarse.

Sin embargo, el siguiente resultado generaliza los ejemplos vistos para el AR(2) y el MA(1).

La proposición establece que el predictor:

\[
\tilde{x}_{n+m|n}
\]

es una combinación lineal de los predictores en los \(p\) instantes anteriores y en los \(q\) errores anteriores.

Tal como vimos en la esperanza condicional, el error es cero si \(t \le 0\) o si \(t > n\).

Mientras que cuando \(t\) está entre 1 y \(n\), el error de predicción se calcula utilizando la estructura del modelo.

En el caso de \(\tilde{x}_{t|n}\), cuando \(t\) está entre 1 y \(n\), el valor predicho es igual a \(x_t\), y cero cuando \(t < n\).

Este resultado permite obtener las predicciones utilizando la estructura del proceso \(X_t\), sin obtener directamente la representación AR infinito.

### Ejemplo: ARMA(1,1)

Veamos cómo funciona la proposición anterior en un ARMA(1,1) causal e invertible.

En primer lugar, obtenemos el predictor:

\[
\tilde{x}_{n+1|n}
\]

como:

\[
\phi x_n + \theta \tilde{w}_{n|n}
\]

y:

\[
\tilde{x}_{n+m|n}
=
\phi \tilde{x}_{n+m-1|n}
\]

para:

\[
m \ge 2
\]

Sin embargo, para calcular \(\tilde{w}_{n|n}\) es necesario estimar recursivamente todos los:

\[
\tilde{w}_{t|n}
\]

con:

\[
t = 1,\ldots,n
\]

En este caso, la recurrencia queda como sigue:

\[
\tilde{w}_{0|n}=x_0
\]

y:

\[
\tilde{w}_{t|n}
=
x_t-\phi x_{t-1}-\theta \tilde{w}_{t-1|n}
\]

Es decir, asumiendo que:

\[
x_0=0
\]

se tiene el resultado para \(\tilde{w}_{1|n}\) que aparece en pantalla.

En este caso particular, recordemos que los coeficientes de la representación causal son \(\psi_j\).

Estos nos permiten obtener el error cuadrático medio de predicción:

\[
P_{n+m|n}
\]

tal como se muestra en pantalla.

Por ejemplo, para una serie de tiempo de tamaño 100 que sigue un proceso ARMA(1,1) con:

- \(\phi=0.5\)
- \(\theta=0.5\)
- \(\mu=10\)
- \(\sigma^2=1\)

la tabla adjunta muestra los valores predichos y su respectivo error cuadrático medio de predicción para:

\[
m = 1,2,3,\ldots,10
\]

Se puede observar que los valores predichos tienden a 10, como era de esperarse.

Asimismo, el error cuadrático medio de predicción tiende a la varianza del proceso:

\[
\gamma_X(0)=\frac{7}{3}
\]

Lo anterior se puede visualizar en la siguiente figura, donde la línea roja segmentada es la media del proceso.

La curva negra corresponde a una serie simulada con los parámetros anteriores.

La curva azul representa los valores predichos.

Mientras que el error cuadrático medio de predicción se visualiza en las bandas azules, las cuales fueron construidas como el predictor puntual más menos la raíz del error cuadrático medio de predicción.

**Prueba tu aprendizaje respondiendo a la siguiente pregunta.**

---

## Resumen

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes:

- El mejor predictor lineal puede ser aproximado con el mejor predictor que utiliza un pasado infinito de la serie.
- La aproximación ocurre al truncar la serie que determina la predicción de los valores observados.
- Es decir, no considera \(x_0\), ni \(x_{-1}\), ni todo el pasado.
- Los coeficientes de las representaciones AR infinito y MA infinito permiten obtener las predicciones y su respectivo error cuadrático medio.
- Los valores predichos de un modelo ARMA causal e invertible convergen al valor medio.
- El error cuadrático medio de predicción converge a la varianza del proceso.
