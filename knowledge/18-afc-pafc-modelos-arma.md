# ¿Cómo calcular la ACF y PACF en modelos ARMA?

Bienvenidos y bienvenidas a una nueva clase. 

La causalidad e invertibilidad son dos características esenciales en procesos ARMA. Específicamente, la causalidad, o más bien la representación MA infinito a través de los coeficientes *epsi sub j*, tomará mayor relevancia al momento de determinar la función de autocovarianza. Mientras que la invertibilidad, o más bien la representación AR infinito, a través de los coeficientes *pi sub j*, será muy importante para definir la predicción de las observaciones futuras. 

Cabe destacar que los modelos ARMA incluyen los modelos AR y MA. Es decir, estos últimos son un caso particular del ARMA. Ya que, en efecto, un ARMA(p,0) es igual a un AR(p) y un ARMA(0,q) es igual a un MA(q). 

Esta clase está enfocada en cómo contextualizar las características más relevantes de los procesos lineales. Con el objetivo de determinar la función de autocorrelación, ACF, y la función de autocorrelación parcial, PACF. 

En esta clase se revisarán los siguientes temas:
* **Tema 1:** ACF para MA(q), AR(p) y ARMA(p,q). 
* **Tema 2:** PACF y algoritmo de Durbin-Levinson. 

---

## Tema 1: ACF para MA(q), AR(p) y ARMA(p,q)

Como vimos anteriormente, para un proceso lineal *x_t* causal, es decir, *x_t* es igual a una serie de 0 a infinito de *psi sub j* por *épsilon t - j*. Su función de autocovarianza está dada por *gamma sub x(h)* = *sigma* cuadrado por la serie de *j* = 0 a infinito, de *psi sub j* por *psi sub j + h*. 

La cual basta con definirla para *h* mayor o igual a 0, ya que tenemos la propiedad que *gamma sub x(-h)* = *gamma sub x(h)*. Que nos permite extender la función a los casos en que *h* es negativo. 

Para el caso del MA(q), la representación causal es directa. Por definición, con *epsi sub j* igual a *theta j* para *j* igual 2 hasta *q*. Y *epsi j* igual 0 para *j* mayor o igual a *q* más 1, redefiniendo *theta sub 0* como *epsi sub 0* igual a 1. 

Así, *gamma sub x(0)* es igual a *sigma* cuadrado por *theta 1* al cuadrado, *theta 2* al cuadrado, hasta *theta q* al cuadrado. *Gamma sub x(h)* se muestra en pantalla para *h* menor a *q*. Y mientras que *gamma sub x(h)* es igual a cero para *h* mayor o igual a *q* + 1. 

Notar que el índice superior de la sumatoria comienza a disminuir hasta llegar a 0, a medida que aumenta *h*. Esto se debe a que *epsi sub j + h* es 0 cuando *j + h* es mayor o igual a *q* + 1. 

En consecuencia, la ACF del modelo MA(q) queda dada por:
* *rho sub x(0)* = 1. 
* *rho sub x(1)* = a *theta 1* + *theta 1* por *theta 2* + *theta 2* por *theta 3*, así hasta *theta q-1* por *theta q*. Dividido por 1 más los *theta sub j* al cuadrado.
* *rho sub 2(x)* se muestra en pantalla.
* *rho sub x(h)* es igual a 0 para *h* mayor o igual a *q* + 1. 

Por lo tanto, la ACF de un MA(q) tiene a lo más hasta el lag *q* diferente de 0 y luego todos los demás son 0. Notar que los lags intermedios entre 1 y *q* pueden ser 0 si la configuración de los parámetros lo permite, es decir, si el numerador es 0. 

Por ejemplo, para los procesos MA(2), *x_t* e *y_t* definidos a continuación:
* *x_t* es igual a *épsilon t* + 0,5 *épsilon t - 2*. 
* E *y_t* = *épsilon t* - 0,8 *épsilon t - 1* + 0,5 *épsilon t - 2*, donde *épsilon t* es un ruido blanco de media 0 y varianza 1. 

Se tiene que la autocorrelación del primer orden es *rho sub x(1)* = 0. Y *rho sub y(1)* es aproximadamente -0,640. Mientras que la autocorrelación de segundo orden es *rho sub x(2)* = 0,4 y *rho sub y(2)* = 0,2646. Y para un lag mayor a 2, ambas autocorrelaciones son 0. 

### Representación causal de los procesos AR(p)

Para el caso de los procesos AR(p) estacionarios, la representación causal no es tan directa. Pero sí existen dos procedimientos que permiten encontrar los coeficientes *epsi sub j*. 

Para ejemplificar estos procedimientos, consideremos el AR(2), que se muestra a continuación. Al asumir que existe la representación causal, *x sub t* igual a *epsi(B)* por *épsilon t*. Se tiene que el producto de los operadores autorregresivos es igual a la identidad. *Phi 2(B)* por *epsi(B)* igual a la identidad. 

1. **El primer procedimiento** consiste en expresar el operador *phi 2(B)* a la -1 en suma de fracciones parciales. Este procedimiento fue mencionado en la clase anterior. 
2. **El segundo procedimiento** consiste en igualar los coeficientes de los polinomios que aparecen en ambos lados de la ecuación *phi 2(B)* por *epsi(B)* igual a identidad. Tal como se muestra en pantalla. 

Es decir, 1 = 1, que corresponde al coeficiente de la identidad, siempre se cumple esta igualdad ya que *epsi sub 0* = 1. *psi sub 1* - *phi 1* = 0, que es el coeficiente de B. Y así llegamos hasta *epsi sub j* - *phi 1* por *epsi sub j - 1* - *epsi 2* por *epsi sub j - 2*, que es el coeficiente de B a la *j* para *j* mayor o igual a 2. Como se puede apreciar, existe una recurrencia a partir de *j* = 2 en adelante. 

Mientras que para el coeficiente de B, no sigue la misma estructura. Es decir:
* 1 = 1, correspondiente al coeficiente de la identidad. Este siempre se cumple, ya que *epsi sub 0* = 1. 
* *epsi(1)* - *phi(1)* = 0, que es el coeficiente de B. 
* *epsi(2)* - *phi 1* por *epsi(1)* - *phi(2)* = 0, que es el coeficiente de B cuadrado. 
* Y así llegamos hasta *epsi sub j* - *phi 1* por *epsi sub j - 1* - *phi 2* por *epsi sub j - 2* = 0. Que es el coeficiente de B a la *j* para un *j* mayor o igual a 2. 

Como se puede apreciar, existe una recurrencia a partir de *j* = 2 en adelante. Mientras que para el coeficiente de B no sigue la misma estructura. La recurrencia puede ser resuelta utilizando ecuaciones en diferencia homogénea de orden 2. Cuya condición inicial son las primeras ecuaciones, es decir, *psi 0* = 1 y *psi 1* = *phi 1*. 

La ecuación en diferencia se resuelve asumiendo que las soluciones de la forma *psi j* igual a *lambda* a la -*j*. La cual, reemplazando la ecuación en diferencia, se obtiene que *lambda* a la -*j* por (1 - *phi 1 lambda* - *phi 2 lambda* cuadrado) = 0. Como *lambda* a la -*j* es distinto de 0, el polinomio característico *p(lambda)* = 1 - *phi 1 lambda* - *phi 2 lambda* cuadrado. Que es exactamente igual al operador polinomial autorregresivo. 

Nos permite encontrar los valores de *lambda* que resuelven la ecuación en diferencia. Estos valores corresponden a las raíces del polinomio, la cual está dada como se muestra a continuación. Donde, como en toda ecuación cuadrática, existen tres casos posibles:

* **Raíces reales diferentes:** Se obtienen cuando el discriminante es positivo, es decir, cuando *phi 1* al cuadrado + 4 *phi 2* es mayor a 0. Luego, la solución en *lambda 1* y *lambda 2* se muestran en pantalla. 
* **Raíces reales iguales:** Se obtienen cuando el discriminante es cero, es decir, para *phi 1* al cuadrado + 4 *phi 2* = 0. Y nuevamente, la solución está en pantalla. 
* **Raíces complejas:** Se obtienen cuando el discriminante es negativo, es decir, cuando *phi 1* al cuadrado + 4 *phi 2* es menor a cero. Nuevamente, la solución está en pantalla, donde *i* es la unidad imaginaria, es decir, es igual a raíz de -1. 

La naturaleza de las raíces determinará la forma de la solución de la ecuación en diferencias. De este modo, tenemos los siguientes casos:
* **Caso 1:** *lambda 1*, *lambda 2* en los reales con *lambda 1* distinto de *lambda 2*. Así, *psi j* será constante 1 por *lambda 1* a la -*j* más constante 2 por *lambda 2* a la -*j*. 
* **Caso 2:** *lambda 1* y *lambda 2* en los reales, con *lambda 1* = *lambda 2* = *lambda*. Así *psi j* será constante 1 *lambda* a la -*j* más constante 2 por *j* por *lambda* a la -*j*. 
* **Caso 3:** *lambda 1*, *lambda 2* en los complejos, con *lambda 2* igual al conjugado de *lambda 1*. En este caso, *psi j* será constante 1, *lambda 1* a la -*j*, más constante 1 conjugada por *lambda 1* conjugado a la -*j*. En esta última, se suele utilizar la forma polar de un número complejo, de donde quedan los valores *psi j* oscilantes. 

Una vez obtenidos los coeficientes *psi j*, se procede a calcular la función de autocovarianza y autocorrelación respectivamente. A través de las expresiones que ya tenemos:
* *Gamma x(h)* es igual a *sigma* cuadrado por la serie de *j* = 0 a infinito de *psi j* por *psi j + h*. 
* Y *rho x(h)* es igual a *gamma(h)* dividido *gamma(0)*. 

Donde los coeficientes *psi j* son absolutamente sumables si y solo si *lambda 1* en módulo es mayor a 1 y *lambda 2* en módulo es mayor a 1. 

Por ejemplo, para el proceso *x_t* definido a continuación: *x_t* igual a cinco sextos *x_t - 1* menos un sexto *x_t - 2* + *épsilon t*, donde *épsilon t* es un ruido blanco de media 0 y varianza 10. El polinomio característico y sus respectivas raíces se muestran a continuación. Donde *lambda 1* = 2 y *lambda 2* = 3, el cual corresponde al caso de raíces reales diferentes. Y como ambas son mayores a 1, se tiene que los *psi j* son absolutamente sumables. Y están dados por *psi j* = constante 1 por 2 a la -*j* + constante 2 por 3 a la -*j*. 

Para determinar las constantes c1 y c2, se utilizan las condiciones iniciales: *psi 0* = 1, *psi 1* = cinco sextos. 
* Así, para *j* = 0 se tiene que c1 + c2 = 1.
* Mientras que para *j* = 1 se tiene que c1/2 + c2/3 = cinco sextos. 

Luego, c1 = 3 y c2 = -2. Por lo tanto, la solución final para *psi j* = 3/2 a la *j* - 2/3 a la *j* para *j* = 0 en adelante. 

Adicionalmente, si quisiéramos utilizar el cálculo anterior para obtener *rho x(h)*. Se tiene que *gamma x(h)* = 48/2 a la *h* - 27/3 a la *h*, por lo que *rho x(h)* se muestra en pantalla, el cual tiende a 0 cuando *h* tiende a infinito. 

Notar que para este ejemplo *rho x(h)* es mayor a 0 y decae rápidamente a 0, tal como se observa en la siguiente figura. Sin embargo, no todos los AR(2) tienen esta estructura en la autocorrelación. Ya que la forma con que decae dependerá del tipo de raíces del polinomio característico. Tal como se muestra en el siguiente gráfico, el cual corresponde al proceso *y_t*, dado por *y_t* = -0,64 *y_t - 2* + *épsilon t*. 

Así el polinomio característico es igual a 1 + 0,64 *lambda* cuadrado. Destaca claramente el decaimiento sinusoidal, junto con los lags impares que son cero. Esto se debe a que el polinomio característico en sub cero obtiene raíces complejas. Específicamente, *lambda* = +-1,25*i*. 

Por último, el detalle visto en el AR(2) se generaliza al AR(p) y al ARMA(p,q) de forma análoga. Donde los coeficientes *psi j* se determinan resolviendo una ecuación en diferencias homogénea. 

En el caso del AR(p), la ecuación *phi p(B)* por *psi(B)* igual a la entidad es equivalente a la siguiente expresión. De donde, igualando los coeficientes de ambos operadores, se obtiene que:
* 1 = 1, que es el coeficiente de la identidad. 
* *Psi 1* - *phi 1* = 0, coeficiente de B. 
* Y así continuamos hasta el coeficiente de B a la *j*. Dado por *psi j* - *phi 1 psi j - 1* - *phi 2 psi j - 2* hasta -*phi p* por *psi j - p* = 0, para *j* mayor o igual a *p*. 

Así, las primeras *p* ecuaciones, equivalente a *j* igual 0, 1 hasta *p - 1*, son utilizadas como condiciones iniciales. Y a partir de *j* igual a *p*, se resuelve la ecuación en diferencia, cuya solución se propone como *phi j* igual a *lambda* a la -*j*. Obteniendo el polinomio característico *p(lambda)* = 1 - *phi 1 lambda* - *phi 2 lambda* cuadrado hasta -*phi p lambda* a la *p*. El cual es idéntico al operador autorregresivo. 

Independiente de la configuración, terminaremos en alguno de los tres casos descritos por el AR(2). Así, por ejemplo, si todas las raíces son reales diferentes. La forma general de los coeficientes *psi j* sería c1 *lambda 1* a la -*j* más hasta la constante c_p *lambda p* a la -*j*. Y las condiciones iniciales servirán para encontrar los coeficientes c1, c2, hasta c_p. 

En el caso del ARMA(p,q), se procede del mismo modo. El único cambio es la ecuación de operadores diferenciales, ya que en este caso se tiene que *phi p(B)* por *psi(B)* = *theta q(B)*. Que es equivalente a la siguiente expresión que se muestra en pantalla. De donde, igualando los coeficientes de ambos operadores, se obtiene que:
* 1 = 1, que es el coeficiente de la identidad. 
* *epsi 1* - *phi 1* = *theta 1*, que es el coeficiente de B. 
* *Psi 2* - *phi 1* por *psi 1* - *phi 2* = *theta 2*, que es el coeficiente de B cuadrado, y así continúa la recurrencia. 

La forma general dependerá de *p* y *q*, en el sentido de cuál de los dos es mayor. De donde, al considerar *phi j* = 0 para *j* mayor a *p* y *theta j* = 0 para *j* mayor a *q*. Se tiene que la forma general de la ecuación en diferencia está dada por la siguiente expresión. Destacando que *j* es mayor o igual al máximo entre *p* y *q* + 1. Cuyas condiciones iniciales se muestran a continuación para *j* entre 0 hasta el máximo de los puntos anteriores. 

Dada la forma general de los coeficientes *psi j*, se tiene que la función de autocorrelación *rho(h)* de los procesos ARMA(p, q) decaerá a 0 exponencialmente a medida que *h* tiende a infinito. Aunque la forma del decaimiento dependerá de los coeficientes *phi* y *theta*. 

> Prueba tu aprendizaje respondiendo la siguiente pregunta. 

---

## Tema 2: PACF y algoritmo de Durbin-Levinson

La función de autocorrelación parcial entrega información complementaria que puede servir para identificar un modelo ARMA(p,q). Dado que la ACF por sí sola tiende a confundirse, ya que la configuración de las raíces puede dar formas similares. 

Como vimos desde el punto de vista muestral, la autocorrelación parcial consiste en medir la correlación entre *x_t* y *x_{t+h}*. Eliminando el efecto de las observaciones intermediarias. Esto lo conseguimos realizando dos regresiones y luego calculando la correlación de Pearson entre los residuos. 

Desde el punto de vista de variable aleatoria, se puede realizar el mismo procedimiento. Para ejemplificarlo, consideremos un AR(1) causal, *x_t* igual a *phi 1 x_t - 1* + *épsilon t*. 

Por definición, la autocorrelación parcial entre *x_t* y *x_t + 1* es igual a la autocorrelación simple. Así que calculamos la autocorrelación parcial entre *x_t* y *x_t + 2* utilizando *x gorro t + 2* y *x gorro t*. 

Se tiene que *phi 2* es igual a la correlación entre *x_t* - *x gorro t* y *x_t + 2* - *x gorro t + 2*, que sería igual a *x_t* - *phi 1 x_t + 1* con *épsilon t + 2* = 0. La última igualdad se tiene desde la representación causal de *x_t*, que nos indica que el proceso depende del error actual y pasado. Mientras que *x_t* - *phi x_t + 1* depende de los errores de *épsilon t + 1*, *épsilon t*, y así hacia atrás. Por lo tanto, *x_t* - *phi 1 x_t + 1* y *épsilon t + 2* tienen correlación 0. 

Notar que cuando el proceso es gaussiano, remover el efecto de las variables intermedias de forma lineal es equivalente a calcular directamente *phi 2* como la correlación entre *x_t* y *x_t - 2* dado *x_t - 1*. En este caso, el argumento consiste en que, dado *x_t - 1*, el término *phi 1 x_t - 1* es conocido. Por lo que no será aleatorio, y como la covarianza de una constante y una variable aleatoria es 0, este término se puede quitar sin problema. 

Siguiendo este mismo argumento, es fácil ver que para un AR(p) causal, la correlación parcial entre *x_t* y *x_t + h* para *h* mayor a *p* es 0. Mientras que la correlación parcial entre *x_t* y *x_t + p* es *phi p*. Esto quiere decir que la PACF de un AR tiene un comportamiento similar a la ACF de un MA. 

En el caso de los modelos MA(q) invertibles y ARMA(p,q) causales e invertibles, el cálculo de la correlación parcial se complica. Ya que desde la representación AR infinito se tiene que el error *épsilon t* está dado a continuación. Es decir, siguiendo la misma lógica del AR(p), la autocorrelación parcial nunca se anulará para estos casos. Ya que los coeficientes *pi j* no se anulan para el caso MA y ARMA. 

Para poder determinar las autocorrelaciones parciales, utilizaremos el algoritmo de Durbin-Levinson. El cual está diseñado para la predicción. La relación que tiene con la PACF radica en que el predictor lineal coincide con las regresiones que realizamos para determinar la correlación parcial. En pantalla se muestra dicho algoritmo. 

Sin entrar en todos los detalles del algoritmo. Para calcular la PACF, solo debemos fijarnos en la recurrencia relativa a los coeficientes *phi nn*. De forma auxiliar, se definen los coeficientes *phi nk*, los cuales se necesitan solo para calcular la autocorrelación parcial *phi nn*. Notar que la autocorrelación parcial depende de la ACF. 

En primer lugar, veamos cómo funciona el algoritmo de Durbin-Levinson para el AR(1) causal, dado por *x_t* = *phi 1 x_t - 1* + *épsilon t*. De donde ya sabemos que *rho(h)* es igual a *phi 1* a la *h*. Notar que cuando el índice superior de la sumatoria es menor al índice inferior, dicho valor lo asumiremos como 0. 

Luego, en pantalla, se muestra la aplicación del algoritmo Durbin-Levinson para obtener *phi sub 22* y *phi sub 33*. Continuando con la recurrencia, en pantalla se muestra el cálculo para *phi 44* y *phi 55*, los cuales ambos son 0. Notar que si *phi sub jj* es igual a 0, entonces *phi 1j* es igual a *phi 1* y *phi jk* es igual a 0, para *k* = 2 hasta *j - 1*. Y para todo *j* igual a 2, 3, hasta infinito. Por lo tanto, *phi sub hh* = 0, obteniendo el mismo resultado que ya teníamos para el AR(1). 

Ahora que ya vimos cómo opera el algoritmo de Durbin-Levinson, podemos determinar la PACF de un MA(q) o un ARMA(p,q). Por ejemplo, para el MA(1) invertible, *x_t* = a *épsilon t* más *theta épsilon t - 1*. 

Sabemos que *rho(0)* es 1, *rho(1)* es *theta* / (1 + *theta* al cuadrado). Y *rho(h)* = 0 para *h* mayor o igual a 2. Luego, en pantalla se muestra el cálculo para *phi 22* y *phi 33*. En este último, se determina el valor auxiliar *phi 21*. Al proceder de forma iterativa, se puede probar que *phi hh* está dado, como se muestra en pantalla, para *h* mayor o igual a 1. El cual tiende a 0 a medida que *h* tiende a infinito. 

Si *theta* es positivo, *phi h* oscila entre valores positivos y negativos. Mientras que si *theta* es negativo, la PACF será negativa para todo *h*. Para visualizar lo anterior, la figura en pantalla muestra la PACF de un MA(1) con *theta* = 0.5. Y otro MA(1) con *theta* = -0.5, respectivamente. 

Por último, la PACF de un MA(q) invertible tendrá el mismo comportamiento que el MA(1). Es decir, decaerá a 0 y la forma en que decae dependerá de los coeficientes. Análogamente, la PACF de un ARMA(p,q) causal e invertible tiene el mismo comportamiento de un MA(q). 

En resumen, las funciones de autocorrelación *rho(h)* y *phi sub hh* de proceso estacionario se comportan como se muestra en la siguiente tabla. Destacando que en el ARMA, ambas funciones decaen exponencialmente a 0. 

> Prueba de aprendizaje respondiendo a la siguiente pregunta. 

---

## Resumen de la clase

Hemos llegado al final de la clase. Ahora recordemos las ideas más importantes:

* Las ecuaciones en diferencia permiten determinar los coeficientes *psi sub j* de la representación causal de los procesos AR y ARMA. 
* En los modelos MA(q) invertibles, la ACF es exactamente 0 para *h* mayor a *q*. Mientras que la PACF decae a 0 exponencialmente. 
* En los modelos AR(p) causales, la PACF es exactamente 0 para *h* mayor a *p*, mientras que la ACF decae a 0 exponencialmente. 
* En los modelos ARMA(p,q) causales e invertibles, tanto la ACF como la PACF decaen a 0 exponencialmente. 
* El algoritmo de Durbin-Levinson permite calcular la función de autocorrelación parcial, *phi sub hh*, de los procesos lineales AR, MA y ARMA. 
* Además, a partir de este algoritmo vemos que la PACF es una función de la función de autocorrelación *rho(h)*. 
* Y reconocer el comportamiento de la ACF y PACF de los modelos ARMA servirá como una herramienta para proponer modelos a partir de las autocorrelaciones muestrales.
