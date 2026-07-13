# Ayudantía 3: descomposición y modelado de una serie temporal

## Inicio de la ayudantía

Esperamos unos dos minutos más y empezamos, ¿ya?

Ahí, tal vez se conectan algunos de sus compañeros más.

No sé si tienen alguna consulta mientras vamos a aprovechar este tiempo.

Ahora sí.

Hola, Pedro.

Sí, los grupos ya han sido asignados, solo que la actividad todavía no fue... Parece que hay un problema de configuración.

He estado hablando en estos días con el profesor, pero los grupos ya están listos. Es un tema netamente de configuración de la actividad.

Así que yo creo que entre hoy y mañana lo vamos a solucionar para que puedan realizar la actividad. Pero todos ya tienen asignado un grupo.

Sí, yo sé que todavía no aparecen. Justamente es porque no se asignó la actividad.

O sea, los grupos ya están creados, pero a esos grupos se les tiene que asignar una actividad. Eso es lo que está fallando: asignar la actividad. Por eso todavía no pueden verlo.

Pero ya están creados. No se preocupen de eso.

De todas maneras, voy a insistir el día de hoy, porque he estado insistiendo durante toda esta semana. Los grupos ya están generados desde la semana pasada.

Así que yo creo que ya se van a poder ver. No se preocupen de eso ahora.

Bien, creo que empezamos.

Voy a compartir pantalla.

¿Ven ahí la pantalla, cierto?

Ya, perfecto. Gracias.

Voy a empezar a grabar igual.

Ah, ya está. Al parecer, ahora directamente se empieza a grabar.

¿A ustedes les aparece que está grabando esto?

Antes se tenía que habilitar, pero parece que ahora es automático.

Ya está. Sí, ya está grabando.

## Recapitulación de las ayudantías anteriores

Esta es la ayudantía de hoy, la Ayudantía 3.

Vamos a recapitular primero lo que hemos visto hasta ahora.

En la Ayudantía 1 vimos cómo hacer la descomposición de las series temporales en:

- Tendencia.
- Parte estacional.
- Error.

Tratamos de modelar la tendencia con ciertas técnicas. Por un lado, utilizamos un modelo de regresión polinomial.

Después también analizamos la parte del error, que tratamos de modelar mediante los modelos exponenciales.

En la Ayudantía 2 empezamos a explorar un poco más el comportamiento de las series de tiempo mediante los modelos de Box-Jenkins.

Vimos `Auto-ARIMA`, que es una función bastante interesante que puede proponer un modelo en función de una métrica determinada, como el AIC.

También vimos cómo podemos modelar la serie de manera visual, utilizando:

- La función de autocorrelación, ACF.
- La función de autocorrelación parcial, PACF.

## Objetivo de la Ayudantía 3

¿Qué es lo que vamos a ver hoy?

Vamos a trabajar nuevamente con una serie de tiempo.

Como saben, las ayudantías están bastante orientadas a los laboratorios que tienen que realizar.

Vamos a tratar de complementar lo que se ha visto en las ayudantías 1 y 2.

Básicamente, vamos a dividir la serie de tiempo en:

- Tendencia.
- Estacionalidad.
- Error.

Sin embargo, vamos a tratar de modelar el error con las herramientas que utilizamos en la Ayudantía 2, mediante un modelo ARIMA.

Todavía no vamos a estudiar la parte estacional como tal mediante la modelación SARIMA. Eso lo vamos a ver en la última ayudantía.

## Paquetes, funciones y herramientas utilizadas

En el código vamos a utilizar paquetes y funciones que ya son bastante habituales.

Vamos a trabajar con:

- Regresión lineal.
- Una función para modelar una relación polinomial.
- Funciones para descomponer una serie de tiempo.
- Métricas de desempeño.

Entre las métricas de desempeño tenemos:

- El error cuadrático medio.
- El error absoluto medio.

Esta última no la hemos utilizado todavía, pero es un buen indicador para comparar modelos de series de tiempo o, en general, para evaluar el desempeño de un modelo.

También utilizaremos los gráficos de la ACF y la PACF, que nos ayudan bastante a modelar procesos de Box-Jenkins, como los modelos ARMA y ARIMA.

En esta clase vamos a utilizar `SARIMAX` de `statsmodels`, que es una función que permite ajustar este tipo de modelos.

También vamos a utilizar una función que nos ayudará a implementar el test de Ljung-Box, que permite determinar si un conjunto de datos presenta o no una estructura de ruido blanco.

## Serie de consumo de agua potable

Para esto vamos a utilizar la serie de tiempo de la primera ayudantía.

Si recuerdan, es una serie temporal correspondiente al índice mensual de consumo de agua potable.

Esta información está disponible desde 1990 hasta 2024.

Tenemos 412 observaciones.

Este indicador refleja la evolución y el comportamiento del consumo de agua potable en los sectores privado y público.

Tenemos como año base 1990, cuyo valor es igual a 100. A partir de ahí, el índice va variando cada año respecto de ese año base.

La serie continúa hasta 2024.

Las variaciones posteriores pueden ser mayores o menores, dependiendo de si ha existido un consumo superior o inferior al correspondiente al año base.

De esta manera se genera la serie temporal.

## Lectura y preparación de los datos

La información está almacenada en un archivo `.txt`.

Básicamente, lo estoy leyendo.

Solamente tengo una columna que contiene la serie de tiempo.

Como estoy leyendo el archivo mediante una función como `read_table`, el objeto resultante será un `DataFrame`.

Aquí se indica que no tengo valores nulos, lo cual es muy importante cuando uno empieza a leer y explorar una base de datos.

Posteriormente, voy a generar el rango de fechas que contiene esta base de datos en una columna denominada `fecha`.

El rango comienza en enero de 1990 y termina en abril de 2024.

La frecuencia `MS` indica que quiero ubicar cada observación al comienzo del mes.

Podría utilizarse, por ejemplo:

- El primer día del mes.
- El último día del mes.
- Alguna otra convención temporal.

En este caso se utilizará el primer día de cada mes.

Después le indico al programa que esa variable temporal sea el índice del `DataFrame`.

De esta manera, podemos ver que las fechas están generadas como índice del `DataFrame`, junto con la variable correspondiente a la serie.

## Conversión a un objeto `TimeSeries`

¿Qué voy a hacer después?

Como hemos trabajado en todas estas ayudantías, voy a convertir el objeto de tipo `DataFrame` en un objeto de tipo `TimeSeries`.

Esto permite que la información sea reconocida como una serie temporal y que podamos utilizar determinadas funciones que solamente están disponibles para objetos de tipo `TimeSeries`.

Simplemente voy a transformarlo y a guardar el resultado en un objeto de serie temporal.

## División entre entrenamiento y validación

Después voy a realizar el *split*, es decir, la división entre:

- El conjunto de entrenamiento.
- El conjunto de validación.

Estoy realizando el corte desde enero de 2023.

Por lo tanto:

- El conjunto de entrenamiento llega hasta diciembre de 2022.
- El conjunto de validación comienza en enero de 2023.

Posteriormente, vuelvo a transformar la información porque la función utilizada para dividir la serie funciona únicamente con objetos de tipo `TimeSeries`.

Esto también lo habíamos visto anteriormente.

Después vuelvo a llevar la información a un `DataFrame`.

Primero se transforma en un objeto de NumPy y posteriormente, a partir de NumPy, se crea nuevamente un objeto de Pandas.

Este será mi objeto `trainData`.

Por lo tanto, estoy convirtiendo y adaptando los datos de la serie temporal para poder trabajar con ellos.

## Visualización de la serie

Después voy a graficar:

- La serie de entrenamiento.
- La serie de validación.

Desde la primera clase he mencionado que es conveniente visualizar detalladamente la serie temporal debido a todos los comportamientos que puede presentar.

Al menos visualmente, uno puede identificar:

- Qué tipo de tendencia podría existir.
- Si hay alguna estacionalidad.
- Si existen cambios en la variabilidad.
- Si hay cambios estructurales.
- Si aparecen valores atípicos o comportamientos particulares.

Claramente, esta serie presenta una tendencia creciente.

—¿Sí?

—Sí.

## Cambios en la variabilidad de la serie

Habíamos mencionado que, durante los primeros años de la serie, aproximadamente entre 1990 y 2000, no existía demasiada variabilidad.

La variabilidad podía mantenerse relativamente similar a lo largo de ese primer periodo.

Sin embargo, a partir de esos años comenzó a existir una diferencia mucho mayor en el consumo de agua potable.

En 2017 se observa una caída bastante fuerte.

Seguramente ocurrió algún evento. Podría estar relacionado, por ejemplo, con una sequía, con falta de lluvias o con una menor disponibilidad de agua.

Puede ser un factor externo. Sin embargo, ocurrió algo que provocó una disminución del consumo de agua potable.

A partir de ese cambio estructural, la variabilidad comenzó a ser mucho más fuerte.

También se observa otra caída importante y un comportamiento bastante variable durante los años correspondientes a la pandemia.

## Importancia del punto de corte

Recuerden que dividir una serie temporal en entrenamiento y validación siempre tiene consecuencias.

Esto lo vimos en la clase anterior.

Si cortamos la serie de tiempo en un determinado instante $t$, la tendencia de los últimos datos puede influir considerablemente en la predicción.

Esto también depende de la estructura de correlación.

Por ejemplo, si la estructura de correlación solamente considera uno o dos periodos anteriores, la tendencia observada en los datos inmediatamente anteriores al punto de corte puede influir mucho en la predicción.

En la clase anterior vimos que habíamos realizado el corte en una parte de la serie que tenía una tendencia decreciente.

Por ello, a la predicción le costó volver a adoptar la tendencia creciente que normalmente presentaba la serie en ese momento.

La parte estacional también puede ayudar bastante en este proceso.

Sin embargo, incorporar estas características significa agregar nuevos parámetros que deberán estimarse posteriormente.

Por eso, la decisión sobre dónde dividir una serie temporal no debe tomarse a la ligera.

Es una decisión importante que debe considerar el comportamiento de los datos.

## Descomposición aditiva de la serie temporal

¿Qué vamos a hacer ahora?

Vamos a realizar la misma descomposición de la serie temporal que utilizamos anteriormente.

Vamos a aplicar una descomposición aditiva.

Mencionamos que la serie está compuesta por:

- Una tendencia.
- Una estacionalidad.
- Un error o residuo.

Hasta ahora, el concepto de estacionalidad debería estar bastante claro.

La estacionalidad corresponde a patrones que se repiten periódicamente en el tiempo.

Cuando tenemos una serie mensual, es muy probable que exista este tipo de comportamiento.

Por ejemplo, lo que sucede en enero, febrero y marzo podría repetirse de manera similar durante enero, febrero y marzo del año siguiente.

Por tanto, existen ciclos y patrones estacionales que pueden repetirse a lo largo del tiempo.

Finalmente, tenemos un componente de ruido o error.

Este componente captura la parte aleatoria de la serie temporal.

Muchas veces, dentro del componente de ruido o residuo aleatorio, quedan patrones que son difíciles de explicar mediante:

- La tendencia.
- La estacionalidad.

Por eso inicié la clase recordando lo que habíamos realizado en la primera ayudantía.

Ahora vamos a trabajar especialmente con esa parte: el ruido.

## Estructura del modelo aditivo

Recordemos que el modelo aditivo se divide básicamente en tres componentes.

Tenemos una variable de interés que, en este caso, corresponde al índice de consumo de agua potable.

Podemos representar la serie como:

$$
Y_t = T_t + S_t + R_t
$$

donde:

- $Y_t$ es el valor observado de la serie en el tiempo $t$.
- $T_t$ es la tendencia.
- $S_t$ es la componente estacional.
- $R_t$ es el error, residuo o componente de ruido.

La función `seasonal_decompose` permite dividir la serie de tiempo en estos componentes.

En esta función estoy ingresando `trainData`.

Hay que prestar atención al tipo de objeto utilizado.

Inicialmente podría parecer un objeto de tipo `DataFrame`, pero en este punto estamos trabajando con un objeto de tipo `TimeSeries` de Darts.

Por eso hay que tener cuidado con los tipos de datos utilizados por cada función.

Voy a emplear un modelo aditivo y voy a indicar que la periodicidad es igual a 12.

Esto se debe a que la serie es mensual y esperamos que el patrón estacional se repita cada doce meses.

Posteriormente, a partir del objeto donde se guarda el resultado de la descomposición, voy a extraer:

- La tendencia.
- La parte estacional.
- El residuo.

También voy a eliminar los valores faltantes que puedan aparecer como consecuencia del procedimiento de descomposición.

Finalmente, voy a graficar los resultados para observar cómo se comporta cada componente.

## Interpretación de la descomposición

En la primera gráfica aparece la serie temporal original.

En la segunda gráfica aparece la tendencia capturada.

Se puede observar la tendencia general y los cambios que habíamos advertido alrededor de 2016 y 2020.

En esas fechas, la tendencia cambió de manera relativamente brusca.

También puede observarse un comportamiento estacional.

Finalmente, tenemos la parte residual, que idealmente esperaríamos que se comportara como ruido blanco, de manera que se cumplan algunos de los supuestos utilizados por los modelos.

¿Voy bien?

¿Hasta ahí hay consultas?

¿Todo claro?

Supongo que todo claro.

## Construcción de la matriz temporal

Ahora vamos a generar una matriz $X$.

Esta matriz contendrá los valores del tiempo desde cero hasta el total de observaciones de la tendencia.

Recuerden que estamos utilizando la parte correspondiente al conjunto de entrenamiento.

Después, en $y$, voy a ingresar el valor de la tendencia.

Por lo tanto:

- $X$ representará el tiempo.
- $y$ será la tendencia que queremos modelar.

## Regresión polinomial de grado 3

Posteriormente voy a utilizar nuevamente la función que permite generar un modelo de regresión polinomial de grado 3.

La elección del grado también podría discutirse.

Uno podría considerar que un polinomio de grado 2 es suficiente para capturar, con cierto nivel de suavidad, los cambios estructurales de la tendencia.

Sin embargo, para este ejercicio estoy utilizando un polinomio de grado 3.

Voy a aplicar esta configuración polinomial de grado 3 a la matriz $X$.

Después voy a imprimir el contenido de `X_poly`.

Podemos ver que la primera columna está formada por unos, que corresponden al intercepto.

Después empieza a aparecer la estructura polinomial de grado 3.

Para una observación $x$, la transformación genera términos como:

$$
1,\quad x,\quad x^2,\quad x^3
$$

Por ejemplo, si el primer valor es cero:

$$
0^2 = 0
$$

y

$$
0^3 = 0
$$

Mientras que el término constante siempre será igual a uno.

Si el valor es dos:

$$
2^2 = 4
$$

y

$$
2^3 = 8
$$

Algunos de estos valores aparecen utilizando notación científica.

Por ejemplo, un número como:

$$
3.93 \times 10^2
$$

corresponde aproximadamente a 393.

Al elevarlo al cuadrado se obtiene un valor cercano a:

$$
1.54 \times 10^5
$$

Y así sucesivamente al elevarlo al cubo.

Esta es la estructura polinomial de la matriz de diseño.

## Ajuste del modelo de tendencia

Después voy a utilizar una regresión lineal.

Puedo usar una regresión lineal porque solamente estoy tratando de modelar la tendencia.

En este momento no estoy modelando ninguna estructura de correlación.

La idea es que la estructura de correlación permanezca en la parte aleatoria, es decir, en el residuo.

Para la parte tendencial, podemos suponer cierto grado de independencia entre los valores y ajustar una regresión.

En este caso, se trata de una regresión polinomial de grado 3.

Bien, el modelo ya quedó ajustado.

## Fechas para el horizonte de predicción

Posteriormente, voy a generar un conjunto de fechas que comienza en enero de 2023 y termina en abril de 2024.

Esto corresponde al periodo de predicción del conjunto de validación.

Voy a utilizar la misma frecuencia mensual que tenía el índice original.

Podemos ver que se generan todas las fechas desde enero de 2023 hasta abril de 2024.

## Matriz de diseño para la predicción

Después voy a generar una nueva matriz $X$, pero esta vez para la estructura de predicción.

Esta matriz comenzará después del último valor utilizado para ajustar la tendencia y continuará hasta cubrir todas las observaciones del conjunto de validación.

Por lo tanto, estoy generando una matriz temporal para las fechas futuras.

A esta matriz le aplico nuevamente la transformación polinomial de grado 3.

Con esta matriz podré predecir la tendencia de los datos futuros.

Básicamente, lo que estoy haciendo en este momento es predecir únicamente la tendencia de la serie temporal.

No estoy haciendo nada más.

Estoy utilizando un modelo de regresión polinomial de grado 3 para extrapolar la tendencia.

Como pueden ver, ya tengo la predicción de la parte estacional... Perdón, de la parte de tendencia.

Ahora voy a trabajar con los datos de la parte estacional.

Aquí me detengo.

¿Tienen preguntas?

—De mi parte no, profesor.

Bien, sigamos entonces.

## Preparación de la componente estacional

Veamos qué se encuentra almacenado en el índice de la parte estacional.

En el índice aparecen valores desde 0 hasta 395, lo que corresponde a 396 observaciones.

Estas observaciones contienen la componente estacional.

Lo que voy a hacer ahora es obtener el promedio de la componente estacional para cada uno de los meses e ingresar esos valores en los datos futuros.

Estamos construyendo nuestra predicción.

Este es un enfoque diferente del que utilizamos en la Ayudantía 2.

En la Ayudantía 2 modelamos toda la serie mediante diferenciación.

Primero diferenciábamos la serie y después ajustábamos el modelo.

Con la diferenciación intentábamos obtener una estructura parecida a ruido blanco para posteriormente modelarla.

Ahora estamos utilizando otro enfoque.

Estamos dividiendo la serie y modelando por separado:

1. La tendencia.
2. La estacionalidad.
3. El ruido.

Son técnicas y enfoques diferentes que finalmente apuntan al mismo objetivo: predecir una serie de tiempo.

## Promedio mensual de la estacionalidad

Tengo la parte estacional y voy a agruparla.

Después voy a calcular una media para cada mes.

Básicamente, voy a calcular:

- La media de todos los eneros.
- La media de todos los febreros.
- La media de todos los marzos.
- Y así sucesivamente.

Por ejemplo, el promedio de todos los eneros es aproximadamente:

$$
5.10
$$

Si observo el dato correspondiente al enero del año siguiente, aparece el mismo valor.

Esto ocurre porque se ha calculado un promedio común para todos los meses de enero.

Para febrero aparece aproximadamente:

$$
-1.84
$$

Y para el febrero del año siguiente se repite el mismo valor.

Para marzo tenemos aproximadamente:

$$
-2.28
$$

Y en el marzo siguiente aparece nuevamente el mismo valor.

De esta manera, en todos los datos, cada doce meses se repite el mismo valor estacional.

Esto se hace porque queremos capturar el promedio de la estructura del componente estacional y sumarlo posteriormente a la predicción de la tendencia.

## Horizonte de predicción

Tenemos los meses que debemos predecir, correspondientes al periodo comprendido entre enero de 2023 y abril de 2024.

Son 16 meses de predicción.

Este horizonte se está utilizando principalmente con fines didácticos.

Cuando uno realiza una división entre entrenamiento y validación, es común utilizar proporciones como:

- 80 % para entrenamiento y 20 % para validación.
- 75 % para entrenamiento y 25 % para validación.

Sin embargo, cuando se obtiene un modelo bien calibrado y se utiliza realmente para predecir una serie temporal, normalmente no se realizan predicciones excesivamente lejanas.

Muchas veces se predicen, como máximo, aproximadamente seis valores hacia el futuro.

Esto se debe a que la incertidumbre aumenta con el horizonte de predicción.

Si intentamos predecir doce meses o más hacia adelante, la varianza de la predicción puede ser muy grande.

Por eso también hay que comprender la diferencia entre:

- El proceso de validación y calibración del modelo.
- El uso final del modelo para realizar predicciones.

## Extensión de la estacionalidad al futuro

¿Qué voy a hacer ahora?

Voy a obtener el comportamiento correspondiente a cada mes.

Por ejemplo:

- Enero utilizará el promedio de todos los eneros.
- Febrero utilizará el promedio de todos los febreros.
- Marzo utilizará el promedio de todos los marzos.
- Y así sucesivamente.

Después del mes 12 comenzamos nuevamente con enero y repetimos la estructura hasta abril del año siguiente.

Estos valores se guardan en un objeto correspondiente a la componente estacional futura.

## Predicción combinada de tendencia y estacionalidad

Finalmente, así como inicialmente descompusimos la serie temporal, ahora vamos a reconstruir parcialmente la predicción.

Vamos a sumar:

$$
\widehat{Y}_t
=
\widehat{T}_t
+
\widehat{S}_t
$$

donde:

- $\widehat{T}_t$ corresponde a la tendencia predicha.
- $\widehat{S}_t$ corresponde a la componente estacional estimada.

Este resultado se guarda en un objeto de pronóstico o `forecast`.

Todavía no contiene la parte residual.

Por ahora, solamente hemos modelado:

- La tendencia.
- La estacionalidad.

Como los resultados estaban almacenados en objetos de tipo `TimeSeries`, vuelvo a convertirlos en un objeto de tipo `DataFrame`.

Si revisamos el resultado, podemos ver las predicciones correspondientes a la suma de:

- La parte tendencial.
- La parte estacional.

Esto se realiza para los 16 meses del horizonte de validación.

Ahora vamos a continuar con la parte de los residuos.

En muchas ocasiones, la estructura de correlación permanece precisamente en esta parte aleatoria de la serie.
