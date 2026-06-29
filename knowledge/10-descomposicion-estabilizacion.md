# Descomposición y Estabilización de Series de Tiempo

Bienvenidos y bienvenidas.

En la clase anterior trabajamos con dos series reales:

- Generación de Energía Eléctrica (GEE)
- Índice de Oscilación Sur (SOI)

Las cuales presentan estructuras muy diferentes.

Mientras la serie GEE muestra una tendencia creciente y patrones repetitivos en el tiempo, la serie SOI presenta un comportamiento estable tanto en media como en varianza.

En la clase anterior, además de presentar estas series, se modelaron mediante un Holt-Winters multiplicativo y un suavizamiento exponencial simple para GEE y SOI respectivamente.

En esta clase extenderemos los modelos a la familia de métodos de descomposición, en conjunto con manipulaciones de los datos que podrían mejorar el ajuste y predicción, como lo son las transformaciones o bien la diferenciación que estabiliza la serie con tendencia.

Para estos fines se analizará exclusivamente la serie GEE, ya que para la serie SOI no tienen sentido estos métodos porque, como se mencionó, ya es estable tanto en media como en varianza.

## Contenidos de la clase

### Tema 1
Método de descomposición. Aplicación a la serie GEE.

### Tema 2
Transformaciones. Aplicación a la serie GEE.

### Tema 3
Diferenciación. Aplicación a la serie GEE.

### Tema 4
Análisis de estructura de dependencia: ACF, PACF y test de blancura.

# Tema 1: Método de Descomposición

## Aplicación a la serie GEE

El método de descomposición permite una mayor flexibilidad en la forma de la tendencia, ya que admite especificaciones lineales o no lineales.

No obstante, esta tendencia se fija en el tiempo, lo que limita su capacidad de adaptación ante cambios en la serie.

Por el contrario, Holt-Winters utiliza una tendencia lineal, pero sus parámetros se ajustan dinámicamente, permitiendo capturar mejor cambios recientes.

Al igual que Holt-Winters, primero se debe identificar si la serie presenta una tendencia aditiva o multiplicativa con la componente estacional.

Esto se determina a través de la gráfica de la serie, donde lo que se debe observar es si la componente estacional tiene una amplitud constante o varía dependiendo del valor de la tendencia.

Tal como se realizó el análisis en el ajuste del modelo Holt-Winters, para la serie GEE es más apropiada una descomposición multiplicativa.

La gráfica adjunta muestra la descomposición de la serie en sus tres componentes:

- Tendencia
- Estacionalidad
- Ruido

para el modelo multiplicativo.

Cabe destacar que la tendencia se obtiene mediante el filtro de media móvil, por lo que es la misma independiente de si se asume una descomposición aditiva o multiplicativa.

Mientras que la componente estacional y el ruido sí se ven afectados por la elección del modelo.

En el caso del modelo multiplicativo, tanto la componente estacional como el ruido fluctúan en torno al valor 1.

## Ajuste de la tendencia

El primer paso es ajustar la tendencia, que en este caso, según la gráfica, es prácticamente lineal.

Adicionalmente se propone un polinomio de grado 2 para tratar de ajustar una leve curva que se observa en la gráfica.

Es decir, se ajustan los siguientes modelos:

### Modelo 1
Relación lineal.

### Modelo 2
Relación cuadrática.

El tiempo se centra en el año 2000 para que los coeficientes no sean excesivamente grandes, sobre todo el intercepto.

Esto no afecta la estructura del modelo.

Aplicando el método de mínimos cuadrados se obtienen los modelos ajustados.

La gráfica muestra:

- Serie observada de la tendencia.
- Modelo 1 en color rojo.
- Modelo 2 en color azul.

Claramente el Modelo 2 ajusta mejor que el Modelo 1.

Además, el p-valor del ANOVA que compara ambos modelos es prácticamente cero.

Es decir, estadísticamente el Modelo 2 se ajusta mejor que el Modelo 1.

A este ajuste de tendencia se debe multiplicar por la componente estacional para obtener finalmente el ajuste completo y las predicciones finales.

## Comparación con Holt-Winters

El error cuadrático medio se presenta en la tabla correspondiente.

Se aprecia que los errores del método de descomposición son considerablemente mayores que los obtenidos por el método Holt-Winters ajustado en la clase pasada.

### Comprueba lo aprendido

Los errores de predicción con el método de descomposición son considerablemente mayores al modelo Holt-Winters.

La principal razón es la rigidez de la tendencia.

En el período de prueba se observa un cambio importante que el modelo no logra capturar.

La figura adjunta contiene:

- Azul: ajuste desde el año 2015.
- Rojo: serie de prueba.
- Verde: serie predicha.

Todos los predictores son mayores a los valores reales.

## Conclusión

La validación cruzada muestra que el método Holt-Winters multiplicativo se ajusta mejor a la serie de Generación de Energía Eléctrica.

# Tema 2: Transformaciones

## Aplicación a la serie GEE

En algunos casos, transformaciones de la serie original permiten mejorar el ajuste.

En general:

- No existe un criterio claro para decidir cuándo aplicar una transformación.
- No se sabe teóricamente si provocará mejores resultados.

Si bien existen muchas transformaciones, una de las más conocidas es la transformación de Box-Cox.

Esta transformación es reversible, por lo que, una vez realizado el ajuste en la serie transformada, es posible retornar a la serie original de manera única.

## Transformación de Box-Cox

Recordemos que la transformación de Box-Cox está dada por:

- Para λ = 0 → transformación logaritmo.
- Para λ ≠ 0 → transformación potencia.

Para la serie GEE, el valor óptimo de λ es:

\[
\lambda = 0.025
\]

Este valor es cercano a cero, por lo que la transformación logarítmica podría ser válida.

En algunos casos se prefiere utilizar logaritmo por sobre el valor óptimo porque resulta mucho más fácil de interpretar.

## Comparación de transformaciones

La gráfica muestra:

- Negro: Box-Cox con λ óptimo.
- Rojo: transformación logarítmica.

En ambos casos, el efecto de la transformación es eliminar el efecto multiplicativo entre la tendencia y la componente estacional.

Por lo tanto, para esta serie es más apropiado asumir un modelo aditivo.

Esto aplica tanto para:

- Holt-Winters.
- Método de descomposición.

La transformación logarítmica tiene un mayor efecto en la parte superior de la serie, aplanando más la curva.

## Resultados

Al replicar el análisis para Holt-Winters y descomposición con la serie transformada:

- Ambos modelos pasan a ser aditivos.
- El método de descomposición asume tendencia cuadrática.

Los resultados muestran que:

- Holt-Winters original sigue siendo el mejor modelo.
- La mejora más importante ocurre en los modelos de descomposición.
- El error de predicción se reduce más de cinco veces.
- Los errores quedan cercanos a los de Holt-Winters.

También se observa que Box-Cox óptimo mejora ligeramente respecto al logaritmo, aunque la diferencia no es relevante.

# Tema 3: Diferenciación

## Aplicación a la serie GEE

Para ajustar series de tiempo con estructura compleja mediante métodos probabilísticos se requiere transformar una serie inestable en una serie estable en media y varianza.

Es decir, obtener algo similar a la serie SOI.

En este contexto, la diferenciación juega un rol fundamental.

Puede ayudar a estabilizar la serie sin necesidad de ajustes previos.

## Tendencia estocástica vs tendencia determinista

Cuando se logra estabilizar una serie mediante diferenciaciones, se dice que presenta una:

### Tendencia estocástica

Por el contrario, cuando la tendencia se determina de forma paramétrica, como en el método de descomposición, se habla de:

### Tendencia determinista

En este último caso:

- Se analiza el ruido de la descomposición.
- Se ajusta un modelo probabilístico sobre dicho ruido.
- Alternativamente se utiliza un modelo de regresión con errores correlacionados.

## Ruido de la descomposición

Por ejemplo, en la serie GEE, al ajustar la descomposición multiplicativa, el ruido presenta:

- Estabilidad alrededor de 1.
- Varianza prácticamente constante.
- Un posible outlier.

## Diferenciación directa

Al aplicar diferenciación directamente sobre la serie original:

- La serie queda centrada en 0.
- La variabilidad aumenta levemente con el tiempo.

## Diferenciación + Logaritmo

La diferenciación puede combinarse perfectamente con Box-Cox y particularmente con logaritmo.

La secuencia es:

1. Aplicar logaritmo.
2. Diferenciar.

La serie resultante es la más estable:

- Media centrada en 0.
- Varianza constante.
- Sin valores anómalos.
- Sin comportamiento creciente en la variabilidad.

Por ahora debemos recordar que tanto:

- Diferenciación.
- Transformaciones Box-Cox.

son herramientas fundamentales para estabilizar series de tiempo.

Este efecto será vital para proponer modelos más avanzados en las próximas clases.

# Tema 4: Análisis de la Estructura de Dependencia

## ACF, PACF y Test de Blancura

Una vez obtenida una serie estable, o si la serie original ya posee dicha estructura como ocurre con SOI, el siguiente paso es determinar si existe dependencia temporal.

## Ruido blanco

Los ruidos blancos son series que:

- No presentan dependencia temporal.
- Cada dato se genera de forma independiente.
- El pasado no sirve para predecir el futuro.

La definición matemática se verá en clases posteriores.

## Problema de la inspección visual

Observando únicamente la serie no es posible determinar si corresponde a:

- Un ruido blanco.
- Un proceso estructurado con dependencia temporal.

Por ejemplo, un ruido blanco gaussiano simulado con:

- Media = 10
- Varianza = 1

y 600 observaciones puede parecer visualmente similar a SOI o a GEE transformada y diferenciada.

## Función de Autocorrelación

Las herramientas principales son:

### ACF
Función de autocorrelación simple.

### PACF
Función de autocorrelación parcial.

Estas funciones corresponden a estimaciones muestrales de las autocorrelaciones poblacionales.

## Comparación entre ruido blanco y SOI

La figura muestra:

- Primera columna: ACF.
- Segunda columna: PACF.

para:

- Ruido blanco.
- Serie SOI.

Se observa que una serie con dependencia temporal luce completamente distinta a un ruido blanco.

Existen lags estadísticamente distintos de cero tanto en ACF como PACF.

## Serie GEE

Al analizar la serie GEE:

- Diferenciada y transformada.
- Ruido de la descomposición.

se concluye que existe estructura de dependencia significativa.

Por lo tanto, un modelo adecuado debería capturar dicha dependencia.

### Evidencia de estacionalidad

A diferencia de SOI, aparecen lags donde vuelve a aumentar la autocorrelación.

Esto indica que:

- Cada 12 meses.
- Cada año.

la serie presenta patrones repetitivos.

Este efecto es más evidente en la serie diferenciada.

En el ruido de la descomposición es menos visible porque la estacionalidad fue removida previamente.

## Persistencia y memoria

Para la serie original GEE:

- La ACF presenta un decaimiento muy lento.

Esto es típico de series con tendencia.

Cuando hablamos de persistencia:

- La ACF decae lentamente.
- Existe capacidad de predicción a largo plazo.

Por el contrario:

### Series de corta memoria

- La ACF decae rápidamente.
- La capacidad predictiva es limitada.

Las gráficas ACF y PACF serán fundamentales en las próximas clases para identificar modelos estocásticos.

## Test de Box-Pierce

### Comprueba lo aprendido

Finalmente, el test de Box-Pierce ratifica si una serie tiene o no dependencia significativa.

En algunos casos:

- Las correlaciones individuales pueden parecer insignificantes.
- Pero al combinarse resultan significativas.

Este tipo de prueba se conoce como test de blancura porque su hipótesis nula establece que:

> La serie es un ruido blanco.

### Interpretación de resultados

Los p-valores muestran que:

- Solo la serie simulada presenta p-valores mayores a 0.05 para todos los lags.
- En general son mayores a 0.3.

Por lo tanto:

- No se rechaza la hipótesis de ruido blanco.

En todos los demás casos:

- Los p-valores son prácticamente cero.

Por lo tanto:

- Existe fuerte evidencia para rechazar la hipótesis de ruido blanco.

## Importancia práctica

La mayoría de las series reales presentan autocorrelación importante.

Por ello, el test de blancura es especialmente útil para analizar residuos de modelos.

Si se rechaza la hipótesis nula:

- El modelo no capturó toda la dependencia.
- Existen patrones sin modelar.
- Es posible mejorar el modelo.

# Ideas Finales

Hemos llegado al final de la clase.

## Resumen

### Método de Descomposición vs Holt-Winters

- Holt-Winters ajusta tendencia y estacionalidad simultáneamente.
- Se adapta mejor a cambios recientes.
- El método de descomposición separa explícitamente las componentes.
- Esto puede limitar su capacidad predictiva cuando la tendencia cambia.

### Transformaciones y Diferenciación

Muchas series reales, como la generación de energía eléctrica, requieren transformaciones previas para estabilizar:

- Media.
- Varianza.
- Estructura temporal.

Las herramientas más importantes son:

- Descomposición.
- Box-Cox.
- Logaritmo.
- Diferenciación.

### Dependencia Temporal

Antes de proponer modelos complejos es fundamental verificar que exista dependencia temporal significativa.

Solo en ese caso tiene sentido utilizar el pasado para predecir el futuro.
