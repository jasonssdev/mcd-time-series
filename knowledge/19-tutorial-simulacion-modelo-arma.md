# Simulación de un Modelo ARMA(p,q)

Bienvenidos y bienvenidas a este nuevo videotutorial. En este videotutorial vamos a hablar sobre el modelo **ARMA(p,q)**, en particular, vamos a realizar una simulación de un modelo **ARMA(2,1)**, y vamos a ver cómo luce su función de autocorrelación y su función de autocorrelación parcial. 

## La ecuación del modelo ARMA(p,q)

Recordemos cómo es la ecuación de un modelo ARMA(p,q). Tenemos que nuestra serie temporal en el momento *t* puede ser explicada a partir de una constante, que está representada por la media de un proceso, porque esperamos que nuestra serie sea una serie estacionaria; depende de los *p* valores del pasado de nuestra serie y de los *q* valores de los errores del pasado. 

Ahora, para nosotros generar esta simulación de una serie ARMA o un proceso ARMA(p,q) tenemos que tener en cuenta dos vectores que están relacionados con los vectores de los parámetros de la parte autorregresiva y los parámetros de la parte de media móvil, y que vienen dados por esta forma de acá, donde se destaca que en la componente autorregresiva los *Fi* aparecen negativos y esto se explica porque todos estos valores que están aquí positivos, los pasamos restando hacia el lado izquierdo, obteniendo así que los valores autorregresivos están todos en la parte izquierda y los valores de los errores están todos en la parte derecha. Estas dos combinaciones lineales. 

## Simulación de un modelo ARMA(2,1)

Con esta estructura, nosotros vamos a generar la simulación de un modelo ARMA(2,1). Vamos a dejar fija una semilla para que usted pueda reproducir esta simulación y obtenga los mismos resultados de este tutorial, y vamos a generar el siguiente vector AR para sus parámetros. Uno, como lo tenemos ahí, menos 0,9 para menos *Fi_1* y 0,2 para menos *Fi_2*. Mientras que para los parámetros MA tenemos el 1 acá, y tenemos que *Theta_1* vale 0,9. 

Generamos el proceso ARMA a partir de esta función `ArmaProcess`, y vamos a simular 100 datos de la estructura de la serie que nosotros hemos creado. 

Cuando la graficamos, tenemos una serie como esta, que es una serie estacionaria que tiene una media constante, no tiene tendencia; por lo tanto, tiene mucha parte de ser una serie estacionaria, y tiene visualmente una varianza bastante controlada. Entonces, si nosotros no sabemos que es un modelo ARMA(2,1) podríamos decir que podríamos modelarla con un proceso ARMA(p,q) o un AR por separado, o una MA por separado. Eso, en esta instancia, no lo sabemos. 

## Funciones de Autocorrelación (ACF y PACF)

Si nosotros hacemos la función de autocorrelación y la función de autocorrelación parcial, ya sabemos cómo podría lucir en un AR por separado y un MA por separado. Pero, ahora, ¿cómo nosotros sabemos que es un proceso ARMA? O sea, que estos dos procesos están en la misma ecuación. 

Entonces, notemos cómo luce la función de autocorrelación y la función de autocorrelación parcial. No existe un patrón claro, como lo veníamos obteniendo en los procesos por separado. Es más, tenemos un decaimiento exponencial en la función de autocorrelación hacia 0 y aquí, en la función de autocorrelación parcial, ocurre lo mismo, pero de forma cíclica. Entonces, tenemos un decaimiento exponencial hacia 0. 

Por lo tanto, cuando nosotros tenemos un modelo ARMA(p,q) en nuestra serie temporal, no tenemos patrones claros en la función de autocorrelación y en la función de autocorrelación parcial. 

## Criterios de Selección (AIC y BIC)

Por lo tanto, ¿qué se sugiere hacer aquí? Es generar valores que podrían ser apropiados como candidatos para un *p* y para un *q*. Uno podría pensar, aquí es generar un "lag", un 4; podría ser un *q* igual 4 y aquí podríamos pensar hasta quizás, no sé, no está muy claro, pero podría ser un *p* igual 5, por ejemplo. 

Entonces, generar toda esa lista de combinaciones que podemos generar con *p* igual 5 y un *q* igual 4, y luego de eso, probarlos todos y generar una elección a partir de otros criterios, como puede ser, por ejemplo:
* El **criterio de información de Akaike**, que lo va a ver en su momento; 
* O el **criterio de información bayesiana**. 

Que el primero se denota como el **AIC** y el otro como el **BIC**. 

## Conclusión

Hasta ahora, nosotros tenemos cómo luce su función de autocorrelación parcial para un modelo AR. Sabemos cómo luce la función de autocorrelación para un modelo MA. Y en este tutorial, ya sabemos cómo luce la función de autocorrelación y la función de autocorrelación parcial para un modelo ARMA(p,q), en particular un ARMA(2,1). 

Espero que este tutorial haya sido de su agrado y nos vemos en el siguiente tutorial.
