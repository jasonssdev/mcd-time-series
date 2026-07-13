# Modelización de Series de Tiempo — Clase Sincrónica 4 (Parte 1)

## Introducción

Hola, ¿me entienden? ¿Me escuchan?

Bien, vamos a dar comienzo a la cuarta clase sincrónica del curso de Series de Tiempo.

En esta clase vamos a discutir los aspectos más relevantes de las últimas dos semanas, que corresponden principalmente a:

- Estimación y selección de modelos **ARMA**.
- Extensión hacia los modelos **ARIMA** y **SARIMA**, que permiten modelar series no estacionarias, las cuales son las más comunes en aplicaciones reales.
- Resumen de la metodología completa de modelización conocida como **Box-Jenkins**.
- Revisión del caso de estudio trabajado en clases anteriores:
  - **SOI (Southern Oscillation Index)**.
  - **GE (Generación de Energía Eléctrica)**.

La serie SOI fue escogida porque presenta un comportamiento aproximadamente estacionario y puede modelarse mediante ARMA.

La serie GE, en cambio, presenta comportamiento no estacionario y estacional, por lo que requiere un modelo SARIMA.

Entre medio del desarrollo dejaremos espacio para consultas relacionadas tanto con la materia como con las evaluaciones del curso.

---

# Estimación de parámetros

En términos generales, la estimación depende de la estructura del modelo.

## Modelo AR(p)

En un modelo AR(p) debemos estimar:

- Los **p parámetros autorregresivos**.
- La **varianza del ruido**, denotada por:

  $begin:math:display$
  \\sigma\^2
  $end:math:display$

Si además el proceso no está centrado en cero, también debemos estimar la media del proceso.

Por lo tanto, normalmente terminamos estimando:

- p parámetros AR.
- La varianza.
- La media.

---

## Método de Yule-Walker

Estos parámetros pueden estimarse mediante las ecuaciones de **Yule-Walker**, que corresponden a un método de momentos.

La idea consiste en igualar:

- Momentos poblacionales.
- Momentos muestrales.

En este contexto, los momentos poblacionales se representan mediante las autocorrelaciones.

Por eso la función de autocorrelación es tan importante.

Recordemos también una representación fundamental vista anteriormente.

Todo el proceso puede escribirse como una suma infinita de errores ponderados.

Lo importante de esa representación no es solamente su elegancia matemática, sino que permite obtener directamente la función de autocovarianza.

Y justamente esa función es la base para estimar los parámetros del modelo.

---

A partir de ello:

- Se estiman las autocorrelaciones muestrales.
- La varianza del ruido.
- La media mediante el promedio muestral.

En clases anteriores resolvimos explícitamente las ecuaciones de Yule-Walker para modelos pequeños (como un AR(2)), donde el sistema resulta relativamente sencillo.

Sin embargo, cuando el orden aumenta, aparece un sistema matricial cuya resolución requiere invertir matrices de dimensión **p**.

---

# Limitaciones del método de Yule-Walker

El problema aparece cuando incorporamos una componente de media móvil.

Por ejemplo:

- Modelos MA.
- Modelos ARMA.

En estos casos las ecuaciones dejan de ser lineales.

El sistema pasa a ser:

- No lineal.
- Difícil de resolver.
- Poco práctico.

Por ello, aunque el método de momentos es útil conceptualmente, en la práctica rara vez se utiliza para modelos con componente MA.

---

# Máxima Verosimilitud

En la práctica, el método más utilizado es la **Máxima Verosimilitud**.

Este método estima simultáneamente:

- La media del proceso.
- Los parámetros AR.
- Los parámetros MA.
- La varianza del ruido.

Si existen:

- **p** parámetros AR.
- **q** parámetros MA.

Entonces terminamos estimando:

- p + q parámetros estructurales.
- La media.
- La varianza.

En total:

$begin:math:display$
p\+q\+2
$end:math:display$

parámetros.

---

## Función de verosimilitud

La verosimilitud corresponde a la densidad conjunta de todas las observaciones.

Dicha densidad puede escribirse mediante probabilidades condicionales.

Es decir:

- El último dato condicionado a todos los anteriores.
- Luego el penúltimo condicionado al pasado.
- Y así sucesivamente.

Asumiendo normalidad en el ruido, cada distribución condicional es una Normal cuya:

- Media depende del modelo.
- Varianza depende de los coeficientes del proceso.

En consecuencia, obtenemos una función de verosimilitud relativamente compleja.

---

## ¿Cómo se maximiza?

Resolver la verosimilitud "a mano" prácticamente nunca ocurre.

Lo habitual es utilizar algoritmos numéricos.

La idea consiste en encontrar el punto donde la función alcanza su máximo.

En lugar de maximizar directamente la verosimilitud, normalmente se maximiza el **logaritmo de la verosimilitud**.

Esto tiene dos ventajas:

- Transforma productos en sumas.
- Mantiene exactamente el mismo punto máximo.

Así, el problema se convierte en encontrar el punto donde el gradiente es igual a cero.

Posteriormente ese sistema se resuelve mediante métodos numéricos.

---

## Dependencia del algoritmo

Como el problema es numérico:

- Depende del algoritmo utilizado.
- Depende de los valores iniciales.

Por ello distintos softwares pueden entregar parámetros ligeramente distintos.

Eso es completamente normal.

---

# Mínimos Cuadrados

Además de máxima verosimilitud existen:

- Mínimos cuadrados condicionales.
- Mínimos cuadrados incondicionales.

Cuando el supuesto de normalidad se cumple:

**Máxima Verosimilitud y Mínimos Cuadrados producen prácticamente los mismos resultados.**

La diferencia principal aparece en la estimación de la varianza.

Cuando los datos no siguen una distribución normal:

- Máxima Verosimilitud continúa siendo válida, cambiando únicamente la distribución asumida.
- Mínimos Cuadrados sigue utilizando exactamente la misma formulación.

---

# ¿Por qué se utiliza Máxima Verosimilitud?

Principalmente porque posee excelentes propiedades estadísticas.

Sabemos que:

- La varianza estimada converge hacia la verdadera varianza.
- Los parámetros convergen hacia su verdadero valor.

Además, los estimadores poseen distribución asintótica normal.

Esto permite realizar pruebas de hipótesis para cada parámetro del modelo y evaluar si conviene o no mantenerlo.

Estas propiedades hacen que Máxima Verosimilitud sea el método estándar para estimar modelos ARMA, ARIMA y SARIMA.
