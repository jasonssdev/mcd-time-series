# Procesos Lineales

Bienvenidos y bienvenidas a una nueva clase.

La estacionariedad juega un papel clave en la predicción de series de tiempo.

Específicamente, la función de autocovarianza es el objeto más importante, ya que está presente para estimación, predicción y simulación de procesos estocásticos.

Pero, tal como se mencionó al final de la clase anterior, puede ser complejo verificar la estacionariedad o encontrar la función de autocovarianza para la mayoría de los modelos comúnmente utilizados, tales como:

- AR(p)
- MA(q)
- ARMA(p, q)

Formalmente, estos modelos se definen a través de un ruido blanco \(\varepsilon_t\) de media cero y varianza \(\sigma^2\), a través de las siguientes relaciones que se muestran en pantalla.

Es decir, un MA(q) es una combinación lineal del error actual y del pasado del error, hasta un lag \(q\), con la restricción de que solo el último coeficiente \(\theta_q\) sea distinto de 0.

El resto de coeficientes no tiene esta restricción.

Mientras que un AR(p) es una combinación lineal entre el error actual y el pasado de la serie, hasta un lag \(p\), con la restricción de que \(\phi_p\) sea distinto de 0.

Nuevamente, el resto de los coeficientes no tiene dicha restricción.

Finalmente, un ARMA(p, q) tiene ambas características.

Esto es, una combinación lineal entre el error actual, el pasado del error y el pasado de la serie, con la restricción de que los últimos coeficientes, tanto autorregresivo como media móvil, deben ser diferentes de 0.

Por definición, un MA(q) es una combinación lineal de ruido blanco, pero, ¿será que el AR(p) y el ARMA(p, q) también lo son?

Afortunadamente, la respuesta es sí.

Por lo que analizar, en general, los procesos lineales nos brindará una herramienta esencial para abordar estos tipos de procesos.

En particular, nos permitiría chequear la estacionariedad de forma directa, así como también nos entrega un procedimiento para determinar la función de autocovarianzas.

Cabe destacar que el término lineal se refiere a que el proceso es una combinación lineal del ruido.

Combinaciones como el producto entre \(\varepsilon_t\) y \(\varepsilon_{t-1}\), u otras relaciones no lineales del ruido, no son incluidas en el modelo.

En esta clase se revisarán los siguientes temas:

1. El AR(1) como un proceso lineal.
2. Definición formal de procesos lineales.

---

## Tema 1: El AR(1) como un Proceso Lineal

Para comprender por qué analizar los procesos lineales, considere, por ejemplo, el AR(1):

\[
X_t = \phi X_{t-1} + \varepsilon_t
\]

E intentemos calcular su función de media, obteniendo la siguiente ecuación en diferencias:

\[
\mu(t) = \phi \mu(t-1)
\]

cuya solución depende de los supuestos sobre el proceso.

Del mismo modo, la función de autocovarianza queda como se muestra a continuación, la cual también es una ecuación en diferencias de la forma:

\[
\gamma(h) = \phi \gamma(h-1)
\]

Notar que la covarianza entre \(X_t\) y \(\varepsilon_{t+h}\) es igual a 0, la cual se justifica a partir de un proceso lineal y cierto supuesto sobre el proceso.

Más aún, al aplicar \(j\) veces la recurrencia del AR(1), se obtiene que \(X_t\) es una combinación lineal del error presente, de los errores pasados hasta el instante \(j\), y el valor de la serie del instante \(t-j-1\), tal como se muestra en pantalla.

Ingenuamente, uno podría asumir que \(|\phi| < 1\) y tomar el límite cuando \(j\) tiende a infinito.

Así, el término:

\[
\phi^{j+1}X_{t-j-1}
\]

debería tender a 0, lo cual sería cierto solo bajo ciertas condiciones que son, justamente, las que entregan los procesos lineales.

Es más, al aplicar la esperanza a la ecuación anterior y asumir que \(\mu(t)\) es finita para todo \(t\), entonces \(\mu(t)\) tiende a 0 cuando \(j\) tiende a infinito, tal como se muestra en pantalla.

Ahora bien, si \(\phi\) fuese mayor a 1 en valor absoluto, podríamos evaluar el AR(1) en \(t+1\), obteniendo la siguiente expresión para \(X_t\).

Luego, aplicar la relación anterior de forma recursiva \(j\) veces para obtener \(X_t\) como una combinación lineal de los errores futuros y de la serie en el instante \(j\) al futuro, tal como se muestra en pantalla.

Luego, como el valor absoluto de \(\phi^{-1}\) es menor a 1, se puede nuevamente tomar esperanza y asumir que es acotada para aplicar el límite cuando \(j\) tiende a infinito y mostrar que \(\mu(t)\) converge a 0.

El problema de este último caso es que la serie depende de su futuro, lo cual es un problema al momento de realizar predicciones.

Notar que en los casos anteriores no fue tan sencillo obtener la función de media.

Por lo que, naturalmente, la función de autocovarianza es aún más compleja.

## Random Walk o Camino Aleatorio

Antes de comenzar con las definiciones generales de los procesos lineales, como última observación sobre el AR(1), notar que para el caso \(\phi = 1\), el proceso se denomina **Random Walk** o **camino aleatorio**.

Si bien tiene media 0, su varianza no es constante, por lo que no puede ser estacionario en el sentido débil.

Más aún, su varianza tiende a crecer a medida que \(t\) crece.

Ya que, asumiendo que \(X_0\) es igual a 0 con cualquier constante, se tiene que la varianza del proceso es proporcional a \(t\).

Es decir, crece a medida que \(t\) crece.

La figura muestra la trayectoria de 4 Random Walk, todos iniciados en \(X_0 = 0\).

Como se puede apreciar, las 4 trayectorias muestran un comportamiento muy irregular.

Este proceso se denomina camino aleatorio, justamente, porque no lo podemos predecir.

Para todos los casos del AR(1), se tiene de forma genérica que \(X_t\) es la serie de menos infinito a más infinito de algunos coeficientes \(\psi_j\) multiplicados por el ruido blanco, tal como se muestra en pantalla.

Es decir, hemos probado que el proceso AR(1) es una combinación lineal del ruido blanco.

Tal como se mencionó en la introducción.

Esto no solo se cumple para el AR(1), sino que para toda la familia AR(p), así como también para la familia ARMA(p, q), donde los coeficientes \(\psi_j\) determinarán el tipo de estructura.

Prueba tu aprendizaje respondiendo a la siguiente pregunta.

---

## Tema 2: Definición Formal de Procesos Lineales

Para poder formalizar los procesos lineales, en primer lugar, consideremos una sucesión de números \(a_n\).

Remarcamos que no son variables aleatorias.

Diremos que dicha sucesión es absolutamente sumable si la serie de los valores absolutos de dicho número es convergente.

Ahora, consideremos dos sucesiones de números \(a_n\) y \(b_n\), cada una absolutamente sumable.

Entonces:

- La suma \(a_n + b_n\).
- El producto \(a_n b_n\).
- La convolución.

Esta última definida como aparece en pantalla, son absolutamente sumables.

Como se puede apreciar, la convolución tiene la misma forma general en cómo escribimos la serie \(X_t\) para el proceso AR(1), lo cual nos permite entregar el siguiente teorema que se muestra en pantalla.

Sin entrar en la rigurosidad de la demostración, el punto i nos dice que al realizar la convolución entre una sucesión de números \(a_j\) absolutamente sumable y una sucesión de variables aleatorias \(Z_t\) con segundo momento finito, se obtiene otra sucesión de variables aleatorias \(X_t\) bien definida.

El punto ii nos indica que el error cuadrático medio entre la serie con todos los términos y la serie truncada hasta \(n\) tiende a cero a medida que \(n\) tiende a infinito.

Mientras que el punto iii nos establece que la serie resultante sigue siendo de segundo orden.

Por otro lado, el siguiente teorema permite calcular la media de una serie obtenida mediante la convolución y la esperanza del producto entre dos series obtenidas por la convolución, donde la diferencia de la serie resultante es la sucesión de números y no la sucesión de variables aleatorias.

Nuevamente, sin entrar en detalles de la demostración, el teorema nos establece, por un lado, que para obtener la función de media de \(X_t\) es posible truncar la serie, calcular el valor esperado de la suma parcial para un \(n\) fijo y arbitrario, y luego tomar el límite cuando \(n\) tiende a infinito.

Notar que este punto justifica el desarrollo empleado para obtener la media del AR(1).

Por otro lado, el teorema también nos indica cómo obtener la esperanza del producto de dos procesos lineales a partir de las series truncadas.

Este último punto es clave para determinar la función de autocovarianza en un modelo lineal.

## Caso Particular: Ruido Blanco

En efecto, al considerar el caso particular en que \(Z_t\) es un ruido blanco de media 0 y varianza \(\sigma^2\), se tiene que todo proceso lineal es de la forma:

\[
X_t = \sum_{j=-\infty}^{\infty} \psi_j \varepsilon_{t-j}
\]

con:

\[
\psi_0 = 1
\]

Además, al considerar que:

\[
Y_t = X_{t+h}
\]

de modo que los coeficientes en el teorema anterior sean:

\[
a_j = \psi_j
\]

y

\[
b_j = \psi_{j+h}
\]

se tiene que la función de media de \(X_t\), notada por \(\mu_{X_t}\), y la función de autocovarianza de \(X_t\), denotada por \(\gamma_X(h)\), son las que se muestran en pantalla.

## Ejemplo: MA(1)

Así, por ejemplo, para un MA(1):

\[
X_t = \varepsilon_t + \theta \varepsilon_{t-1}
\]

se tiene que:

\[
\psi_0 = 1
\]

\[
\psi_1 = \theta
\]

y:

\[
\psi_j = 0
\]

para todos los otros valores de \(j\).

En consecuencia:

\[
\gamma_X(0)
=
\sigma^2
\sum_{j=-\infty}^{\infty}
\psi_j^2
\]

lo cual es igual a:

\[
\gamma_X(0)
=
\sigma^2(1+\theta^2)
\]

También:

\[
\gamma_X(1)
=
\sigma^2\theta
\]

y:

\[
\gamma_X(h)=0
\]

para todo \(h \geq 2\).

Recuperando así la función de autocovarianza que habíamos calculado por definición para este modelo en las clases anteriores.

## Ejemplo: AR(1)

Como otro caso particular, para el proceso AR(1) con \(|\phi| < 1\), por la construcción realizada anteriormente, se tiene que:

\[
\psi_j = \phi^j
\]

para:

\[
j = 0, 1, 2, \ldots, \infty
\]

y:

\[
\psi_j = 0
\]

para:

\[
j = -1, -2, -3, \ldots, -\infty
\]

Luego, para \(h > 0\):

\[
\gamma_X(h)
=
\frac{\sigma^2 \phi^h}{1-\phi^2}
\]

La media es 0 y la función de autocovarianza es:

\[
\frac{\sigma^2 \phi^h}{1-\phi^2}
\]

## Autocorrelación Muestral

Por último, los procesos lineales también justifican la distribución asintótica de la autocorrelación muestral, la cual está dada en el siguiente teorema.

De esta, podemos decir que la autocorrelación muestral \(\hat{\rho}(h)\) es un estimador insesgado y consistente de la autocorrelación poblacional \(\rho(h)\).

Este teorema también justifica la banda de confianza que trazamos en la gráfica de la autocorrelación muestral que vimos en las clases pasadas.

Prueba tu aprendizaje respondiendo a la siguiente pregunta.

---

## Resumen

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

- Los modelos comunes en series de tiempo, tales como AR, MA y ARMA, son procesos lineales, ya que se pueden escribir como una combinación lineal del ruido blanco.
- Los procesos lineales, en general, dependen del presente, pasado y futuro del ruido blanco.
- Sin embargo, los que son útiles para la predicción son aquellos que dependen exclusivamente del presente y pasado del error.
- Para el caso de los modelos MA(q), el proceso lineal es una suma finita del error.
- Mientras que para los modelos AR(p) y ARMA(p, q), el proceso lineal subyacente es una serie infinita del error.
- A partir de los procesos lineales, es posible chequear la estacionariedad y determinar la función de autocovarianza de modelos lineales.