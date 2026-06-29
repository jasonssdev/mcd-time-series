# Modelos Autorregresivos AR(p)

Bienvenidos y bienvenidas a este nuevo videotutorial.

En este videotutorial vamos a hablar sobre los modelos autorregresivos, que en este caso se representan con las siglas **AR**.

El parámetro asociado a estos modelos es la letra **p**.

## Objetivo del Modelo AR(p)

El objetivo de este nuevo modelo AR(p) es generar una ecuación que nos permita predecir nuestra serie temporal en el momento \(t\), pero como una combinación de los datos del pasado.

Mientras que en el videotutorial anterior nosotros nos enfocábamos en construir una ecuación que nos permitiera generar una predicción utilizando los errores del pasado, aquí la predicción se realiza utilizando los **valores observados en el pasado**.

Para esto, la ecuación es la siguiente.

Tenemos:

- Una constante relacionada con la media.
- Una combinación lineal de los valores pasados.
- Un error en el momento \(t\).

Es decir:

\[
X_t = \mu + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \cdots + \phi_p X_{t-p} + \varepsilon_t
\]

donde:

- \(\mu\) es la media del proceso.
- \(\phi_i\) son los coeficientes autorregresivos.
- \(\varepsilon_t\) es un ruido blanco.

## Relación con el Modelo ARMA

Tenemos la generalización de este modelo AR(p), que viene dada por el modelo ARMA.

En este caso estamos asumiendo que la parte de media móvil no existe.

En la ecuación general ARMA:

\[
ARMA(p,q)
\]

la componente MA desaparece cuando:

\[
q = 0
\]

Por lo tanto:

\[
ARMA(p,0) \equiv AR(p)
\]

## Simulación de un Modelo AR(p)

Ahora, ¿por qué necesitamos esta expresión?

Porque nosotros queremos simular una serie de tiempo que esté definida a partir de un modelo autorregresivo.

Para esto tenemos que ingresar dos vectores como input.

Esto está principalmente motivado por la representación utilizada por las funciones de simulación.

### Vector Autorregresivo

El vector autorregresivo se define como:

\[
[1,\,-\phi_1,\,-\phi_2,\,...,\,-\phi_p]
\]

Los signos negativos aparecen porque la parte autorregresiva de la ecuación se pasa restando al otro lado.

### Vector de Media Móvil

El vector MA se define como:

\[
[1,\theta_1,\theta_2,\ldots,\theta_q]
\]

Incluso cuando no existe componente de media móvil, debemos incluir el valor:

\[
[1]
\]

Esto ocurre porque:

- Existe un coeficiente implícito igual a 1 frente a \(X_t\).
- Existe un coeficiente implícito igual a 1 frente a \(\varepsilon_t\).

## Ejemplo: Simulación de un AR(2)

Buscamos generar una simulación de un modelo autorregresivo de orden 2.

Para ello definimos:

### Componente autorregresiva

\[
[1,\;0.7,\;-0.2]
\]

### Componente de media móvil

\[
[1]
\]

### Importante

Hay que tener cuidado con los signos.

Este valor:

\[
0.7
\]

representa:

\[
-\phi_1
\]

Por lo tanto:

\[
\phi_1 = -0.7
\]

Asimismo:

\[
-0.2
\]

representa:

\[
-\phi_2
\]

Por lo tanto:

\[
\phi_2 = 0.2
\]

Todo esto está motivado por la forma en que se especifica el modelo ARMA.

## Serie Simulada

Cuando nosotros simulamos un modelo AR(2), obtenemos una serie temporal que luce aproximadamente de esta manera:

- Serie estacionaria.
- Media constante.
- Varianza aparentemente constante.

Nuestro objetivo ahora es estudiar su función de autocorrelación.

## Función de Autocorrelación (ACF)

Transformamos nuevamente la serie simulada a un objeto de la librería `Darts` y graficamos su función de autocorrelación.

¿Qué obtenemos?

Tenemos una función de autocorrelación que:

- Oscila entre valores positivos y negativos.
- Va decreciendo de forma exponencial.
- No luce como la de un modelo MA(q).

### ¿Por qué ocurre esto?

Porque la función de autocorrelación de un modelo AR(p) no tiene una fórmula explícita para cada lag, excepto en el caso especial del AR(1).

Para un AR(2) o superior, la función de autocorrelación se obtiene resolviendo un sistema de ecuaciones.

Por lo tanto, una ACF de un modelo AR(p) suele presentar:

- Decrecimiento exponencial.
- Oscilaciones amortiguadas.
- Ausencia de corte abrupto.

## Diferencia con los Modelos MA(q)

En los modelos MA(q), la ACF era muy útil porque:

- Permitía identificar el número de lags.
- Mostraba un corte claro después del lag \(q\).

En cambio, para un modelo AR(p):

- La ACF no permite identificar directamente el valor de \(p\).
- Solo nos da indicios de que podríamos estar frente a un modelo autorregresivo.

Por ello necesitamos otra herramienta.

## Función de Autocorrelación Parcial (PACF)

Para identificar el orden \(p\), utilizamos la función PACF (*Partial Autocorrelation Function*).

Cuando calculamos la PACF para nuestra serie simulada ocurre algo interesante.

### Resultados observados

Recordemos que:

\[
PACF(0)=1
\]

por definición.

Luego aparecen dos lags importantes:

#### Lag 1

Valor aproximado:

\[
-0.77
\]

#### Lag 2

Valor aproximado:

\[
0.22
\]

Esto resulta curioso porque nosotros simulamos precisamente un AR(2).

Recordemos que:

\[
\phi_1=-0.7
\]

\[
\phi_2=0.2
\]

Y la PACF nos está entregando valores muy cercanos a esos parámetros.

## Interpretación de la PACF

Cuando observamos:

### ACF

- Decaimiento exponencial.
- Oscilaciones amortiguadas.

### PACF

- Corte abrupto en el lag \(p\).

Entonces tenemos evidencia de que estamos frente a un modelo AR(p).

En este caso:

- La PACF resalta los lags 1 y 2.
- Después prácticamente desaparece.

Por lo tanto, esto sugiere un:

\[
AR(2)
\]

Además, los valores observados en la PACF corresponden aproximadamente a las estimaciones de:

\[
\phi_1
\]

y

\[
\phi_2
\]

## Estimación del Modelo

Tal como hicimos en el tutorial anterior, vamos a ajustar un modelo ARIMA.

La configuración utilizada es:

\[
ARIMA(2,0,0)
\]

porque:

- \(p=2\) → modelo autorregresivo de orden 2.
- \(d=0\) → sin diferenciación.
- \(q=0\) → sin componente de media móvil.

## Parámetros Estimados

Al ajustar el modelo obtenemos:

### Media

Corresponde a la constante del proceso.

La serie está centrada aproximadamente en cero, por lo que la estimación resulta coherente.

### Primer parámetro

Estimación:

\[
\hat{\phi}_1 \approx -0.71
\]

Valor real utilizado en la simulación:

\[
\phi_1=-0.7
\]

Existe una gran cercanía entre ambos.

### Segundo parámetro

Estimación:

\[
\hat{\phi}_2 \approx 0.16
\]

Valor real utilizado:

\[
\phi_2=0.2
\]

También existe una buena concordancia.

### Varianza del ruido blanco

Finalmente obtenemos:

\[
\hat{\sigma}^2
\]

que corresponde a la estimación de la varianza del ruido blanco.

## ¿Por qué necesitamos \(\sigma^2\)?

Porque el modelo incluye:

\[
\varepsilon_t
\]

y este término representa un ruido blanco con:

\[
E(\varepsilon_t)=0
\]

y

\[
Var(\varepsilon_t)=\sigma^2
\]

Por lo tanto, necesitamos estimar esa varianza para poder generar futuras predicciones.

## Predicción Futura

Una vez identificados todos los parámetros, podemos construir una ecuación predictiva:

\[
X_{t+1}
=
\mu
+
\phi_1 X_t
+
\phi_2 X_{t-1}
+
\varepsilon_{t+1}
\]

Ya conocemos:

- La constante.
- \(\phi_1\).
- \(\phi_2\).
- La varianza del ruido blanco.

Por lo tanto, podemos generar un candidato para la perturbación futura y construir una predicción de la serie temporal.

## Conclusión

La principal característica del modelo AR(p) es que:

- Utiliza valores pasados de la serie para realizar predicciones.
- La ACF suele decaer gradualmente.
- La PACF presenta un corte abrupto en el lag \(p\).

Por ello, la PACF es una herramienta fundamental para identificar el orden de un modelo autorregresivo.

Espero que este tutorial haya sido de su agrado y nos vemos en el siguiente.