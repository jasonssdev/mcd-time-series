# Modelos Ingenuos

## Introducción

Modelos ingenuos.

Bienvenidos y bienvenidas.

En esta clase vamos a revisar las metodologías de modelos ingenuos.

Uno de los principales objetivos de los datos medidos secuencialmente en el tiempo es predecir hacia el futuro.

Obviamente, no se restringe solo a esta aplicación, pero esto es lo que veremos en el transcurso de este curso.

Para obtener dichas predicciones, existen dos tipos de metodologías, denominadas modelos ingenuos y procesos estocásticos, respectivamente.

En esta clase nos enfocaremos en el primer tipo de modelos, los cuales se pueden definir como un conjunto de ecuaciones que describen una serie de tiempo de forma heurística.

Desde este punto de vista, el modelo ingenuo se construye solamente usando la intuición.

En otras palabras, no existe un modelo probabilístico para describir el fenómeno.

Algunos de los modelos ingenuos más utilizados son suavizamientos exponenciales y métodos de descomposición.

En esta clase se revisarán los siguientes temas:

1. Suavizamiento exponencial simple
2. Suavizamiento exponencial de Holt
3. Suavizamiento exponencial de Holt-Winters

---

## Tema 1: Suavizamiento Exponencial Simple

Considera una serie de tiempo en que `x_t`, observada desde `t = 1` hasta `n`, y la siguiente notación:

- `x̄_t` representa el nivel medio en el instante `t`.
- `x̂_t(k)` es el predictor del instante `k`, utilizando la información hasta `t`.

En primer lugar, asumamos que la serie no presenta tendencia.

En consecuencia, el nivel medio `x̄_t` es el predictor de `x_t+1`.

El nivel medio está dado por la ecuación que vemos a continuación, la cual es equivalente a decir que el nivel medio es alfa veces el último dato observado, más uno menos alfa, el nivel medio anterior.

Como los pesos que definen el valor medio decaen exponencialmente a 0, este método se denomina **suavizamiento exponencial simple**, el cual da mayor ponderación al pasado reciente, intensificándose cuando alfa tiende a 1 y aportando cada vez más el pasado remoto cuando alfa decrece a 0.

Este promedio ponderado solo está bien definido cuando tenemos un pasado infinito, ya que, en ese caso, la suma de los pesos es 1.

Ahora bien, en la práctica no tenemos una serie de pasado infinito, por lo que se asume la condición inicial de que el nivel medio, cuando `t = 1`, es el primer dato.

Esto permite obtener las siguientes ecuaciones de pronóstico:

- `x̄_1 = x_1`
- `x̂_t(1) = x̄_t`
- `x̂_t(h) = alfa x_t + (1 - alfa) x̂_t(h - 1)`

El valor de alfa se suele elegir como aquel que minimiza el error cuadrático de predicción a un paso, `SSE`.

La ecuación de pronóstico a `h` pasos se utiliza solo cuando `t = n`, ya que en los pasos intermedios se predice a un solo paso.

Claramente, esta ecuación converge a medida que `h` crece al último valor medio calculado `x̄_n`, por lo que se suele considerar:

- `x̂_n(h) = x̄_n`

Esto es equivalente a asumir un modelo de regresión solo con intercepto dependiente del tiempo.

Es decir, para este caso se tiene que:

- `x_t = a_t + error`

Donde `a_t` es el nivel medio de `x`.

Por ejemplo, al aplicar un suavizamiento exponencial simple a la serie de la temperatura global, se obtiene un valor alfa óptimo de `0,52`.

La gráfica muestra el ajuste, un periodo de validación de seis años, de 2010 a 2015, y una predicción a 35 años, de 2016 a 2050.

Se aprecia que las predicciones son constantes, tal como se esperaba, y el error cuadrático medio en los seis años de validación fue de `0,01`, un valor pequeño.

Sin embargo, este modelo no es apropiado para representar la serie, ya que claramente esta presenta tendencia.

Prueba tu aprendizaje respondiendo la siguiente pregunta.

---

## Tema 2: Suavizamiento Exponencial de Holt

Para aquella serie de tiempo que presenta una tendencia lineal, es posible extender la metodología anterior a modelos de regresión, tanto con intercepto y pendiente variables en el tiempo.

Esta metodología se conoce como **suavizamiento exponencial de Holt**.

El modelo se puede expresar como:

- `x_t+h = l_t + m_t h + ε_t+h`

Para estimar este modelo, se asume que la serie se comporta localmente como la suma de un nivel y una tendencia lineal, por lo que se actualizan el nivel y la pendiente mediante un suavizamiento simple de diferentes parámetros.

La ecuación de pronóstico para `h` pasos al futuro, considerando la información de las primeras `t` observaciones, viene dada por:

- `x̂_t(h) = nivel medio de t + pendiente multiplicada por h`

Al igual que en el suavizamiento exponencial simple, para valores de `t` menores a `n` se predice a un solo paso y luego, cuando `t = n`, se predice `h` pasos al futuro.

El resultado es una recta con intercepto y pendiente iguales a las últimas suavizadas.

Con respecto a los parámetros alfa y beta, estos se determinan minimizando el error cuadrático de predicción a un paso.

Por ejemplo, nuevamente se utiliza la serie de la temperatura global, pero esta vez se ajusta a un modelo de Holt considerando los mismos años para el ajuste.

Se obtiene:

- Alfa igual a `0,665`
- Beta igual a `0,091`
- Mismo período de validación de seis años
- Error cuadrático de `0,00749`

El cual es considerablemente menor que en el caso del modelo de suavizamiento exponencial simple.

Notar que la predicción de los 35 años sigue la tendencia lineal esperada.

Prueba tu aprendizaje respondiendo la siguiente pregunta.

---

## Tema 3: Suavizamiento Exponencial de Holt-Winters

Para variaciones con componente periódica, el modelo anterior se extiende incorporando dicha componente de forma aditiva o multiplicativa.

Esta metodología se denomina **Holt-Winters**.

Para el caso multiplicativo, se requiere que los datos sean distintos de 0 para estar bien definidos, pero tiene más sentido si todos son positivos.

Asumiremos que la componente periódica tiene período `p`, es decir:

- `s_t+p = s_t` para todo `t`

En este caso, se suavizará:

- El nivel
- La pendiente
- La componente periódica

Obteniendo para el caso aditivo las ecuaciones de suavizado correspondientes.

Notar que las condiciones iniciales implican perder un período completo al inicio del ajuste.

En la ecuación de predicción aditiva, la componente periódica se suma a la tendencia lineal.

Mientras que para el caso multiplicativo, se obtienen las ecuaciones de suavizado con su respectiva condición inicial.

Al igual que en el caso aditivo, las condiciones iniciales implican perder un período completo al inicio.

En la ecuación de predicción multiplicativa, la componente periódica se multiplica a la tendencia lineal.

Note que cuando se presenta componente periódica, antes de realizar el suavizamiento en el nivel, se debe remover dicha componente.

Así:

- En el caso aditivo, se remueve mediante la diferencia.
- En el caso multiplicativo, se remueve mediante el cociente.

Nuevamente, los parámetros suavizados alfa, beta y gamma se determinan minimizando el error cuadrático de predicción a un paso.

Cabe destacar que, si una serie no presenta tendencia, pero sí componente periódica, se pueden utilizar las ecuaciones anteriores considerando `m_t = 0` para todo `t` y sin incorporar el parámetro theta.

Por ejemplo, al aplicar los modelos anteriores a la base de temperatura global bajo los mismos escenarios que en los casos anteriores, pero asumiendo un período de 25 años, se obtienen los siguientes resultados.

### Caso Aditivo

- Alfa: `0,443`
- Beta: `0,014`
- Gamma: `0,703`
- Error cuadrático medio en el período de evaluación: `0,00751`

Este resultado es levemente peor que el caso Holt.

### Caso Multiplicativo

Al ejecutar el modelo multiplicativo se suma una constante igual a `2`, necesaria para lograr que todos los valores de la serie sean positivos y, al final, se resta el valor de `2` en los valores predichos.

Para este caso:

- Alfa: `0,188`
- Beta: `0,017`
- Gamma: `0,717`
- Error cuadrático medio: `0,01524`

Este fue el peor de todos los modelos, posiblemente influenciado por el valor de la constante `2`.

Cabe destacar que, mientras más grande es esta constante, los resultados del modelo multiplicativo y aditivo se parecen más.

Prueba tu aprendizaje respondiendo la siguiente pregunta.

---

## Conclusiones

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

Los modelos ingenuos permiten describir el patrón de diferentes tipos de series y aprovechan dicha estructura para realizar predicciones hacia el futuro desde una perspectiva heurística.

Los métodos de suavizamiento exponencial de Holt-Winters permiten modelar series con o sin tendencia lineal y con o sin componente periódica.

Para el caso de modelos con componente periódica, se debe decidir si esta ingresa de forma aditiva o multiplicativa al modelo.