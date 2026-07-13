# Inferencia estadística en modelos ARMA

Bienvenidos y bienvenidas a este nuevo podcast, donde vamos a hablar principalmente de la inferencia estadística relacionada con los modelos ARMA.

Ya sabemos, por todo lo que hemos visto hasta ahora, que los modelos ARMA son buenos modelos que nos permiten realizar análisis de series temporales. También sabemos que estos modelos nos ayudan a capturar y entender patrones complejos en los datos que varían en el tiempo.

Pero aquí surge una pregunta importante:

> ¿Cómo sabemos si los patrones que identificamos son realmente significativos o son simplemente producto del azar?

Es aquí donde la inferencia estadística nos proporciona un marco para evaluar la robustez de nuestras predicciones y entender la fiabilidad de los coeficientes de nuestro modelo.

Cuando ajustamos un modelo ARMA, obtenemos una serie de estimaciones para cada uno de nuestros coeficientes. Para cada una de estas estimaciones tenemos asociado un valor p.

Estos valores p son nuestra primera parada en este viaje por la inferencia estadística, ya que nos indican la probabilidad de que un coeficiente específico sea significativamente diferente de cero.

Un valor p bajo sugiere que el efecto observado no es aleatorio y que el coeficiente tiene un impacto real en la serie temporal.

Pero ¿qué sucede cuando encontramos coeficientes con valores p altos?

¿Significa que deberíamos descartar estos coeficientes de nuestro modelo?

La respuesta es: no necesariamente.

Es aquí donde tenemos que ser muy cautelosos. Podría ser tentador simplificar el modelo eliminando estos términos, pero debemos detenernos antes de hacerlo.

Cada coeficiente del modelo ARMA, incluso aquellos que no son estadísticamente significativos, puede estar capturando una parte de la variabilidad de los datos que no es inmediatamente obvia.

Al eliminar estos términos, podríamos estar perdiendo información valiosa que afecta el comportamiento general del modelo.

La clave para interpretar correctamente estos modelos es comprender que la significancia estadística de un término no siempre es sinónimo de su relevancia práctica.

Un término no significativo puede actuar como un ajuste fino para los demás términos que sí son significativos. De esta manera, ayuda a capturar la complejidad subyacente de los datos.

En lugar de centrarnos únicamente en la significancia estadística, debemos adoptar un enfoque más holístico.

Esto implica considerar cómo el modelo, en su conjunto, se ajusta a los datos y cómo cada componente, ya sea significativo o no, contribuye al modelo.

Debemos preguntarnos:

- ¿Mejora el modelo general si se eliminan estos términos?
- ¿Este modelo tiene un criterio de Akaike alto o bajo?
- ¿Cómo cambia el diagnóstico del modelo?

Es decir, debemos evaluar otras pruebas, como, por ejemplo, el test de Ljung-Box.

Ya sabemos que esta prueba nos ayuda a determinar si existe autocorrelación en los residuos de nuestros modelos.

Si los residuos muestran una autocorrelación significativa, significa que nuestro modelo podría estar omitiendo información importante.

Es crucial que un modelo ARMA capture adecuadamente la autocorrelación de los datos para que sea efectivo.

Otra prueba que también podríamos verificar es la prueba de Jarque-Bera. Esta prueba nos ayuda a comprobar la normalidad de los residuos.

En la inferencia estadística, a menudo asumimos que los residuos de nuestro modelo siguen una distribución normal. Es aquí donde esta prueba nos indica si dicha suposición se mantiene o no.

La normalidad de los residuos es importante porque muchos de los métodos estadísticos que utilizamos se basan en esta suposición.

Otra prueba importante está relacionada con la heterocedasticidad.

Esta prueba nos ayuda a verificar si la varianza de los residuos cambia o no con el tiempo.

En un modelo ideal, queremos que la varianza de los residuos sea constante.

¿Por qué?

Porque, si esta cambia, podría indicar que nuestro modelo no está capturando toda la dinámica de los datos.

Por lo tanto, debemos llevar nuestra reflexión a considerar el modelo desde una perspectiva más amplia. De esta manera, podremos tomar decisiones mucho más informadas.

Espero que este podcast haya sido de su agrado y nos vemos en una próxima oportunidad.
