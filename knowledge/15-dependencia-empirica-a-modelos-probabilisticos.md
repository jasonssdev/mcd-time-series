# Modelos lineales y autocorrelación en series de tiempo

Bienvenidos y bienvenidas.

Recordemos que trabajamos con dos series reales:

- La generación de energía eléctrica, GEE.
- El índice de oscilación sur, SOI.

La serie GEE muestra una tendencia creciente y patrón repetitivo en el tiempo, mientras que la serie SOI presenta un comportamiento más regular.

Primeramente, ambas series fueron ajustadas por modelos ingenuos, donde el suavizamiento exponencial simple fue el más adecuado para SOI y el método de Holt-Winters para GEE.

Adicionalmente, se verificó que es posible modificar la serie GEE a través de transformaciones y diferenciaciones con el objetivo de obtener una serie con un comportamiento más estable, similar a la serie SOI, la cual ya presentaba estas características sin necesidad de ser modificada.

En el proceso de pasar a modelos probabilísticos, un paso inicial es verificar si las series que lucen estables se comportan similar a un ruido blanco.

En caso afirmativo, no tiene sentido ajustar un proceso estocástico.

En caso contrario, significa que los valores pasados contienen información relevante para explicar o predecir el comportamiento futuro de la serie, por lo que es fundamental estudiar cómo se comporta la dependencia temporal, donde las ACF y PACF muestrales son muy importantes.

En consecuencia, el primer paso en el modelamiento es descartar que la serie sea un ruido blanco, ya que en ese caso no existe estructura que modelar.

En esta clase daremos un paso adicional.

Bajo el supuesto que la serie no es un ruido blanco, pasaremos desde un análisis empírico hacia una formulación formal de la autocorrelación, con el objetivo de construir modelos que sean capaces de reproducir la estructura de dependencia observada en los datos.

## Contenidos de la clase

En esta clase se revisarán los siguientes temas:

1. Análisis empírico de la dependencia.
2. Comportamiento empírico de modelos lineales mediante simulación.
3. Aplicación a las series SOI y GEE.

# Tema 1: Análisis empírico de la dependencia

Para estudiar la dependencia temporal utilizamos herramientas como las funciones de autocorrelación y la función de autocorrelación parcial.

Al analizar la serie SOI se observa que, aunque visualmente puede parecer similar a un ruido blanco, su ACF presenta valores distintos de cero en algunos rezagos, lo que indica la presencia de dependencia temporal.

De forma similar, al analizar la serie GEE, luego de aplicar una transformación logarítmica y una diferenciación, también se observa una estructura clara de la autocorrelación.

En particular, aparecen patrones que se repiten con ciertos rezagos, lo que sugiere la presencia de componentes periódicas.

Estas herramientas permiten identificar si existe estructura en la serie, pero surge una pregunta clave:

> ¿Cómo podemos construir un modelo que reproduzca este tipo de comportamiento?

El objetivo no es replicar exactamente cada valor de la serie o sus autocorrelaciones, sino capturar su estructura de dependencia.

Esto implica encontrar un modelo cuya función de autocorrelación tenga una forma similar a la observada empíricamente.

En otras palabras, buscamos modelos que generen series con patrones de dependencia consistentes con los datos observados.

## Funciones que describen una serie de tiempo

Para formalizar esta idea, es necesario recurrir a las funciones que describen el comportamiento de una serie de tiempo desde un punto de vista de procesos estocásticos.

Estas fueron definidas matemáticamente en las clases previas, las cuales podemos describir en palabras como:

### Función de media

Describe el nivel promedio de la serie a lo largo del tiempo.

En muchas aplicaciones se espera que este valor sea constante.

### Función de autocovarianza

Mide la relación entre los valores de la serie en distintos instantes del tiempo, en función de la distancia entre ellos.

### Función de autocorrelación

Corresponde a una versión estandarizada de la autocovarianza, y es precisamente la que se estima empíricamente mediante la ACF.

Estas funciones permiten describir formalmente características que anteriormente observábamos de manera gráfica, como la estabilidad en el tiempo o la existencia de dependencia entre observaciones.

No olvidar que un proceso estocástico es débilmente estacionario si:

- Su función de media es constante.
- Su función de autocovarianza solo depende de la diferencia en los tiempos y no de los instantes donde se mide la serie.

Series que son estacionarias lucen como las descritas anteriormente.

En general, determinar estas funciones es la clave para modelar la serie de tiempo, donde existen familias de modelos bastante conocidas como casos particulares de los modelos lineales.

## Familias de modelos lineales

Los ejemplos vistos en las clases previas son las familias de modelos:

### AR(p)

El instante actual se puede explicar por una combinación lineal de instantes pasados más un término completamente aleatorio.

La constante `p` representa la cantidad de rezagos con que el pasado incide en el futuro.

### MA(q)

Este modelo representa la serie de interés como una combinación lineal de una componente completamente aleatoria, en varios instantes del tiempo.

La constante `q` representa el rezago máximo de la componente aleatoria.

### ARMA(p, q)

Corresponde a una mezcla de los dos anteriores.

Es decir:

- `p` representa la cantidad de rezagos de la misma serie.
- `q` representa la cantidad de rezagos de la componente aleatoria.

Ejemplos específicos son:

- Autoregresivo de orden 1.
- Media móvil de orden 1.
- ARMA(1,1).

## Forma característica de la autocorrelación

Un aspecto clave es que cada tipo de modelo genera una forma característica de las funciones de autocorrelación.

Los modelos autoregresivos presentan una ACF que decae gradualmente.

Los modelos de media móvil presentan una ACF que se corta después de ciertos rezagos.

Los modelos ARMA presentan combinaciones de ambos comportamientos.

Esto permite utilizar la ACF como una herramienta para identificar qué tipo de modelo podría ser adecuado en una serie de tiempo.

Por ejemplo, las funciones de autocorrelación de los tres ejemplos anteriores son las que se muestran a continuación.

Encontrar analíticamente estas expresiones no es una tarea fácil.

Más aún, determinar generalizaciones a valores de `p` y `q` arbitrarios, a excepción del MA(q), requiere de un formalismo matemático importante.

Es decir, una dificultad técnica es cómo determinar la función de autocorrelación a partir de la estructura del modelo.

Es ahí donde la teoría de los modelos lineales y las representaciones como un MA infinito tienen una importancia esencial.

Esta representación permite entender que la dependencia temporal se transmite a través de los coeficientes del modelo, lo que explica directamente la forma que adopta la función de autocorrelación.

Los coeficientes psi sub j se determinan mediante ecuaciones en diferencia o fracciones parciales.

Más aún, para chequear la estacionariedad directa desde esta representación, implica condiciones sobre los coeficientes phi de la parte autoregresiva de los modelos AR y ARMA.

Por ejemplo, tanto en el modelo AR(1) como en el ARMA(1,1), se tiene la condición de que phi debe ser menor a 1 en valor absoluto, para que los modelos sean débilmente estacionarios.

Antes de pasar a analizar las series SOI y GEE, veamos una comparación a partir de simulaciones donde sí conocemos el verdadero modelo.

# Tema 2: Comportamiento empírico de modelos lineales mediante simulación

En un estudio de simulación donde la serie de tiempo tiene longitud 200 y el ruido blanco tiene una distribución normal con media 0 y varianza 4, se obtuvo Xt para diferentes estructuras y valores de los parámetros.

En todos los casos la serie se centra en 10.

Los resultados se muestran en la siguiente figura.

## Simulación de un modelo AR(1) con phi positivo

La figura que se muestra en pantalla corresponde a tres realizaciones de un AR(1) con parámetro phi igual a 0,7.

Desde las realizaciones de las series se observan tres comportamientos diferentes, con la particularidad de que lucen estables en torno al 10 y la varianza también es prácticamente constante.

La teoría nos dice que la varianza de un AR(1) es gamma 0, por lo que al graficar la media más o menos 1,96 veces la desviación estándar debería cubrirse aproximadamente el 95% de los datos.

Y eso efectivamente ocurre en las tres realizaciones.

La segunda fila contiene las ACF muestrales de color negro y las ACF teóricas de color rojo.

Se puede apreciar que en ninguno de los tres casos coinciden exactamente, salvo en h igual a 0, en donde ambas por definición son 1.

En general, lo que uno debería esperar es que la ACF muestral esté cerca de la ACF teórica, pero no exactamente igual.

En la práctica, lo importante es que capture su forma general más que coincidir punto a punto.

En algunos casos el estimador ACF muestral está por debajo de la teórica, mientras que en otros está por sobre.

Esto es natural, ya que sabemos que la ACF muestral converge en distribución a la ACF teórica.

## Simulación de un modelo AR(1) con phi negativo

La siguiente figura corresponde nuevamente a un AR(1), pero esta vez con coeficiente negativo igual a menos 0,7.

Las realizaciones cambian un poco, ya que ahora los cambios son bastante bruscos, lo cual es una consecuencia de correlación negativa a un paso.

Tanto la ACF muestral como la teórica muestran un patrón cambiante de signo, consecuente con la forma de la autocorrelación para este modelo.

Nuevamente, la ACF muestral está relativamente cerca de la ACF teórica.

## Simulación de modelos MA(1)

Las siguientes dos figuras muestran el modelo MA(1) con coeficiente positivo y negativo, respectivamente.

En términos de realizaciones, esta luce muy similar a los casos AR(1), tanto positiva como negativa.

Ahora bien, la ACF tiene un cambio radical porque esta debería anularse para h mayor o igual a 2.

La teórica, por supuesto, muestra eso, y la ACF muestral no es exactamente cero, pero sí muy cercana a este valor.

Incluso en algunos casos disminuye y luego vuelve a aumentar.

Este efecto es conocido como correlación espuria, ya que no es una correlación real, sino que producto del término completamente aleatorio.

Adicionalmente, en este modelo la correlación teórica a un paso es menor a 0,5 en valor absoluto.

Esto se debe a que para cualquier valor de theta se cumple la siguiente relación para obtener una solución real.

Adicionalmente, la correlación a un paso muestral puede superar 0,5 debido a errores de muestra finita.

Lo mismo pasa con lags mayores a 1, que teóricamente son cero pero muestralmente son cercanos a cero.

## Simulación de un modelo ARMA(1,1)

La siguiente figura muestra el comportamiento de un ARMA(1,1), donde ambos coeficientes son positivos e iguales a 0,7.

Como se puede apreciar desde la realización, predomina el comportamiento tipo AR(1) positivo.

Esto se debe a que ambos coeficientes son positivos, por lo que la correlación a un paso aumenta, pero también aumenta la variabilidad, siendo consecuente con gamma 0 de un ARMA(1,1).

Desde la ACF, tanto teórica como muestral, predomina sustancialmente el comportamiento del AR(1).

De hecho, luce casi similar a la ACF del AR(1).

Esto se debe a que en el ARMA(1,1), la ACF teórica es la ACF del AR(1) amplificada por el factor siguiente, el cual es mayor a 1 si theta es positivo, como en este caso.

Entonces, para diferenciar un AR de un ARMA, no es suficiente la ACF, porque distintas estructuras pueden generar funciones de autocorrelación similares.

Por esta razón, es necesario complementar este análisis con otra herramienta, como la función de autocorrelación parcial, que veremos en detalle en la próxima clase.

## ¿Por qué creer en la ACF muestral?

Finalmente, ¿por qué debemos creer en la ACF muestral para acercarnos a la ACF teórica y así poder encontrar un buen modelo?

La razón radica en el teorema que muestra que la distribución conjunta de las ACF muestrales son asintóticamente normales, con media la ACF teórica y varianza controlada que disminuye a medida que aumenta el tamaño de la muestra.

Esto igualmente se puede verificar mediante simulaciones.

Consideremos un ARMA(1,1) con parámetros phi y theta iguales a 0,7, como en el caso anterior.

En un estudio de simulación de Monte Carlo, donde se simulan mil series de tamaño 40, 100 y 1000 respectivamente, podemos controlar las densidades de los estimadores muestrales de rho 1 hasta rho 5 respectivamente.

En un ARMA(1,1), con estos parámetros, se tiene que el valor teórico es:

- Rho 1: 0,84.
- Rho 2: 0,59.
- Rho 3: 0,41.
- Rho 4: 0,29.
- Rho 5: 0,20.

La figura en pantalla muestra la densidad estimada mediante Monte Carlo, donde la línea segmentada de color rojo corresponde al valor teórico.

Como se puede apreciar, cuando el valor de n es igual a 40, un valor pequeño, hay bastante incertidumbre en los estimadores puntuales.

Pero a medida que el valor de n crece, la incertidumbre se reduce y prácticamente el valor muestral corresponde al valor teórico, sobre todo en los lags pequeños como h igual a 1 o h igual a 2.

La teoría refuerza el hecho de que mientras más extensa sea la serie, más información tenemos para ajustar un modelo que replique el comportamiento de la ACF teórica.

Comprueba lo aprendido respondiendo a la siguiente pregunta.

# Tema 3: Aplicación a la serie SOI y GEE

Ahora veamos cómo aplicar la teoría anterior a la serie SOI y GEE, que son nuestros ejemplos reales.

Es necesario recordar que es difícil que una serie real tenga el comportamiento ideal de una serie simulada con un modelo conocido.

Nosotros solo vemos una realización y a partir de ello proponemos un modelo o varios modelos.

También es importante recalcar que la elección del modelo no queda simplemente vinculada al esquema visual, sino que más tarde veremos pruebas de bondad de ajuste para ratificar la selección.

## Aplicación a la serie SOI

Comenzando con la serie SOI, recordemos que la serie luce estable en media y varianza.

Además, la prueba de Box-Jenkins que aplicamos la clase pasada nos ratifica que hay dependencia importante y que debe ser moderada.

También recordemos que la ACF muestral clave en este punto es la que se muestra en pantalla, la cual muestra hasta tres ciclos completos de 12 meses cada uno.

Junto con esta gráfica, la tabla adjunta muestra los primeros 12 valores de la autocorrelación muestral de la serie SOI.

Se aprecia claramente que la ACF muestral es prácticamente cero desde el lag 10 en adelante, lo cual es consistente con el decaimiento de una estructura tipo AR(1) o ARMA(1,1), como las vistas en los ejemplos de simulación.

Otra característica relevante de la ACF muestral de SOI es que todas las correlaciones significativas son positivas.

Este es un indicio para creer que un parámetro phi de un AR(1) o de un ARMA(1,1) es positivo.

En el caso del modelo ARMA, se debe agregar la condición de que phi más theta por 1 más phi por theta es positivo, es decir, ambos factores positivos o ambos negativos.

Estas implicancias son directas desde las funciones de ACF teóricas.

Para proponer un modelo sencillo, basta con considerar la convergencia asintótica de la ACF muestral a la teórica.

Es decir, en el caso del AR(1), la correlación a un paso muestral converge a la correlación teórica igual a phi.

Por lo tanto, phi es igual a 0,6 aproximadamente.

En el caso del ARMA(1,1), se deben tener en cuenta dos convergencias:

- Rho 1 muestral a rho 1 teórica.
- Rho 2 muestral a rho 2 teórica.

Dado que es un sistema no lineal de dos ecuaciones y dos incógnitas, se obtiene la solución correspondiente.

Reemplazando rho 1 y rho 2 por sus estimadores puntuales, se obtienen los siguientes estimadores puntuales:

- Phi igual a 0,9 aproximadamente.
- Theta con dos valores posibles: menos 0,5 y menos 1,8 aproximadamente.

Ambos valores encontrados para theta satisfacen la condición anterior.

Entonces, se debe buscar otro mecanismo para distinguir entre ellos, ya que dos valores de parámetros diferentes generan la misma ACF teórica.

Esto se conoce como problema de identificabilidad.

Esto lo abordaremos en detalle en las próximas clases.

## Caso MA(1)

En el caso del MA(1), que es el menos apropiado de todos, de todas formas mostramos el ajuste para comparar con los anteriores.

En este caso, solo rho 1 es diferente de 0.

Por lo tanto, se tiene la expresión correspondiente para theta.

Reemplazando rho 1 por su valor muestral 0,6, se obtiene que el discriminante de la raíz cuadrática es menor a 0, por lo que se ratifica que el MA(1) no es apropiado.

Como en un MA(1) se sabe que rho 1 igual a 0,5 se alcanza solo en theta igual a 1, podríamos forzar theta igual a 1.

Aunque esto no es lo apropiado, es lo más cerca que tenemos por el momento.

Más adelante veremos métodos de estimación más adecuados, como máxima verosimilitud condicional o mínimos cuadrados condicionales, donde sí se podría estimar en cualquier contexto.

Finalmente, la siguiente figura muestra el ajuste de rojo y las ACF muestrales de color negro para cada modelo.

Se aprecia claramente que ninguno de los modelos ajustados replica correctamente la ACF muestral.

Esto significa que debemos explorar alternativas de estimación más eficaces y otras herramientas para identificar correctamente el modelo.

Una observación importante sobre el modelo ARMA(1,1) es que dos conjuntos de parámetros diferentes generan la misma ACF teórica.

Este es un problema estadístico serio que es denominado no identificable, lo cual veremos en detalle en las próximas clases para abordar desde una perspectiva teórica.

Vuelvo a lo aprendido respondiendo a la siguiente pregunta.

## Aplicación a la serie GEE

Con respecto a la serie GEE, si bien la transformación logarítmica más una diferenciación estabilizan la serie para lucir estable, similar a una serie estacionaria, aún queda un problema adicional.

La ACF muestral presenta una estructura que se escapa de las ACF de los modelos ARMA, porque la ACF que se muestra en pantalla indica que cada 12, 24 y 36 meses la correlación vuelve a subir muy significativamente, indicando que hay un componente periódico muy relevante.

Esto se puede apreciar tanto en la gráfica como en la tabla con los resultados de los primeros 18 lags.

En consecuencia, con las herramientas disponibles en esta etapa, no es posible proponer un modelo adecuado que capture correctamente la estructura de dependencia observada en la serie.

Esto motiva la necesidad de introducir modelos que consideren explícitamente la estacionalidad, lo cual será abordado en las clases posteriores.

# Ideas finales

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

El modelamiento de series de tiempo no consiste en replicar los datos observados, sino en capturar su estructura de dependencia.

En este contexto, la función de autocorrelación juega un rol fundamental, ya que permite identificar patrones que orienten la elección de modelos apropiados.

El comportamiento de la función de autocorrelación no es arbitrario, sino que está determinado por la estructura del modelo que genera la serie.

En particular, los modelos lineales permiten representar la serie como una combinación del pasado y de un componente aleatorio, lo que explica las distintas formas que puede adoptar la ACF en la práctica.

Una idea fundamental es que muchos modelos de serie de tiempo pueden representarse como combinaciones infinitas de perturbaciones aleatorias, lo que se conoce como representación MA infinito.

Esta representación permite comprender por qué la dependencia temporal se propaga en el tiempo y por qué la ACF puede decaer gradualmente o anularse después de ciertos rezagos.

El análisis basado en la ACF es una herramienta poderosa, pero tiene limitaciones.

Como se observó en la serie GEE, existen patrones más complejos, como la estacionalidad, que no pueden ser capturados por los modelos lineales básicos vistos hasta ahora, lo que motiva la necesidad de extender el marco de modelamiento en las siguientes clases.
