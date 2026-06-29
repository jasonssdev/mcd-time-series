# Validación cruzada y bandas de predicción

Bienvenidos y bienvenidas a este podcast sobre series temporales.

En este podcast, hoy día vamos a profundizar en temas de las complejidades que tiene el modelo ARMA.

Nosotros ya sabemos que el modelo ARMA es una combinación de dos procesos.

Uno es el proceso AR, que es un proceso autoregresivo, y la otra es la componente MA, que es la componente media móvil.

Juntos nos proponen este nuevo proceso llamado ARMA.

Ya sabemos que es muy importante en el tema de las series temporales.

Ahora, un tema que es muy importante siempre tener en cuenta es la elección de un buen modelo de serie temporal.

Existen distintas formas para poder elegir modelos.

Una es a partir del coeficiente de información de Akaike, que es un indicador que usted lo va a poder conocer a futuro, en las siguientes semanas.

Pero yo me quiero centrar en algo que usted ya conoce, que es el concepto de validación cruzada.

Pero no en la validación cruzada usual que usted conoce, que es omitir un conjunto de datos de nuestro conjunto de datos de forma aleatoria y, con el resto, tratar de hacer predicciones en nuestro conjunto que hemos dejado para validar.

Y eso hacerlo muchas veces, sino que vamos a hablar de lo que llamamos la **validación cruzada por bloques** y cómo es de importante este tipo de validación en el contexto de series temporales.

Entonces, partamos.

## ¿Qué es la validación cruzada por bloques?

A diferencia de la validación cruzada tradicional, esta validación cruzada por bloques divide la serie temporal por bloques, considerando segmentos consecutivos.

Por lo tanto, respeta cómo es la secuencia temporal de nuestra serie.

Con eso nosotros podemos preservar cómo es la estructura temporal que tiene nuestra serie de tiempo y así poder ajustar nuestro modelo ARMA a esa parte del bloque que nosotros estamos omitiendo.

Y eso es súper importante.

¿Por qué?

Porque ya sabemos que esta serie de tiempo, en particular en un modelo ARMA, un momento \(t\) va a depender de \(p\) datos del pasado.

Pero esos \(p\) datos del pasado, en la parte autoregresiva, dependen de una secuencia.

Y si nosotros rompemos esas secuencias, estamos diciendo que vamos a perder la dependencia temporal.

Y eso es un problema.

Porque aquí nosotros estamos yendo un poco más allá con lo que es el análisis de datos, llamémoslo tradicional.

Estamos yendo más allá porque estamos asumiendo que nuestros datos tienen una dependencia temporal, la cual no podemos perder.

Por lo tanto, la validación cruzada por bloques nos permite mantener esa secuencia temporal.

Y que, al final, es lo que nosotros queremos capturar y lo que queremos estudiar.

Es un tema importante hacer validación cruzada por bloques para tratar de entender que nuestro proceso de ARMA es capaz de generalizar de una forma lo más robusta posible.

Entonces, ese es un tema.

## Bandas de predicción

Otro tema importante que nosotros queremos tener en cuenta cuando queremos ajustar un modelo ARMA, en este caso, es cómo es capaz de hacer predicciones a futuro, pero construyendo lo que se conoce como una **banda de predicción**.

La banda de predicción, en palabras simples, es un rango en el cual nosotros esperamos que nuestros valores futuros, que nosotros estamos prediciendo, caigan con un cierto nivel de confianza.

Esto implica que calcular intervalos toma en cuenta la parte autoregresiva y la parte MA, con el fin de poder proporcionar un rango que sea realista para los datos que nosotros queremos predecir a futuro.

Entonces, tenemos dos cosas muy importantes.

La primera, la validación cruzada por bloques.

Ya sabemos que, a partir de la validación cruzada tradicional, esta nos permite saber qué tan capaz es nuestro modelo de generalizar en datos que no conoce.

Pero en este caso lo hacemos por bloques para no perder la dependencia temporal.

Y las bandas de predicción nos permiten generar este rango realista para donde pueden estar nuestros posibles resultados.

Juntar estas dos técnicas, la validación cruzada y las bandas de predicción, es crucial en el tema de series de tiempo.

Y no solo para los modelos ARMA o los modelos ARIMA o ARIMAX que usted va a ver a futuro, sino para cualquier técnica de serie temporal a la cual usted se vea envuelto en aplicaciones reales.

¿Por qué?

Porque esto nos va a permitir tomar decisiones correctas sobre la elección de nuestro proceso o de nuestro modelo de serie de tiempo, para así tomar decisiones muy informadas sobre cómo generaliza nuestro modelo y cuál es su banda de predicción, la cual nosotros vamos a reportar en algún informe, por ejemplo.

Ese es un valor agregado muy importante en este mundo de modelados, en particular en este curso de series de tiempo, porque en realidad nos permite llevar a una visión más profunda con respecto a estos modelos de series de tiempo.

En particular, los que estamos viendo en esta semana, que son los modelos ARMA.

Entonces, quédese con esas dos cosas.

Nosotros ya hemos conocido hartas cosas para manejar modelos ARMA.

Sabemos transformar nuestros datos.

Conocimos varias técnicas para transformar nuestros datos y buscar que se cumplan ciertos supuestos, en particular, la estacionariedad.

También conocemos gráficas importantes, como lo son:

- La función de autocorrelación.
- La función de autocorrelación parcial.

Estas funciones nos permiten tomar decisiones con respecto al modelo que nosotros queremos ajustar.

Pero siempre nosotros queremos hacer predicciones a futuro, queremos generalizar.

Nuestro objetivo no es tan solo ajustar el mejor modelo, sino elegir el que mejor haga predicciones, que cometa el menor error posible.

Para eso ocupamos la validación cruzada por bloques.

Y también generamos estas bandas de confianza, que nos permiten tener un rastreo completo del comportamiento de nuestro modelo.

Entonces, espero que este tutorial haya sido de su agrado y nos vemos en el siguiente.
