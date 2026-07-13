# Modelización de Series de Tiempo — Clase Sincrónica 4 (Parte 2)

# Criterios de selección de modelos

Una vez estimados los parámetros mediante **Máxima Verosimilitud**, surge la siguiente pregunta:

> **¿Cuál modelo es mejor?**

No basta con escoger el modelo que mejor se ajusta a los datos, ya que un modelo con muchos parámetros siempre tenderá a ajustarse mejor.

El objetivo es encontrar un equilibrio entre:

- Calidad del ajuste.
- Complejidad del modelo.

Para ello se utilizan los criterios de información.

---

# AIC (Akaike Information Criterion)

El criterio AIC se construye a partir de la log-verosimilitud penalizada.

La idea es sencilla:

- Mientras mayor sea la cantidad de parámetros, mejor será el ajuste.
- Pero agregar parámetros innecesarios genera sobreajuste (*overfitting*).

Por ello el AIC incorpora una penalización proporcional al número de parámetros.

Su objetivo es encontrar un compromiso entre:

- buen ajuste;
- baja complejidad.

En la práctica:

> **Se prefiere el modelo con el menor AIC.**

---

# BIC (Bayesian Information Criterion)

El BIC utiliza exactamente la misma filosofía que el AIC.

La diferencia es que penaliza mucho más la incorporación de nuevos parámetros.

Esto significa que:

- exige mayor evidencia para justificar un parámetro adicional;
- favorece modelos más simples.

En consecuencia:

- **AIC** privilegia capacidad predictiva.
- **BIC** privilegia parsimonia.

---

# AIC corregido (AICc)

Cuando el tamaño muestral es pequeño, el AIC puede favorecer modelos demasiado complejos.

Para corregir ese efecto existe el **AIC corregido (AICc)**.

En general:

- si el número de observaciones es pequeño (aproximadamente menos de 20–30 observaciones), conviene utilizar **AICc**;
- cuando el tamaño muestral es grande, **AIC** y **AICc** prácticamente coinciden.

---

# Diagnóstico del modelo

Seleccionar un modelo únicamente por AIC o BIC no es suficiente.

Después de seleccionar un modelo siempre debe realizarse un diagnóstico de residuos.

El objetivo es verificar que los residuos se comporten como un **ruido blanco**.

Es decir, que:

- tengan media aproximadamente cero;
- tengan varianza constante;
- no presenten autocorrelación;
- idealmente sigan una distribución normal.

---

# ¿Por qué analizar los residuos?

Cuando el modelo captura correctamente toda la dependencia temporal, los residuos representan únicamente el ruido aleatorio.

Si los residuos siguen mostrando estructura, significa que:

> todavía existe información del pasado que el modelo no logró explicar.

En consecuencia:

> el modelo aún puede mejorarse.

---

# Independencia de los residuos

El supuesto más importante es la independencia.

Esto se verifica observando:

- la ACF de los residuos;
- la PACF de los residuos;
- pruebas estadísticas como **Box-Ljung**.

Si los residuos presentan autocorrelación significativa:

- el modelo no es adecuado;
- aún queda estructura temporal sin modelar.

---

# Normalidad

También se analiza si los residuos siguen una distribución aproximadamente normal.

Las pruebas más utilizadas son:

- Shapiro-Wilk.
- Anderson-Darling.
- Lilliefors.
- Gráfico Q-Q.

Aunque la normalidad es importante, el profesor enfatiza que:

> Es mucho más grave tener residuos autocorrelacionados que residuos no normales.

El principal objetivo del modelo es eliminar toda la dependencia temporal.

---

# Homocedasticidad

Otro supuesto importante es la homocedasticidad.

Esto significa que la varianza de los residuos permanezca constante en el tiempo.

Si existen zonas donde los residuos tienen mucha mayor variabilidad que otras, el supuesto se incumple.

Esto afecta principalmente:

- intervalos de confianza;
- inferencia estadística;
- significancia de parámetros.

---

# Más de un modelo puede ser válido

Es perfectamente posible que varios modelos superen todas las pruebas diagnósticas.

En ese caso la decisión final se toma utilizando:

- AIC;
- BIC;
- capacidad predictiva;
- parsimonia.

No existe una única regla universal.

---

# Modelos ARIMA

Hasta ahora los modelos ARMA sólo podían utilizarse sobre series estacionarias.

Sin embargo, la mayoría de las series reales presentan:

- tendencias;
- cambios de nivel;
- componentes no estacionarias.

Para solucionar este problema aparecen los modelos **ARIMA**.

---

# Idea fundamental de ARIMA

El objetivo consiste en transformar una serie no estacionaria en una serie estacionaria.

La herramienta utilizada es la **diferenciación**.

Se diferencia la serie tantas veces como sea necesario hasta conseguir estacionariedad.

El número mínimo de diferenciaciones necesarias corresponde al parámetro:

**d**

---

## Significado del parámetro d

- **d = 0** → la serie ya es estacionaria.
- **d = 1** → se diferencia una vez.
- **d = 2** → se diferencia dos veces.

Siempre debe escogerse el menor valor posible que logre estacionarizar la serie.

---

# ¿Por qué "Integrated"?

La letra **I** proviene de **Integrated**.

Después de ajustar un modelo ARMA sobre la serie diferenciada, es necesario reconstruir la serie original.

Esa reconstrucción corresponde justamente al proceso inverso de la diferenciación:

> la integración discreta.

Por eso el modelo recibe el nombre de:

**AutoRegressive Integrated Moving Average**

---

# Definición de un modelo ARIMA

Si una serie diferenciada d veces sigue un modelo:

ARMA(p,q)

entonces la serie original sigue un:

ARIMA(p,d,q)

donde:

- **p** representa el orden autorregresivo;
- **d** representa el número de diferenciaciones;
- **q** representa el orden de media móvil.

---

# Predicción en ARIMA

Las predicciones se realizan sobre la serie diferenciada.

Posteriormente se reconstruye la serie original mediante integración.

Es decir:

1. Se predice la serie estacionaria.
2. Se van acumulando esas diferencias.
3. Se obtiene la predicción de la serie original.

Toda la teoría desarrollada para ARMA sigue siendo válida.

---

# Transformaciones adicionales

En ocasiones la diferenciación no es suficiente.

También pueden utilizarse transformaciones como:

- Logaritmo natural.
- Transformación Box-Cox.

Estas transformaciones ayudan principalmente cuando:

- la varianza aumenta con el tiempo;
- la serie presenta crecimiento exponencial;
- existen efectos multiplicativos.

---

# Transformación Box-Cox

La transformación Box-Cox busca estabilizar la varianza.

Dependiendo del parámetro λ:

- λ = 1 → prácticamente no transforma.
- λ = 0 → equivale al logaritmo natural.
- λ = 0.5 → raíz cuadrada.
- λ = 2 → potencia cuadrática.

Cuando λ es cercano a cero suele preferirse utilizar directamente el logaritmo natural por su facilidad de interpretación.

---

# Modelos SARIMA

Los modelos SARIMA extienden ARIMA incorporando una componente estacional.

Además de los parámetros:

- p
- d
- q

se agregan:

- P
- D
- Q

junto con el período estacional **S**.

---

# Diferenciación estacional

La diferenciación estacional compara una observación con otra separada exactamente S períodos.

Por ejemplo:

Si:

- S = 12

y la serie es mensual,

entonces cada observación se compara con el mismo mes del año anterior.

Ejemplos:

- enero con enero;
- febrero con febrero;
- marzo con marzo.

Esto permite eliminar componentes estacionales.

---

# Parámetros de SARIMA

Un modelo SARIMA queda definido mediante:

- (p,d,q)

para la parte no estacional,

y

- (P,D,Q)<sub>S</sub>

para la parte estacional.

En total existen dos conjuntos de parámetros que deben identificarse.

---

# Identificación del modelo

El procedimiento sigue siendo exactamente el mismo utilizado para ARMA.

Se analizan:

- Serie temporal.
- ACF.
- PACF.

Pero ahora también deben analizarse las componentes estacionales observando los lags múltiplos del período S.

Por ello identificar un SARIMA suele ser considerablemente más complejo que identificar un ARMA.

---

# Metodología de Box-Jenkins

Toda la construcción de modelos ARMA, ARIMA y SARIMA puede resumirse mediante la metodología de **Box-Jenkins**.

Las etapas son:

1. Graficar la serie.
2. Aplicar transformaciones si son necesarias.
3. Identificar posibles modelos mediante ACF y PACF.
4. Estimar parámetros.
5. Seleccionar candidatos utilizando AIC, BIC u otros criterios.
6. Analizar los residuos.
7. Si los residuos no son ruido blanco, volver a la etapa de identificación.
8. Si los residuos son adecuados, aceptar el modelo.

Este proceso es iterativo.

No siempre el primer modelo propuesto será el correcto.

En muchas ocasiones será necesario probar varios modelos hasta encontrar uno que satisfaga todos los supuestos.

La idea central de la metodología de Box-Jenkins es:

> **Buscar un modelo suficientemente bueno cuyos residuos se comporten como un ruido blanco.**

Una vez logrado esto, el modelo puede utilizarse con confianza para realizar predicciones e inferencias.
