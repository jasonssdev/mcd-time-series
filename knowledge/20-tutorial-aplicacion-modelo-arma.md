# Aplicación a Datos Reales: Modelado de Series Temporales

Bienvenidos y bienvenidas a este nuevo videotutorial en el cual vamos a generar una aplicación a datos reales y con el fin de proponer modelos a una serie temporal que podrían ser buenos modelos para ajustarse a nuestra serie original. 

## Obtención de los Datos

Entonces, para esto vamos a usar nuestra librería **Darts** y, en particular, también vamos a considerar la librería de **Yahoo Finance** que nos permite descargar datos de acciones que estén cotizando en la bolsa americana. 

Para esto, la descarga la vamos a hacer a partir de este comando de acá y les vamos a decir los años que nosotros queremos descargar. En particular, vamos a considerar desde enero 2014 hasta septiembre de 2023 y le estamos diciendo que tienen que ser datos de un mes, o sea, vamos a considerar los cierres mensuales de nuestra acción de **Microsoft**. 

## Análisis de Estacionariedad y Transformaciones

La gráfica de nuestra acción luce así, tiene una tendencia clara, por lo tanto, visualmente sabemos que no es estacionaria, por lo tanto, eso nos genera un problema. Tenemos que usar técnicas que hemos aprendido en tutoriales anteriores para modificar nuestra serie temporal y que cumpla el supuesto que nosotros queremos que es, en particular, que la serie sea estacionaria. 

Una de las formas que nosotros podemos hacer que nuestra serie sea estacionaria es diferenciándola. Pero fíjense que es lo que pasa aquí. Cuando nosotros diferenciamos nuestra serie, vemos que le quitamos la tendencia, buen punto. Sin embargo, no tiene una varianza que sea controlada, sino que tiene una varianza constante, levemente constante aquí, pero aquí se descontrola demasiado. 

Por lo tanto, diferenciar la serie, en primera instancia, no es una buena forma para modelar nuestra serie de Microsoft. Por lo tanto, ¿qué vamos a hacer? Vamos a aplicar el **logaritmo** a nuestra serie original y luego de eso vamos a aplicar la **diferenciación**. 

¿Qué logramos con eso? Fíjense lo siguiente: logramos que nuestra serie sea estacionaria gracias a la diferenciación, pero el logaritmo nos permite transformar esta serie con varianza no tan controlada a una serie con una varianza más constante. Por lo tanto, esto podría ser una serie que es estacionaria y que podríamos modelar. 

## Selección de Modelos Candidatos (ACF y PACF)

La pregunta es, ¿qué modelos apropiados podríamos considerar para esta serie?, que es la serie diferenciada de los logaritmos de la acción de Microsoft. 

Entonces, para eso, realizamos las gráficas del **ACF** y las gráficas del **PACF**, la función de autocorrelación y la función de autocorrelación parcial, y obtenemos estos dos gráficos. 

Entonces, nosotros sabemos que cuando hay un lag que es significativo y después los otros se hacen abruptamente a 0 en el ACF, podría ser un candidato, un modelo **MA**; mientras que en la PACF si tenemos lags que son considerables y después se hacen abruptamente 0, son un modelo autorregresivo, y cuando es un modelo **ARMA**, nosotros tenemos decaimientos exponenciales y no hay un patrón bien claro de cuál es el que se destaca. 

Pero aquí nosotros podríamos decir: "Okey, como este lag es el que se destaca en el ACF, podríamos pensar que un buen modelo podría ser un **MA(1)**, mientras que aquí en el PACF, un buen modelo que se podría proponer es un **AR(1)**". O sea, por un lado tenemos un MA(1) como un buen modelo u otro podría ser un AR(1). 

Por lo tanto, tenemos dos candidatos, tenemos el **AR(1)** y el **MA(1)**. Sin embargo, como no tenemos claro si en un proceso ARMA no hay un patrón definido, nosotros sabemos simplemente que tiene que haber un decaimiento hacia 0, nosotros también podríamos proponer que un buen modelo que se ajuste a nuestra serie podría ser un **ARMA(1, 1)**. 

## Criterios de Selección (AIC y BIC)

Por lo tanto, tenemos tres modelos candidatos de los cuales no sabemos cuál va a ser el mejor y eso lo tenemos que ver con otras técnicas de selección de modelos, donde lo veremos más adelante, y se basa a partir de dos criterios de selección: uno, a partir del criterio de información de Akaike, que usualmente se llama el **AIC**, o el **BIC**, que es el criterio de información bayesiano. 

Estos dos indicadores nos permiten elegir un mejor modelo cuando tenemos una lista larga de modelos que podrían ser apropiados a partir de lo que nosotros hemos visto que, en este caso, en el ACF y en el PACF, estos dos modelos podrían ser candidatos, pero nosotros proponemos uno más, que es la combinación del *p* candidato que nosotros tenemos y del *q* candidato que nosotros tenemos. 

## Transformación Inversa

Pero aquí hay algo que hay que tener en cuenta: estos tres modelos candidatos son candidatos para esta serie de acá, que es la serie de los logaritmos y que está diferenciada. Por lo tanto, para poder tener nuestra serie original, que es predecir el valor de nuestra serie de Microsoft, tenemos que hacer la transformación inversa, ¿qué quiere decir eso? Hacer la suma acumulada para retroceder en la diferenciación y después aplicar la exponencial porque hemos aplicado el logaritmo natural. 

Espero que esta aplicación a una serie de datos reales haya sido de su agrado y que le haya aclarado ciertos puntos importantes de las series temporales y nos vemos en un siguiente tutorial.
