# Representación de un ARMA como proceso lineal

Bienvenidos y bienvenidas a una nueva clase. 

En la clase pasada vimos los procesos lineales desde una perspectiva general. Y que dadas estas condiciones podemos determinar la función de autocovarianza de un modelo lineal. Donde también mencionamos que los modelos típicamente utilizados como AR, MA y ARMA son lineales. 

Ahora bien, para el caso del MA(q), esto es evidente desde su definición. Sin embargo, para los otros procesos, puede llegar a ser complejo describirlos como proceso lineal. 

En el caso del AR(1), resulta directo expandiendo la recurrencia. Sin embargo, en un AR(2) o bien en un ARMA(1,1), esto no es tan evidente. Por ejemplo, para el ARMA(1,1) se muestra en pantalla la expansión hasta el cuarto término. Cabe destacar que un proceso queda en la forma lineal cuando logramos encontrar los coeficientes **epsi sub j** de la serie. Y como se puede apreciar de este ejemplo del ARMA(1,1), no es tan evidente que el valor de **epsi sub j**, en términos de **phi** y **theta** es:

* **Epsi0 = 1**
* **epsi1 = phi + theta**
* **epsi sub j = epsi 1 por phi elevado a j -1** para j igual 2 en adelante
* **epsi sub j = 0** para j negativo. 

A su vez, la condición de absoluta sumabilidad de los coeficientes **epsi sub j** permite definir condiciones sobre los parámetros autoregresivos, de modo de garantizar la estacionalidad. 

En esta clase, veremos una estrategia que nos permitirá encontrar dicha representación. Así como también condiciones específicas que garanticen la estacionalidad de los procesos. 

En esta clase, se revisarán los siguientes temas:
1. **Tema 1:** Operador de rezago y polinomios característicos. 
2. **Tema 2:** Parámetros redundantes. 
3. **Tema 3:** Representación MA infinito y AR infinito, causalidad e invertibilidad. 

*[SOUND]*

---

## Tema 1: Operador de rezago y polinomios característicos

Para expresar los modelos lineales de forma compacta, se define el operador de rezago u operador *backshift* como **B aplicado a X de t, igual a X de t - 1**. El cual permite escribir la serie rezagada en un lag en términos del presente de la serie. Naturalmente, este operador se puede aplicar de forma recursiva. Permitiendo así expresar el término rezagado **j** instantes en el pasado y escribirlo en términos del presente. 

Por ejemplo:
* **B cuadrado xt = X de t - 2**. 
* Y en general, **B a la j de xt = X de t - j**, tal como se muestra en pantalla. 

Para ver la aplicabilidad de este operador, el proceso AR(1) quedaría escrito como sigue:
**Identidad menos phi B por xt es igual a épsilon t.** Donde identidad es igual a **B a 0**, representa el operador identidad. Es decir, **identidad aplicado a X de t es igual a X de t**. 

De manera similar podemos usar este operador para describir el ARMA(2,1) de la siguiente forma: 
**Identidad menos phi1 B menos phi2 B cuadrado, por xt igual a identidad más theta B por épsilon t.** Por lo tanto, definiendo:
* El operador autoregresivo como **phi sub p(B) igual a la identidad menos phi1 por B menos phi2 por B cuadrado, hasta phi sub p por B a la p.** * Y el operador de media móvil como **theta sub q(B) igual a la identidad más theta1 por B más theta2 por B cuadrado, hasta theta sub q por B a la q.** Podemos finalmente escribir de forma compacta los modelos:
* **MA(q)** como **x sub t igual a theta sub q(B) por épsilon t.** * **AR(p)** como **phi sub p(B) por x de t igual a épsilon t.** * Y **ARMA(p,q)** como **phi sub p(B) por xt igual a theta sub q(B) por épsilon t.** Donde los subíndices **p** y **q** hacen referencia al orden del operador polinomial y del modelo, respectivamente. De esta forma, por ejemplo, los polinomios asociados al proceso ARMA(2,1) son **phi sub 2(B) igual a la identidad menos phi 1(B) menos phi 2(B) cuadrado**, y **theta sub 1(B) igual a 1 más theta por B**. 

Notar que **phi sub p(B)** y **theta sub q(B)** son operadores. Por lo que no es posible llegar y realizar algunas manipulaciones algebraicas, tales como dividir. En su lugar, se suele escribir los respectivos polinomios característicos utilizando una variable auxiliar **z** en **R**. Con la misma forma de los respectivos operadores. Es decir, el polinomio autoregresivo será **phi sub p(z)** y el polinomio de media móvil será **theta sub q(z)**. 

Esto nos permitirá, por ejemplo, determinar que **identidad menos phi(B) a la -1 es igual a la serie de j = 0 hasta infinito de phi a la j por B a la j**. Ya que la serie geométrica de la suma de **j igual 0 hasta infinito de r a la j**, eso es igual a **1 dividido 1 - r**, cuando el valor absoluto de **r** es menor a 1. Así, tomando **r = phi por z**, se tiene el resultado anterior. En consecuencia, el orden del polinomio y operador es infinito. 

> Prueba tu aprendizaje respondiendo a la siguiente pregunta.

*[SOUND]*

---

## Tema 2: Parámetros redundantes

Con la ayuda de los polinomios característicos, podemos apreciar que un modelo ARMA puede tener parámetros redundantes. Ya que los polinomios autoregresivo y media móvil pueden tener raíces en común. Es decir, podríamos especificar un modelo de mayor orden del que realmente es. 

Por ejemplo, considere el proceso: 
**x sub t igual a un sexto x de t -1, más un sexto por x de t -2, más epsilón t, dos quinceavos epsilón t -1, menos un quinceavos epsilón t -2**, y epsilón, un ruido blanco de media 0 y varianza 1. 

A primera vista, este proceso es un ARMA(2,2), cuyos polinomios característicos son los que se muestran a continuación. Los cuales, al factorizarlos, se aprecia que ambos polinomios tienen un factor en común. Por lo que en términos de operadores el proceso puede ser escrito como sigue, concluyendo que el proceso en realidad es un ARMA(1,1). 

En todo modelo ARMA debemos eliminar la redundancia de los parámetros. Esto se consigue imponiendo la condición de que los polinomios característicos autoregresivo y media móvil no contengan raíz en común. 

> Prueba tu aprendizaje respondiendo la siguiente pregunta.

*[SOUND]*

---

## Tema 3: Representación MA infinito y AR infinito, causalidad e invertibilidad

Retomando los procesos lineales en su forma general, **x de t es igual a la serie de j igual menos infinito a infinito de psi sub j por epsilon t - j.** Se tiene que **x sub t** es una combinación lineal del ruido blanco. Que depende tanto del presente, del pasado, así como el futuro de dicho error. 

Notar que el proceso dependerá del futuro cuando **psi sub j** sea distinto de 0 para **j** negativo. Así, cuando el proceso depende exclusivamente del presente y del pasado del error, diremos que dicho proceso es causal. 

Estos procesos también podemos escribirlos a través del operador **B**, tal como se muestra en pantalla. Donde **epsi(B) es igual a la identidad más epsi1(B) más epsi2 por B cuadrado más hasta epsi sub j por B a la j.** Y así sucesivamente, obteniendo un operador de orden infinito. Es decir, **x sub t** admite una representación MA infinito. 

Esta representación es la que nos permitirá encontrar las condiciones sobre los parámetros de un AR(p) y un ARMA(p,q), para que sean procesos estacionarios. 

En primer lugar, suponga que un AR(p) admite la representación MA infinito. Es decir, **epsi(B)** tal que sus coeficientes son absolutamente sumables. Luego, tendríamos que **phi sub p(B) por epsi(B) es igual a la identidad**. Es decir, el producto entre el operador autoregresivo con el operador **epsi(B)** es el operador de identidad. Luego, **epsi(B) es igual al operador phi sub B a la -1**, con lo que se obtiene el siguiente teorema. 

### Teorema para AR(p)
Para que el proceso AR(p) con operador **phi sub p(B)** represente un proceso estacionario, se requiere que las raíces del polinomio **phi sub p(z)** estén fuera del disco unitario. 

Sin entrar en los detalles de la demostración. El argumento principal es usar el teorema fundamental del álgebra en el polinomio **phi sub p(z)**. Es decir, dicho polinomio tiene exactamente **p** raíces. Donde algunas de ellas podrían ser números complejos o bien raíces repetidas. Es decir, tendríamos lo siguiente: **Phi sub P(z) sería el producto de z por r sub 1 hasta z por r sub p.** Luego, al realizar la descomposición en sumas de fracciones parciales, cada elemento corresponde a una serie geométrica o su derivada. Cuya condición para que converja es que la raíz esté fuera del disco unitario. Por ejemplo, asuma que **r** es una raíz real sin multiplicidad. Luego, **1 dividido z - r es igual a la serie de j = 0 hasta infinito de z partido en r a la j**, sí y solo sí, **1 partido en r** es menor a 1 en valor absoluto, implicando que **r** debe ser mayor a 1. Para los otros tipos de raíces se utilizan argumentos similares. 

Análogamente, en un proceso ARMA(p,q) se tiene el siguiente teorema. 

### Teorema para ARMA(p,q)
Para que el proceso ARMA(p,q), sin parámetros redundantes y con operador autoregresivo **phi sub p(B)** represente un proceso estacionario, se requiere que las raíces del polinomio **phi sub p(z)** estén fuera del disco unitario. 

Como se puede apreciar, la condición de estacionalidad para el ARMA(p,q) es la misma que para un AR(p). Y esto se debe a que **phi sub p(B) por epsi(B) es igual theta sub q(B)**. Es decir, **epsi(B) es igual a phi sub p(B) a la -1 por theta sub q(B)**. El cual existe solo si **phi sub p(B) a la -1** existe. 

No se entrega una condición sobre los parámetros del MA(q) para que este sea estacionario, ya que, por definición, los coeficientes **epsi sub j** son absolutamente sumables. Por lo tanto, sería estacionario para cualquier **theta**. 

Sin embargo, podría existir una cierta ambigüedad en el modelo. Por ejemplo, los procesos MA(1), **Xt** e **Y sub t**, descritos a continuación, tienen la misma función de autocorrelación. Además, se pueden escoger ruidos blancos, **épsilon t** y **Wt**, que hagan coincidir las funciones de autocovarianza de **Xt** e **Yt**. Adicionalmente, si asumimos normalidad en dichos ruidos, los procesos **Xt** e **Yt** serían idénticos. 

Para eliminar esta ambigüedad, se le exigirá a los procesos MA(q) que sean invertibles. Lo que se define como aquellos procesos que admiten una representación AR infinito. Es decir, es el ruido blanco el que se escribe como una combinación lineal del proceso. La cual se denotará por **epsilon t igual a pi(B) por x sub t**. Donde los coeficientes **pi sub j** son absolutamente sumables. Y el operador **pi(B)** está dado por la **identidad más pi sub 1(B), más pi sub 2(B) por B cuadrado**, y así sucesivamente. 

Finalmente, tenemos los teoremas:

### Teorema 1
Para que el proceso MA(q) con operador **theta sub q(B)** represente un proceso invertible, se requiere que las raíces del polinomio **theta sub q(z)** estén fuera del disco unitario. 

### Teorema 2
Para que el proceso ARMA(p,q) sin redundancias y con operador media móvil **theta sub q(B)** represente un proceso invertible, se requiere que las raíces del polinomio **theta sub q(z)** estén fuera del disco unitario. 

Los teoremas tratan a los MA(q) y ARMA(p,q) iguales en términos de la condición de invertibilidad. Y esto se debe a que **pi(B) es igual a theta sub q(B) a la -1** en los MA. Y **pi(B) es igual a theta sub q(B) a la -1 por phi sub p(B)** en los ARMA. Es decir, los coeficientes de **pi(B)** son absolutamente sumables si **theta sub q(B) a la -1** existe. 

> Prueba tu aprendizaje respondiendo a la siguiente pregunta. 

---

## Resumen de la clase

Hemos llegado al final de la clase. Ahora recordemos las ideas más importantes:

* Representar los modelos AR, MA y ARMA como un proceso lineal es útil para establecer condiciones sobre el espacio paramétrico, de modo que los procesos sean estacionarios. 
* Para que los procesos AR(p) y ARMA(p,q), sin redundancia, sean estacionarios, las raíces del polinomio autoregresivo deben estar fuera del disco unitario. 
* La invertibilidad elimina el problema de identificación en los modelos MA y ARMA. 
* Para que los procesos MA(q) y ARMA(p,q) sin redundancia sean invertibles, las raíces del polinomio de media móvil deben estar fuera del disco unitario.
