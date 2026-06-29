# Ayudantía 1: Series de Tiempo

En casos de tráfico de materiajes de conductos y objetos néutrales, el inframundo no es un término.

Ya, esperemos unos minutos, porque no hay nadie más conectado, así que ahí daremos unos 3 minutos más y empezamos. Si no se conecta nadie más, arrancamos nomás, ¿ya?

Ya, bien. Bueno, se conectó una persona más.

Hola María Eugenia, buenas tardes.

Hola.

Hola, hola. Ya, perfecto. Miren, vamos a empezar la clase nomás. Ya yo creo que esperamos los minutos necesarios. No sé qué pasó con los compañeros, pero de todas maneras igual se graban las clases, así que no hay problema en ese sentido, ¿sí?

Voy a empezar a grabar.

Ya, ahí empezó la grabación.

Bueno, muy buenas tardes a todos. Vamos a dar inicio a la ayudantía 1 del curso de series de tiempo del magíster en ciencia de datos.

Vamos a iniciar la clase de hoy. Voy a compartir la pantalla. Ahí me confirman, por favor, si ven.

¿Se ve?

Ya, perfecto.

## Objetivo de la Ayudantía

Bien, ¿qué es lo que vamos a ver hoy?

Las ayudantías en este bimestre siempre van a estar orientadas a poder ayudar y a complementar algún conocimiento que ya tienen en la parte como de la plataforma, la parte teórica y también la parte práctica.

Y además va a estar orientada bastante al laboratorio 1 que tienen que realizar, que es sobre métodos ingenuos, modelación mediante métodos ingenuos.

Y las otras ayudantías van a ser orientadas a cada uno de los laboratorios, así como para dar algún tipo de ayuda en esta parte.

Bien, lo voy a agrandar un poquitito.

Entonces empecemos.

## Librerías y Herramientas en Python

Como la programación del curso está orientada al software Python, vamos a ocupar Python.

Yo, en este caso, uso Visual Studio y ocupo los paquetes usuales que se conocen:

- NumPy
- Pandas

Justamente que son para manejo tanto de arrays como de DataFrames, etcétera.

Básicamente, tratar de tener un manejo bastante flexible en cuanto a datos.

Vamos a ocupar `TimeSeries` de `Darts`.

`Darts` es un paquete que pertenece a Python. Aquí uno puede instalar, bueno, ahí lo dejé como comentario en caso de que no lo tengan instalado, que también `Darts` está en el laboratorio y en la plataforma.

Después, `Matplotlib` con el alias de `plt`.

También `StatsModels`, que es algo bastante usado y que tiene muchas métricas guardadas.

Y de `sklearn` vamos a ocupar, al menos en esta ayudantía:

- Regresión lineal.
- Configuración polinomial.

Además, va a estar orientado a métodos ingenuos en la parte de la modelación, ya sea de Holt-Winters, modelación mediante el método exponencial de uno o dos parámetros, que es Holt, o de tres parámetros.

Pero bueno, todo eso viene en `ExponentialSmoothing`.

También vamos a ocupar de `StatsModels` el `seasonal_decompose`, que sirve para descomponer una serie de tiempo.

Y bueno, de `sklearn.metrics`, esta función `mean_squared_error`, que básicamente saca el error cuadrático medio.

Además, también esta función `boxcox`, que nos va a ayudar a hacer la transformación mediante Box-Cox.

## Archivo de Datos

Para esta ayudantía vamos a ocupar un archivo que está en la nube, está en un Google Drive, que es el ICAP.

Es un índice de consumo de agua potable del año 90 al año 2024, que ahí tiene una descarga directa. También la voy a subir a la plataforma.

Es un archivo `.txt` que básicamente tiene una columna donde tiene esta variable temporada.

Bien, entonces, viendo un poco cómo está configurado este archivo, vean que solamente tiene una columna y en cada una de las filas tiene este índice de consumo de agua potable.

Este índice de consumo de agua potable va a ser un índice que va variando en el tiempo de acuerdo a un año base.

Por ejemplo, el año base va a ser el año 90 y, a partir de ese año 90, el siguiente año se va a registrar la variación respecto a ese año base.

¿Cuánto varió en el consumo de agua potable?

Y es importante siempre, para cualquier tipo de análisis, entender qué variable estamos ocupando y conocer las características que tiene esta variable.

Claramente, como es un índice que está en base a un año base, uno puede asumir desde la construcción de los datos que esta serie temporal tiene una estructura de correlación, tiene alguna estructura de dependencia en el tiempo.

## Construcción del Objeto de Serie de Tiempo

Bien, de acá, ¿qué es lo que vamos a hacer?

Simplemente vamos a empezar a inicializar o generar un objeto, básicamente, que va a ser `df`, donde nosotros en la fecha vamos a ingresar con un objeto de tipo serie de tiempo.

Vamos a iniciar en el mes 1 de 1990 y va a terminar en el mes 4 del 2024.

Y aquí en `freq` vamos a poder decirle a esta función `date_range` qué tipo de configuración voy a ingresar en este tiempo.

Por ejemplo, si yo ingreso `MS`, se va a hacer como que se inicialice el 1 de enero de 1990 y que sea cada mes, o sea, a nivel mensual, pero que inicialice el primer día de cada mes.

Si es `M`, va a ser final de mes.

Si es `D`, va a ser una configuración diaria.

Y si es `H`, va a ser por hora.

Ahí se los dejo en comentarios cada una de las configuraciones que puede tener.

Después voy a convertir que esta fecha de `df` sea como la indexación, básicamente, el conjunto de indexación del DataFrame.

Y después le voy a decir que este índice sea de tipo DataFrame.

¿Bien?

¿Y para qué voy a hacer eso?

Con `TimeSeries` le voy a convertir este objeto en serie de tiempo, y lo que estoy ingresando ahí, básicamente, es esa columna `icap`.

Si veo qué es lo que me está generando en `df_series`, vean cómo el objeto `icap` tiene una estructura ya de fechas.

Y como nosotros lo inicializamos con `MS`, empieza el 1 de enero, el 1 de febrero, el 1 de marzo, etcétera, y aquí está mi columna de la variable que quiero estudiar.

¿Por qué es importante tener una configuración correcta de la variable que voy a estudiar?

Porque muchos de los modelos están indexados a un tipo de dato, que en este caso mi tipo de dato va a ser serie de tiempo, y no así a un DataFrame usual que maneja Pandas, por ejemplo.

Así que ahí estoy haciendo como la conversión de un objeto que era un DataFrame, básicamente, a un objeto de tipo `TimeSeries`.

Después, lo que voy a hacer va a ser dividir la serie de tiempo en un conjunto de entrenamiento, que lo voy a guardar en un objeto `df_train`, y un objeto `df_val`, que va a ser el conjunto de validación o el conjunto de testeo.

Vamos a ocupar al menos en el curso solamente dos conjuntos de datos:

- Train.
- Validación.

Bien, entonces, ahí lo estoy haciendo con el `split_before`. Básicamente, a partir de octubre del 2023 va a ser la división entre data de train y validación.

Y ojo que acá estoy ingresando mi objeto de tipo serie de tiempo.

Bien, entonces, ahí se puede ver que al final el tipo de objeto que genera `TimeSeries` es un array, que tiene una configuración diferente a los objetos que se manejan en un común DataFrame.

## Visualización Inicial de la Serie

Después, lo que voy a visualizar va a ser simplemente el plot de la serie de tiempo.

Ahí está el índice de consumo de agua potable.

Lo importante acá es ver cómo se comporta la serie de tiempo.

Eso es como algo, lo primero que uno tiene que hacer visualmente: cómo se comporta la serie de tiempo.

Claramente, esta serie de tiempo tiene una tendencia positiva, creciente básicamente.

Hay una tendencia en la serie de tiempo y también puedo empezar a visualizar que la variabilidad que tiene esta serie de tiempo en base al tiempo va creciendo.

Por ejemplo, acá en los meses iniciales de 1990, 91, 92, etcétera, la variación mensual no era bastante fuerte, pero podemos ver que, por ejemplo, desde el año 96 existe un aumento de la variabilidad.

Después, no sé si visualmente al menos uno podría decir que tal vez desde el año 2008 o tal vez 2016 hubo bastante cambio en la variabilidad.

De hecho, si nosotros nos fijamos acá en el año 2016, hubo una caída bastante fuerte en el consumo de agua y esto se puede deber a muchos factores.

Puede deberse, por un lado, a un error de dato, o tal vez ahí es necesario estudiar qué ha pasado en esas fechas, que puede ser una baja del índice de consumo que ha sido necesariamente justificado.

Puede ser porque ha habido una crisis del agua, etcétera.

Pero ahí había un cambio bastante brusco en el consumo de agua, ha bajado bastante.

A partir de eso existe un cambio de variabilidad bastante más grande que en los años anteriores.

Y de hecho, en el año 2020, que fue la pandemia, se pudo ver ahí que igual hubo una baja bastante grande del consumo de agua potable y la variabilidad fue mucho, mucho más grande.

Entonces, como lo básico que uno tiene que hacer cuando uno va viendo cómo se comporta la serie de tiempo:

- Hay tendencia.
- La variabilidad es bastante diferente en el tiempo.
- Existe un aumento de variabilidad.
- También puede existir una variabilidad constante en el tiempo o una reducción de variabilidad.

Pero lo importante es que si existen cambios de variabilidad, que es bastante usual en datos mensuales, porque recuerden que estos son datos mensuales.

## Transformación de Box-Cox

Bien, entonces cuando uno ve tendencia, uno ve variabilidad, lo que va a hacer es una transformación de Box-Cox.

Esa es una transformación bastante usual que se utiliza no solo en series de tiempo, también en modelos de regresión lineal.

¿Qué es lo que me va a ayudar la transformación de Box-Cox?

- A estabilizar la varianza.
- A reducir la heterocedasticidad.
- A aproximar a la normalidad, si nosotros tenemos en el modelo algún supuesto de normalidad.

Todavía actualmente no tenemos ese supuesto, pero es importante conocer que la transformación de Box-Cox me ayuda a aproximar normalidad a una variable.

También ayuda a mejorar el comportamiento de modelos lineales.

Esto es bastante general, pero en series de tiempo nos va a ayudar mucho a las dos primeras:

- Estabilizar varianza.
- Reducir heterocedasticidad.

Y en modelos de series de tiempo más avanzados, que no vamos a ver hoy, que vamos a ver en futuras clases, tener un supuesto de normalidad.

Bien, entonces la transformación va a estar dada por esta ecuación, donde básicamente yo tengo mi variable de interés.

Si el lambda es distinto de 0, yo voy a utilizar esa transformación.

Si mi lambda es muy cercano a 0 o igual a 0, yo simplemente puedo utilizar el logaritmo de la variable de interés.

Entonces, en la práctica, los valores grandes básicamente se van a empezar a comprimir.

De alguna manera, la serie va a volverse mucho más estable en cuanto al tiempo y claramente el modelamiento va a mejorar, porque voy a tener una serie más estable.

¿Cómo voy a transformar mi serie de tiempo?

Básicamente voy a ocupar la función `boxcox`, le voy a entregar la variable de interés, que en este caso es `icap` de este objeto `df`.

Ojo que acá no estoy utilizando mi objeto de tipo serie de tiempo.

Entonces voy a insistir mucho en que tengan cuidado en cómo manejar los objetos en Python, diferenciar los objetos de tipo DataFrame y los objetos de series de tiempo, porque muchas veces ahí ocurren muchos errores para poder aplicar posteriormente los modelos.

Bien, lo estoy guardando en un objeto `lambda`.

Después simplemente lo muestro y voy a mostrar cómo queda esta transformación que estoy guardando en mi objeto `df`, pero en `icap_boxcox`.

Mi lambda es 0.43, entonces como es distinto de 0 se está ocupando esa transformación.

Con esa transformación voy a tener mi variable transformada que se denomina `icap_boxcox`.

Vean que claramente los resultados de esa transformación son mucho más estables porque de una diferencia de 102 a 96 simplemente ya son decimales.

Entonces acá lo que voy a hacer es graficar mi serie de tiempo, pero con la transformación de Box-Cox.

Vean que, de alguna manera, si bien ha cambiado ya la escala, ha tratado de estabilizar la varianza.

Pero aún así existe bastante variabilidad en esta parte, aunque es mucho menor a lo que se tenía anteriormente.

Entonces, ya con esta transformación de Box-Cox voy a poder modelar y poder ocupar los métodos que conozco.

## Diferenciación de la Serie

Por otro lado, también se puede utilizar, y es recomendable utilizar, una diferenciación de la serie.

¿Qué es lo que me hace la diferenciación?

¿Cuándo se utiliza esta diferenciación?

Cuando existe tendencia creciente, como la tiene mi serie de tiempo.

También cuando existe tendencia decreciente.

O sea, si hay tendencia, recomendable es utilizar diferenciación.

Además, cuando la serie tiene cambios persistentes en el tiempo.

¿Y qué es lo que me va a ayudar esta transformación?

Implica que la media va a cambiar temporalmente, por lo tanto, la serie no es estacionaria.

La diferenciación busca eliminar estos cambios sistemáticos.

¿Qué es lo que hace básicamente la diferenciación?

Muchas veces la literatura lo ocupa como:

\[
\Delta Y_t = Y_t - Y_{t-1}
\]

Voy a restar mi variable objetivo en el tiempo \(t\) menos el tiempo \(t-1\).

Por ejemplo, si yo quiero tener la diferenciación del mes de febrero de 1990, voy a restar el ICAP de febrero de 1990 con enero de 1990.

Y así me va a ir construyendo mi serie de tiempo diferenciada.

### Interpretación

Se compara cada observación del tiempo \(t\) con la anterior, es decir, con el tiempo \(t-1\).

Se mide el cambio temporal.

Se elimina la parte de la tendencia, que eso es algo importante.

Después de diferenciar, la media suele estabilizarse en un valor que normalmente es 0.

Disminuye la dependencia temporal fuerte, que igual es bastante importante. De hecho, eso me va a ayudar posteriormente a tener un supuesto en los modelos ARIMA, por ejemplo.

Además, la serie queda más cercana a ser estacionaria.

Esto es importante porque muchos modelos temporales clásicos requieren estacionariedad, como los ARIMA, etcétera.

Lo que voy a hacer acá es bastante sencillo.

Voy a ocupar esta función `diff` a mi variable de interés y estoy eliminando los `NA`.

Eso lo estoy guardando en mi objeto `icap_diff`.

Entonces, todas mis diferenciaciones, mis transformaciones que estoy haciendo, lo estoy guardando en `df` para mantener la estructura de un DataFrame.

Entonces podemos ver acá que claramente la primera observación va a ser un `NA`.

¿Por qué?

Porque en enero de 1990 no tiene con qué restarse, no hay un tiempo \(t-1\), entonces siempre tienen que empezar desde la segunda observación.

Aquí podemos ver que -5.73 da el resultado de restar 96 con 102.45.

Esos son mis valores diferenciados.

Si grafico esos valores diferenciados, vean que esta serie tiene una media muy cercana a cero.

La variabilidad, de alguna manera, igual se trata de estabilizar, aunque claramente esos choques que ha tenido la serie de tiempo en los últimos años me van a afectar en la diferenciación también.

## Consulta: ¿Qué Significa que Sea Estacionaria?

Bien, a ver, hay una consulta.

Germán Vega pregunta:

> ¿Qué significa que sea estacionaria?

Que sea estacionaria significa que tenga una media constante y una varianza también constante.

Eso es lo que uno esperaría de una serie estacionaria.

Por eso la diferenciación trata de acercarse a la estacionariedad.

La media, al menos, acaba de ser muy cercana a cero y eso puede ser un paso a la estacionariedad.

El segundo paso es que la varianza también sea constante.

O sea, vale decir que de todo el proceso, de toda la serie de tiempo, su varianza sea igual.

Lo cual acá, por esos cambios bastante bruscos que se han tenido, podríamos tal vez no decir que es una serie totalmente estacionaria, pero habría que evaluar la varianza de toda la serie.

Visualmente, al menos, podríamos decir que tal vez se compensa la varianza de acá con esto, pero eso se podría evaluar.

De hecho, existen test estadísticos, los cuales vamos a ver después, que me van a decir si es estacionaria o no la serie de tiempo.

Pero esta transformación de la diferenciación es un paso muy importante para tratar de llegar a que la serie sea estacionaria.

No sé si con eso se responde la pregunta, Germán.

Perfecto.

## Serie de Entrenamiento y Validación

Bien, entonces ahora simplemente vamos a mostrar la serie total, donde está la serie de entrenamiento y la serie de validación.

Simplemente es eso.

## Método de Holt

Bien, entonces entremos al método de Holt.

El método de Holt es una extensión del suavizamiento exponencial.

De hecho, muchas veces se conoce también como el método de suavizamiento exponencial con dos parámetros, porque básicamente trata de estimar o de encontrar dos parámetros que traten de mostrar el comportamiento que tiene la serie de tiempo.

Acá pongo esto porque el suavizamiento exponencial simple solo modela el nivel promedio que tiene una serie de tiempo.

Pero, ¿qué pasa cuando una serie de tiempo tiene tendencia, por ejemplo, como la tiene mi serie de tiempo actual o la del ejemplo?

Recomendable es utilizar un modelo de Holt.

Este modelo de Holt no solamente modela el nivel promedio, sino también la tendencia.

Eso es bastante importante.

De hecho, existe un modelo más que, aparte de modelar el nivel y la tendencia, también modela la parte estacional.

La parte estacional es también algo muy importante que se tiene que evaluar en las series de tiempo.

Para que no quede duda, una serie de tiempo estacional es cuando tiene ciclos repetitivos en el tiempo.

Por ejemplo, muchas series de tiempo, este ICAP por ejemplo, podría tener alguna estacionalidad porque es una serie de tiempo mensual.

Por ejemplo, si uno evalúa el PIB trimestral, esa serie de tiempo también tiene tendencia, tiene estacionalidad.

Son como ciclos que se repiten en el tiempo.

Pero bueno, para el ejercicio y también, como les dije, este laboratorio está orientado a ayudar al laboratorio, vamos a intentar modelar esta serie de tiempo con Holt.

### Idea Principal del Método

¿Cuál es la idea principal de este método?

Es actualizar continuamente:

- El nivel de la serie.
- La tendencia.

Este método utiliza ecuaciones recursivas que seguramente ya vieron en la parte de la plataforma.

Las ayudantías no están orientadas tal vez a profundizar la parte teórica, porque eso también lo ven con el profesor Jonathan.

Esta ayudantía está más orientada a algo práctico, orientado al laboratorio.

Bien, ¿qué es lo que voy a hacer?

Voy a aplicar este suavizamiento exponencial.

Acá vean que lo que estoy haciendo es que mi data de entrenamiento la estoy volviendo en un objeto de tipo NumPy primero con el `squeeze`.

Después lo voy a volver en un objeto de tipo Pandas para que sea un DataFrame.

Recuerden que el `train_data` estaba construido con un objeto de serie de tiempo, entonces estoy haciendo como la migración de ese tipo de objetos.

El `ExponentialSmoothing` va a ingresar acá el `train_data`, pero que es de tipo DataFrame, porque no me va a aceptar un objeto de tipo serie de tiempo.

Después, en `trend` le estoy agregando o le estoy diciendo que la serie de tiempo tiene tendencia.

En `seasonal` estoy poniendo `None`, que no tiene un comportamiento estacional.

¿Por qué?

Porque quiero modelar mediante un modelo de Holt.

Si `trend` y `seasonal` fueran `None`, entonces ahí yo tendría un modelo de suavizamiento exponencial simple.

Y si en `seasonal` le pongo que sí modele la parte estacional, ahí tendría un modelo de tres parámetros o Holt-Winters, que también se llama así.

Entonces ahí tienen como la flexibilidad de escoger qué tipo de modelación quieren hacer.

Eso lo guardo en un objeto `model`.

Después ajusto los datos, lo guardo en un objeto `result`.

Después simplemente voy a guardar el `smoothing_level` en el objeto alfa y el `smoothing_trend` en mi objeto beta.

Esos son básicamente los parámetros que está encontrando este modelo de suavizamiento exponencial.

Aquí puedo ver que el alfa es 0.3346 y el beta es muy cercano a 0.

Debe ser un valor bastante cercano a 0, básicamente.

Entonces ahí uno también podría decir si realmente este tipo de modelo es recomendable.

## Ajuste del Modelo de Holt

¿Qué es lo que vamos a hacer ahora?

Vean que vamos a graficar la serie de tiempo y además en `fittedvalues`, de mi objeto `result`, donde está mi modelo de Holt, están los valores ajustados de este modelo.

Básicamente se va a ver así la serie de tiempo.

Vean que la línea negra es la serie de tiempo original y la línea roja es cómo se está comportando o cómo está ajustando mi serie de tiempo mediante este modelo exponencial.

Claramente se puede ver que, de alguna manera, este tipo de modelo sí está capturando de manera correcta el comportamiento de mi serie de tiempo.

Por ejemplo, en los momentos más complicados que ha habido aquí, una tendencia a la baja, sí captura ese tipo de tendencia y ese cambio de nivel que tiene la media en este punto.

Entonces, de alguna manera, está capturando el comportamiento de mi serie de tiempo.

## Predicción con el Modelo de Holt

Después voy a hacer lo mismo, pero con mi data de validación.

Es el mismo proceso:

- `squeeze` para volverlo de tipo NumPy.
- Después DataFrame.

Acá, ¿cuál va a ser el cambio?

De mi objeto `result` voy a ocupar el `forecast`, que básicamente permite predecir.

Aquí le digo el tamaño de cuántos quiero predecir de mi modelo de Holt.

Eso lo guardo en mi objeto `forecast_holt`.

Esta es mi data de validación, que básicamente son siete datos.

Con el `forecast` estoy estimando básicamente o estoy prediciendo específicamente estos siete valores.

Veamos cómo se comporta esta predicción.

Aquí estoy justamente graficando el `forecast_holt`.

Vean que el ajuste, bueno, al menos la predicción en base al ajuste del modelo, no se ve tan bien.

De hecho, no captura estos cambios de tendencia y estos cambios de media en mi modelo.

Entonces, estos modelos de suavizamiento exponencial han sido como los primeros modelos en la historia en series de tiempo.

No voy a decir como el primero, pero han sido uno de los primeros que han tratado de modelar series de tiempo.

Si bien el modelo captura como un buen comportamiento, la predicción no es tan buena.

Tal vez ajustando un modelo de Holt con la parte estacional esto podría mejorar.

Pero ahí uno puede explorar, puede jugar un poco con los datos, con el ajuste y ver cómo se comporta.

Bien, preguntas.

¿Hay alguna consulta hasta ahí?

Bien, a ver, ¿cuántas personas estamos?

Somos 6.

Wilmer, ¿tienes alguna consulta?

Me escucha, buenas tardes.

Sí.

Decirle disculpa que llegué tarde, estaba en el trabajo.

No hay problema.

¿Tienes consulta?

¿Respecto a la clase o respecto a la tarea?

A las de la tarea lo podemos hablar al final, pero de la clase hasta el momento, ¿tienes alguna consulta?

No, hasta ahora.

Perfecto.

Bien, sigamos entonces.

## Descomposición de una Serie Temporal

Ahora vamos a ver la descomposición de una serie temporal.

Una serie temporal normalmente tiene cierto tipo de partes que, sumadas o multiplicadas, construyen una serie temporal.

Es como una descomposición que se va a hacer en tres elementos:

1. Tendencia.
2. Estacionalidad.
3. Ruido.

### Tendencia

La tendencia es un cambio a largo plazo de la serie de tiempo.

Puede tener tendencia creciente, no creciente, etcétera.

### Estacionalidad

La estacionalidad aparece cuando tenemos patrones que se repiten periódicamente.

### Ruido

El ruido son las variaciones aleatorias que no entran en algo totalmente determinístico.

Bien, la idea de la descomposición es separar estos componentes para entender mejor el comportamiento de la serie.

## Modelo Aditivo y Modelo Multiplicativo

Por un lado, voy a tener una descomposición mediante un modelo aditivo, donde se tiene la siguiente descomposición:

\[
Y_t = T_t + S_t + E_t
\]

Mi serie de tiempo \(Y_t\) se va a descomponer en tres componentes:

- Tendencia.
- Estacionalidad.
- Ruido.

En base a estos tres elementos yo puedo recuperar mi serie de tiempo.

Eso es lo que me dice el modelo aditivo.

Cuando yo tengo un modelo multiplicativo, yo puedo recuperar mi serie de tiempo en base a una multiplicación de estos tres elementos:

\[
Y_t = T_t \times S_t \times E_t
\]

Esto a veces es muy común verlo en economía y en finanzas, este tipo de modelos multiplicativos.

Para efectos de la ayudantía de hoy, vamos a descomponer con esta función `seasonal_decompose` mi data de entrenamiento, pero mediante un modelo aditivo.

También le tengo que entregar qué tipo de serie de tiempo tengo.

Aquí, como es una serie de tiempo mensual, le agrego 12, porque en el año tengo 12 meses.

Básicamente es eso.

Ahora, en este objeto que generé, voy a graficar cómo se está dividiendo cada uno de estos componentes:

- Tendencia.
- Estacionalidad.
- Ruido.

Y voy a tener este gráfico.

Voy a ir explicando cada uno de estos.

Esto es importante: que al menos gráficamente se entienda cómo se descompone la serie de tiempo.

Este primer gráfico es mi serie de tiempo original, sin ningún cambio.

Después, cómo de esto se descompone esta serie de tiempo mediante la tendencia.

Pueden ver que la tendencia está básicamente dada por esta línea.

Claramente, cuando yo tengo bastante ruido, la tendencia baja.

Esta va a ser mi primera parte, mi primer elemento en la descomposición, que básicamente es la tendencia, representada por \(T_t\).

Después, la parte estacional.

Vean que sí tiene una estructura estacional.

Al menos mi serie de tiempo, mediante esta descomposición, sí puedo ver que hay un componente estacional, que básicamente es este \(S_t\).

Después mi error, bueno, no error sino ruido, que básicamente es la parte aleatoria que tiene mi serie de tiempo.

Entonces, en base a eso, yo puedo descomponer mi serie en estos tres elementos que están mostrados acá.

## Modelamiento de la Tendencia

Entonces, ¿qué es lo que voy a hacer?

Voy a guardar esta parte de mis elementos de la tendencia en `estimate_trend`, de mi objeto que guardaba toda la parte de la descomposición.

Y la parte estacional justamente en este elemento.

Bien, entonces, ¿qué es lo que vamos a hacer?

Vamos a tratar de modelar la parte de la tendencia.

Lo cual vamos a tratar de ajustar al final mediante esta descomposición, modelando la tendencia por un lado y después sumando la parte estacional.

¿Cómo voy a modelar la tendencia?

Puede haber muchas técnicas.

Por un lado, se puede hacer mediante una regresión lineal simple cuando la tendencia es bastante lineal.

Por ejemplo, se puede aplicar una regresión simple.

Pero en algunos casos, cuando una línea recta no es suficiente, entonces yo puedo utilizar una regresión polinomial.

Por ejemplo, la tendencia puede acelerarse en algunos puntos o desacelerarse, o existen curvaturas bastante marcadas.

Ahí uno puede elegir qué tipo de regresión polinomial o a qué grado de regresión polinomial quiero llegar.

En este caso vamos a ocupar una regresión polinomial de grado 3.

Aquí hay que tener cuidado en la decisión, porque muchas veces tener una regresión polinomial de muchos grados me puede llevar a tener un error de especificación del modelo.

Por eso, a veces solamente es suficiente modelar una regresión lineal o una regresión polinomial de grado 2.

Aquí, por cuestiones netamente prácticas, lo vamos a hacer de grado 3.

Pero ahí uno tiene que ir viendo cómo se van comportando los estimadores.

Entonces, yo sé que ustedes antes han tenido un curso donde han conocido la regresión lineal.

Pero esto acá, porque la regresión lineal tenía covariables, tenía una variable de respuesta y tenía covariables, que eran variables \(X\), que aportaban de alguna manera a la variable de respuesta, a la variabilidad de la variable de respuesta.

En este caso la idea es similar, pero acá mis covariables van a ser el tiempo.

Por eso puse esta ecuación donde mi variable \(Y_t\), que básicamente es mi variable de tendencia, va a estar explicada por un intercepto, por un coeficiente beta 1, pero aquí estoy multiplicando la variable del tiempo, que normalmente es una variable temporal del 1 hasta el número de observaciones que tengo.

Después ese mismo tiempo al cuadrado.

Y finalmente el tiempo al cubo, porque yo estoy ocupando una regresión polinomial.

\[
Y_t = \beta_0 + \beta_1t + \beta_2t^2 + \beta_3t^3 + \varepsilon_t
\]

Bien, ahí explico todo lo que se tiene.

También se va a tener asociado un grado de error, pero netamente la tendencia.

Entonces aquí estoy tratando de modelar la tendencia.

Que eso no nos escape de la idea del modelamiento.

Para eso nosotros vamos a generar estas variables polinomiales, que van a ser de grado 3.

Eso lo estoy guardando en un objeto `X`.

Después estoy guardando básicamente la tendencia.

Finalmente voy a ocupar esta transformación polinomial y lo voy a guardar aquí.

Básicamente este `X_poly` va a tener mi variable temporal.

Como tengo intercepto, va a ser unos, el \(t\), \(t^2\) y \(t^3\).

Así va a estar estructurada mi matriz.

Después vamos a construir nuestros periodos futuros.

Para eso estoy generando un objeto de Pandas que tenga un rango desde octubre del 2023 hasta abril del 2024, que son los objetos que quiero predecir.

Recuerden que yo dividí mi serie de tiempo en data de entrenamiento y en data de test.

Por eso estoy haciendo eso.

Después acá simplemente voy a generar mi matriz que va a contener mis valores polinomiales, pero para mi predicción.

Después simplemente voy a aplicar la transformación en base a mi regresión polinomial de grado 3.

Aquí menciono básicamente lo que estoy haciendo:

> Se generan nuevos índices temporales correspondientes al futuro y el modelo necesita conocer qué posiciones temporales desean pronosticar para construir las variables polinomiales futuras.

## Estimación de Parámetros

Bien, entonces ahora vamos a estimar mis parámetros:

\[
\beta_0, \beta_1, \beta_2, \beta_3
\]

Para eso voy a ocupar regresión lineal, que ya se conoce.

Lo guardo en un objeto `trend_model`.

Después voy a ajustar en base a mi matriz `X_poly` y mi variable `Y`, que es mi tendencia básicamente.

Después aquí muestro el intercepto y los coeficientes estimados que me ha generado esta regresión polinomial.

También estoy mostrando el \(R^2\), que es qué tanto de la variabilidad está siendo explicada por mis covariables.

Ahí se puede ver que tengo una varianza explicada de mi variable de respuesta de 98%, así que se está ajustando bastante bien esta regresión polinomial de grado 3.

Ahí uno podría evaluar si el último coeficiente me está aportando a mi regresión, porque vean que es bastante cercano a 0.

Eso se puede ir testeando.

De hecho, se conocen también métodos de selección de variables.

Entonces ahí ustedes pueden aplicar toda esa teoría de regresión lineal que se tiene.

Bien, entonces aquí el modelo extrapola la curva polinomial hacia periodos futuros.

Es decir, utiliza el patrón histórico de la tendencia para estimar cómo continuará evolucionando.

Después voy a hacer las predicciones y eso lo estoy guardando en `predicted_poly_trend`, en base a este modelo que construí polinomial.

## Incorporación de la Estacionalidad

Bien, entonces ahí la regresión polinomial solo modela la tendencia.

Ojo que no se pierda de vista eso.

Pero la serie original también contiene patrones estacionales, ¿cierto?

Porque si yo quiero recuperar eso, tengo que sumar la parte de tendencia más la parte estacional, en base a la descomposición aditiva que hice.

Para eso vamos a recuperar la componente estacional estimada previamente que estaba guardada en mi objeto de la parte estacional.

Aquí estoy seleccionando mis últimos 12 valores y básicamente me voy a quedar con los primeros siete, que son los que necesito para mi tendencia.

¿Qué es lo que estoy haciendo acá?

Por un lado, yo tengo aquí mi predicción en base a mi regresión polinomial, que ya estaría prediciendo la parte de la tendencia, pero le tengo que sumar el componente estacional.

Para eso voy a agarrar mis últimos datos que corresponden a la parte estacional.

Es decir, por ejemplo, si yo quiero recuperar la estacionalidad de noviembre, voy a seleccionar la parte del componente estacional de noviembre de un año antes.

Eso es lo que estoy haciendo con esto.

¿Por qué?

Porque al final, para que se entienda, vean que mi parte estacional se va repitiendo.

Entonces yo estoy ocupando básicamente el componente estacional de los 12 últimos meses y solamente estoy tratando de capturar los meses que necesito para mi predicción, que era noviembre del 2023, para llegar así hasta abril del 2024.

Eso es lo que estoy haciendo con este código.

Finalmente sumo, porque como es aditivo, ahí voy a recuperar mis predicciones básicamente.

Después lo voy a volver en un tipo de serie de tiempo, pero que está dado desde mi paquete de Pandas.

Ahí estoy indexando básicamente los datos futuros para tener esta estructura.

Voy a tener los meses que estoy prediciendo, como se puede ver:

- Octubre del 2023.
- Noviembre del 2023.
- Y así sucesivamente.

Y como he encontrado esto mediante esta suma:

\[
\hat{Y}_t = \hat{T}_t + \hat{S}_t
\]

Estoy sumando en base a la tendencia más la estacionalidad.

## Comparación Visual de la Predicción

Bien, si grafico cómo se comporta mi predicción en base a mi descomposición de serie de tiempo, vean que está:

- La serie original de mi data de train.
- La curva azul, que era mi data de testeo.
- La curva morada, que es la predicción.

Y bueno, si hago un zoom, básicamente vean que esta descomposición en serie de tiempo, al menos en la predicción visualmente, se comporta mejor que el modelo de Holt.

Al menos visualmente puedo decir eso.

Pero yo necesito algo numérico que me diga cuál de mis dos modelos es mejor.

Una métrica de desempeño bastante conocida es el error cuadrático medio, el `mean_squared_error`.

En esta fórmula, básicamente es un promedio de la diferencia de los valores observados menos los ajustados al cuadrado.

\[
MSE = \frac{1}{n}\sum_{t=1}^{n}(Y_t - \hat{Y}_t)^2
\]

Para eso voy a ocupar la función `mean_squared_error` y voy a ingresar mis datos de validación y mi predicción en base a Holt.

Vean que mi error cuadrático medio es 68.35.

Si hago lo mismo, pero con los datos de validación y hago la comparación con esta predicción mediante la descomposición, vean que ese error cuadrático medio es de 30.67.

Entonces, el mejor modelo mediante esta métrica de desempeño del error cuadrático medio es mediante mi descomposición de la serie de tiempo, porque es menor al modelo de Holt.

Visualmente ya lo habíamos advertido.

Entonces aquí la conclusión sería que el modelo mediante descomposición está mucho mejor en la predicción que el de Holt.

Recuerden que en la serie de tiempo, si bien yo puedo capturar bien el comportamiento en la serie de tiempo de mi data de entrenamiento, lo que me importa es la predicción.

Qué tanto me voy a acercar a los valores reales en la predicción.

Porque al final eso es lo que quiere tener uno cuando hace modelación por series de tiempo.

Bien, eso es lo que tengo preparado para hoy.

Ahora vengan las preguntas.

## Preguntas y Respuestas

Buenas tardes, profesor, ¿qué tal?

Hola, Maribel.

Tenía una duda.

Si bien al inicio no contempla la parte estacional y luego está teniendo esta parte de la tendencia a la parte de estacionalidad más el ruido, ¿debería tener más un ruido, cierto? ¿O solo son dos componentes?

Exactamente. Muy buena observación.

Y lo otro era que sé que hay la otra que es la mixta y la multiplicativa.

En un inicio, ¿cómo elijo?

Si bien yo podría hacer cada paso individual considerando solo tendencia, es que al inicio no es que considera solo tendencia, sino decides modelar de una forma, pruebas, consideras la estacionalidad, la tendencia y luego multiplicas eso.

Pero, ¿cómo de un inicio puedo elegir un solo camino o tengo que probar y ver cuál es el que tenga menor error?

Y en este caso, a la hora en la segunda parte que hace el ejercicio, no sé si se me pasó, cómo es que ya tienes la tendencia, decides modelar de una forma, tienes la estacionalidad.

En la estacionalidad no se consideró como que los ciclos, no sé, cada seis meses hay cierta estación que se repite.

Eso no se contempla, ¿no?

Y al final, tanto la tendencia como la estacionalidad también tienen ruidos y al final tienes un ruido general de toda la serie, ese proceso.

¿Me podría explicar las dudas?

Gracias.

Súper, Maribel. Súper, súper muy buenas las preguntas y gracias por las consultas.

Bien, vamos a ir respondiendo en base a esto.

### Sobre el Modelo Aditivo y el Componente de Error

Efectivamente existe un componente de error.

Este componente de error muchas veces yo lo voy a poder modelar con modelación que voy a ver posteriormente.

Por ejemplo, este error o este ruido yo puedo asumir una cierta distribución.

Yo puedo decir que quiero modelar esta parte de error de alguna manera.

En este ejercicio yo no estoy considerando todavía eso.

Simplemente estoy tratando de modelar la tendencia y la estacionalidad.

¿Por qué?

Porque en futuras ayudantías yo voy a poder ver de alguna manera que este grado de error puede ser modelado con otro tipo de modelos.

Por ejemplo, vamos a ver posteriormente que existe la parte de correlación entre los datos.

Por ejemplo, un tiempo \(t\) va a estar correlacionado con datos anteriores de alguna manera.

Eso, al menos en este modelo, no se está viendo.

Muchas veces esa parte aleatoria está cargada en el error.

Con modelos como el ARIMA o el SARIMA, este tipo de errores se puede modelar cuando tengo algún grado de correlación con datos anteriores.

### Sobre la Elección del Modelo

Ahora, no existe un camino único para modelar una serie de tiempo.

Claramente, esto es como ser cirujano, donde yo tengo que tener bastante delicadeza en encontrar la mejor manera de solucionar un problema.

No hay una regla general para modelar series de tiempo.

Al menos en la parte inicial, cuando vimos los modelos de Holt, claramente nosotros no consideramos la parte estacional.

Simplemente consideramos la tendencia.

Pero por eso decía que, por ejemplo, sería un buen ejercicio preguntarse:

¿Qué pasa si este modelo Holt yo lo vuelvo un modelo Holt-Winters?

Cuando yo considero no solamente la tendencia y también el nivel, sino además la parte estacional, posiblemente mejore la predicción.

Puede ser, no lo sé, pero habría que ver.

Entonces, al final, yo puedo ir jugando con los modelos.

Por un lado, el modelo Holt puede tener:

- Un parámetro.
- Dos parámetros.
- Tres parámetros en el modelo de suavizamiento exponencial.

Ver cuál se comporta mejor entre ellos y quedarme con el que tiene mejor métrica de desempeño.

La métrica de desempeño igual es debatible cuál es mejor utilizar.

En esta clase solo vimos el error cuadrático medio, pero existen otras también, como el MAPE, etcétera.

### Sobre Modelo Aditivo o Multiplicativo

Por otro lado, volviendo a la parte de la elección de si yo quiero elegir un modelo aditivo o multiplicativo, de la misma manera, no existe una regla para decir:

> Este tipo de serie debería ser aditiva, este tipo multiplicativa.

Yo podría hacer los dos, de alguna manera, y ver cuál se acomoda mejor a mis datos.

Pero aquí yo puse algo bastante interesante.

Este modelo multiplicativo, al menos cuando hago la descomposición en series de tiempo, se utiliza mucho en economía y en finanzas.

¿Por qué?

Porque en ese tipo de datos existe mucha variabilidad.

Por ejemplo, si yo veo alguna serie de tiempo de la bolsa, a veces hay datos que tienen choques bastante altos.

Tal vez hubo un disparo o se cayó la bolsa.

Entonces, a veces, en ese tipo de información, es mejor aplicar este modelo multiplicativo.

Pero repito, no existe una fórmula escrita en papel.

Uno puede ir probando y, en base a las métricas de desempeño, quedarse con un mejor modelo.

Eso, María Eugenia, o Maribel, si no me equivoco. ¿Cierto, Maribel?

Sí.

Respecto al modelar cada componente, tanto la tendencia y la estacionalidad tienen ruidos y también sé que a nivel general ese \(E_t\) también es otro ruido.

Entonces, al final, eso se tiene que hacer alguna cosa que sea independiente.

Claro.

De hecho, cuando estás modelando la tendencia, al asumir que es un modelo de regresión lineal, porque este \(Y_t\) es la tendencia, no es la variable original.

Y aquí yo tengo un error.

Bajo el supuesto de la regresión, en este caso polinomial, el error asociado a la tendencia es normal.

Ese es el supuesto que está en la tendencia.

¿Se entiende?

Sí, y la siguiente componente, la estacionalidad.

Ya, ¿cómo estoy obteniendo?

En la parte estacional no estoy asumiendo ningún error.

¿Por qué?

Porque al final la parte estacional es un componente cíclico.

Si yo agarro estos datos, va a ser lo mismo que agarrar estos datos o lo mismo que este dato.

Entonces, simplemente agarrar este o este de acá va a ser lo mismo, porque gráficamente la parte estacional es la misma.

Ahí no tiene, al menos para estos datos, mucho sentido tratar de modelar, porque es un ciclo repetitivo.

Entonces, por eso solamente voy a asumir que para los datos futuros la componente estacional se comporta como la de los últimos 12 meses.

¿Ahí se entiende, Maribel?

El ruido que muestras, por ejemplo, en la gráfica, es de la ecuación general, ¿verdad?

Esta.

Ese es de la general.

Exactamente.

Si bien, porque tiene como ciclos la estacionalidad, no se considera en la ecuación un error asociado a la estacionalidad.

Eso entiendo.

Claro.

Es que, a ver, este error es de la serie original.

Acá en la tendencia estoy separando la tendencia y estoy aplicando un modelo, que es un modelo de regresión polinomial, que tiene asociado un error normal.

Pero simplemente de la tendencia.

Acá no lo estoy modelando.

Simplemente, como es un ciclo repetitivo, estoy utilizando información que se repite, básicamente.

Para mis datos futuros, lo que mencionaba, para octubre del 2023, estoy ocupando la parte estacional que tenía octubre del 2022, básicamente.

No tengo un grado de error, porque los datos no me piden que modele este tipo de estacionalidad, al menos en esta serie de tiempo.

OK.

Creo que sí, porque luego no es que llegues a ajustar esto, sino ajustas la suma.

Claro, exacto.

De la estacionalidad más la serie.

Ah, OK.

Y esa suma es, o sea, solo se suma y ya.

Sí, porque al final mi modelo inicial es el aditivo.

Ah, OK.

Y claro, ahí viene tu consulta de:

¿Qué pasa con este error?

Yo no estoy sumando este error, ¿cierto?

Y eso es cierto, porque claro, el error que está acá es algo totalmente aleatorio que va a componer, que va a tener un componente como autocorrelación en el tiempo.

Todavía no vimos modelos ARIMA-SARIMA, que lo vamos a ver después, que justamente me van a ayudar a tener ese grado de error y a tratar de manejarlo de alguna mejor manera.

Pero para al menos esta clase, no lo estamos tomando en cuenta.

Pero sí, cuando uno ya trabaja con series de tiempo de manera más correcta, uno también tendría que modelar este grado de error.

Sí.

Ya creo que sí, mejor.

Porque al inicio pensé que cada componente tenía un error.

Y como veía otro error de la serie general, me preguntaba qué pasaba al final con esos errores.

Pero ahora entiendo que solo hay un ajuste en la tendencia, que si bien su error tiene una distribución normal, entendería que se agrega igual.

No sé, ¿en qué quedó ese error?

Ahí lo reviso mejor.

No, es que el error de la regresión lineal ya está implícito en la tendencia.

A la hora que haces el ajuste, entiendo.

Claro, porque esto es un modelo de regresión lineal que se conoce, el usual.

Entonces, ya está implícito dentro de esto.

Ahora, claramente, por eso decía que al menos en este ajuste de la tendencia, yo podría hacer y aplicar todos los conocimientos que tengo de regresión lineal.

Podría ver si estos son significativos.

Si no, podría hacer un test de hipótesis para ver si estos parámetros corresponden o no ajustarlos, etcétera.

Pero eso asumiendo que son errores normales.

Pero eso es netamente de la tendencia.

No tiene nada que ver con este error.

Sí, me quedó clarísimo.

Gracias.

Súper, Maribel.

Más bien a ti, gracias por las consultas.

Siempre es bueno conversar de este tipo de cosas.

No sé si existe alguna otra consulta más.

Ya, perfecto.

Voy a detener la grabación.