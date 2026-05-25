# Series Cronológicas y Tipos de Dependencia

[MUSIC]

## Introducción

Bienvenidos y bienvenidas.

En esta clase vamos a revisar las series de tiempo y sus aplicaciones en algunos contextos.

Hoy en día estamos viviendo algunas consecuencias del calentamiento global, donde podemos apreciar eventos que en el pasado eran considerados extremos y poco frecuentes, ahora son cada vez más frecuentes.

Algunos ejemplos son:

- Temperaturas muy elevadas en verano
- Lluvias muy intensas en invierno

Es así como cada nueva temporada vemos que se superan los récords históricos en diferentes partes del mundo.

Es cierto que algunos científicos nos advirtieron de estas consecuencias hace mucho tiempo, pero ¿cómo pudieron saber hace 50 años que esto ocurriría?

Con el tiempo, muchos científicos se sumaron a las advertencias sobre el cambio climático, mientras que otros plantean que este es un proceso natural, y que la información histórica nos postula que era inevitable.

Por cierto que es un tema complejo, y no cabe duda que estamos viviendo eventos de la naturaleza que en el corto plazo no se habían visto.

Contar con la información medida en el tiempo ha ayudado a tener una idea de la evolución de ciertos fenómenos, por lo que ajustar modelos a dichos tipos de datos nos permite predecir.

Si bien existen muchas herramientas que nos ayudan a realizar predicciones al futuro, las series de tiempo también permiten cuantificar el error de la predicción.

Obviamente, las series de tiempo se aplican en una gran variedad de contextos, de los cuales veremos cómo lucen algunos de ellos a continuación.

---

## Aplicación de Series de Tiempo

[SOUND]

Para representar una serie de tiempo, usaremos la notación:

- x sub t

Donde:

- x representa la variable de interés medida en el instante t

Para contextualizar esto, consideremos algunos ejemplos donde aparecen naturalmente las series.

### Datos Financieros

En primer lugar, considere los datos financieros, donde existen una gran cantidad de indicadores.

Como, por ejemplo, el promedio industrial Dow Jones, que refleja el comportamiento del precio de la acción de las 30 compañías industriales más importantes y representativas de los Estados Unidos.

La gráfica muestra el valor de este indicador de forma diaria desde el 20 de abril de 2006 hasta el 20 de abril de 2016.

Se puede apreciar el comportamiento errático de la serie, como una clara baja a finales del 2008.

En las series financieras se suele analizar los retornos o cambio porcentual, ya que reflejan de mejor forma el comportamiento del mercado.

El retorno corresponde al cambio relativo del indicador entre dos instantes de tiempo consecutivos, el cual es aproximado por el cambio logarítmico, apareciendo el concepto de diferenciación discreta.

El cual será muy relevante en los modelos que analizaremos en el curso.

La gráfica de los retornos del DJIA se aprecia en la siguiente figura, donde es fácil detectar la crisis financiera del 2008, representada por los retornos más extremos.

Este es un comportamiento típico de los datos financieros:

- Retornos centrados en cero
- Periodos de gran volatilidad
- Periodos de baja volatilidad

### Datos Experimentales Medidos por Sensores

Otra área donde las series de tiempo surgen de forma natural corresponde a los datos experimentales medidos por sensores.

Como, por ejemplo, resonancias del cerebro.

La figura muestra los datos recogidos en cuatro localizaciones del cerebro mediante imágenes de resonancia magnética funcional (fMRI).

El valor observado corresponde al promedio de la intensidad de la señal dependiente del nivel de oxigenación de la sangre de 5 sujetos.

Los cuales son sometidos a:

- 32 segundos de estimulación
- 32 segundos sin estimulación

Con una frecuencia de medición de 2 segundos.

En este tipo de series, se observa una clara componente periódica.

### Temperatura Mundial

Como se mencionó en la introducción, existen muchas mediciones en el tiempo que nos entregan una alerta mundial.

Como ejemplo, considere el índice de temperatura media mundial entre la tierra y el océano desde 1880 hasta 2015, con un periodo base de 1951 a 1980.

Los datos observados corresponden a la diferencia con el periodo base.

Se observa:

- Una clara tendencia al alza entre 1930 y 1950
- Que se estabiliza hasta 1980
- Luego de eso, existe otra clara tendencia al alza

Esto entrega evidencia empírica de que algo no anda bien.

Existen muchos otros ejemplos de series de tiempo, como las mediciones de los anillos de los árboles, que se utilizan para reconstruir el clima del pasado.

---

## ¿Por Qué No Usar Solo Regresión Lineal?

Sin entrar en todas las posibles aplicaciones, suponga que modelamos los datos anteriores con regresiones lineales.

Tendríamos algunos problemas que debemos evitar.

Prueba tu aprendizaje respondiendo la siguiente pregunta.

### Caso de los Datos Financieros

¿Por qué no usar sólo el modelo de regresión lineal?

En el caso de los datos financieros, los retornos tienen media cero, sin tendencia.

Por lo que el modelo de regresión lineal:

- rt = beta 0 + beta 1t + un error épsilon t

Tendría el coeficiente beta 1 como no significativo.

Es decir:

- No se puede descartar que su verdadero valor sea 0
- Lo mismo ocurre para beta 0

Por lo tanto, la ecuación de predicción sería:

- r ajustado de t igual a 0

### Caso del fMRI

Para el caso del fMRI, se pueden proponer modelos de regresión sinusoidal, como se pueden ver en las siguientes ecuaciones.

Donde las diferencias son las frecuencias:

- omega 0
- omega 1
- omega 2

Para que estos modelos efectivamente sean modelos de regresión lineal, las frecuencias omega deben ser conocidas.

Pero:

- ¿Cómo identificar la componente periódica?
- ¿Qué valor o valores asignar a las frecuencias omega?
- ¿Cuántas frecuencias utilizar?

Esto también se responde con el análisis de series de tiempo, pero en el dominio de la frecuencia conocido como análisis espectral.

### Caso de las Mediciones de Temperatura

Para el caso de las mediciones de la diferencia de temperatura, suponga que probaremos los siguientes tres modelos:

1. Modelo lineal
2. Modelo cuadrático
3. Modelo cúbico

Una vez realizado el ajuste, se pueden visualizar:

- La recta de color rojo para el modelo 1
- Las curvas de color verde y azul para el modelo 2 y 3 respectivamente

La gráfica nos sugiere el modelo 2.

El cual es ratificado a partir de la tabla de ahora, que nos dice que el modelo 2 explica significativamente mejor que el modelo 1.

Mientras que el modelo 3 tiene una explicación marginalmente mejor que el modelo 2.

Sin embargo, al observar los residuos, se aprecia que tienen correlación importante.

Por lo que si bien el modelo de regresión captura buena parte de la información, los residuos aún contienen información importante que debe ser incorporada en el modelo.

Prueba tu aprendizaje respondiendo la siguiente pregunta.

---

## Conclusiones

Hemos llegado al final de la clase.

Ahora recordemos las ideas más importantes.

Los datos medidos secuencialmente en el tiempo deben ser modelados apropiadamente para capturar la información secuencial del muestreo.

Existen diferentes patrones en series de tiempo, por lo que al momento de modelar una serie se deben tener presentes posibles transformaciones o diferenciaciones.

Las series de tiempo pueden tener:

- Tendencia
- Componente estacional
- Ruido sin estructura

Los modelos de regresión lineal pueden capturar la tendencia de una serie, así como la estacionalidad.

Pero, por lo general, sus residuos presentan autocorrelación, debido a la naturaleza temporal con que se toman los datos.