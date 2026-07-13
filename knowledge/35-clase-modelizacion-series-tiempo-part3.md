# Modelización de Series de Tiempo — Clase Sincrónica 4 (Parte 3)

# Caso de estudio 1: Índice de Oscilación del Sur (SOI)

Para finalizar la modelización de los modelos ARMA, se analiza la serie **SOI (Southern Oscillation Index)**.

El objetivo es:

- ajustar distintos modelos ARMA;
- comparar sus parámetros;
- evaluar su capacidad predictiva;
- seleccionar el mejor modelo utilizando criterios estadísticos y análisis de residuos.

---

# Estimación mediante Máxima Verosimilitud

En clases anteriores se estimaron algunos modelos utilizando el método de los momentos (Yule-Walker).

Ahora se realiza la misma estimación utilizando **Máxima Verosimilitud**.

Los modelos evaluados inicialmente son:

- AR(2)
- ARMA(1,1)

Se comparan:

- parámetros estimados;
- varianza del error;
- capacidad predictiva.

El resultado muestra que:

- ambos métodos entregan parámetros muy similares;
- las diferencias aparecen principalmente en la estimación de la varianza.

Cuando existe componente de media móvil, Máxima Verosimilitud suele producir mejores estimaciones que Yule-Walker.

---

# Propuesta de nuevos modelos

La selección de modelos comienza observando:

- la ACF;
- la PACF.

A partir de estas gráficas se proponen varios modelos candidatos, entre ellos:

- AR(3)
- AR(4)
- ARMA(2,1)
- ARMA(2,2)
- ARMA(3,1)
- ARMA(3,2)
- ARMA(3,3)

Todos son ajustados posteriormente mediante Máxima Verosimilitud.

---

# Comparación mediante AIC y BIC

Una vez ajustados los modelos, se comparan utilizando:

- AIC;
- BIC;
- AIC corregido;
- RMSE de ajuste;
- RMSE de predicción.

Se observa que:

- distintos criterios pueden seleccionar modelos distintos;
- un modelo puede tener mejor AIC pero peor capacidad predictiva;
- otro puede predecir ligeramente mejor pero utilizar más parámetros.

Por ello ningún criterio debe utilizarse de manera aislada.

---

# Significancia de los parámetros

Posteriormente se revisa el resumen estadístico de cada modelo.

Para cada parámetro se observa:

- estimación;
- error estándar;
- estadístico Z;
- p-valor.

El objetivo es verificar que todos los parámetros sean estadísticamente significativos.

Cuando un parámetro posee un p-valor alto:

- puede considerarse cercano a cero;
- probablemente no aporta información relevante;
- podría eliminarse para simplificar el modelo.

---

# Diagnóstico de residuos

Una vez seleccionado un modelo candidato, se analizan sus residuos.

Se revisan:

- ACF de residuos;
- PACF de residuos;
- prueba de Box-Ljung;
- normalidad;
- simetría;
- curtosis.

El profesor enfatiza nuevamente que:

> El supuesto más importante es que los residuos no presenten autocorrelación.

Si todavía existe autocorrelación, significa que el modelo no capturó completamente la dependencia temporal.

---

# Comparación de modelos

Tras el diagnóstico, varios modelos cumplen adecuadamente los supuestos.

Por ejemplo:

- AR(3)
- ARMA(2,2)

Ambos presentan residuos compatibles con un ruido blanco.

En este escenario, la decisión final se toma utilizando:

- AIC;
- BIC;
- parsimonia;
- capacidad predictiva.

---

# Comparación entre ACF teórica y muestral

El profesor muestra además una comparación poco habitual entre:

- ACF observada;
- ACF teórica del modelo.

La idea es verificar que el modelo reproduzca correctamente el patrón de dependencia observado en los datos.

No se espera que ambas curvas coincidan exactamente.

Lo importante es que reproduzcan la misma estructura general.

---

# Predicciones

Finalmente se realizan predicciones futuras.

Se observa que:

- el intervalo de confianza aumenta conforme crece el horizonte de predicción;
- las predicciones de modelos ARMA tienden gradualmente hacia la media del proceso.

Por esta razón los modelos ARMA funcionan especialmente bien para:

- predicciones de corto plazo.

---

# Comparación con Suavizamiento Exponencial

También se compara el modelo ARMA con un modelo de **Suavizamiento Exponencial Simple**.

Aunque este último presenta un error de predicción relativamente bajo para los datos utilizados, su comportamiento futuro es poco realista.

El suavizamiento exponencial tiende a mantener constante el último nivel observado.

En cambio, el modelo ARMA reproduce mejor la estructura temporal del proceso.

---

# Caso de estudio 2: Generación de Energía Eléctrica (GE)

A continuación se analiza una serie claramente no estacionaria.

Visualmente se observan:

- tendencia;
- aumento progresivo de la varianza;
- estacionalidad.

Por ello se requiere un modelo SARIMA.

---

# Transformación logarítmica

El primer paso consiste en aplicar el logaritmo natural.

El objetivo es estabilizar la varianza.

Después del logaritmo, las oscilaciones presentan una amplitud mucho más constante.

---

# Diferenciación

Posteriormente se aplica una diferenciación de primer orden.

Ahora:

- la media se mantiene aproximadamente constante;
- la serie parece estacionaria.

Para verificarlo se aplica el test **ADF (Augmented Dickey-Fuller)**.

El resultado indica que:

- la serie original no es estacionaria;
- la serie diferenciada sí lo es.

Por ello:

- d = 1.

---

# Identificación mediante ACF y PACF

Se analizan las funciones:

- ACF;
- PACF.

Ahora aparecen claramente picos repetidos cada 12 rezagos.

Esto confirma la existencia de una componente estacional anual.

Por ello se propone:

- D = 1;
- S = 12.

---

# Propuesta de modelos SARIMA

A partir del análisis de ACF y PACF se generan distintos modelos candidatos.

Se prueban diferentes combinaciones de:

- p;
- d;
- q;
- P;
- D;
- Q.

Todos ellos se ajustan mediante Máxima Verosimilitud.

---

# Problema de las condiciones iniciales

El profesor destaca un detalle importante de la implementación en Python.

Cuando existe diferenciación:

- se pierden observaciones iniciales.

Por ejemplo:

Si existe una componente estacional de período 12,

entonces deben descartarse aproximadamente los primeros 13 registros.

Si estos datos no se eliminan correctamente:

- el RMSE;
- el AIC;
- y otras métricas

pueden quedar completamente distorsionadas.

Por ello se implementa una función auxiliar para eliminar correctamente esas observaciones.

---

# Comparación de modelos

Después del ajuste se comparan todos los modelos utilizando:

- AIC;
- BIC;
- RMSE de ajuste;
- RMSE de predicción.

El profesor recuerda que:

Los modelos ajustados sobre distintas escalas (por ejemplo, serie original vs. logaritmo) **no pueden compararse mediante AIC o BIC**.

En esos casos únicamente tiene sentido comparar:

- errores de predicción.

---

# Sobreparametrización

Algunos modelos presentan demasiados parámetros.

Esto produce:

- parámetros no significativos;
- errores estándar elevados;
- pérdida de interpretabilidad.

Aunque estos modelos pueden presentar un excelente ajuste, no necesariamente son los mejores.

Siempre debe privilegiarse un modelo:

- simple;
- significativo;
- con residuos adecuados.

---

# Análisis de raíces

También se analizan las raíces del modelo.

Si algunas raíces autorregresivas y de media móvil son muy similares, puede existir sobreparametrización.

En ese caso conviene eliminar algunos parámetros.

---

# Diagnóstico final

Los modelos seleccionados vuelven a someterse al análisis de residuos.

Se revisan nuevamente:

- independencia;
- normalidad;
- homocedasticidad.

Solo aquellos modelos cuyos residuos se comportan como un ruido blanco pueden considerarse apropiados.

---

# Predicciones finales

Con el modelo definitivo se generan las predicciones futuras.

Se observa que:

- las predicciones siguen correctamente la estacionalidad;
- los intervalos de confianza aumentan conforme crece el horizonte de predicción.

Esto es completamente esperable desde el punto de vista teórico.

---

# Preguntas de los estudiantes

## ¿Qué ocurre si Dickey-Fuller recomienda dos diferenciaciones pero visualmente una parece suficiente?

El profesor responde que esto puede ocurrir cuando la serie presenta **larga memoria**.

En esos casos:

- una diferenciación puede dejar la serie casi estacionaria;
- dos diferenciaciones pueden eliminar demasiada estructura.

Existen modelos más avanzados llamados **ARFIMA (ARIMA fraccional)** que permiten utilizar órdenes de diferenciación fraccionarios.

---

## ¿Qué pasa si el modelo no cumple normalidad pero sí independencia?

El profesor indica que esto es relativamente frecuente.

Lo verdaderamente importante es que los residuos sean independientes.

La falta de normalidad puede abordarse utilizando otras distribuciones distintas de la Normal, por ejemplo la distribución t de Student.

---

## ¿Cómo detectar un cambio estructural?

Si una intervención modifica el nivel de una serie temporal, los residuos suelen mostrar un patrón sistemático:

- inicialmente negativos;
- posteriormente positivos (o viceversa).

Esto indica la existencia de un cambio estructural.

Existen modelos específicos para este tipo de situaciones, como los **Modelos Autorregresivos con Umbral (TAR)**.

---

## ¿Qué ocurre si los residuos son heterocedásticos?

La heterocedasticidad afecta principalmente:

- los errores estándar;
- la inferencia estadística;
- los intervalos de confianza.

Generalmente no modifica significativamente la predicción puntual del modelo.

---

## ¿Cómo funcionan los modelos SARIMAX?

Los modelos SARIMAX incorporan variables exógenas.

Estas variables pueden mejorar considerablemente el ajuste.

Sin embargo, presentan un inconveniente importante:

> Para realizar predicciones futuras también es necesario conocer los valores futuros de las variables exógenas.

Por ello, cuando varias variables evolucionan conjuntamente, suele ser más conveniente utilizar modelos multivariados, como los **Modelos Autorregresivos Vectoriales (VAR)**, donde todas las series se predicen simultáneamente.

---

# Conclusiones

El profesor cierra la clase destacando las ideas principales:

- La metodología **Box-Jenkins** constituye el procedimiento estándar para construir modelos ARMA, ARIMA y SARIMA.
- La selección del modelo nunca debe basarse únicamente en el AIC o el BIC.
- Siempre debe verificarse que los residuos se comporten como un ruido blanco.
- Un modelo con más parámetros no necesariamente es un mejor modelo.
- La interpretación correcta de la ACF y la PACF sigue siendo la herramienta más importante para proponer modelos adecuados.