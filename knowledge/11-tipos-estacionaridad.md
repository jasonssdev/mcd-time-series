# Tipos de Estacionariedad

Bienvenidos y bienvenidas a esta nueva clase.

Para modelar de forma probabilística una serie de tiempo, es preciso imponer algunas condiciones que garanticen la repetibilidad en el tiempo, lo que nos entregará poderosas herramientas para predecir hacia el futuro.

## Definición Formal de una Serie de Tiempo

En primer lugar, comenzaremos con la definición formal de una serie de tiempo.

Para ello, considera la definición de un proceso estocástico que se muestra en pantalla.

Es decir, un proceso estocástico, \(X_t\) con \(t \in T\), es una colección de variables aleatorias indexadas en \(t\).

Luego, se define una serie de tiempo como un pedazo o fracción de una trayectoria de un proceso estocástico \(X_t\).

Esto es, para una serie de largo \(n\), se tendría:

\[
X_{t_1}, X_{t_2}, \ldots, X_{t_n}
\]

Donde los \(t_j\) son los instantes de tiempo donde se realiza la medición.

Además, sin pérdida de generalidad y con el fin de simplificar la notación, se realiza la biyección \(t_j \rightarrow j\), con \(j\) de 1 hasta \(n\), ya que solo analizaremos series de tiempo medidas regularmente en el tiempo.

En esta clase se revisarán los siguientes temas:

1. Estacionariedad fuerte.
2. Funciones de media, autocovarianza y autocorrelación.
3. Estacionariedad débil.

---

## Tema 1: Estacionariedad Fuerte

[SOUND]

Una condición ideal para proyectar series de tiempo es la condición de estacionariedad estricta o fuerte, la cual está definida como se muestra en pantalla.

Esta definición quiere decir que la distribución finito-dimensional del proceso estocástico es invariante bajo traslaciones en el tiempo.

En otras palabras, si trasladamos el proceso en \(h\) unidades, la distribución no cambia.

Por lo que comprenderíamos todo acerca del proceso.

Como ejemplo, se tiene que cualquier secuencia independiente e idénticamente distribuida (iid) es fuertemente estacionaria.

Para procesos no iid, claramente esta condición es demasiado estricta y compleja de chequear, lo que la hace intratable.

Para poder entregar una definición más adaptable a diferentes escenarios, se exigirá que el proceso sea de segundo orden.

### Proceso de Segundo Orden

Se define como un proceso estocástico que tiene segundo momento finito para cualquier instante de tiempo \(t\).

Es decir:

\[
E(X_t^2) < \infty
\]

Por ejemplo, considere el proceso:

\[
X_t = \varepsilon_t + \theta \varepsilon_{t-1}
\]

Donde \(\varepsilon_t\) es iid de media cero y varianza \(\sigma^2\).

Este proceso es conocido como **MA(1)**, lo que significa que \(X_t\) es igual al ruido más \(\theta\) veces el ruido en el instante anterior.

Luego:

\[
E(X_t^2) = (1+\theta^2)\sigma^2
\]

La cual claramente es finita.

El detalle del cálculo se muestra en pantalla.

Concluyendo que \(X_t\) es un proceso de segundo orden.

### Resultados Relevantes para Ruido Blanco

Es importante destacar algunos resultados relevantes que fueron utilizados en el ejemplo anterior y que serán útiles para futuros procesos.

Cuando se involucra la esperanza de un ruido blanco \(\varepsilon_t\) de varianza \(\sigma^2\), se tiene:

\[
E(\varepsilon_t)=0
\]

para todo \(t\).

\[
E(\varepsilon_t^2)=\sigma^2
\]

para todo \(t\).

\[
E(\varepsilon_t\varepsilon_s)=0
\]

para todo \(t \neq s\).

En general:

\[
E[h(\varepsilon_t)g(\varepsilon_s)]
=
E[h(\varepsilon_t)]E[g(\varepsilon_s)]
\]

para todo \(t \neq s\), cuando el ruido blanco es independiente.

Prueba tu aprendizaje respondiendo a la siguiente pregunta.

---

## Tema 2: Funciones de Media, Autocovarianza y Autocorrelación

[SOUND]

La importancia de trabajar con un proceso de segundo orden radica en que podemos definir:

- La función de media.
- La función de autocovarianza.
- La función de autocorrelación.

Las que servirán para caracterizar un proceso estocástico.

Sea \(X_t\), con \(t \in T\), un proceso estocástico.

### Función de Media

Se define la función de media como:

\[
\mu:T \rightarrow \mathbb{R}
\]

tal que:

\[
\mu(t)=E(X_t)
\]

### Función de Autocovarianza

Se define:

\[
\gamma:T\times T \rightarrow \mathbb{R}
\]

tal que:

\[
\gamma(t,s)=Cov(X_t,X_s)
\]

### Función de Autocorrelación

Se define:

\[
\rho:T\times T \rightarrow \mathbb{R}
\]

tal que:

\[
\rho(t,s)=Corr(X_t,X_s)
\]

Notar que ambas funciones se relacionan mediante:

\[
\rho(t,s)=
\frac{\gamma(t,s)}
{\sqrt{\gamma(t,t)\gamma(s,s)}}
\]

Si bien en las definiciones anteriores no se utiliza explícitamente que el proceso sea de segundo orden, esta característica es esencial para garantizar que las tres funciones anteriores sean finitas para todo \(t\).

Es decir, se satisface la siguiente proposición:

> Sea \(X_t\), \(t \in T\), un proceso estocástico de segundo orden. Entonces \(\mu(t)\) es finita y \(\gamma(t,s)\) es finita.

Como resultado inmediato se tienen las siguientes características de la función de autocorrelación:

\[
-1 \leq \rho(t,s)\leq 1
\]

y

\[
\rho(t,t)=1
\]

### Ejemplo MA(1)

Para el proceso:

\[
X_t=\varepsilon_t+\theta\varepsilon_{t-1}
\]

se tiene que la función de media es cero.

Mientras que la función de autocovarianza está dada por la expresión mostrada en pantalla.

Destaca que es igual a cero cuando la diferencia entre los tiempos \(t\) y \(s\) es mayor o igual a 2.

En consecuencia, la función de autocorrelación viene dada por:

\[
\rho(t,s)=1
\]

cuando la diferencia es 0.

\[
\rho(t,s)=
\frac{\theta}{1+\theta^2}
\]

cuando la diferencia entre \(t\) y \(s\) es 1.

Y

\[
\rho(t,s)=0
\]

si la diferencia es mayor a 2.

Es decir, existe correlación solo cuando los tiempos están separados por un lag 1 y luego es 0.

### Propiedad Bilineal de la Covarianza

Nuevamente, para el cálculo de la función de autocovarianza se utilizaron algunos resultados de probabilidades.

En específico, la propiedad bilineal de la covarianza.

En general, esta propiedad establece que:

> La covarianza de una combinación lineal de variables aleatorias con otra combinación lineal de variables aleatorias es igual a la expresión que está en pantalla.

Donde \(X\), \(Y\), \(Z\) y \(W\) son variables aleatorias y \(a\), \(b\), \(c\), \(d\), \(e\) y \(f\) son constantes.

Prueba tu aprendizaje respondiendo a la siguiente pregunta.

---

## Tema 3: Estacionariedad Débil

[SOUND]

Como mencionamos inicialmente, para describir un proceso estocástico debemos conocer la distribución finito-dimensional.

La cual debe ser invariante bajo traslación en el tiempo.

Sin embargo, podemos relajar la hipótesis anterior estableciendo condiciones únicamente en los primeros dos momentos.

La cual se formaliza a través de la definición de un proceso débilmente estacionario.

### Definición

Sea \(X_t\), con \(t \in T\), un proceso estocástico de segundo orden.

Diremos que el proceso estocástico es débilmente estacionario si y solo si satisface las siguientes condiciones:

1. \(\mu(t)=\mu\) para todo \(t\).
2. \(\gamma(t,s)=g(t-s)=g(h)\), con \(h=t-s\).

La condición 1 establece que la media es constante respecto al tiempo.

Mientras que la condición 2 indica que la correlación depende exclusivamente de la separación temporal y no del instante en que se realizan las mediciones.

En este sentido, es muy frecuente encontrar el abuso de notación:

\[
\gamma(t,t+h)=\gamma(h)
\]

para describir la autocovarianza de un proceso débilmente estacionario.

### Consecuencias

Como consecuencias directas de la definición de estacionariedad débil, se tiene que:

La varianza del proceso es constante, dada por:

\[
\gamma(0)
\]

La función de autocovarianza es una función par:

\[
\gamma(h)=\gamma(-h)
\]

para todo \(h\).

Mientras que la función de autocorrelación queda expresada como:

\[
\rho(h)=
\frac{\gamma(h)}
{\gamma(0)}
\]

Enfatizando que es una función que depende exclusivamente de la diferencia temporal.

Además, como la correlación es menor o igual a 1:

\[
|\gamma(h)|\leq \gamma(0)
\]

para todo \(h\).

### Ejemplo: MA(1)

Para el proceso:

\[
X_t=\varepsilon_t+\theta\varepsilon_{t-1}
\]

vimos que:

\[
\mu(t)=0
\]

cumpliendo la condición 1.

Mientras que la función de autocovarianza está dada por una función por tramos, la cual puede reescribirse como \(\gamma(h)\), tal como aparece en pantalla.

Verificando que se trata de una función que depende exclusivamente de \(h\), la separación temporal.

Por lo tanto, el proceso MA(1) es un proceso débilmente estacionario.

### Otro Ejemplo: Ruido Blanco

Otro ejemplo sencillo de verificar que es débilmente estacionario es el ruido blanco.

Ya que por definición tiene media 0, satisfaciendo la condición 1.

Y varianza constante, no correlacionado, satisfaciendo la condición 2.

Sin embargo, en otros procesos puede ser complejo verificar la estacionariedad.

Como es el caso de los procesos:

#### AR(1)

\[
X_t=\phi X_{t-1}+\varepsilon_t
\]

#### ARMA(1,1)

\[
X_t=\phi X_{t-1}+\varepsilon_t+\theta\varepsilon_{t-1}
\]

donde el ruido \(\varepsilon_t\) tiene media 0 y varianza \(\sigma^2\).

Prueba tu aprendizaje respondiendo la siguiente pregunta.

---

## Resumen

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

- La propiedad de estacionariedad fuerte nos garantiza conocer todos los aspectos del proceso estocástico cuando se traslada \(h\) unidades en el tiempo.
- Sin embargo, dicha condición es demasiado estricta.
- Un proceso de segundo orden garantiza la existencia de las funciones de media, autocovarianza y autocorrelación.
- Para caracterizar un proceso estocástico en un sentido débil, se imponen condiciones sobre la función de media y la función de autocovarianza.
- Una condición necesaria, pero no suficiente, para que un proceso sea estacionario débil es que su gráfica debe lucir estable en media y varianza.
