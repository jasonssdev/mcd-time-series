# Estimación de momentos y máxima verosimilitud

Bienvenidos y bienvenidas a una nueva clase.

Como se pudo apreciar en clases anteriores, la función de autocovarianza es la clave para poder realizar predicciones en modelos ARMA. Dicha función, a través de la ACF y PACF, también nos sirve para identificar un modelo de la familia ARMA.

Sin embargo, la función de autocovarianza y, en consecuencia, las predicciones, dependen de los parámetros del modelo. Es decir, es necesario contar con los coeficientes de los polinomios autorregresivos y de media móvil, junto con la varianza del ruido blanco, los cuales en la práctica son desconocidos.

La presente sección tiene por objetivo revisar las principales técnicas de estimación de parámetros en los modelos de series de tiempo.

No obstante, la mayoría de los métodos existentes consisten en resolver sistemas de ecuaciones no lineales, cuya solución la obtendremos solo de forma numérica a través de algoritmos iterativos.

En esta clase se revisarán los siguientes temas:

- **Tema 1:** Método de los momentos para los AR(p).
- **Tema 2:** Método de máxima verosimilitud.

---

# Tema 1. Método de los momentos para los AR(p)

Si la media del proceso es $\mu$, entonces el estimador de momentos de $\mu$ es el promedio de los datos observados; es decir,

$$
\hat{\mu} = \bar{x}
$$

En consecuencia, para encontrar los estimadores de los otros parámetros:

- $\phi_1, \phi_2, \ldots, \phi_p$
- $\theta_1, \theta_2, \ldots, \theta_q$
- $\sigma^2$

podemos asumir que la media del proceso es cero.

El método de estimación de los momentos es particularmente útil para estimar los parámetros de un modelo AR(p), donde asumiremos que la estructura del modelo es fija, es decir, el valor de $p$ es fijo.

## Ejemplo: modelo AR(1)

Para un AR(1):

$$
X_t = \phi X_{t-1} + \varepsilon_t
$$

se tiene que calcular la autocovarianza entre $X_t$ y $X_{t+h}$.

Se obtiene:

$$
\gamma(h)=\phi\gamma(h-1), \qquad h\ge1
$$

Luego, para $h=1$:

$$
\gamma(1)=\phi\gamma(0)
$$

En consecuencia:

$$
\phi=\frac{\gamma(1)}{\gamma(0)}=\rho(1)
$$

Así, el estimador de momentos de $\phi$ se obtiene igualando los momentos centrales poblacional y muestral para $h=0$ y $h=1$.

Es decir:

$$
\gamma(0)=\hat{\gamma}(0)
$$

y

$$
\gamma(1)=\hat{\gamma}(1)
$$

Por lo tanto, al igualar la correlación poblacional con la correlación muestral de orden 1, se obtiene que:

$$
\hat{\phi}=\hat{\rho}(1)
$$

Esto significa que el estimador de momentos de $\phi$ es la autocorrelación muestral de orden 1.

Por otro lado, al calcular la covarianza del proceso consigo mismo, se tiene que:

$$
\gamma(0)=\phi\gamma(1)+\sigma^2
$$

Al despejar la ecuación anterior:

$$
\sigma^2=\gamma(0)-\phi\gamma(1)
$$

Por lo tanto, el estimador de momentos de la varianza es:

$$
\hat{\sigma}^2=\hat{\gamma}(0)-\hat{\phi}\hat{\gamma}(1)
$$

## Ecuaciones de Yule-Walker

En general, las ecuaciones de Yule-Walker permiten encontrar los estimadores de momentos de los parámetros autorregresivos de un AR(p).

Dichas ecuaciones establecen un sistema para encontrar el vector de parámetros autorregresivos.

Resolviendo:

$$
\Gamma_p\phi=\gamma_p
$$

o equivalentemente:

$$
R_p\phi=r_p
$$

donde:

- $R_p$ corresponde a la matriz de correlación poblacional.
- $r_p$ corresponde al vector de correlaciones poblacionales.

Finalmente, considerando los estimadores de momentos de las autocovarianzas o autocorrelaciones, se tiene que el estimador del vector $\phi$ es:

$$
\hat{\phi}=\hat{\Gamma}_p^{-1}\hat{\gamma}_p
$$

o equivalentemente:

$$
\hat{\phi}=\hat{R}_p^{-1}\hat{r}_p
$$

Del mismo modo, se obtiene el estimador de momentos de $\sigma^2$, tal como se muestra en pantalla.

## Aplicación al modelo AR(2)

Antes de enunciar las ecuaciones de Yule-Walker vimos cómo obtener los estimadores de momentos de los parámetros de un AR(1) de forma directa.

Ahora veamos cómo usar las ecuaciones de Yule-Walker para un AR(2).

En primer lugar, planteamos el sistema de dos ecuaciones con dos incógnitas que se muestra en pantalla, cuya solución se presenta a continuación.

Además, la varianza del ruido blanco queda expresada como:

$$
\sigma^2=\gamma(0)-\phi_1\gamma(1)-\phi_2\gamma(2)
$$

Por lo tanto, los estimadores de momentos del AR(2), es decir:

- $\hat{\phi}_1$
- $\hat{\phi}_2$
- $\hat{\sigma}^2$

dependen de las autocovarianzas muestrales:

- $\hat{\gamma}(0)$
- $\hat{\gamma}(1)$
- $\hat{\gamma}(2)$

a través de las expresiones que se muestran en pantalla.

El método de los momentos es muy útil para los AR(p), ya que en este caso se cumple la siguiente proposición:

- El estimador de momentos de la varianza del ruido blanco es consistente.
- Los estimadores de los parámetros autorregresivos son consistentes.
- Son asintóticamente sesgados.
- Su distribución límite es la distribución Gaussiana.

## Método de los momentos para MA(q) y ARMA(p,q)

El método de los momentos también puede aplicarse en modelos MA(q) y ARMA(p,q).

Sin embargo, no se garantiza que los estimadores encontrados sean óptimos, ya que dichos modelos no son lineales en los parámetros.

Esto puede apreciarse en un MA(1), donde se obtiene una ecuación cuadrática en $\theta$, con coeficientes:

- 1
- $1/\rho(1)$
- 1

para los términos cuadrático, lineal y constante, respectivamente.

Su solución factible se muestra en pantalla.

El término **factible** se refiere a la solución que hace que el modelo sea invertible, ya que, como toda ecuación cuadrática, posee dos raíces.

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

---

# Tema 2. Método de máxima verosimilitud

El método de máxima verosimilitud es uno de los métodos de estimación de parámetros más utilizados en los diferentes modelos estadísticos, principalmente porque, en la mayoría de los casos, los estimadores encontrados son asintóticamente insesgados y eficientes, con distribución asintótica normal.

Para un modelo ARMA(p,q) se define:

$$
\beta=(\mu,\phi_1,\ldots,\phi_p,\theta_1,\ldots,\theta_q)
$$

como el vector de parámetros de dimensión $p+q+1$, que contiene:

- el parámetro de la media;
- los parámetros autorregresivos;
- los parámetros de media móvil.

Así, la verosimilitud del modelo, que corresponde a la densidad conjunta de las observaciones, puede escribirse como se muestra en pantalla.

Si se asume normalidad en el ruido blanco, entonces:

$$
X_t \mid X_{t-1},\ldots,X_1
$$

sigue una distribución normal con media y varianza como se muestran en pantalla.

A partir de la representación causal se define $r_t$.

Entonces, la varianza queda expresada como:

$$
\sigma_w^2\,r_t(\beta)
$$

Por lo tanto, la verosimilitud del modelo ARMA queda como se muestra en pantalla, donde:

$$
S(\beta)
$$

es la suma de cuadrados residual estandarizada por $r_\theta(\beta)$.

Aplicando logaritmo natural se obtiene la log-verosimilitud, salvo una constante, tal como se muestra a continuación.

## Estimación por máxima verosimilitud

Finalmente, se resuelve el sistema:

$$
\nabla l = 0
$$

Es decir, se deriva parcialmente la log-verosimilitud respecto de cada una de las componentes de $\beta$, así como también respecto de $\sigma_w^2$.

Notar que la derivada respecto de $\sigma_w^2$ permite determinar:

$$
\hat{\sigma}_w^2=\frac{S(\hat{\beta})}{n}
$$

Ahora bien, $\beta$ solo se obtiene de forma numérica.

Por otro lado, típicamente,

$$
S(\beta)
$$

se denomina **mínimos cuadrados incondicionales**, el cual, minimizando respecto a $\beta$, permite encontrar los estimadores de mínimos cuadrados incondicionales.

En este caso, el estimador de la varianza del ruido es:

$$
\hat{\sigma}_w^2=\frac{S(\hat{\beta})}{n-p-q-1}
$$

También existe la alternativa condicional respecto a la primera observación, obteniendo las metodologías de:

- máxima verosimilitud condicional;
- mínimos cuadrados condicionales.

## Caso particular: AR(1)

En el caso particular del AR(1), existe una forma cerrada para resolver el sistema anterior.

Se obtiene que:

- $\hat{\mu}$ es aproximadamente el promedio.
- $\hat{\phi}$ es aproximadamente $\hat{\rho}(1)$.

Los términos $\bar{x}_1$ y $\bar{x}_2$ se muestran en pantalla.

## Métodos numéricos

En general, para los modelos ARMA no existe una forma cerrada para resolver el sistema.

Por ello es habitual resolverlo mediante los algoritmos de:

- Newton-Raphson.
- Scoring.

Este último reemplaza la segunda derivada por la información de Fisher.

A pesar de que los estimadores son encontrados de forma numérica, se satisface la siguiente proposición:

- El estimador de máxima verosimilitud de la varianza del ruido es consistente.
- El estimador de máxima verosimilitud de $\beta$ es asintóticamente normal.

La matriz de varianza aproximada de $\hat{\beta}$ para $n$ fijo es:

$$
\frac{\sigma_w^2\Gamma_{p,q}^{-1}}{n}
$$

**Prueba tu aprendizaje respondiendo la siguiente pregunta.**

---

# Resumen

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

- Para estimar los parámetros de un modelo ARMA es necesario especificar completamente el modelo, es decir, conocer los órdenes $p$ y $q$.
- El método de los momentos es muy útil para los modelos AR(p), ya que permite obtener los estimadores resolviendo un sistema lineal.
- En los modelos MA(q) y ARMA(p,q) el sistema de ecuaciones es no lineal.
- Los métodos de máxima verosimilitud pueden expresarse de forma incondicional o condicional.
- La máxima verosimilitud condicional expresa la verosimilitud en términos de la primera observación.
- En general, para encontrar los estimadores de máxima verosimilitud es necesario utilizar métodos numéricos, como Newton-Raphson y Scoring.