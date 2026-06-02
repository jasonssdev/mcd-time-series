Método de descomposición, diferenciación y transformación

Bienvenidos y bienvenidas a esta nueva clase.

Los alisamientos exponenciales son una buena alternativa para modelar series que no tienen tendencia, o bien que presentan una tendencia lineal a las que se les puede agregar una componente periódica de forma aditiva o multiplicativa.

No obstante, existen series que presentan otros patrones, como exponenciales o logarítmicos, para las cuales es preferible cambiar de modelo, donde una alternativa son los métodos de descomposición.

En esta clase se revisarán los siguientes temas:

1. Métodos de descomposición.
2. Filtro de media móvil.
3. Diferenciaciones y transformaciones.

⸻

Tema 1: Métodos de descomposición

Los métodos de descomposición asumen que una serie se puede descomponer en tres partes.

Estas partes son:

* Tendencia, denotada por $T_t$.
* Estacionalidad, denotada por $S_t$.
* Ruido, denotado por $A_t$.

Las tres componentes anteriores se pueden relacionar de modo aditivo, multiplicativo o mixto.

El modelo aditivo asume que las tres partes se suman, el modelo multiplicativo asume que las tres partes se multiplican y el modelo mixto considera de forma multiplicativa la tendencia y estacionalidad, mientras que el ruido se incorpora de forma aditiva.

El caso multiplicativo se comporta como el caso aditivo al aplicar la transformación logaritmo, por lo que se especifica solo el caso aditivo y mixto.

Para estimar estos modelos se comienza determinando la tendencia, para la cual debemos especificar alguna estructura determinista, tales como lineal, polinomial, exponencial, exponencial modificada, entre muchas otras.

Los primeros dos casos son lineales, mientras que el tercero es linealizable, por lo que el método de mínimos cuadrados lineales funciona muy bien para estimar dichos parámetros.

Para ajustar el modelo exponencial modificado, suponga que la data se divide en tres grupos y sumamos cada uno de ellos.

Considerando que tenemos $3 \cdot n$ datos, podemos definir las sumas parciales de los tres grupos como:

* Caso uno, que considera la suma del primer tercio de la serie.
* Caso dos, que corresponde a la suma del segundo tercio de la serie.
* Caso tres, representa la suma del último tercio de la serie.

Estas tres sumas tienen un término en común denotado por $K$, el cual es una suma geométrica.

Resolviendo el sistema, se obtienen los valores estimados para $a$, $b$ y $r$. A partir de estos, encontramos la tendencia estimada.

En consecuencia, el método de descomposición incorpora mayor libertad al momento de modelar la tendencia que el método de Holt-Winters.

Por ejemplo, para la serie de calentamiento global, se ajustan la tendencia cuadrática y una tendencia exponencial modificada y se reservan los últimos 10 años para validación.

Los modelos estimados son:

* Exponencial modificada:
    $$
    \hat{T}_t = -0,65 + 0,305 \cdot 1,01^t
    $$
* Cuadrático:
    $$
    T_t = -0,22 - 0,0034 \cdot t + 0,0001 \cdot t^2
    $$

Donde $t = 1$ representa el primer año de medición, es decir, a 1880.

Las tendencias estimadas se pueden visualizar en la imagen, donde se observa que la tendencia cuadrática se ajusta mejor a los datos.

Una vez estimada la tendencia, se procede a calcular la componente estacional.

Para ello, se definen los residuos $W_t$, que corresponden a la serie original removiendo la tendencia, restando en el caso aditivo y dividiendo en el caso mixto.

Si el período de la serie es $p$, basta estimar $S_t$ para $t = 1$ hasta $p$.

Así, para estimar la componente periódica, primero se definen los $e_k$, correspondiendo al promedio de los valores de $W$ en el instante $k$, y $\bar{e}$ como el promedio de los $e(k)$.

Por ejemplo, si $p = 12$, nos encontramos en el caso mensual y $e(k)$ corresponde al promedio de la serie residual para el mes $k$.

Continuando con el contexto general, para $k = 1$ hasta $p$, se tiene la componente estacional estimada, donde $\bar{e}$ actúa como una corrección de $e(k)$ para estimar finalmente la estacionalidad del siguiente modo:

* Aditivo:
    $$
    S_k = e(k) - \bar{e}
    $$
* Mixto:
    $$
    S_k = e(k) - \bar{e} - 1
    $$

En el caso aditivo, $\bar{e}$ es cercano a 0, mientras que en el caso mixto, $\bar{e}$ es cercano a 1, por lo que en este último caso se debe restar 1 a $\bar{e}$.

Una vez ajustadas las componentes por separado, tendencia y estacionalidad, se calculan las respectivas ecuaciones de pronóstico.

Las respectivas ecuaciones de pronóstico a $h$ pasos son:

* Modelo aditivo:
    $$
    \bar{X}t(h) = \bar{T}{t+h} + \bar{S}_{t+h}
    $$
* Modelo mixto:
    $$
    \bar{X}t(h) = \bar{T}{t+h} \cdot \bar{S}_{t+h}
    $$

Volvamos ahora a nuestro ejemplo de la serie de calentamiento global, para aplicar descomposición según lo que hemos aprendido hasta ahora.

En primer lugar, se determina la serie residual de forma aditiva a partir de la tendencia cuadrática y exponencial modificada, respectivamente.

Luego, se ajusta la componente periódica asumiendo, solo con fines ilustrativos, un período de 10 años.

Notar que, en general, se debe determinar analíticamente el período de una serie de tiempo.

Finalmente, se predice para los últimos 10 años.

La gráfica muestra, en color verde, el modelo aditivo con tendencia cuadrática y, en color rojo, el modelo aditivo con tendencia exponencial modificada.

Claramente, desde la gráfica, el modelo aditivo con tendencia cuadrática ajusta mejor, lo cual es ratificado con la suma de cuadrados del error, que corresponde a 0,060 versus 0,373 para el modelo aditivo con tendencia exponencial modificada.

Prueba tu aprendizaje respondiendo la siguiente pregunta.

⸻

Tema 2: Filtro de media móvil

En algunos casos, resulta útil aplicar un filtro de media móvil a la serie original.

Esto permite, por un lado, identificar de mejor forma la tendencia y, por otro lado, permite quitar el efecto de la tendencia y así construir $W_t$.

Suponga que $Z_t$ es la serie suavizada, entonces la tendencia ajustada $\hat{T}_t$ se obtiene utilizando $Z_t$ en vez de $X_t$, mientras que la serie $W_t$ se encuentra utilizando $Z_t$ en vez de $\hat{T}_t$, es decir:

* Modelo aditivo:
    $$
    W_t = X_t - Z_t
    $$
* Modelo mixto:
    $$
    W_t = \frac{X_t}{Z_t}
    $$

Los filtros de media móvil consisten en promediar valores vecinos para suavizar la serie.

El conjunto de vecinos toma tanto valores futuros como pasados.

La cantidad de vecinos utilizados para suavizar la serie es el orden denotado por $q$, es decir, $Z_t$ toma esta forma cuando $q$ es par, mientras que toma la siguiente forma si $q$ es impar.

También es posible modificar los pesos, pero no es muy habitual.

Retomemos el ejemplo de la serie de calentamiento global y veamos qué resultados entrega la aplicación de este filtro.

Al aplicar filtros de media móvil a la base de temperatura global, se observa el efecto de suavizamiento a medida que aumenta el orden, así como también se aprecia cómo aumenta la cantidad de datos perdidos a los extremos.

Pon a prueba tu aprendizaje respondiendo la siguiente pregunta.

⸻

Tema 3: Diferenciaciones y transformaciones

Si bien en los métodos de descomposición, vistos como un modelo ingenuo, no se suele analizar el ruido para predecir la serie, en algunos casos, dichos residuos presentan información relevante que puede ayudar a mejorar las predicciones.

Como se verá en las próximas clases, cuando se ajusta una serie de tiempo mediante modelos probabilísticos, en primer lugar, se analizarán series de tiempo sin tendencia y con varianza constante.

Pero, como sabemos, muchas series de la vida real presentan tendencia, por lo que aplicar una descomposición a una serie de este tipo es una buena estrategia, de modo de ajustar de forma probabilística el ruido de dicha descomposición.

No obstante, este no es el único camino, ya que, como se vio en el ejemplo de las series financieras, al aplicar una transformación logaritmo y luego una diferenciación, observamos una serie de tendencia constante.

En general, este será el procedimiento para ajustar series con tendencia estocástica donde debemos considerar dos tipos de diferenciaciones:

$$
\nabla X_t = X_t - X_{t-1}
$$

$$
\nabla_S X_t = X_t - X_{t-S}
$$

Dichos operadores son lineales y se pueden aplicar de forma recursiva, de modo de conseguir una serie estable en media y varianza.

Por ejemplo, las diferenciaciones de orden 2 se pueden ver a continuación.

Como caso particular, si la serie $X_t$ es igual a:

$$
X_t = a + bt + Z_t
$$

Donde $Z_t$ tiene media constante, entonces la media de $X_t$ no es constante, mientras que $\nabla X_t$ sí tiene media constante.

En efecto:

$$
\nabla X_t = b + Z_t - Z_{t-1}
$$

Si ahora:

$$
X_t = q_t + Z_t
$$

Donde $q_t$ es un polinomio de grado $d$, entonces $\nabla^d X_t$ tiene tendencia constante.

De forma análoga, si la serie:

$$
X_t = S_t + Z_t
$$

Donde $S_t$ es una componente periódica de período $p$, entonces la media de $X_t$ no es constante, mientras que $\nabla_p X_t$ sí tiene media constante.

En efecto:

$$
\nabla_p X_t = Z_t - Z_{t-p}
$$

Por otro lado, la transformación logaritmo antes mencionada es un caso particular de la transformación de Box-Cox, definida por la siguiente ecuación, donde $\lambda_2$ es un desplazamiento de la serie.

Por lo general, $\lambda_2$ es 0, salvo en aquellos casos donde la transformación no está bien definida; mientras que $\lambda_1$ controla la forma obtenida de la transformación, donde $\lambda_1 = 1$ representa la no transformación.

Por lo general, $\lambda_1$ se encuentra de modo que la serie transformada es estable en varianza.

A modo de ilustración, la figura muestra la gráfica de:

* La serie original.
* La transformación logaritmo con traslado 1.
* Diferenciación de la serie original.
* Diferenciación de la transformación logaritmo con traslado 1.

Prueba tu aprendizaje respondiendo la siguiente pregunta.

⸻

Cierre de la clase

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

Los métodos de descomposición permiten modelar la tendencia con cualquier forma funcional en el tiempo, así como también presentan una estimación para la componente periódica.

Los filtros de media móvil son una alternativa para suavizar la serie, al igual que los suavizamientos exponenciales, pero se utilizan solo para detectar de mejor forma la tendencia y la componente periódica.

Para el caso de modelos con componente periódica, se debe decidir si este ingresa de forma aditiva o multiplicativa al modelo.

En general, una serie con tendencia no constante puede ser modelada de forma determinista o bien de forma estocástica, mientras que algunas transformaciones permitirán estabilizar la varianza.