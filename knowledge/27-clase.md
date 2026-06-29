# Clase sincrónica 3: predicción de modelos ARMA

Hola, ¿estás listo para la tercera clase sincrónica?

¿Sí?

Perfecto.

Bien, vamos a dar comienzo a la tercera clase sincrónica.

Voy a dejar la sala de espera habilitada para que puedan ingresar directamente.

Un segundo.

Buenas noches.

Buenas noches, Pedro.

Bien, entonces, en esta tercera clase vamos a repasar contenidos conceptuales de las últimas dos semanas.

Aparte de eso, vamos a consultar cómo ha ido en el curso hasta el momento.

El ayudante me confirmó que ya los grupos para el proyecto estaban listos. Así que no sé si ustedes ya tienen acceso desde Coursera a los grupos. Y si no lo tienen, que me avisen, porque a veces hay que habilitarlo manualmente.

O sea, hay que asignarle una actividad para que puedan ver a los integrantes.

Consultas generales, obviamente, se pueden hacer en este espacio.

Esta clase la he organizado igual que la clase anterior.

Pedro Pérez puso:

> No tengo grupo.

En realidad, ya todos tienen grupo. Había un plazo para que ustedes mandaran los integrantes del grupo. Ese plazo ya pasó. Luego, los que estaban sin grupo fueron agrupados aleatoriamente.

Eso ya está listo en la plataforma.

Solo falta verificar que ustedes tengan acceso a esa parte. Si no tienen acceso, voy a tratar de gestionarlo lo más pronto posible.

Creo que es lo que queda esta semana: que ya todos sepan de antemano con quiénes tienen que trabajar en la última semana.

Si es la clase 3, estamos en la semana 5.

El enfoque de la clase es igual a la anterior.

Primero, un resumen conceptual. Trataré de hacerlo lo más breve posible.

Después continuaremos con el estudio de casos que partimos en las clases pasadas. Ahí nos cambiaremos directamente a notebook para analizar algunas cosas y ver un poco más directo todos estos conceptos que estamos viendo semana a semana, como uno los tiene que ver en una serie real.

---

## Semana 4: conceptos teóricos

La semana 4, como les dije, era una de las semanas más pesadas teóricamente y conceptualmente.

Vimos:

- La representación del modelo ARMA como un proceso lineal.
- La causalidad.
- La invertibilidad.
- Cómo calcular teóricamente la función de autocorrelación simple, la ACF.
- La función de autocorrelación parcial, la PACF.

Todos estos conceptos fueron vistos desde el punto de vista teórico.

Básicamente, la causalidad y la invertibilidad tienen que ver con estas representaciones:

- AR infinito.
- MA infinito.

Estas representaciones nos ayudan para proponer modelos y para predecir posteriormente.

Luego, en los conceptos de esta semana apareció el concepto de predicción, donde la idea de usar toda la estructura probabilística que hay detrás de los procesos es utilizar el mejor predictor asumiendo pasado infinito.

Esa es la idea fundamental.

---

## Operador de rezago

Para comprender la parte conceptual de la semana 4 y escribir un modelo ARMA como un modelo lineal, uno recurre al operador de rezago.

Básicamente, el operador de rezago dice que:

\[
B X_t = X_{t-1}
\]

Eso quiere decir que si uno hace:

\[
B^2 X_t
\]

eso es lo mismo que:

\[
B(BX_t)
\]

Por lo tanto, esto es lo mismo que:

\[
B(X_{t-1})
\]

y eso sería:

\[
X_{t-2}
\]

En general, uno puede probar que:

\[
B^p X_t = X_{t-p}
\]

Entonces, con esta forma, o en realidad esta forma fundamental, es la que nosotros usamos para escribir los modelos ARMA como un proceso lineal.

---

## Ejemplo: AR(1)

Tenemos:

\[
X_t = \phi X_{t-1} + \varepsilon_t
\]

Esto es lo que se llama un AR(1).

El procedimiento es:

\[
X_t - \phi X_{t-1} = \varepsilon_t
\]

Como:

\[
X_{t-1} = B X_t
\]

entonces:

\[
X_t - \phi B X_t = \varepsilon_t
\]

Factorizando:

\[
(I-\phi B)X_t = \varepsilon_t
\]

La idea aquí es factorizar. Esta factorización es lo que llamamos linealidad y lo que nos permite despejar:

\[
X_t = (I-\phi B)^{-1}\varepsilon_t
\]

Entonces, ¿por qué ayuda este operador?

Porque aquí uno puede utilizar un resultado bastante directo de la serie geométrica:

\[
\sum_{j=0}^{\infty} R^j = \frac{1}{1-R} = (1-R)^{-1}
\]

siempre que:

\[
|R| < 1
\]

Aquí nosotros tenemos ese resultado, por lo tanto, esto se puede escribir como:

\[
\sum_{j=0}^{\infty}(\phi B)^j \varepsilon_t
\]

Esto es lo mismo que:

\[
\sum_{j=0}^{\infty}\phi^j B^j \varepsilon_t
\]

y como:

\[
B^j \varepsilon_t = \varepsilon_{t-j}
\]

entonces:

\[
X_t = \sum_{j=0}^{\infty}\phi^j \varepsilon_{t-j}
\]

Esto de los operadores, lo que llamamos después el polinomio característico, es lo que nos permite escribir rápidamente el proceso de esta forma.

Aquí \(X_t\) está escrito como un proceso lineal, porque depende linealmente de un proceso de ruido blanco.

La condición es que:

\[
|\phi| < 1
\]

Y esa condición viene de la invertibilidad que tiene aquí la serie de potencias.

---

## Modelo ARMA general

En un proceso más general, como el ARMA, donde \(X_t\) depende de:

- \(p\) valores de \(\phi\).
- \(q\) valores de \(\theta\).
- Errores rezagados.

Uno puede escribir dos polinomios:

- El operador autorregresivo.
- El operador de media móvil.

Por ejemplo, si escribimos un proceso ARMA(3,2):

\[
X_t = \phi_1X_{t-1}+\phi_2X_{t-2}+\phi_3X_{t-3}+\varepsilon_t+\theta_1\varepsilon_{t-1}+\theta_2\varepsilon_{t-2}
\]

Reescribiendo:

\[
(1-\phi_1B-\phi_2B^2-\phi_3B^3)X_t
=
(1+\theta_1B+\theta_2B^2)\varepsilon_t
\]

Entonces:

- \(BX_t = X_{t-1}\)
- \(B^2X_t = X_{t-2}\)
- \(B^3X_t = X_{t-3}\)
- \(B\varepsilon_t = \varepsilon_{t-1}\)
- \(B^2\varepsilon_t = \varepsilon_{t-2}\)

Uno puede simplificar por factor común y factorizar.

Esto es lo que llamamos:

- Polinomio autorregresivo.
- Polinomio de media móvil.

Al verlo como polinomio, uno dice:

- Si quiero despejar \(X_t\), invierto hacia ese lado.
- Si quiero despejar \(\varepsilon_t\), invierto hacia el otro lado.

Esas son las operaciones esenciales en el proceso estacionario.

---

## Estacionariedad, causalidad e invertibilidad

Para ajustar el modelo ARMA, necesitamos que las raíces del polinomio que se genera estén fuera del disco unitario.

En el ejemplo del AR(1), el polinomio es:

\[
1-\phi B
\]

Creamos un polinomio:

\[
1-\phi z
\]

Si igualamos esto a cero:

\[
1-\phi z = 0
\]

entonces:

\[
z = \frac{1}{\phi}
\]

Si queremos que esté fuera del disco unitario, significa que:

\[
|z| > 1
\]

lo cual es equivalente a decir que:

\[
\left|\frac{1}{\phi}\right| > 1
\]

y, a su vez:

\[
|\phi| < 1
\]

Es la misma condición que sale de la serie geométrica.

Lo bueno de verlo como un polinomio es que uno encuentra automáticamente, de modo general, cuáles son las condiciones de los coeficientes para generar un proceso estacionario.

La condición es que las raíces sean mayores a uno en módulo.

Por otro lado, uno no quiere que la serie quede dependiendo del futuro, porque si no, sería no predecible. Por eso se agrega la condición de causalidad.

La condición de causalidad significa que el proceso se puede escribir como una combinación lineal del ruido, que es lo mismo que la representación lineal del ARMA.

Para lograr esta representación, las raíces del polinomio autorregresivo tienen que estar fuera del disco unitario.

Además, estos coeficientes son importantes porque después determinan la función de covarianza o de autocovarianza.

En los modelos ARMA también existe un problema de ambigüedad.

Dos conjuntos paramétricos podrían generar exactamente el mismo modelo. Entonces, eso hace que el modelo sea no estimable.

Hay que restringir el conjunto paramétrico para que sea estimable, y eso se llama condición de invertibilidad.

Básicamente, se logra cuando el ruido se puede escribir como una combinación del proceso.

Para que este polinomio se pueda invertir, necesitamos que sus raíces estén fuera del disco unitario.

Esto se llama representación AR infinito, y las condiciones surgen naturalmente a partir de las raíces.

En un modelo ARMA(p,q):

- Sabemos si es causal si dentro del disco unitario no hay ninguna raíz del polinomio autorregresivo.
- Sabemos si es invertible si dentro del disco unitario no hay ninguna raíz del polinomio de media móvil.

---

## Representaciones MA infinito y AR infinito

Cuando queremos encontrar la representación MA infinito para la causalidad, tenemos que resolver una ecuación.

Cuando queremos escribir el operador para la invertibilidad, tenemos que resolver otra ecuación.

Eso permite encontrar coeficientes de forma relativamente directa.

Ahora, ¿para qué queremos todo eso?

Eso se justifica en dos cosas.

La ACF teórica se justifica al tener los coeficientes \(\psi_j\). Cada vez que logramos escribir el proceso como:

\[
X_t = \sum_{j=0}^{\infty}\psi_j\varepsilon_{t-j}
\]

podemos calcular la función de covarianza directamente.

Si logramos encontrar estos coeficientes, vamos a tener inmediatamente la función de covarianza para:

- \(h=0\)
- \(h=1\)
- \(h=2\)
- \(h=3\)

y así sucesivamente.

Por definición del ARMA(p,q), la función de covarianza queda expresada en términos de recurrencia.

Esto es equivalente a la expresión de la representación MA infinito.

Entonces, ¿qué necesitamos para encontrar estos coeficientes?

Necesitamos saber las raíces del polinomio característico.

Con eso tenemos los coeficientes. Con esos coeficientes tenemos la función de autocovarianza. Y si ya tenemos la función de autocovarianza, podemos calcular las correlaciones.

Con las correlaciones nosotros podemos identificar modelos.

---

## ACF y PACF

Siempre hay que tener cuidado, porque cuando el orden aumenta a un grado mayor que uno, empiezan a aparecer múltiples raíces.

Recordemos que en un polinomio de grado \(p\) hay \(p\) raíces. Estas pueden ser:

- Todas reales.
- Algunas reales iguales.
- Algunas complejas.
- Algunas con multiplicidad.
- Raíces repetidas.

Pueden existir muchos casos, y eso provoca diferentes formas de la función de autocorrelación.

Generalmente, la función de autocorrelación decae a cero, pero cómo decae depende del comportamiento de las raíces.

Por otro lado, para obtener la PACF no es tan directo.

Aparece el algoritmo de Durbin-Levinson, donde uno empieza a hacer una descomposición.

La correlación parcial es la correlación de los residuos de un modelo, entonces no es tan directo.

La PACF es una función de la ACF.

Dentro del algoritmo de Durbin-Levinson aparece el error cuadrático medio, que vamos a utilizar para cuantificar la variabilidad o incertidumbre de la predicción.

Todos estos términos son conceptualmente necesarios.

Un caso particular interesante es que, si uno sigue esta recurrencia, la autocorrelación parcial de orden 1 es igual a la autocorrelación simple de orden 1.

Es el único caso donde ocurre eso.

---

## Identificación de modelos usando ACF y PACF

En una serie estacionaria, por ejemplo, un AR(1), tenemos distintas trayectorias y observamos un decaimiento exponencial.

Aquí tenemos una sola raíz, y esa raíz obviamente es real, por lo tanto, trae este decaimiento exponencial.

También tenemos un solo lag importante en la PACF, siempre cercano a 0.6.

Eso nos entrega una idea:

Si vemos una serie con una ACF que decae exponencialmente y una PACF con un lag significativo y el resto cercano a cero, entonces eso corresponde a un AR(1).

La serie en sí misma nunca dice nada. Podemos ver tres comportamientos distintos y no podríamos saber solo desde la serie que corresponde a un AR(1).

La otra parte interesante es que ese número cercano a 0.6 aparece porque, en el modelo AR(1), los coeficientes muestrales convergen a los teóricos.

En general:

- En un AR(p), la ACF siempre decae a cero cuando \(h\) tiende a infinito.
- En un MA(q), la ACF se anula completamente cuando \(h > q\).
- En un ARMA(p,q), como tiene ambas cosas, la ACF decae a cero.

La PACF tiene el comportamiento opuesto:

- En un AR(p), la PACF se anula después de \(p\).
- En un MA(q), la PACF decae exponencialmente.
- En un ARMA(p,q), tanto la ACF como la PACF tienden a decaer.

Ahí cuesta distinguir:

- ¿Es un MA grande?
- ¿Es un AR grande?
- ¿O es un ARMA con dos parámetros pequeños?

Esa es la parte más difícil, donde uno tiene que ver muchas series para tener una idea de cómo usar apropiadamente estas funciones para proponer modelos coherentes.

---

## Predicción

En esta semana vimos la predicción.

Aquí toma aún más sentido por qué hacer el AR infinito y el MA infinito.

Si logramos escribir el ruido como un AR infinito y el proceso tiene su representación MA infinito, ya tenemos todo lo necesario para hacer predicción y cuantificar incertidumbre.

El predictor lineal es el predictor que podríamos hacer en cualquier caso.

Asumimos que el valor que queremos predecir:

\[
X_{n+m}
\]

lo queremos predecir por una combinación lineal de los datos observados con un intercepto.

Queremos minimizar:

\[
E[(\hat{X}_{n+m|n}-X_{n+m})^2]
\]

Para minimizar esto derivamos con respecto a cada coeficiente, y eso genera las ecuaciones normales.

Como es una función cuadrática, las derivadas quedan lineales en los parámetros. Por lo tanto, es un sistema relativamente directo de calcular.

Sin pérdida de generalidad, uno puede asumir que la media es cero. En ese caso, el intercepto es igual a cero para que el estimador sea insesgado.

Cada vez que cambie el horizonte de predicción, cambian los coeficientes.

Este problema, que es básicamente un problema de mínimos cuadrados, nos permite hacer predicción siempre. Pero aquí no estamos usando toda la estructura del proceso.

---

## Relación con Durbin-Levinson

Cuando resolvemos este problema de optimización, aparecen exactamente los coeficientes del algoritmo de Durbin-Levinson.

Esto es importante porque representa la correlación parcial.

La matriz de covarianzas, multiplicada por el vector de parámetros que quiero ubicar, es igual al vector de covarianzas.

Ese vector de covarianzas es la covarianza entre el instante que quiero predecir y cada uno de los términos observados.

Al invertir la matriz, se obtiene el vector de parámetros.

El algoritmo de Durbin-Levinson no es otra cosa que una forma de calcular este cálculo matricial a partir de particiones de matriz.

El valor objetivo que estábamos minimizando es el error cuadrático medio de predicción.

Todo queda expresado en términos de la función de covarianza.

Entonces, si conocemos la función de covarianza, básicamente tenemos:

- Los parámetros estimados.
- La incertidumbre estimada.

Por eso es tan importante la función de autocorrelación.

Recordemos que la correlación en el instante \(h\) es:

\[
\rho(h)=\frac{\gamma(h)}{\gamma(0)}
\]

Lo que hay que calcular básicamente es:

- \(\gamma(0)\)
- \(\gamma(h)\) para distintos valores de \(h\)

Con eso tenemos la función de autocorrelación.

Ahí tenemos la relación dato-modelo a través de la función de covarianza.

Por eso es el ingrediente más importante en el modelamiento de series de tiempo o de datos dependientes.

---

## Predicción usando pasado infinito

Todo el cálculo anterior se hace resolviendo un problema de mínimos cuadrados.

Pero se podría aproximar usando un pasado remoto.

Es decir, aunque en la práctica conocemos solo desde:

\[
X_1,\ldots,X_n
\]

asumimos que también existen datos hacia atrás, que la serie tiene pasado infinito.

Como resultado, el mejor predictor es la esperanza condicional.

La esperanza condicional coincide con el mejor predictor lineal solamente si la distribución de los datos es gaussiana.

Si la distribución no es gaussiana, la esperanza condicional sigue siendo el mejor predictor, pero no necesariamente va a ser una función lineal de los datos.

Entonces, en la práctica podemos usar la esperanza condicional con pasado infinito para aproximar el mejor predictor lineal.

La aproximación será buena si la longitud de la serie es suficientemente grande.

¿Por qué asumir pasado infinito si los datos son finitos?

Porque así podemos aprovechar mejor la estructura de la serie.

Ahí aparece la representación AR infinito:

\[
\varepsilon_t = \sum_{j=0}^{\infty}\pi_j X_{t-j}
\]

Con esta estructura podemos calcular predicciones e incertidumbre sin resolver el problema de optimización en cada etapa.

Resolver el problema de optimización en cada etapa significa invertir una matriz de orden \(n \times n\).

Si la serie tiene largo 10.000, habría que invertir una matriz de 10.000 por 10.000, lo cual es muy lento.

Con la representación AR infinito no necesitamos invertir matrices.

Esa es la ganancia de asumir pasado infinito.

---

## Ecuaciones de predicción

La serie en el dato que queremos predecir se puede escribir usando su representación causal.

Al aplicar esperanza condicional, los errores futuros tienen esperanza cero porque no podemos conocerlos.

En cambio, los errores pasados pueden ser usados porque ya están contenidos en la información observada.

Por eso:

- Si \(t > n\), el error esperado es cero.
- Si \(t \le n\), el error es observado.

La esperanza condicional de \(X_t\) dado el pasado será igual al valor observado si \(t \le n\).

Esto permite encontrar los predictores en el instante \(n+m\) a partir de los predictores anteriores.

Por un lado, la predicción depende de los datos observados.

Por otro lado, depende de los predictores anteriores.

En la práctica, como solo conocemos desde \(X_1\) en adelante, se trunca la serie.

Si queremos predecir \(m\) instantes hacia el futuro, necesitamos predecir hasta \(m-1\) primero y después usar los datos observados anteriores.

La importancia de la representación causal es encontrar la función de autocorrelación.

La importancia de la representación invertible es escribir las predicciones de forma directa.

---

## Predicción en modelos ARMA

Cuando aplicamos esto a un ARMA, podemos escribir el predictor como:

\[
\hat{X}_{t|n}
=
\phi_1\hat{X}_{t-1|n}
+
\cdots
+
\phi_p\hat{X}_{t-p|n}
+
\theta_1\hat{\varepsilon}_{t-1|n}
+
\cdots
+
\theta_q\hat{\varepsilon}_{t-q|n}
\]

El error será cero si \(t > n\), y si no, se puede calcular mediante los polinomios respectivos.

Adicionalmente, como el algoritmo trae por defecto el error cuadrático medio, uno puede construir intervalos de confianza.

Si tenemos el estimador puntual, podemos construir:

\[
\hat{X}_{n+m|n} \pm c\sqrt{P_{n+m|n}}
\]

Cuando los datos son gaussianos y queremos un intervalo de confianza del 95%, esta constante \(c\) es aproximadamente 2.

Esto nos permite no solamente predecir, sino también cuantificar la incertidumbre en el proceso.

¿Cuál es la ganancia de usar en la predicción la estructura del modelo ARMA?

Que uno escribe la predicción de forma recursiva.

Si uno quiere usar siempre el mejor predictor lineal, está obligado a resolver sistemas lineales que pueden ser muy grandes.

Eso sería muy lento computacionalmente.

---

## Pregunta de un estudiante

> Profe, una duda. Cuando yo tengo \(n\) datos y estimo los coeficientes ACF y estimo el mejor modelo, no sé, un ARMA(3,2). El día de mañana me va a llegar otro dato. Pasado mañana me va a llegar otro. ¿Esos estimadores van a cambiar?

Podrían cambiar, pero no necesariamente.

Para el modelo, los parámetros quedan fijos hasta que no haya evidencia de un cambio estructural grande.

Lo que sí van a cambiar son los predictores.

Por ejemplo, pensemos en un AR(2).

Con \(n\) datos, el predictor de un dato hacia adelante sería:

\[
\hat{X}_{n+1|n}
=
\hat{\phi}_1X_n+\hat{\phi}_2X_{n-1}
\]

Aquí depende solamente de los dos últimos datos observados.

Para predecir dos instantes hacia el futuro:

\[
\hat{X}_{n+2|n}
=
\hat{\phi}_1\hat{X}_{n+1|n}+\hat{\phi}_2X_n
\]

Si después llega el dato real \(X_{n+1}\), ya no necesito usar el valor predicho. Puedo actualizar la predicción con el dato real:

\[
\hat{X}_{n+2|n+1}
=
\hat{\phi}_1X_{n+1}+\hat{\phi}_2X_n
\]

Eso puede cambiar la predicción, pero no significa que haya cambiado el modelo.

Lo que cambió fue el valor usado en la predicción.

Si la estructura de la serie sigue estable, con la misma media y varianza, no necesariamente hay que reestimar.

Pero si nuevos datos empiezan a mostrar un cambio estructural importante, ahí podría convenir reestimar parámetros o cambiar de modelo.

Uno puede ir chequeando con nuevas ACF y PACF.

Si siguen con la misma estructura, no hay un cambio estructural grande.

También existen modelos no lineales, como los TAR, que son modelos umbrales autoregresivos, donde aparecen cambios de régimen. Pero eso se escapa un poco de los modelos que estamos estudiando en este curso.

---

## Estudio de caso: serie SOI

En las primeras dos clases presentamos el problema y de dónde venían los datos.

En la clase 2 hicimos los primeros pasos:

- Composición.
- Transformación.
- ACF.
- PACF.
- Propuesta de modelos.

Ahora, en la clase 3 vamos a identificar más modelos y hacer predicción.

Seguimos trabajando con la serie SOI, índice de oscilación sur, porque luce estacionaria desde un comienzo.

La serie GEE, generación de energía eléctrica total, tiene un comportamiento no estacionario, y eso lo analizaremos en la última clase.

---

## Análisis de PACF

Ahora analizamos con más detalle la PACF.

Se propusieron varios modelos:

- AR(1) con parámetro positivo.
- AR(1) con parámetro negativo.
- MA(1) con parámetro positivo.
- MA(1) con parámetro negativo.
- ARMA(1,1) con parámetros positivos.

En una simulación, la PACF teórica es la misma, pero las muestrales son distintas.

Puede aparecer alguna correlación débil producto del azar, pero no necesariamente debe considerarse en el modelo.

Por eso existen bandas de confianza.

En los modelos MA(1), la PACF tiene un decaimiento tipo exponencial.

Eso cambia el orden respecto a los modelos AR.

Si observamos varios lags importantes, uno podría pensar que es un AR(3) o AR(4), pero en realidad puede ser la PACF de un MA(1).

Por eso hay que mirar ACF y PACF al mismo tiempo.

En el ARMA(1,1), ambas pueden tener decaimiento exponencial, lo que hace más difícil diferenciar modelos.

---

## Modelos de orden mayor

En un polinomio de orden mayor pueden aparecer:

- Raíces reales distintas.
- Raíces dobles.
- Raíces complejas.

Todas las raíces deben ser mayores a uno en módulo para estar fuera del disco unitario y cumplir la condición de estacionariedad.

Cuando las raíces son reales distintas, la ACF teórica decae y la PACF tiene dos lags importantes y luego cero. Eso corresponde a un AR(2).

Si la raíz es doble, puede haber más persistencia y la autocorrelación cae más lento.

Si hay raíces complejas, la ACF puede tener un comportamiento periódico o sinusoidal.

Uno podría pensar que hay un ciclo escondido, pero eso puede ser producto de raíces complejas.

Antes de ajustar un modelo periódico, habría que revisar si las raíces del modelo son complejas.

---

## Invertibilidad y redundancia

En un MA(2) puede aparecer el concepto de no invertibilidad.

Puede haber dos conjuntos de parámetros distintos que generan prácticamente el mismo patrón en los datos.

Desde las gráficas puede no ser posible distinguir los modelos.

Entonces se usa la representación AR infinito.

El modelo invertible tiene representación AR infinito; el no invertible no.

También pueden existir raíces comunes en los polinomios de un ARMA.

Por ejemplo, en un ARMA(1,1), cuando \(\phi_1=0.7\) y \(\theta_1=-0.7\), puede haber cancelación entre polinomios.

Entonces el modelo, que parece ARMA(1,1), en realidad puede reducirse a ruido blanco.

En la práctica, los parámetros no van a ser exactamente iguales, pero pueden ser muy parecidos. Por eso hay que mirar la significancia de los parámetros o calcular las raíces y ver si son similares.

A lo mejor hay dos raíces muy parecidas en la parte autorregresiva y de media móvil, y entonces conviene reducir el orden.

---

## Pregunta sobre intervalos de confianza de raíces

> ¿Las raíces tienen intervalos de confianza?

Teóricamente se pueden calcular con el método Delta.

No estoy seguro si los softwares lo traen directamente disponible. Habría que revisarlo.

La incertidumbre de las raíces se hereda de la incertidumbre de los parámetros.

Por lo tanto, teóricamente sí se puede construir.

---

## Modelos propuestos para la serie SOI

Para la serie SOI, la PACF tiene cierto decaimiento.

Podríamos pensar en:

- AR(1), aunque parece estar lejos.
- ARMA(1,1), que podría ser razonable.
- AR(2), que parece una opción más razonable.
- AR(3), que también podría ser.

En el AR(1), el \(\phi\) estimado es aproximadamente:

\[
0.6253
\]

En el MA(1), el \(\theta\) estimado es 1, porque la primera autocorrelación es mayor a 0.5, y en un MA(1) teóricamente la autocorrelación máxima en valor absoluto no puede superar 0.5.

En el ARMA(1,1), aparecen dos conjuntos de parámetros, pero hay que revisar cuál es invertible.

En el AR(2), se obtiene aproximadamente:

\[
\phi_1 = 0.43
\]

\[
\phi_2 \approx 0.3
\]

Al comparar la ACF y la PACF observadas con las teóricas, el AR(1) no logra capturar bien la dependencia.

El ARMA(1,1) captura demasiada correlación.

El AR(2) anda bastante mejor, pero parece que todavía le falta capturar algo.

Probablemente el mejor modelo sea un AR(3), pero para decidir entre AR(2) y AR(3) necesitamos un criterio de bondad de ajuste.

---

## Serie GEE

La PACF de la serie GEE luce diferente.

Aparecen comportamientos periódicos importantes.

Un modelo ARMA probablemente no va a capturar esto, porque aunque pueden existir raíces complejas, estas generan formas más regulares, como sinusoides.

Aquí aparecen patrones más irregulares y periódicos.

Por lo tanto, probablemente se necesitan modelos SAR.

---

## Predicción de la serie SOI

Primero, la serie original se centra en el promedio para que quede en torno a cero.

Estimamos la media con el promedio y luego trabajamos con la serie centrada.

Podemos calcular la representación AR infinito.

En el AR(2), tenemos dos coeficientes importantes y el resto cero.

En el ARMA(1,1), los coeficientes decaen exponencialmente a cero.

Esto muestra que el ARMA(1,1) puede ser equivalente a un AR de orden superior, aproximadamente un AR(5) o AR(6).

Las predicciones usando las ecuaciones vistas muestran que:

- La predicción del AR(2) converge a la media.
- La predicción del ARMA(1,1) también converge a la media, pero más lento.

La media era aproximadamente:

\[
0.25
\]

El AR(2) decae hacia 0.25.

El ARMA(1,1) decae más lentamente hacia ese valor.

---

## Varianza de predicción

También se puede estimar la varianza.

La varianza en el modelo AR(2) es aproximadamente:

\[
1.31
\]

En el ARMA(1,1), aproximadamente:

\[
1.32
\]

Son muy parecidas.

La varianza de predicción empieza a crecer a medida que aumenta el horizonte de predicción.

Es decir, mientras más instantes hacia el futuro queremos predecir, más crece la varianza.

Con eso se pueden construir intervalos de confianza.

Por ejemplo, si el predictor es 0.6 y la varianza es grande, el intervalo puede ir desde valores negativos hasta valores positivos amplios.

Aquí usamos toda la capacidad del AR infinito truncado para obtener predictores y cuantificar la varianza de predicción.

Si usamos \(K=12\), estamos aproximando el ARMA(1,1) mediante un AR(12).

Esto permite que la ecuación de predicción sea mucho más directa.

---

## Comparación final de predicciones

Finalmente, construimos las predicciones para SOI con:

- AR(2)
- ARMA(1,1)

Ambos modelos convergen a la media.

El ARMA(1,1) converge más lento.

La serie de test era muy corta, solo dos valores, enero y febrero.

Además, hubo un cambio radical, porque los últimos valores venían a la baja y de repente subieron.

Eso es muy difícil para el modelo.

Lo más probable es que si incorporamos ese valor real y volvemos a predecir con el mismo modelo, la predicción se corregiría bastante.

En la última clase vamos a ver cómo los modelos se actualizan con los nuevos datos que van llegando.

Todo esto se hizo de forma manual, pero hay funciones que hacen estos cálculos automáticamente.

---

## Conclusión de la clase

Un estudiante pregunta:

> ¿La conclusión de la clase podría ser que los modelos tienen que ser causales, o sea, que se pueden construir con un AR infinito, e invertibles, o sea, que se pueden construir con una media móvil infinita?

La respuesta es:

Al revés.

- Causalidad implica representación MA infinito.
- Invertibilidad implica representación AR infinito.

La causalidad nos entrega la estacionariedad, básicamente.

La invertibilidad nos entrega cómo podemos utilizar los datos para predecir modelos complejos como los ARMA.

Los modelos AR son fáciles de predecir.

Los modelos MA son más complejos.

Las raíces de los polinomios son importantes para la redundancia de los modelos, porque el modelo teórico podría ser mucho más simple del que uno está probando.

Cualquier duda que tengan, recuerden que los canales oficiales son el foro y Salesforce.

Revisen los grupos para ver si tienen acceso a sus compañeros, sobre todo los que mandaron los integrantes de los grupos, para que hayan quedado correctamente asignados.

Y los que fueron asignados de forma aleatoria, para que sepan con quién les toca trabajar.

Cualquier duda, nos avisan.
