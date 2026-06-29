# Predicción en procesos ARMA con datos reales

Bienvenidos y bienvenidas a este nuevo videotutorial, en el cual vamos a ajustar modelos ARMA a una serie de datos real.

En este caso en particular, vamos a utilizar una data real, que es una acción de la bolsa americana, en particular, la acción de Tesla.

Primero, vamos a realizar nuestro análisis de siempre.

En este caso en particular, necesitamos importar e instalar las librerías necesarias, y vamos a utilizar los datos mensuales de la acción de Tesla desde enero del 2014 hasta octubre del 2023.

Ojo aquí, que yo pongo noviembre, pero en este caso termina con el último día del mes, 31 de octubre, y nos vamos a enfocar directamente en el valor del cierre del mes.

Hacemos la gráfica de nuestra acción.

Vemos que, claramente, es una serie que no es estacionaria.

Tiene valores muy bajos aquí durante mucho tiempo, hasta el 2020; después se da una alza significativa hasta los 350, baja hasta alrededor de los 120, y ahora está aquí, alrededor de los 200 dólares el precio de una acción de Tesla.

Vamos a realizar nuestras transformaciones respectivas para que nuestro ajuste cumpla el supuesto de estacionariedad.

Entonces, ¿qué vamos a hacer?

Vamos a aplicar el logaritmo de nuestra base de datos, para que podamos controlar la varianza de nuestra serie temporal, y luego vamos a diferenciar nuestra serie logarítmica.

Recuerde que este comando de aquí es para transformar nuestra data a un objeto de la librería Darts.

Hacemos la gráfica.

Esta sería nuestra gráfica de nuestra serie original, que está transformada con el logaritmo y está diferenciada para quitarle su tendencia.

Visualmente, vemos que tiene un comportamiento estacionario, tiene una media constante y también tiene varianzas que podríamos considerar controladas.

Luego de eso, vamos a realizar las gráficas de la autocorrelación y de la autocorrelación parcial, y esto es lo que tenemos.

Pasan cosas curiosas.

No tenemos un decaimiento lento en la parte de la función de autocorrelación, y lo mismo no ocurre en la función de autocorrelación parcial.

Sin embargo, tenemos estos lags de acá, tanto en la función de autocorrelación como en la función de autocorrelación parcial, que es lag 4, es significativo; sale por estas barras de aquí.

Sin embargo, a la altura del lag 10 también se podría considerar significativo.

Sin embargo, considerar algo que dependa hasta un lag 10, teniendo en cuenta que el lag 4 también es bastante considerable, uno va a tratar de elegir algo que tenga menos parámetros a algo que tenga muchos parámetros.

Es un consejo que yo les dejo en la mesa.

Ahora, la pregunta es, teniendo en cuenta esta función de autocorrelación y esta función de autocorrelación parcial:

> ¿Cuáles son los modelos que uno podría considerar para la serie temporal de los logaritmos y luego diferenciarlos?

Entonces, si miro la función de autocorrelación, uno podría pensar:

> “Puede ser que un MA(4) sea un buen modelo”.

Pero alguien que mire la función de autocorrelación puede pensar que quizás puede ser un AR(4).

La pregunta es:

> ¿Cuál de los dos podré elegir?

> ¿Será que un ARMA(4,4) sea una buena opción?

Entonces, dadas esas tres propuestas:

- ARMA(4,4)
- AR(4)
- MA(4)

la pregunta es:

> ¿Cuál de los tres elegimos?

Y ahí es cuando yo les presento este nuevo comando, que se llama `auto_arima`, y es parte de la librería `pmdarima`.

Lo que hace este comando es, principalmente, evaluar muchos modelos ARMA.

En particular, es ARIMA, pero ya vamos a ver qué significa el modelo ARIMA.

Pero en este caso vamos a considerar ARMA, que es donde la componente `d` del modelo ARIMA es igual a 0.

Este comando `auto_arima` me ayuda a ajustar muchos modelos ARMA, con el fin de elegir al mejor modelo ARMA en base a algún criterio.

En este caso en particular, tenemos hartos input:

- Si su análisis es `false`, no estamos asumiendo que hay una componente estacional.
- `stepwise` es una forma de hacer la estimación del proceso y lo vamos a situar en `false`.
- Vamos a considerar que nos puede encontrar `warnings`.
- Los errores de acción los vamos a ignorar.
- No vamos a poner un máximo orden.
- El `trace`, que sea verdadero, significa que nos muestre en pantalla todos los modelos que está ajustando y sus respectivos valores.

Y esto es importante también, porque lo que le estamos diciendo al modelo es que considere en todos los modelos que va a combinar, que empiece con:

\[
p = 0
\]

y el máximo \(p\) que va a considerar es:

\[
p = 4
\]

Lo mismo con \(q\). El mínimo valor, o vamos a comenzar con:

\[
q = 0
\]

y el máximo \(q\) que vamos a evaluar es:

\[
q = 4
\]

¿De dónde salen estos 4?

Salen directamente de los \(p\) que surgen de estas gráficas de acá.

Aquí vamos a seleccionar:

\[
q = 4
\]

y:

\[
p = 4
\]

¿Qué hace este modelo?

Nos imprime todos los modelos que está ajustando.

Fíjense que es una lista de modelos gigante, con todas las combinaciones que se pueden formar con estos parámetros.

Aquí surgen dos columnas:

- `AIC`
- `Time`

donde `Time` es cuánto se demora en ajustar y hacer la estimación de los parámetros.

Pero este `AIC`, que es el coeficiente de información de Akaike, es un numerito, un número real, que nos dice qué tan bueno es el modelo que estamos ajustando.

Existen reglas de criterios para elegir modelos en base al AIC, que es el coeficiente de información de Akaike, y la regla es la siguiente:

> Un buen modelo es el que tiene el menor coeficiente de información de Akaike.

Y eso se traduce en elegir el más pequeño.

Insisto, también considerando los signos negativos.

O sea, si yo quiero considerar un valor menor, si tenemos -1 y el otro tiene 1, el que es menor, siguiendo el orden de los números reales, es -1.

Por lo tanto, aquí el signo sí importa.

Siempre hay que elegir el que tenga el menor coeficiente de Akaike.

Fíjense que, además, el comando me dice cuál es el mejor modelo, y el mejor modelo que hemos ajustado es el ARIMA que, en este caso, omitan la componente `d`, que es igual a 0.

Por lo tanto, es un ARMA(0,4), y eso es equivalente a un MA(4).

Y es justamente lo que nosotros habíamos intuido, porque o era un MA(4), o podría haber sido un AR(4), o una combinación entre los dos.

Fíjense que aquí hicimos todas las combinaciones posibles y la que tiene el menor valor es un MA(4), donde tiene un coeficiente de Akaike de -92,346.

Todos los otros son mayores a ese valor, están en la recta real, en el sector derecho de este valor de aquí.

Por lo tanto, nuestra intuición de pensar que un modelo MA(4) podría ser un buen modelo aquí la confirmamos, porque hicimos todas las combinaciones posibles entre el \(p=4\) y el \(q=4\), empezando desde 0.

¿Cuáles son los parámetros estimados con ese mejor modelo?

Si nosotros ocupamos estos comandos de aquí, podemos imprimir en pantalla cuáles son nuestros valores estimados para los parámetros.

En este caso, tenemos cuatro parámetros para el modelo.

Tenemos el que vendría siendo:

- \(\theta_1\)
- \(\theta_2\)
- \(\theta_3\)
- \(\theta_4\)

y tenemos la estimación de:

\[
\sigma^2
\]

que vendría siendo la varianza del ruido blanco.

Con esto, nosotros podemos escribir la ecuación de nuestra serie temporal, y vamos a decir que la serie \(X_t\) se puede expresar por la siguiente ecuación.

El \(\varepsilon_t\), que es el ruido blanco de un paso anterior, con su respectivo coeficiente.

Lo mismo a dos pasos del pasado, tres pasos del pasado, cuatro pasos del pasado, todos con su respectivo coeficiente, y donde vamos a asumir que este \(\varepsilon_t\) es un ruido blanco de media 0 y con la varianza estimada que nos dio el ajuste.

Hay que tener algo en cuenta: el \(X_t\) es la diferencia de los logaritmos.

Esta ecuación nos permite modelar esto de aquí, donde nuestra serie original es la serie \(Y_t\), donde \(t\) es un dato mensual.

Entonces, nos tenemos que devolver.

¿Cómo vamos a hacer eso?

Aquí yo les dejo un código que ustedes pueden reciclar.

Antes de entrar a esta parte de aquí, me voy a saltar directamente acá, donde lo que nosotros vamos a hacer es predicción un paso hacia adelante.

Entonces, vamos a hacer las predicciones a un paso hacia adelante, pero esto va a ser la predicción de \(X_t\).

Ahora, teniendo en cuenta que el último valor de la acción, y ahí sale por qué imprimí esto, porque la última acción al cierre del mes de octubre fue de 200,83 dólares y más números.

Esto lo vamos a transformar aquí.

Entonces, vamos a ocupar el logaritmo de esto de aquí.

Eso principalmente porque el \(X_t\), que nosotros vamos a estimar, va a depender del logaritmo en ese momento.

Nosotros queremos estimar el \(Y_t\), pero eso depende del logaritmo en el momento anterior.

Por lo tanto, fíjense que si yo tomo el \(X_t\), hago la predicción, esto que está restando lo paso sumando, este valor que ya tengo, la predicción, y este valor, que va a ser el valor del pasado que yo conozco, que sería octubre, puedo estimar de esa forma el logaritmo del valor en noviembre.

Y para tener el valor exacto en noviembre, tendría que sacar la exponencial.

Es justamente lo que hace esto de acá.

Porque tomamos el logaritmo del último valor, después se lo sumamos al logaritmo de ese último valor y vendría siendo el logaritmo de la predicción.

Por lo tanto, si yo quiero tener el valor de la predicción directamente, lo obtengo con la función exponencial.

Eso me da que la predicción para noviembre vendría siendo 196,38 con nuestro modelo, que vendría siendo un MA(4).

¿Qué quiere decir eso?

Que para nuestra acción de Tesla existe una probabilidad de que ese valor sea 196 dólares, o sea, que siga bajando.

Ahora, surgen hartas cosas con este código.

¿Por qué?

Porque yo estoy haciendo predicción a un valor hacia adelante, pero yo podría ser más ambicioso y pensar que quiero predecir cuatro valores hacia adelante.

¿Por qué?

Porque si mi modelo depende de los cuatro valores anteriores, significa que yo puedo hacer predicciones a cuatro valores hacia adelante.

Entonces, si ejecuto el código y hago el `Y_preds`, fíjense que sigo teniendo las predicciones para los meses que siguen.

O sea, sigue una tendencia:

- 196
- aumenta en diciembre
- baja en enero
- baja después fuertemente en febrero

Entonces, alguien que es inversionista puede tomar decisiones con respecto a estas predicciones.

¿Será que podemos hacer predicciones más a futuro?

Por ejemplo, diez períodos hacia adelante.

Veamos qué nos da.

Si hacemos la predicción hacia adelante, fíjense que pasa algo bastante curioso.

Ya desde los cuatro meses a futuro, si nosotros hacemos más predicciones, esto se mantiene constante.

Entonces, la pregunta es:

> ¿Por qué se mantiene constante después de esto hacia adelante?

Es principalmente porque ya cuando yo hago la predicción a cuatro meses hacia adelante, tengo la dependencia de los cuatro meses del pasado.

Yo ya hice la predicción a cuatro meses hacia el futuro, lo que significa que después, cada vez que yo vaya agregando más valores, no van a ir cambiando, y esto se queda pegado en la media del proceso, se queda pegado en el último valor, porque ya no tengo más valores que van cambiando para hacer la predicción.

Entonces, ese vendría siendo nuestro ajuste de muchos modelos que hemos propuesto a partir de un análisis de la función de autocorrelación y función de autocorrelación parcial.

También hemos introducido este nuevo coeficiente de AIC, que es el coeficiente de información de Akaike, que nos permite elegir cuál es el mejor modelo de todos los que hemos propuesto.

Espero que este tutorial haya sido de su agrado y nos vemos en el siguiente tutorial.
