# Clase aplicada de la dependencia observada a modelos válidos

Bienvenidos y bienvenidas. Recordemos que trabajamos con dos series reales: la generación de energía eléctrica (**GE**) y el índice de oscilación sur (**ZOI** / **SOI**). 

La serie GE muestra una tendencia creciente y patrones repetidos en el tiempo, mientras que la serie ZOI presenta un comportamiento más regular. 

En la clase anterior dimos un paso clave. A partir de la función de autocorrelación (**ACF**) fuimos capaces de proponer modelos para describir la dependencia de una serie de tiempos. Esto fue posible para la serie ZOI, donde vimos que modelos como **AR(1)** o **ARMA(1,1)** parecían razonables, aunque aún imperfectos, ya que visualmente su ACF presentaba discrepancias importantes con respecto a la observada. Adicionalmente, vimos que la estructura de la ACF de la serie GE transformada y diferenciada tenía un comportamiento claramente estacional, por lo que deberíamos esperar a una familia de modelos más amplios para que incluyera este tipo de comportamientos para realizar un ajuste razonable. 

Pero aquí aparece una pregunta fundamental: **¿Basta con que la ACF de modelos se parezca a la ACF de los datos?** La respuesta es categóricamente **no**. 

De hecho, puede ocurrir algo más delicado. Distintos modelos pueden generar exactamente la misma función de autocorrelación. Justamente nos ocurrió con el modelo ARMA(1,1) planteado para la serie ZOI, que tenía dos conjuntos de parámetros diferentes que generaban la misma ACF teórica. Esto significa que la ACF por sí sola no identifica completamente el modelo, entonces necesitamos un criterio adicional. 

No cualquier modelo que reproduce la dependencia observada es un modelo válido. En esta clase vamos a profundizar esta idea, entendiendo qué hace que un modelo sea realmente adecuado para describir una serie de tiempos. Junto con esto analizaremos la **PACF** (Función de Autocorrelación Parcial), que es otro componente importante que nos ayudará a discriminar entre modelos posibles. 

En esta clase se revisarán los siguientes temas:
1. **Tema 1:** Análisis estructural de la dependencia. 
2. **Tema 2:** Comportamiento empírico de modelos lineales mediante simulación. 
3. **Tema 3:** Aplicación a la serie ZOI-GE. 

---

## Tema 1: Análisis estructural de la dependencia

Para estudiar la dependencia temporal utilizamos herramientas como la función de autocorrelación (ACF) y la función de autocorrelación parcial (PACF). Recordemos que la ACF nos muestra la dependencia total entre observaciones, mientras que la PACF mide la dependencia directa, eliminando el efecto de los rezagos intermedios. 

Para ver explícitamente cómo luce la PACF teórica, consideremos los siguientes ejemplos específicos: un **AR(1)**, un **MA(1)** y un **ARMA(1,1)**. Así, las funciones de autocorrelación parcial de los tres ejemplos anteriores son las que se muestran a continuación. 

Notar que en todos los casos la autocorrelación parcial y la autocorrelación simple coinciden por definición para un *lag* igual a 1, mientras que *phi_00* no está definida, aunque algunos software consideran *phi_00* igual a 1 como un símil a la ACF en *h* igual a 0. 

Un aspecto clave que es generalizable de las expresiones anteriores es que cada tipo de modelo genera una forma característica de las funciones de autocorrelación parcial:
* Los modelos **autoregresivos (AR)** presentan una PACF que se corta después de ciertos rezagos. 
* Los modelos de **media móvil (MA)** presentan una PACF que decae gradualmente a 0. 
* Los modelos **ARMA** presentan combinaciones de ambos comportamientos. 

Esto permite utilizar la PACF como una herramienta complementaria para identificar qué tipo de modelo podría ser adecuado para una serie específica. Estas cantidades se obtienen a partir del **algoritmo de Durbin-Levinson**, el cual fue desarrollado en detalle en las clases teóricas. En esta clase no profundizaremos en su cálculo, pero es importante notar que el algoritmo permite construir la PACF a partir de la ACF, lo que explica por qué ambas funciones están estrechamente relacionadas y justifica la notación *phi sub hh*. 

En particular, en un modelo **AR(p)**, la PACF en el rezago *p* coincide con el último coeficiente del modelo, es decir, *phi sub p* es igual a *phi sub p*. En la práctica, esto significa que si la PACF se anula después de *p* rezagos, podemos proponer un modelo AR(p) como primera aproximación. 

Antes de pasar a analizar las series SOI y GE, veamos una comparación a partir de simulaciones donde sí conocemos el verdadero modelo. 

> Comprueba lo aprendido respondiendo a la siguiente pregunta. 

---

## Tema 2: Comportamiento empírico de modelos lineales mediante simulación

Complementando el análisis de simulación de las clases pasadas, pero ahora fijamos nuestra atención en la PACF. Recordemos que la serie de tiempos simulada tiene longitud 200 y el ruido blanco tiene una distribución normal con media 0 y varianza 4. Así se obtiene *x_t* para diferentes estructuras y valores de los parámetros. Además, en todos los casos la serie se centra en 10. 

La figura que se muestra en pantalla corresponde a la PACF de tres realizaciones de un **AR(1)** con parámetro *phi* igual a 0.7 y *phi* igual a -0.7 respectivamente. Estas PACF muestrales corresponden exactamente a las series simuladas presentadas en la clase anterior. Las PACF muestrales de color negro y las PACF teóricas de color rojo. 

Se puede apreciar que en ninguno de los tres casos coinciden exactamente. Al igual que en la ACF, en general rara vez coinciden. Lo que uno debería esperar es que la PACF muestral esté cerca de la PACF teórica, pero no exactamente igual. Nuevamente, la PACF muestral presenta una variedad intrínseca producto del ruido blanco, que hace que el resultado cambie aunque el modelo subyacente sea el mismo. Lo importante es que la PACF muestral converge a la PACF teórica y esto es consecuencia directa del resultado que discutimos sobre la ACF muestral, ya que desde el algoritmo de Durbin-Levinson podemos ver que la PACF es una función continua de la ACF, lo que significa que la propiedad de convergencia de la ACF se hereda a la PACF. 

La siguiente figura muestra ahora la comparación para el modelo **MA(1)**, cuando el parámetro *theta* toma el valor 0.7 y -0.7 respectivamente. Nuevamente, los colores negro y rojo representan las versiones muestrales y teóricas de la PACF. En ambos casos, la PACF decae exponencialmente a cero, donde la principal diferencia entre el parámetro positivo con el negativo es que el primero provoca que la PACF itere entre positivo y negativo, mientras que en el caso negativo todas las PACF son negativas. En algunos casos, la PACF muestral pareciera que vuelve a crecer de forma significativa cuando los lags aumentan, pero este efecto es producto de la aleatoriedad del ruido blanco y no es un componente sistemático. Naturalmente, diferenciar esto es fácil cuando disponemos del verdadero modelo, pero en la práctica es complejo ya que el verdadero modelo es desconocido. 

La siguiente figura corresponde a la PACF del modelo **ARMA(1,1)** con *phi* igual a 0.7 y *theta* igual a 0.7, donde se aprecia claramente el decaimiento exponencial que debería tener la PACF. También se aprecia que existe una clara concordancia entre la PACF muestral y teórica. La alternancia se debe a la elección de los parámetros *phi* y *theta*, y si bien este es un caso particular, lo esencial que caracteriza a la PACF de un ARMA es su decaimiento exponencial, aunque por sí sola esta PACF tiene un comportamiento muy similar a la PACF del MA(1), cuando el parámetro *theta* es positivo. 

Estos dos ejemplos muestran que la PACF por sí sola tampoco permite determinar un modelo, sino que ambas, la ACF y PACF en conjunto son las que facilitan la elección del modelo. 

Adicionalmente, consideraremos nuevos experimentos con modelos más sofisticados, con el objetivo de comprender de mejor forma los aspectos teóricos relevantes y por sobre todo el uso de los operadores diferenciales de los modelos lineales, los cuales permiten representar estos modelos mediante polinomios en el operador rezago, facilitando el análisis de sus raíces y propiedades. 

### Análisis de Polinomios y Raíces

Dentro de la familia de los modelos autoregresivos, en particular el AR(1) no permite identificar completamente las diferentes estructuras que este tipo de modelo posee. Sin embargo, desde el modelo **AR(2)** en adelante se observa el efecto positivo de analizar los polinomios característicos. 

En el AR(1) la condición de estacionalidad es simplemente que el parámetro *phi* en valor absoluto sea menor a 1, la cual se puede obtener desde múltiples formas. En cambio, en el AR(2) la condición no se basa directamente en los valores de *phi_1* y *phi_2*, sino que en las raíces del polinomio autoregresivo, las cuales deben ser en módulo mayores a 1. Esta condición no solo garantiza la estacionalidad del modelo, sino que también permite escribir el proceso como una combinación infinita del ruido blanco, lo que justifica interpretar la serie en función de su pasado. 

En el caso del AR(2) se tiene un polinomio de orden 2. Existen tres casos de raíces diferentes: reales distintas, reales iguales y complejas. Por ejemplo, consideremos los siguientes tres modelos: 
* El primero presenta raíces reales distintas.
* El segundo tiene raíces reales iguales.
* El tercero raíces complejas. 

De los modelos de ejemplo se aprecia claramente que los parámetros pueden ser mayores o iguales a 1 en valor absoluto, por lo que mirar solo los parámetros sin calcular las raíces no es un indicio para la estacionalidad, ya que los tres modelos anteriores son débilmente estacionarios. 

La figura en pantalla muestra en la primera fila una realización de cada uno de estos modelos. La segunda y tercera fila contienen la ACF y PACF respectivamente, donde de color negro está la versión muestral y de color rojo la teórica de cada una de estas funciones. Existen dos características bien marcadas en esta gráfica:
1. La primera es que la PACF reconoce muy bien que el valor *p* es igual a 2, es decir, se puede reconocer un AR(2). 
2. La segunda tiene que ver con el tipo de raíces, donde destaca el caso de raíces complejas, ya que la ACF muestra un comportamiento oscilatorio, la cual no es un componente periódico, sino más bien es parte de la estructura del modelo. 

En la práctica esto se traduce en que un comportamiento oscilatorio en la ACF no necesariamente indica estacionalidad, sino que puede ser consecuencia de raíces complejas de un modelo autoregresivo. 

### Modelos de Media Móvil (MA) y ARMA

Con respecto a la familia de modelos **MA(q)**, el análisis se invierte. La ACF se corta y la PACF decae, pero nuevamente la forma del decaimiento queda determinada por las raíces del polinomio asociado. Esto quiere decir, por ejemplo, que ahora es la PACF la que tendría un comportamiento oscilatorio cuando las raíces del polinomio característico son complejas. 

Ahora bien, en los modelos de media móvil no hay problema de estacionalidad, ya que indiferente del valor de sus parámetros, estos modelos siempre resultan ser débilmente estacionarios. Pero sí existe el problema de **identificabilidad**. Esto quiere decir que existen diferentes conjuntos de parámetros que generan la misma ACF y, en consecuencia, la misma PACF. Desde el punto de vista de estimación, el problema de identificabilidad es muy importante, ya que el modelo no sería consistentemente estimable, por lo que se impone una condición adicional, denominada **invertibilidad**, la cual corresponde a exigir que las raíces del polinomio característico estén fuera del disco unitario. Esto eliminaría dicha ambigüedad en el modelo. 

A diferencia de los modelos de media móvil, en los modelos autoregresivos las autocorrelaciones determinan completamente los parámetros del modelo, lo que garantiza su identificabilidad. Consideremos por ejemplo los modelos MA(2) que se muestran a continuación. La figura en pantalla muestra una realización de cada modelo, en conjunto con sus respectivas ACF y PACF. Las realizaciones no son iguales, tal como ocurre cuando se simula el componente aleatorio de un mismo modelo, por lo que la realización no es útil para indicar si el modelo es el mismo o no. En cambio, al observar la ACF y PACF, tanto muestral de color negro como teórica de color rojo, son exactamente iguales para ambos modelos, lo cual no es coincidencia, sino que es parte del problema de no identificabilidad. En consecuencia, al imponer la restricción de invertibilidad, solo el primer modelo cumple dicha condición, descartando así el segundo modelo. En la práctica, esto implica que no basta con ajustar un modelo, sino que es necesario verificar que cumple las condiciones que aseguren su identificabilidad. Adicionalmente, este ejemplo muestra claramente que la ACF tiene solo dos lags significativos, mientras que la PACF decae exponencialmente, evidenciando así la estructura real, la cual corresponde a un MA(2). 

> Comprueba lo aprendido respondiendo a la siguiente pregunta. 

Finalmente, en los modelos **ARMA**, la estructura de dependencia resulta de la combinación de un componente autoregresivo y uno de medias móviles. Como consecuencia, ni la función de autocorrelación ni la función de autocorrelación parcial presentan cortes claros, sino que ambas decaen gradualmente. La forma de este decaimiento está determinada por las raíces de los polinomios asociados al modelo. Cuando estas son reales, el decaimiento es monótono, mientras que si son complejas, se observa un comportamiento oscilatorio. Además, dependiendo de los parámetros, las autocorrelaciones pueden alternar de signo o no. 

En este contexto, la identificación del modelo ya no puede basarse únicamente en la inspección visual de la ACF y la PACF, sino que requiere herramientas adicionales que permitan distinguir entre estructuras que pueden generar comportamientos similares. Un aspecto importante que se debe considerar en los modelos ARMA es la **redundancia o sobreparametrización** de un modelo. Esto ocurre cuando se propone un modelo de un orden mayor al que corresponde, lo cual es factible que efectos de la parte autoregresiva con la parte media móvil se puedan cancelar. Esto se traduce en que los polinomios característicos de ambas partes poseen raíces iguales y en realidad no debería aumentarse artificialmente el orden del modelo. Esto se traduce en términos de incertidumbre en las predicciones. 

Por ejemplo, consideremos los siguientes dos modelos ARMA(1,1):
* En el primero, la parte AR(1), el *z_1* es igual a 1 / 0.7 y la parte MA(2), el *z_1* también es igual a 1 / 0.7. En realidad, este modelo se puede escribir de la siguiente forma en su versión de polinomios característicos, simplificando ambas raíces. Es decir, el modelo en realidad es un **ruido blanco**. 
* El modelo 2, presentado a continuación, tiene una parte AR con el *z_1* igual a 1 / 0.7 y la parte MA, el *z_1* es igual a -1 / 0.7. Esto significa que no hay cancelación y el modelo efectivamente es un **ARMA(1,1)**. 

La figura que se muestra en pantalla sigue el patrón de las otras figuras, mostrando una realización, la ACF y la PACF de cada modelo, con los colores representativos para la versión muestral y teórica de estas funciones. En la primera fila se observa que efectivamente la ACF y PACF del primer modelo corresponden a las de un ruido blanco, y eso es porque realmente es un ruido blanco. Mientras que en el segundo caso se observa el decaimiento tipo exponencial de ambas, la ACF y PACF. Cabe destacar que el modelo 2 ya había sido analizado, pero de forma separada a ambas funciones. Esto muestra que aumentar el orden de un modelo no siempre mejora su capacidad explicativa, y que es fundamental trabajar con representaciones mínimas. 

---

## Tema 3: Aplicación a las series SOI y GE

Ahora veamos cómo aplicar la teoría anterior a las series SOI y GE, que son nuestros ejemplos reales. Al igual que la ACF, comenzamos mostrando la PACF de la serie SOI. La figura en pantalla contiene la PACF muestral, considerando hasta tres ciclos completos de 12 meses cada uno. Junto con esta gráfica, la tabla adjunta muestra los primeros 12 valores de las autocorrelaciones parciales muestrales de la serie SOI. 

Se aprecia claramente que la PACF muestral tiene un decaimiento fuerte a partir del *lag* 4 en adelante. Esto podría suponer un AR(2) o AR(3), ya que si bien el tercer *lag* supera la curva de significancia, este no es muy alto. En la tabla se observa que alcanza un valor de 0.11 aproximadamente. Ahora bien, alguien podría pensar que al haber 3 lags significativos al comienzo, esto podría ser considerado como un decaimiento exponencial, y en consecuencia lo que se visualiza es un modelo ARMA. 

Como revisamos en detalle en la sección anterior de esta clase, no basta con observar la PACF individualmente, sino que debemos observar tanto la ACF como la PACF de forma conjunta, tal como se muestra en pantalla. En su conjunto se descartan modelos de la familia MA. Esto sugiere un modelo **AR(3)** como una alternativa plausible, dado el decaimiento exponencial de la ACF y el corte abrupto en la PACF. Un modelo alternativo podría ser el **ARMA(2,1)**, considerando que el decaimiento en la ACF es más lento. En realidad se podrían proponer más modelos, y esta no es una elección basada únicamente en la ACF y PACF, por lo que es de vital importancia contar con métodos adicionales para discriminar entre modelos. Estos métodos serán vistos en las próximas clases. 

Volviendo a las gráficas de la ACF y PACF, y observando con detalle también se descarta el AR(1) y el ARMA(1,1) propuesto en la clase pasada. Esto implica que la identificación del modelo no puede basarse únicamente en la inspección visual, sino que requiere herramientas adicionales para discriminar entre alternativas plausibles. Los métodos de estimación se verán en detalle en las próximas clases, pero podríamos seguir un tratamiento similar al presentado en la clase anterior, utilizando las primeras dos autocorrelaciones muestrales para estimar un AR(2) y las primeras tres para estimar un AR(3). También sería posible estimar el ARMA(2,1), sin embargo las ecuaciones se complican demasiado y los métodos que veremos en la siguiente clase son mejores, así que no tiene sentido en este punto igualar autocorrelaciones muestrales con teóricas. 

La estimación del AR(2) utilizando las primeras dos correlaciones muestrales se obtiene en las siguientes ecuaciones, obteniendo finalmente que *phi_1* es igual a 0.4382 y *phi_2* es igual a 0.2992. Por otra vez, en la clase pasada se ajustaron los modelos AR(1), MA(1) y ARMA(1,1) y en este último caso habían dos conjuntos de parámetros. Como se dijo, ya descartamos el MA(1) y para las dos versiones del ARMA obtenemos los siguientes dos conjuntos de parámetros. El primer conjunto de parámetros arroja un modelo identificable, mientras que el segundo no. Esto significa que sólo el primero de los ARMA(1,1) es un modelo válido. 

La figura en pantalla muestra el ajuste obtenido por los tres modelos actuales que son válidos. Como era de esperarse, el AR(2) captura de mejor forma la dependencia que los otros dos modelos. En particular el AR(1) subestima la dependencia, mientras que el ARMA(1,1) la sobreestima. Si bien el modelo AR(2) obtenido es bastante razonable, éste aún puede ser mejorado si se cambia de método de estimación, ya que hasta el momento sólo estamos usando la consistencia de las autocorrelaciones muestrales, pero no hemos utilizado la distribución de probabilidad subyacente, que es lo que hace el método de **máxima verosimilitud**, que además en muchos modelos estadísticos es el que presenta mejores resultados de estimación. Adicionalmente aún falta explorar los modelos AR(3) y ARMA(2,1), que podrían resultar en un modelo más adecuado, pero como se mencionó anteriormente, para ajustar estos modelos es mejor esperar al método de máxima verosimilitud. 

Con respecto a la serie **GE**, nuevamente no se puede realizar un análisis completo como en el caso de la serie SOI, aún cuando la serie GE haya sido transformada y diferenciada para lograr la estacionalidad. La gráfica de la PACF se muestra en pantalla, también muestra un comportamiento diferenciador a los modelos de la familia ARMA, y que vuelven a aparecer lags muy significativos luego de 12 meses, indicando también a través de esta gráfica que la serie presenta un comportamiento periódico, que no es producto de posibles raíces complejas, ya que estos nuevos lags significativos son casi tan altos como los primeros. En consecuencia, debemos esperar hasta incluir la componente estacional en el modelo para realizar un correcto ajuste de esta serie. 

---

## Resumen de la clase

Hemos llegado al final de la clase, ahora recordemos las ideas más importantes:
* La identificación de un modelo no puede basarse únicamente en la PACF. La PACF permite distinguir entre estructuras que presentan comportamientos similares en la autocorrelación, siendo ambas herramientas (ACF y PACF) necesarias para proponer modelos adecuados. 
* El comportamiento de la ACF y la PACF está determinado por las raíces de los polinomios del modelo. En particular, raíces reales generan decaimientos exponenciales, mientras que raíces complejas producen comportamientos oscilatorios. 
* Un modelo adecuado no solo debe ajustarse a los datos, sino también ser **identificable** y estar en su forma mínima. Condiciones como la **invertibilidad** y la ausencia de factores comunes entre los polinomios aseguran que el modelo represente de manera única la estructura de dependencia.