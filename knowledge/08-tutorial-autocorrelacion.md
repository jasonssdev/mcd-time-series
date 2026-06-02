# Funciones de Autocorrelación Simple y Autocorrelación Parcial

Bienvenidos y bienvenidas a este nuevo videotutorial en el cual vamos a abordar dos funciones importantes en temas de series de tiempo.

Estas son:

- Autocorrelación simple (ACF)
- Autocorrelación parcial (PACF)

Estas dos funciones son muy importantes porque nos permiten describir cómo es la dependencia de nuestra serie de tiempo que estemos analizando.

Principalmente, la autocorrelación, como su palabra lo dice, es una correlación de la serie consigo misma.

Aquí, en la autocorrelación, estamos considerando cierta temporalidad del pasado que está correlacionada con un cierto momento.

Mientras que la autocorrelación parcial busca también tener una medida de correlación de la serie consigo misma, considerando *lags* del pasado. Sin embargo, todos los *lags* que hay entremedio los está omitiendo.

Entonces, directamente mide una correlación desde el punto en el que estamos hacia un número $k$ de períodos en el pasado.

---

## Utilizando la librería Darts

Vamos a utilizar nuestra librería **Darts**, que es la librería que hemos estado ocupando desde los tutoriales anteriores.

Recuerde tener instalada esta librería.

Vamos a ocupar directamente la misma serie temporal utilizada en los tutoriales anteriores.

El gran cambio que vamos a realizar es usar:

- El gráfico de la **ACF** (*Autocorrelation Function*).
- El gráfico de la **PACF** (*Partial Autocorrelation Function*).

Importando las librerías respectivas, tenemos nuestra serie temporal.

Recordemos que esta es una serie del número de pasajeros de una aerolínea a lo largo del tiempo.

También recordemos que hemos realizado ajustes utilizando modelos ingenuos y vimos que, para esta serie temporal, un modelo de suavizamiento exponencial se ajusta bastante bien.

---

## Analizando la función de autocorrelación (ACF)

¿Qué vamos a realizar con esta serie temporal?

Vamos a calcular la función de autocorrelación y obtenemos el siguiente resultado.

### Interpretación del gráfico

En el eje **X** tenemos los *lags*, es decir, las temporalidades que estamos mirando hacia el pasado.

En el eje **Y** tenemos el valor de la autocorrelación para cada *lag*.

Además, aparecen unas bandas azules.

### ¿Qué significan las bandas azules?

Principalmente, si una autocorrelación está fuera de estas bandas, podríamos decir que dicha autocorrelación es significativamente distinta de cero.

---

### Comportamiento de la serie de pasajeros

Para el *lag* 0, la autocorrelación es igual a 1.

Esto tiene mucho sentido porque estamos considerando la autocorrelación del momento actual consigo mismo.

Por definición, eso siempre debe ser igual a 1.

A medida que vamos calculando autocorrelaciones para *lags* superiores, observamos que la autocorrelación comienza a decrecer.

Es decir, empieza a disminuir la correlación de la serie con su pasado.

Sin embargo, ocurre algo interesante.

La autocorrelación vuelve a aumentar justo en el *lag* número 12.

### ¿Qué significa esto?

Nuestra serie temporal comienza con una autocorrelación perfecta con el momento actual.

Luego, al mirar hacia el pasado, la autocorrelación disminuye.

Posteriormente vuelve a aumentar exactamente en el *lag* 12.

Esto tiene mucho sentido porque la serie temporal posee una componente cíclica que parece ser anual.

La autocorrelación está mostrando precisamente esa dependencia con el pasado.

---

### ¿Qué ocurre en el lag 24?

Si observamos el *lag* 24 (dos años), la autocorrelación ya no resulta significativa.

Por lo tanto, el *lag* 12 es un valor que debemos tener muy presente porque puede ser muy importante para análisis posteriores.

---

## Analizando la función de autocorrelación parcial (PACF)

Ahora observemos la autocorrelación parcial.

La forma del gráfico cambia y también cambia la interpretación.

Sin embargo, los ejes contienen la misma información.

### Eje X

Representa los *lags*.

En este ejemplo:

- Comienza en el lag 0.
- Termina en el lag 25.

### Eje Y

Representa la autocorrelación parcial.

Las bandas azules tienen exactamente la misma interpretación que en el caso anterior.

Es decir, si una autocorrelación parcial se encuentra fuera de dichas bandas, podríamos considerarla significativa.

---

### Lag 0

Por definición, la autocorrelación parcial para el lag 0 también debe ser igual a 1.

---

### Lag 1

Observamos que la serie está bastante correlacionada con el primer período en el pasado.

Además, si miramos la autocorrelación simple, obtenemos exactamente el mismo valor.

Esto tiene mucho sentido porque la autocorrelación parcial elimina los *lags* intermedios.

Pero entre el *lag* 0 y el *lag* 1 no existe ningún *lag* intermedio que eliminar.

Por definición, ambos valores deben coincidir.

---

### Desde el lag 2 en adelante

A partir del *lag* 2 la situación cambia.

Ahora sí existen *lags* intermedios que son eliminados.

En particular, se elimina el efecto del *lag* 1.

Incluso podemos observar una autocorrelación parcial negativa.

---

### El lag más llamativo

El valor que más llama la atención corresponde aproximadamente al:

- Lag 13

Este *lag* presenta una autocorrelación parcial importante.

### ¿Qué significa?

Significa que existe una fuerte correlación con el período 13 unidades atrás, eliminando el efecto de todos los *lags* intermedios.

Sin embargo, esta correlación aparece en sentido inverso, es decir, como una autocorrelación parcial negativa.

Eso resulta bastante interesante y merece atención.

---

## Resumen

Estos dos gráficos nos permiten analizar mejor la estructura temporal de la serie de pasajeros.

### ACF

Nos muestra que:

- El *lag* 12 parece estar asociado a una componente cíclica importante.
- Existe una dependencia anual en la serie.

### PACF

Nos muestra que:

- El *lag* 13 presenta una autocorrelación parcial negativa importante.
- Existe información adicional que no se aprecia directamente en la ACF.

Tanto el *lag* 12 como el *lag* 13 serán valores de interés y los utilizaremos de alguna manera en los próximos tutoriales.

---

Espero que este tutorial haya sido de su agrado.

¡Nos vemos en el siguiente!