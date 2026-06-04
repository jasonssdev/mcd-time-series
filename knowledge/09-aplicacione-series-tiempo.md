# Aplicaciones de Modelos de Series de Tiempo

## Introducción

Bienvenidos y bienvenidas.

Al comienzo del curso mencionamos varios casos donde aparecen de forma natural datos medidos en el tiempo y la importancia de conservar la estructura temporal para su análisis.

En esta clase concretaremos los contenidos conceptuales de las clases previas en dos ejemplos específicos:

- Generación de Energía Eléctrica (GEE).
- Índice de Oscilación Sur (SOI, por sus siglas en inglés).

Desarrollaremos estos dos ejemplos en detalle a medida que avanza el curso, con el objetivo de resolver un par de problemas reales de predicción.

En esta clase se revisarán los siguientes temas:

1. Contextualización de los datos.
2. Ajuste de la serie SOI.
3. Ajuste de la serie GEE.

---

# Tema 1: Contextualización de los datos

## Serie de Generación de Energía Eléctrica (GEE)

La serie **Generación de Energía Eléctrica (GEE)** corresponde a la medición mensual de la generación real de las centrales generadoras del Sistema Eléctrico Nacional.

Esta serie se encuentra disponible en la página del Banco Central y se puede acceder directamente a ella a través del enlace correspondiente.

Utilizaremos toda la información disponible a la fecha de generación del material, la cual va desde enero de 1999 hasta enero de 2026.

Cuando ingresen a la página visualizarán un gráfico del cual podemos apreciar rápidamente que la generación de energía eléctrica total va al alza de forma sostenida.

Solo a modo de recuerdo, si bien un modelo lineal inicial es factible para este tipo de comportamiento utilizando como variable regresora el tiempo, no es lo más adecuado, ya que los residuos suelen quedar correlacionados, lo que significa que aún hay información importante que no ha sido utilizada en el modelo.

Cabe destacar que estamos trabajando con datos reales del sistema eléctrico chileno, con frecuencia mensual, lo que nos permite aplicar modelos de series de tiempo de forma directa.

En sistemas eléctricos, la generación debe ajustarse continuamente a la demanda, por lo que ambas magnitudes son muy cercanas.

Por ello utilizaremos esta serie como un **proxy de la demanda agregada** para efectos de interpretación.

---

## Horizonte de predicción para la serie GEE

En todo estudio de series de tiempo se debe tener presente el horizonte de predicción, el cual por lo general corresponde a estrategias de inversión para satisfacer la demanda sin incurrir en pérdidas innecesarias.

Para efectos de este caso de estudio, supongamos que el objetivo es predecir la generación eléctrica mensual en Chile para los próximos **12 meses**.

Este horizonte permite evaluar si el modelo captura adecuadamente la dinámica anual de la serie, sin exigirle una precisión irrealista a largo plazo.

Esto es razonable porque la serie presenta:

- Una estructura de largo plazo claramente persistente.
- Un patrón anual visible.

### ¿Por qué es importante fijar el horizonte de predicción?

La importancia radica en que, al momento de comparar modelos de distintas naturalezas, como modelos ingenuos y modelos probabilísticos, no existe una única forma estándar para realizar dicha comparación.

Por ejemplo, no es posible aplicar la evaluación cruzada tradicional utilizada en Machine Learning, porque realizar una separación aleatoria de los datos no respeta la estructura temporal de la serie.

En este contexto utilizaremos una forma de evaluación cruzada adaptada a datos temporales.

Esta consiste en separar la serie en:

- Conjunto de entrenamiento (*train*).
- Conjunto de pruebas (*test*).

Utilizando los últimos datos disponibles para evaluar la capacidad predictiva de los modelos.

Si bien no es la única versión de evaluación cruzada, es muy simple de implementar y fácil de comprender.

Volviendo a la aplicación de la serie GEE, realizaremos el ajuste de la serie sin considerar los 12 meses más recientes.

A partir de esto podremos comparar modelos de diferente naturaleza en términos de error de predicción.

La figura adjunta muestra esta separación, dejando en rojo el conjunto de prueba, donde se aprecia un ciclo completo de la generación eléctrica.

---

## Serie Índice de Oscilación Sur (SOI)

El otro ejemplo de análisis es la serie de **Índice de Oscilación Sur (SOI)**.

Este es un indicador climático utilizado para monitorear la variabilidad atmosférica en el océano Pacífico Tropical.

Se construye a partir de la diferencia de presión atmosférica a nivel del mar entre las estaciones meteorológicas de:

- Tahiti, Polinesia Francesa.
- Darwin, Australia.

El índice SOI es uno de los principales indicadores del fenómeno **El Niño**, el cual tiene impactos relevantes en el clima a nivel mundial, incluyendo:

- Precipitaciones.
- Temperaturas.
- Eventos extremos.

Estos datos son recopilados de forma sistemática por organismos meteorológicos internacionales y forman parte del monitoreo del sistema climático global.

Se encuentran disponibles en varios softwares a través de librerías específicas, con el formato apropiado para aplicar técnicas de series de tiempo.

Sin embargo, para obtener una versión actualizada a la fecha de hoy, se puede ingresar a la página de NOAA o al enlace correspondiente.

Para los ejemplos de esta clase utilizaremos todos los datos disponibles a la fecha, que van desde enero de 1951 hasta febrero de 2026.

La serie luce de forma tal que se aprecia centrada en torno a cero, con una variación aproximada entre:

$$
-4 \leq SOI \leq 4
$$

Con algunos puntos extremos en valores negativos.

---

## Características de la serie SOI

La característica principal de esta serie es que **no presenta tendencia**, lo cual representa un caso totalmente diferente al caso anterior de la serie GEE.

Estas series sin tendencia y con variabilidad prácticamente constante son complejas de predecir con técnicas clásicas, como una regresión lineal contra el tiempo.

Esto ocurre porque, en general:

- La variable tiempo no resulta significativa.
- El modelo termina reduciéndose a una constante.
- Todas las predicciones corresponden prácticamente al promedio.

Las técnicas de series de tiempo permiten predecir estas series, pero no puede hacerse a muy largo plazo como en el caso de GEE.

Si el horizonte de predicción es muy extenso, el predictor tiende a estabilizarse en un valor prácticamente constante, perdiendo la capacidad de reflejar la variabilidad de la serie.

Por ello, debemos ser especialmente cuidadosos al comparar modelos mediante validación cruzada.

---

## Horizonte de predicción para la serie SOI

Consideraremos un horizonte de predicción de corto plazo.

Mostraremos solamente los dos últimos instantes de la serie como conjunto de prueba:

- Enero de 2026.
- Febrero de 2026.

Esta elección es coherente con la naturaleza de la serie, ya que en este tipo de datos la capacidad predictiva se concentra en pocos pasos hacia adelante.

La figura correspondiente muestra esta división utilizando un zoom desde el año 2010 en adelante.

Los datos de prueba aparecen destacados en rojo.

---

## Series estacionarias y no estacionarias

Las dos series estudiadas presentan estructuras diferentes.

Conceptualmente, se denominan:

### Serie estacionaria

Como el caso del SOI.

### Serie no estacionaria

Como el caso de la GEE.

Aunque el concepto de estacionariedad se estudiará en detalle más adelante, es importante saber diferenciar visualmente si una serie podría o no ser estacionaria.

Esto limita los modelos posibles, tanto ingenuos como probabilísticos.

---

# Tema 2: Ajuste de la serie SOI

Comenzaremos con la serie SOI porque presenta una estructura estacionaria.

Para este tipo de serie, el modelo adecuado dentro de la familia de suavizamientos exponenciales es el:

## Suavizamiento Exponencial Simple

Recordemos que este modelo posee un único parámetro de ajuste:

$$
\alpha
$$

Este parámetro controla la compensación entre pasado y presente.

### Interpretación de α

- Si α es cercano a 1, importa principalmente el pasado reciente.
- Si α es cercano a 0, importa más el pasado remoto.

Para determinar α se realiza una validación cruzada a un paso.

A medida que llegan nuevos datos, estos se comparan con el valor predicho utilizando la pérdida cuadrática.

Naturalmente, α no puede estimarse manualmente, por lo que utilizamos software especializado.

Utilizando Python o R se obtiene:

$$
\alpha \approx 0.47
$$

Esto indica que el predictor entrega:

- 47% de peso al dato inmediatamente anterior.
- 53% al resto de la historia.

---

## Resultados del ajuste

La tabla muestra los primeros y últimos valores ajustados.

El primer valor se pierde porque la estructura del modelo solamente permite estimar desde la observación siguiente.

Con respecto a la predicción de enero y febrero de 2026:

$$
\hat{X}=0.77
$$

Lo que implica un error considerable.

Sin embargo, si hubiésemos utilizado el promedio como predictor:

$$
\bar{X}=0.253
$$

El error habría sido aún mayor.

La gráfica muestra:

- Serie entrenamiento (negro).
- Serie ajustada (azul).
- Serie test (rojo).
- Predicción (verde).

Además, una línea vertical segmentada separa entrenamiento y prueba.

Visualmente se observa que:

- El predictor se aleja de los valores reales.
- Permanece dentro de rangos razonables.
- La serie ajustada sigue la serie original con cierto desfase.

Este efecto se debe a que α es relativamente elevado.

---

## Comparación con Holt-Winters

Como contraste, podríamos intentar ajustar un modelo Holt-Winters sin tendencia.

Es decir:

- Nivel constante.
- Componente estacional.
- Periodicidad 12.

Sin embargo, este modelo no resulta apropiado para esta serie.

La comparación mediante Error Cuadrático Medio (MSE) muestra que el suavizamiento exponencial simple obtiene mejores resultados.

Además, el error de ajuste resulta levemente menor que el error de predicción, lo que indica que las predicciones se encuentran dentro de lo esperado para este modelo.

---

# Tema 3: Ajuste de la serie GEE

Para ajustar la serie GEE debemos volver a observar la serie y verificar si existe una componente periódica además de la tendencia.

Observando la gráfica, se aprecia claramente un patrón estacional.

Los puntos altos y bajos tienden a repetirse cada año.

Además, la amplitud de estas variaciones aumenta con el tiempo.

Por ejemplo, si comparamos:

- Año 2000.
- Año 2020.

La amplitud es considerablemente mayor en el segundo caso.

Este aumento de amplitud es una señal de una relación multiplicativa entre:

- Tendencia.
- Componente estacional.

Por lo tanto, existe evidencia para proponer un modelo:

## Holt-Winters Multiplicativo

Este modelo puede proponerse porque:

- La serie es positiva.
- Existe estacionalidad.
- La amplitud aumenta con el tiempo.

---

## Período estacional

El período se fija inicialmente en:

$$
P = 12
$$

Meses.

Más adelante veremos técnicas para estimar el período de manera sistemática.

---

## Parámetros del modelo

El modelo Holt-Winters Multiplicativo requiere estimar tres parámetros:

- α (nivel).
- β (tendencia).
- γ (estacionalidad).

Estos parámetros se estiman minimizando el error cuadrático de predicción a un paso.

Dado que:

$$
P = 12
$$

Los primeros 12 valores se utilizan como condiciones iniciales y no pueden ajustarse.

---

## Resultados

Las tablas muestran:

- Valores ajustados.
- Errores de ajuste.
- Predicciones.
- Errores de predicción.

Los errores de predicción son del mismo orden que los errores de ajuste.

La gráfica muestra:

- Entrenamiento (negro).
- Ajuste (azul).
- Test (rojo).
- Predicción (verde).

La línea vertical segmentada marca la separación entre entrenamiento y prueba.

Se observa que:

- El modelo se ajusta muy bien.
- Las predicciones siguen adecuadamente la estructura real.

---

## Comparación con Holt-Winters Aditivo

Un modelo alternativo sería Holt-Winters Aditivo.

Este modelo supone amplitud constante.

Sin embargo, visualmente este supuesto parece poco razonable.

Al revisar los resultados, se confirma que el modelo multiplicativo obtiene errores menores tanto en ajuste como en predicción.

Particularmente, la mejora es más evidente en el conjunto de prueba.

También es posible ajustar esta serie utilizando métodos de descomposición, los cuales serán estudiados en la próxima clase.

---

# Resumen

En la práctica, el punto de partida en el análisis de series de tiempo no es el modelo, sino la comprensión de la estructura de los datos.

En particular, debemos identificar:

- Tendencias.
- Estacionalidad.
- Patrones repetitivos.

Series con estructuras diferentes requieren estrategias de modelamiento distintas.

Mientras algunas series permiten predicciones principalmente a corto plazo, otras presentan patrones más persistentes que permiten trabajar con horizontes de predicción más amplios.

La elección del horizonte de predicción y del conjunto de prueba no es arbitraria.

Debe ser coherente con:

- La estructura de la serie.
- El uso que tendrá el modelo.
- El número de períodos que se desea anticipar.
- La capacidad real del modelo para predecir dicho horizonte.