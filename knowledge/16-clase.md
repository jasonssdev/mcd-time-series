**Profesor:** Bueno, ¿alguna pregunta, comentario que quede grabado para todos? ​¿Alguna duda? ​Vamos bien, vamos bien con el curso. ​Ok, entiendo el silencio, como que sí, ah, dime, dime.

**Estudiante:** ​No sé, en realidad no es una pregunta como individual, es que me quedaron varias dudas ​con las últimas clases, sobre todo con las distribuciones continuas, me cuesta harto ​entenderlo, no sé si tendrá algún tip o no sé si lo podemos revisar de nuevo, y también ​de las funciones de densidad.

**Profesor:** ​O sea, ¿la distribución normal no quedó muy clara?

**Estudiante:** ​Es que yo creo que son muchos conceptos y cuesta como llevarlos a la práctica con los ​ejercicios, como son hartas fórmulas.

**Profesor:** ​Ya, pero lo más importante que rescaten de eso es la distribución normal, sus propiedades, ​la estandarización y mirar las tablas. ​A lo mejor María José, ¿podrías incorporar algún ejercicio de eso el otro jueves?

**María José:** ​Sí, sí lo vamos a hacer porque en la última ayudantía hicimos algunos ejercicios de probabilidades ​y revisamos un poco de la distribución normal, pero para la otra ayudantía ya podemos verlo ​con más profundidad.

**Profesor:** ​Claro, que igual hay que avanzar en los otros temas que son los intervalos de confianza. ​Y el concepto de valor P se puede ir aplicando de a poco, desde hipótesis. ​Ya Paula, ahora si tienes alguna duda puntual, puedes escribirnos también y ves que no puedo ​dejar esta clase para explicar de nuevo eso, porque si no pierdo el contenido de esta clase, ​ese es el tema Paula, no es que no quiera.

**Paula:** ​Y así no se preocupe.

**Profesor:** ​Y entonces María José puede puntualizar un poco más ese tema el próximo jueves con ejercicio ​y cualquier duda puntual también escríbenos, ¿vale? ​Ya, entonces, bienvenidos y bienvenidas, ya estamos grabando, voy a compartir la clase ​de hoy, nuestra segunda sesión sincrónica. ​¿No estamos en presentación aún? ​Ahora sí. ​¿Me ven y me escuchan bien?

**Estudiantes:** ​Sí. ​Sí, ok.

---

## Introducción: Miremos Encuestas y Estimación Puntual

**Profesor:** ​Si hay alguna pregunta en el chat María José me cuentas porfa y si alguien quiere abrir ​el audio para preguntar no necesitan levantar la mano, me preguntan nomás, ¿vale? ​Me interrumpen, no hay problema. ​Y entonces nuestra clase de hoy se llama *Miremos encuestas, estimación puntual*. ​Vamos a contextualizar de inmediato. ​Bueno, ya me conocen. ​Voy a retomar el contexto en que estamos antes de partir con esto específicamente.

​Estamos en un contexto en que hay una población de interés, con alguna característica de interés ​que nos interesa, valga la redundancia, estudiar, pero no puedo acceder a esa población, ​entonces tomo una muestra. ​Idealmente representativa, o sea, de tamaño mínimo adecuado y aleatoria, pero no suele ​ser así, esa es la realidad, se hace lo que se puede, que suelen ser muestras por conveniencia.

​Y entonces a partir de esos datos de la muestra, nosotros vimos la primera parte del curso, ​lo que es realizar análisis descriptivo, y ahora pasamos a la segunda etapa, entramos ​en la segunda etapa que es inferencia. ​Lo que nosotros queremos es poder sacar conclusiones sobre el parámetro de interés de la población. ​No nos interesa solo el resultado muestral, sino que nos interesa poder extrapolar ese ​resultado muestral a una pregunta, a un parámetro de la población.

​Y entonces hay tres maneras de realizar inferencia:
1.  La primera es la inferencia puntual, que es lo que voy a ver hoy.
2.  La segunda es a través de intervalos de confianza, que es lo que ya están haciendo en este módulo, ​ver intervalos, construcción de intervalos de confianza, que es decir, bueno, el parámetro ​entonces poblacional, el que está acá, que es donde se plantea la pregunta de investigación, ​se encuentra entre tales valores.
3.  Y van a comenzar con la etapa de inferencia, que es test de hipótesis.

---

## ¿Qué es la estimación puntual?

**Profesor:** ​Entonces, ¿qué es la estimación puntual? ​Se los voy a explicar ahora y les voy a mostrar para eso dos tipos de encuestas. ​Pero primero les voy a especificar que nos referimos a estimación puntual cuando el ​valor de la muestra se asume como si fuera el valor poblacional. ​Es decir, un 30% de los chilenos dicen estar de acuerdo con la creación de ciclovías, ​cualquier cosa, la construcción de ciclovías. ​Ese valor de un 30% en realidad se obtiene de una muestra, y lo que corresponde a realizar ​estimación puntual es que ese resultado de la muestra se utiliza directamente como ​si fuera el resultado poblacional.

​Concluir, "el 30% de los chilenos opina tal cosa", que es lo que les mostré en el webinar ​de Bienvenidas, ¿se acuerdan? ​Esa diapo donde estaba llena de titulares, donde sacan conclusiones como si fuera la ​opinión de los chilenos, o de cualquier localidad, a partir solo de un resultado ​muestral.

​¿Cuál es el problema de eso? ​Que no considera que hay variabilidad muestral, y que eso depende, esa variabilidad va a depender ​de la desviación estándar, va a depender del tamaño muestral, que es el concepto que ​vieron del error estándar de la media para la construcción de los intervalos.

​La diferencia entre puntual e intervalos de confianza es que en puntual observo un valor ​muestral, y así a mis anchas, sin considerar que aquí hay variabilidad, lo que hago es ​asumirlo como si fuera el parámetro poblacional. ​En cambio, por intervalos de confianza observo valores muestrales, y a partir de ellos construyo ​un valor, o construyo un rango, donde con un 95% de confianza se encuentra el parámetro ​poblacional. ​¿Ok?

​Viene una pregunta en el chat, Paola. ​Dime.

**Paola:** ​¿Qué dice? ​"A eso llamamos expansión", pregunta Marcela.

**Profesor:** ​Expansión, no sé si existe esa palabra que no la he usado nunca dentro de los términos ​de estadística, pero si te refieres, es que no es, bueno, es expandir, pero es expandir ​como expandir así más bien, ¿sí? ​No expandir así, porque es sólo el valor, el estimador muestral, convertirlo directamente ​en parámetro poblacional. ​Si eso lo entiendes con el término expandir, está bien, ¿sí?

**Natalia:** ​Ahí serían, profe, y ahí serían, por ejemplo, estas encuestas que hacen, todas estas que ​tienen como impacto, ¿ok?

**Profesor:** ​Exacto. ​Entonces, eso es lo que les voy a mostrar ahora. ​Les voy a mostrar dos grupos grandes de encuestas, que las he agrupado en dos tipos, una son ​las encuestas de opinión, que son las que te refieres, Natalia, que las vamos a revisar, ​y lo que son las encuestas poblacionales, que ese es otro nivel, otro presupuesto también, ​otros tiempos, ¿ok? ​Entonces, vamos a mirar estos dos casos, voy a partir con encuestas de opinión, luego ​encuestas poblacionales, y luego vamos a tener, como siempre, un espacio para preguntas y ​opiniones.

---

## Encuestas de Opinión

**Profesor:** ​Esto funciona en todas partes del mundo igual. ​Aquí les traigo una encuesta de Colombia. ​Entonces, todas las encuestas, y todas las que ustedes ven en Chile o en sus propios ​países, si ustedes entran a la página de la encuesta, en todas está publicado el informe ​oficial, y en todas se incorpora la metodología utilizada, eso lo pueden encontrar en cualquier ​encuesta. ​Entonces, aquí les traigo, por ejemplo, la de Colombia, para no mostrar solo cosas chilenas.

​Esta es de opinión pública de gestión del gobierno. ​Voy a ir leyendo las cosas que me importan:
* **Universo poblacional**, ¿a quién quieren representar? ​Mujeres y hombres mayores de edad, residentes de las cinco principales ciudades de Colombia. ​Que son las cinco que se mencionan ahí.
* **El sistema de muestreo.** ​Fíjense que este sistema de muestreo lo voy a comparar después con la siguiente que ​traigo. ​Por ejemplo, es un sistema de muestreo bastante complejo, de alta calidad. ​Un muestreo aleatorio simple estratificado. ​¿Eso qué quiere decir? ​Aquí está. ​Los estratos manejados son ciudad y no nivel socioeconómico. ​Eso quiere decir que definen, por ejemplo, para Bogotá necesito tantas personas en nivel ​socioeconómico bajo, tantas personas como ellos lo hayan definido. ​Tanto nivel socioeconómico medio, tanto alto.

​Entonces me aseguro, al estratificar, tomo muestras en cada uno de esos estratos para ​asegurar la representatividad de esa combinación ciudad-nivel socioeconómico, ¿está bien? ​Y dentro de cada estrato se selecciona aleatoriamente el hogar que cumple con el perfil deseado, ​de acuerdo al estrato, y se selecciona directamente el hogar dentro de la base de datos. ​O sea, cuentan con una base de datos donde están empadronados los hogares y conocen ​las características del hogar. ​Eso ya es maravilloso. ​Y se contacta al encuestado idóneo del hogar.

​Entonces el marco muestral es una base de datos suministrada por tal empresa, con número ​telefónico y las variables de estratificación que interesa, que es ciudad y nivel socioeconómico.
* **Tamaño de la muestra** es 700, este es el tamaño usual mínimo, el DESDE, de las encuestas ​de opinión pública.
* **Margen de error**, el margen de error para una confianza del 95% es de 3,7%.

​Están asumiendo, y esto es lo que corresponde, que yo al tomar una muestra y observar un dato ​no puedo dar con precisión, no puedo asegurar que ese dato muestral sea el parámetro poblacional ​directamente. ​Y están asumiendo que el error es de un 3,7%. ​Eso significa que cuando yo dé una proporción, una prevalencia, el intervalo de confianza queda ​construido por más o menos 3,7%. ​¿Estamos? ​Hacia arriba y hacia abajo. ​¿Ok?

​Les voy a comentar más de esto en las diapos que vienen. ​Y bueno, el resto de las cosas es que se pondera por ciudad, por edad, etc.

*(Dirigiéndose a un estudiante)* ​¿Quieres preguntarme algo? ​¿No? ​Ok. ​Y nada más que me interese. ​¿Estamos?

​Eso entienden el contexto, entonces. ​Lo importante aquí, lo bonito, es que efectivamente se eligen los hogares por muestra aleatoria simple. ​Y telefónicamente se contacta a una persona de ese hogar. ​Y el tamaño de encuesta es de 700 personas y el margen de error de 3,7%.

### Análisis de Resultados: Colombia

**Profesor:** ​Entonces, este es uno de los resultados que yo saqué de los que ellos presentan en este informe. ​Entonces, marcan cuáles son las prioridades, temas prioritarios para que los candidatos presidenciales promuevan en las próximas elecciones. ​Entonces, la gran mayoría habló de educación, el 62%, en primer lugar, habló de educación y oportunidad de los jóvenes.

​Y así pueden ver aquí. ​Después, corrupción y transparencia, salud y acceso a servicios, etc. ​Y luego, fíjense, aquí hacen algo bastante bonito, que aquí en nuestras encuestas se ve muy poco. ​Que es identificar cuando hay una diferencia significativa de una ciudad respecto del total. ​O sea, por ejemplo, en Cali, un 73% priorizó educación. ​Y eso tiene una diferencia significativa respecto del 62% del total. ​¿Se entiende?

​Entonces, ellos reportan una... y así para todas las cosas, ¿sí? ​Y respecto de hombres y mujeres, y por grupo etario. ​Ellos reportan, entonces... ​Estoy tratando de buscar el lápiz. ​Cuando ellos reportan un error de 3,7%, lo que están diciendo es, mira, un 62% ​No diría el 8 con lápiz. ​Lo que están diciendo es, un 62% reporta que su primera preocupación es la educación. ​Pero, si consideramos el 4%, es 3,7, pero déjenme decir 4% por facilidad para sumar y restar, ¿ok?

​3,7, voy a hablar de 4. ​significa que en realidad entre un 58% reste 4 y un 66% de la población total parámetro ​prioriza la educación. Se fijan, presentar un 4% de error significa que a cada resultado ​debo sumarle y restarle un 4% de error y este es el intervalo de confianza donde se encuentra ​el verdadero parámetro poblacional. El 62% es el estimador puntual. Entre 58 y 66% se encuentra ​el verdadero parámetro poblacional con un 95% de confianza.

​Entonces, miren este 73, ​si a ese 73% yo le sumo y le resto el 4% quedaría un intervalo de confianza que va del 69% al 77%. ​¿Me siguieron todos y todas? Que al estimador puntual estoy restando y sumando el margen de ​error, entonces construye el intervalo de confianza. Se fijan que entre este intervalo ​que es del total y el intervalo para Cali, los intervalos de confianza no quedan así ​traslapados, quedan excluyentes. Por lo tanto, efectivamente Cali presenta una mayor preocupación, ​lo presenta con una mayor proporción de tema prioritario que el total, que es lo que marcaron ​en rojo. En cambio, si uso cualquier otro, no se va a dar eso. ¿Estamos?

​Hay un tema también que ​ese 4% es para el total de la población. Sin embargo, cuando la población se empieza a dividir ​por ciudad, por ejemplo, por hombres y mujeres, por grupo etario, ese error empieza a aumentar ​porque voy achicando el tamaño muestral. Empieza a dividir a la muestra, por lo tanto, ​y se lo voy a mostrar en la próxima encuesta del efecto que eso tiene. Entonces, importante, ​estos son estimadores puntuales.

**Estudiante:** Dígame. En este caso, como usted dice que se achica la muestra, ​podríamos aplicarlo, pero ahí, por ejemplo, el error muestral no sería de 4, probablemente sea ​mayor.

**Profesor:** Exacto, sea mayor. Yo aquí asumí el 4% para Cali, pero seguro que es mayor porque tengo ​menos n's, solo que no lo conozco.

**Estudiante:** Perfecto. Entonces, solamente este 4 sería para el valor ​total.

**Profesor:** Eso sería lo correcto. Para el valor total, exacto, tal cual. Y entonces, por ejemplo, ​si yo les preguntara si existe diferencia significativa en que la mayor prioridad está ​en educación por sobre corrupción y salud y acceso a servicios, no. De hecho, estos son todos ​empates técnicos porque son del nacional, salvo el último, infraestructura. Ese es el único que ​es significativamente más bajo, pero en realidad los colombianos opinan de estas cinco cosas lo ​mismo. Es igual de importante porque si construyo los intervalos de confianza con el 4%, que en ​este caso sí es nacional, sí corresponde, estarían todos los intervalos de confianza traslapados. O ​sea, no hay ninguna de estas prioridades que sea más significativa. Y ahora les muestro el titular.

**María José:** ​Hola, perdón, hay una pregunta en el chat que dice que qué pasa con el 50% de Medellín.

**Profesor:** ​¿Qué pasa con el 50% de Medellín? Este, ¿por qué no sale significativo? Esa es la pregunta. ​Respecto al 62, pasa que el problema es que no nos dan los tamaños muestrales y los errores ​de cada, al utilizar cada ciudad. En la próxima encuesta que tengo se los puedo mostrar bien. ​¿Contesté? ¿Esa era la pregunta?

**María José:** ​Sí, esa era la pregunta, gracias.

**Profesor:** ​Sí, ya, ok. Entonces, miren cómo sale el titular: *"Costo de vida, corrupción de educación, las principales preocupaciones de los colombianos"*. ​Dos comentarios. Uno, no son las principales, son todas iguales las primeras cinco, excepto ​la infraestructura. No son las principales, miren la diferencia de un 1% o un 4%. Eso es ​solo error muestral, no son realmente las principales. Segundo comentario, *de los ​colombianos*. ¿Se fijan? Ahí lo que hicieron fue tomar el estimador muestral y usarlo como ​resultado poblacional. Se olvidaron del 4% de error, se olvidaron de todo. Se olvidaron del ​95% confianza. Simplemente lo tomaron y lo convirtieron en… Ah, y además se olvidaron ​de que aquí hay cuatro ciudades muestreadas, no todo Colombia. ¿Se entiende? A esto me ​refiero con estimador muestral. ¿Preguntas hasta aquí?

---

### Análisis de Resultados: Chile (Pulso Ciudadano vs Criteria)

**Profesor:** ​Les voy a mostrar otro ejemplo. Este ejemplo es chileno y es más… les va a ayudar a entender ​mejor los que les quiero contar respecto a los errores. Este es de hace poco, por supuesto, ​mayo del 26, 6 de mayo, y entonces reconoce el titular que son dispares las cifras de las ​encuestas. El Pulso Ciudadano habla de… ¿Cuál es Pulso Ciudadano? Un 29,1% que aprueba la gestión ​de nuestro actual presidente. En cambio, en Criterio un 38%. ¿Ven la diferencia? Nueve ​puntos de diferencia, es mucho. Y así la variabilidad entre una encuesta de opinión ​y otra. Pasa todo el tiempo.

​Les voy a mostrar una de estas, porque obviamente no les puedo ​mostrar muchas por tiempo, que es la de Activa, esta que habla Criteria, del 38%. ¿Estamos? Falso, ​es la otra. Pulso Ciudadano, del 29%. ¿Por qué elijo esta? Esta la elijo porque de todas las ​encuestas que conozco de opinión pública de nuestro país, es la que es más transparente ​en el error que cometen. Se los voy a mostrar ahora.

​Veamos, es un estudio cuantitativo sobre ​la base de entrevistas online a través de un panel representativo de cobertura nacional. ​Esto es lo usual que hacen todas las encuestas de opinión pública, sobre todo las que salen ​rápidos. Hay algunas como de la UDD, que son más con visitas a hogares, son más lentas, más caras, ​pero CADEM, como me preguntaron recién, y todas las que conocen de respuesta rápida, ​funciona con un panel. Esto es que tienen y generalmente le compran la información a una ​empresa. Hay una empresa que tiene un panel de información, es decir, tiene a muchas personas ​registradas online con sus características sociodemográficas.

​Y entonces viene Activa, ​en este caso, y les dice, miren, mil entrevistas. Entonces les dicen, véndeme, porque estas son ​ventas en realidad, pero pásame entrevistas hechas a mil nueve personas. Estratificada ​por género, edad, grupo socioeconómico y zona, lo que les expliqué antes para que ​queden todos estos grupos representados. Entonces, lo que hace es mandar la encuesta ​a muchas personas dentro de este panel y con ese panel responden a estas mil nueve entrevistas que ​se solicitan, que necesitan. ¿Estamos?

​Miren, la tasa de respuesta está aquí. Seleccionen base ​un panel online con una tasa de respuesta del 3,6 por ciento. El panel utilizado corresponde ​a la empresa opinando online. ¿Se fijan? Ellos son los que tienen este panel. Y fíjense la tasa de ​respuesta, 3,6 por ciento. O sea, tuvieron que, para tener mil entrevistas, tuvieron que mandar ​como 30 mil mails para que les puedan contestar y obtener las mil entrevistas. ¿Se fijan?

​Entonces, hablemos de sesgos. ¿Por qué valoró de la que vimos Ración de Colombia? En Colombia ​realmente es un muestreo aleatorio. Eligen, de acuerdo a la… tienen empadronamiento. La ​población… ¿Cuál es la definición de aleatorio? Que cada persona de la población tiene alguna ​probabilidad de ser elegido. Eso es aleatorio. En la encuesta anterior, según como lo mencionan, ​en que están empadronados, aunque son cuatro ciudades, pero toda persona de la población ​tiene alguna probabilidad de ser elegido. En esta, cuéntenme, ¿tenemos toda la población alguna ​probabilidad de ser elegidos? ¿Cuántos de ustedes pertenecen al panel opinando online? ¿Alguien?

​¿Acepto eso como un no? O sea, esta encuesta realmente… y se están haciendo así porque ​antes eran telefónicas la mayoría, pero desde que está… bueno, no tan reciente, ​pero la gente ya no contesta el teléfono a las llamadas desconocidas. Entonces, ​este método de encuesta de partida tiene el sesgo de tener una población cautiva. ¿Se fijan? ​Solo los que pertenecen al panel. Y ahora, ¿quiénes pertenecen al panel? Bueno, ​quienes hayan sido invitados y hayan aceptado. Entonces, el tema es quiénes reciben la invitación ​y quiénes aceptan. ¿Estamos?

*(Leyendo el chat)* Entonces, tiene… alcancé a leer el chat, tiene un claro sesgo de ​selección, es lo que quiero decir. Una persona rural con baja señal va a estar en este panel, ​va a recibir esta invitación. Una persona mayor que no ni siquiera usa el correo, que no sabe ​hacerlo, va a recibir esta invitación, etcétera. Efectivamente, tiene un sesgo de selección. ​Incluso, porque no es aleatoria, porque habemos muchas personas, por lo visto todos los que ​estamos aquí, que no pertenecemos al panel, por lo tanto no tenemos ninguna posibilidad de ser ​escogidos. ¿Estamos bien?

​Luego, lo que me interesa, ¿declaran su error muestral? Fíjense ​en 3,1. ¿Se fijan que es dependiente del tamaño muestral? El anterior de 700 era 3,7, que es el ​mismo número que maneja Cadena. 700 personas, 3,7. En este, sube un poquito el tamaño muestral, ​1000, con un error de 3,1. Fíjense que ese error sí es calculado bajo supuestos de aleatoriedad, ​cuando se acaba de decir, mostrar que en realidad no es aleatoria. ¿Se fijan? La anterior sí era ​aleatoria. Ese 3,7 de error es real. En cambio, aquí nos informan...

**Estudiante:** ¿Es correcto decir bajo ​supuesto de aleatoriedad? Están diciendo, es de 3,1 si es que nuestra encuesta fuera aleatoria.

**Profesor:** Ajá, tal cual. Fíjense que está hecha en dos días. O sea, en dos días mandan 30.000 encuestas ​para con esa tasa de un 3,6% tener las 1.000 personas que necesitan. ¿Ok?

​Bien, entonces, ​esto es lo que les quiero contar. Ese 3,7 corresponde al total nacional con las 1.000 ​personas, que es lo que yo sí valoro mucho de Activa, que les digo que es la única que veo ​que transparente. Lo siguiente, no lo he visto ninguna otra, que reconocen el tamaño muestral ​y entonces el error asociado por segmento, que es lo que les traté de explicar antes con Cali. No sé ​cuántas personas de esas 700 eran de Cali, por lo tanto no conozco su error. Aquí me lo están ​presentando. Miren, por grupo socioeconómico hay C1, C2, C3 y DE. Ahí están los, no sé lo que es.

​Por edad están estos rangos etarios que aquí ven, estos n's, y fíjense cómo varía el margen de ​error. Miren este entre 18 y 30 años, son 100 personas. El margen de error es prácticamente ​de 10. O sea, al estimador que me den, tenemos que sumarle y restarle 10. Eso casi deja de ser ​informativo, ¿se entiende? Que es lo mismo que pasa, aquí está por hombre y mujer, se fijan que al ​achicar el N, obviamente crece el margen de error. Entonces ya no es ese 3,1 que me informaron, ​¿estamos? Ese 3,1 es aquí abajo para el total. Miren cuando miramos por zona, la zona norte está ​muy subrepresentada, por lo tanto su margen de error es de un 10%.

​Entonces, por un lado obtenemos ​transparente en darnos los márgenes de error, muy bien, lo aplaudo. Sin embargo, dejan evidencia ​que al hacer comparaciones segmentadas prácticamente los errores son enormes, por lo ​tanto poder comparar y encontrar diferencias significativas es muy difícil. Y ni hablar si ​además el grupo etario, imaginen cómo quedaría el tamaño muestral si el grupo etario se me ocurre ​mirarlo por sexo, por género, o sea, ¿se entiende? Entonces, muy bien ​la transparencia hasta aquí, pero después empiezan a hacer comparaciones igual, y lo que nos aparece ​en las noticias son comparaciones de los estimadores puntuales, con todas las condiciones que le esté ​mostrando, y eso no es sólo con activa, insisto que son todas, más o menos mejor, pero son todas, ​y nos aparecen los resultados estimadores y empiezan a hacer comparaciones, se fijan quién ​desaprueba más, quién aprueba menos, así después nos salen los titulares, entonces eso es estimación ​puntual.

​Ahora qué es lo otro que transparenta, activa y que tampoco lo he visto en otras partes, ​es que miren la baja tasa de respuesta, eso sí lo transparentan casi todas, pero entonces lo que ​si transparentan ellos, es que ellos premian por responder, hacen sorteos a las personas que ​responden, y de hecho publican a los ganadores, esto son, esto lo saqué ahora, publican a los ​ganadores, o sea hay un estímulo, y de nuevo, eso produce sí o sí un sesgo de selección, sin duda, ​entonces quiénes van a contestar, los que tienen internet, de partida los que pertenecen al panel, ​los que tienen internet, los que tienen tiempo también, ¿cierto? y para quiénes es más importante ​este incentivo, ¿se entiende? ¿comentarios?

**Estudiante:** En una de las clases, si me recuerdo decían que era la ​menos recomendada utilizar el estimador puntual.

**Profesor:** Absolutamente, lo que yo quiero transmitirles ​con esto, es que la estimación puntual es lo peor, no es riguroso estadísticamente, y yo ​quisiera que las encuestas de opinión dejen de entregar la información como si el estimador ​fuera el parámetro, esa es como una lucha que yo tengo en mi vida, de transmitir esto, no le crean ​por favor a los resultados de la prensa de estimadores puntuales, vayan a mirar el informe, ​porque además estos comentarios, en mi opinión, mi opinión es que estos resultados cambian la opinión ​de la gente, se genera un círculo.

​Si yo veo que mucha gente no está de acuerdo con KAST y me ​preguntan, entonces ¿qué digo? empiezo a no estar de acuerdo también, o en periodos de elecciones ​políticas en cualquier país, si estoy entre dos candidatos y una encuesta me muestra que a éste ​le está yendo mejor, entonces yo no quiero perder mi voto, y voto por el que tiene más preferencia. ​Las encuestas, en mi opinión, efectivamente cambian el comportamiento de la población, ​¿se fijan? y ahí yo encuentro que hay una tremenda responsabilidad.

​De hecho no sé si se acuerdan las ​últimas elecciones, para los que son de aquí disculpen los de afuera, pero hay un candidato ​que por dos elecciones consecutivas ha salido en tercer lugar, Parisi, ¿se acuerdan? sin embargo ​en ninguna encuesta le dieron ese tercer lugar, siempre salió más abajo, eso es una mala publicidad ​en el fondo para el candidato, y no es que yo esté a favor de Parisi, yo no hablo política de mis ​preferencias, son hechos concretos. Ninguna encuesta le dio un lugar a Parisi, siempre salió ​último, de los últimos, casi sin votos, y en los dos procesos de elecciones en realidad salió en tercer ​lugar, y él atacó la última vez, atacó las encuestas, pero con todo, porque decía que si no hubiera ​tenido esa mala publicidad, él podría haber salido entre los dos primeros, a segunda vuelta, y yo le ​creo, porque estaba muy cercano en tercer lugar, imagínense si las encuestas hubieran mostrado ​confianza en él, que nunca apareció, ¿se entiende?

​Entonces este es un círculo que a mí me parece que ​hay una tremenda responsabilidad de parte de las encuestas, obviamente sirven para mirar el parecer ​de las personas, y tener un pulso más o menos de qué está pasando, pero para mi gusto hay ​una responsabilidad importante. Miren, este cuadro es más viejo, pero uno puede encontrar más nuevo, que son ​distintas encuestas, todas conocidas, de opinión pública, para las elecciones anteriores, anteriores, ​miren las estimaciones de cada una, de partida, la variabilidad entre encuestas, que la pregunta ​por quién votaría usted hoy día, cuando estaban todos los candidatos, de aquí salen los dos que ​pasan a segunda vuelta, ¿por quién usted votaría? Miren la variabilidad entre las encuestas, desde ​17%, 18%, un 32%, ¿ven la gran variabilidad? Es enorme, bueno, miren este, un 4% le daba ​a algunas encuestas, y solo dos, y este fue el resultado final, este es el parámetro, ¿se fijan?

​Esto de arriba son estimadores, el de abajo es el parámetro, y esto salió como un reporte de ​que solo dos de las siete mediciones dieron como ganador a Boric, ​que bueno, eso fue resultado de la segunda muestra, de la segunda vuelta, ¿sí? Pero ¿se fijan la ​variabilidad que hubo? Este fue el parámetro, hay algunos que están muy lejos, parámetro 28, ​este está más o menos cercano, este 12 está más o menos cercano, ​este 1,4, ¿se fijan? Cuando son poquitos votos es más fácil moverse cerca, pero aquí adentro, ​esta es la variabilidad, entonces, variabilidad natural no está mal, el tema es que hay que ​reconocerlo, que existe variabilidad muestra. ¿Estamos bien hasta ahí? ¿Se entiende? ¿Comentarios?

---

## Encuestas Poblacionales

**Profesor:** ​Ok, ahora quiero hablar de otra calidad de encuestas. Por supuesto, ​son más caras, requieren más tiempo, generalmente son recursos de Estado, ​se abren concursos públicos para hacerlo, etcétera. Les muestro esta ENSANUT primero, ​que es de México, y que si ustedes van a la página web, esta encuesta la hacen todos los años, ​de hecho, ENSANUT continúa, es una maravilla, en Chile no tenemos eso, es maravillosa, ​esto es un recurso de Estado enorme, es una tremenda inversión.

​Entonces, y fíjense que ​además están disponibles, yo aquí tomé cualquiera el 23, están disponibles hasta las bases de datos, ​está todo disponible, miren, están disponibles las bases de datos incluso en tres formatos, ​usted la quiere en SPSS, en STATA, o en CSV, que es separado por, es como en Excel, pero separado ​por coma, es un tipo de texto, bueno, sí, están los cuestionarios, las bases de datos, es maravilloso. ​Esto es una encuesta poblacional, diferencias, aquí está la 2021, es la que tengo, que tenía ​una información que les voy a mostrar, que quería mostrarles.

​Entonces, cuáles son estas, ​el paralelo en Chile es nuestra encuesta nacional de salud, que se hizo el 2003, el 2010 y el 2016, ​y hasta ahora han pasado 10 años y no ha, el ministerio no ha logrado licitar una nueva, ​y han pasado 10 años, porque no han llegado a lograr acuerdo entre lo que están pidiendo y ​la plata que tienen, entonces las licitaciones han quedado desiertas. ¿Cuál es el gran objetivo ​de estas encuestas? Es actualizar, ellos dicen actualizar porque lo hacen todos los años, ​para nosotros ya después de 10 años es una actualización bien retardía, tardía.

​Entonces, ​la distribución y tendencias de indicadores sobre condiciones de salud y nutrición en habitantes y ​viviendas particulares de México, en Chile es básicamente salud, no habla tanto de nutrición, ​pero hay preguntas de todas las áreas, de todas las áreas que quieran, todas, todas, todas, ​y entonces aquí hay un tema especial por el periodo que tiene que ver con el COVID, ​¿ok? Esto es una encuesta, esto es una encuesta poblacional.

​Fíjense, ​un diseño muestral probabilístico estratificado por conglomerados, o sea, ​se van, es igual que la encuesta nacional de salud, hay un empadronamiento, se elige ​aleatoriamente una manzana en cada comuna, de esa manzana se elige aleatoriamente un hogar, ​y de ese hogar se elige aleatoriamente a una persona, y esa es la persona que se encuesta, ​¿ok? Por lo menos en Chile, aquí no sé si hacen más de una por hogar, en Chile es una por hogar.

​Y esto es lo que les quiero leer, miren qué bonito, respecto a la incertidumbre de las ​estimaciones presentadas, todas las estimaciones son inciertas debido al error de muestreo, ​miren qué bonito, esta es una clase estadística este párrafo. Es decir, ​a la obtención de conclusiones a partir de un subconjunto de la población, de una muestra, ​el error de muestreo de cualquier estimador puede ser cuantificado por un intervalo de ​confianza, y en este informe no se incluyeron todos los intervalos de confianza dado la gran ​cantidad de estimaciones reportadas, o sea, sería infinito. Sin embargo, estas pueden ser calculadas ​a partir de la fase de datos que nos entregan.

​Adicionalmente, es importante señalar que dada ​la cantidad de intervalos confianza que se presentan, existe la posibilidad de que algunos ​de ellos sean equivocados en el sentido de no incluir el parámetro. Esa frase es maravillosa, ​eso es entender estadística. Cuando, si ya vieron la clase intervalo confianza, ​cuando uno construye un intervalo al 95% de confianza, lo que está diciendo en realidad ​es que hay un 5% de probabilidad de que ese intervalo no contenga el parámetro, ¿se acuerdan? ​Es decir, que yo no le haya apuntado al rango donde está el parámetro. Dicho de otra manera, ​cada 100 intervalos de confianza que yo haga, es probable que en 5 de ellos queden fuera, ​sin contener al parámetro, y que en 95 efectivamente lo contengan, ¿se entiende?

​Y ellos lo están asumiendo porque están construyendo, si tú construyes dos intervalos ​confianza y la probabilidad es de 95%, seguro que esos dos están bien, pero si tú construyes ​la cantidad de intervalos de confianza que aquí se construyen, porque son muchas variables, ​evidentemente empieza a existir la posibilidad de que algunos de ellos sean equivocados en el ​sentido de no incluir el parámetro. ¿Se fijan qué bonito?

​También se desea enfatizar que algunos ​intervalos confianza podrían no ser de utilidad práctica para los tomadores de decisiones, ​especialmente si los estimadores son muy amplios, lo cual es más frecuente que suceda cuando se ​hacen estimaciones con pocas observaciones. ¿Se han cuentado la tremenda clase estadística que ​es este párrafo? Lo que estábamos viendo recién, en la medida que tengo un n pequeño, ​los intervalos de confianza se hacen más amplios y entonces dejan de ser informativos. En este caso, ​estas encuestas poblacionales, como estas de salud, es para las toma de decisiones, ​es para aporte de políticas públicas, ¿ok? Entonces lo reconoce. Hay casos en que tengo ​tan poquitas observaciones que el intervalo de confianza es muy amplio, por lo tanto deja de ser ​utilidad práctica para los tomadores de decisiones. ¿Ven qué bonito? ¿Alguna consulta? ¿Se entendieron ​los conceptos que ellos recalcan acá? No hay ningún comentario, no parece.

**Estudiante:** ​Súper específico, profe, cómo ellos relatan lo que han incorporado.

**Profesor:** ​Es muy bonito. Bueno, para mí que soy estadística es bonito, a lo mejor usted no lo encuentra tan ​bonito.

**Estudiante:** Pero es muy específico, que no se ve habitualmente.

**Profesor:** No, no se ve. Yo no he visto ​este párrafo tomando en cuenta lo que es error de muestreo, lo que es error de muestreo ajustado ​al tamaño, edad, lo que es la confianza. Aquí están todos los conceptos incorporados y tomados, ​y además se fijan que están dichos en un lenguaje que puede ser entendido para cualquier lector. ​¿Estamos? Yo lo valoro muchísimo, por eso me quedé pegada hace tiempo ya en esta del 2021, ​porque en las siguientes no la he encontrado y me da mucha pena, porque está muy bonito, ​que no quiero dejar de mostrarlo.

### Factores de Expansión y Resultados

**Profesor:** Entonces, les voy a mostrar resultados de las encuestas ​poblacionales. De partida, bueno, aquí hay una pregunta que tiene que ver con seguridad alimentaria ​en los hogares. Miden un puntaje, y a partir de ese puntaje habla de la calidad o cantidad de ​alimentos que acostumbran a ver disponibles en el hogar. A eso se refiere seguridad alimentaria. Y ​habla, crean una escala, como dicen acá, y generan puntos de corte. Las escalas además son distintas, ​tiene más preguntas si es que en el hogar hay menores de edad o no.

​Y entonces aquí están las ​escalas, ¿ven? Aquí hay seguridad alimentaria, inseguridad alimentaria leve, moderada, ​inseguridad alimentaria severa, que llega a ser ese punto en que las personas del hogar tienen ​hambre y no pueden satisfacer sus necesidades, ¿ok? Y ese es como el RAP. Entonces, una característica ​de las encuestas poblacionales es que existe lo que se llaman factores de expansión. Cada persona... ​Yo, Paola Viviani, mujer de veinticinco años, ¿a cuántas mujeres represento yo? ​A mujeres como yo, con mi nivel de educación, con mi género, con mi edad, ¿estamos? ​¿A cuántas mujeres yo represento?

​Entonces, eso es lo que se llama factores de expansión, ese multiplicador que se crea, ​que se construye a partir de los datos del INE, que por eso es tan importante el censo, ​todos los países tienen censo, y ese censo te da la estructura poblacional. ​Entonces, ¿cuántas mujeres como yo, de acuerdo a esas variables que interesa, hay en el país? ​Y entonces, el n muestral se puede expandir, y esto sí que es un expandir, ​a miles de personas. ​Ahora, este miles en México debe ser como treinta y seis miles, ​¿habrán treinta y seis millones? Yo creo que es poco para México, ​no sé cuántos millones hay en México. ​Ah, pero son adultos, mayores de dieciocho, podría ser. ​¿Se fijan?

​Entonces, el n muestral es de cuatro mil setecientos doce, ​eso representa a catorce mil trescientas personas, o lleva a millones, no sé lo que es. ​¿Vale? Pueden ser catorce millones de personas. ​Entonces, ¿esto qué es lo que permite? ​Permite hacer una estimación, de alguna manera, de lo que sería una política pública. ​¿Se fijan? Lo lleva a la realidad. ​Todas las preguntas de, todas las encuestas poblacionales, ​trabajan con estos factores de expansión, que son muy difíciles de construir. ​Hay pocas personas que tienen ese talento de saber construir factores de expansión. ​¿Estamos? ​Entonces, entregan el estimador puntual y el intervalo de confianza. ​¿Ok?

​Entonces, ¿qué sí es correcto decir? ​Estimador puntual, un diez por ciento de los mexicanos mayores de dieciocho años, ​porque tienen la representatividad nacional, ​presentan inseguridad severa en su hogar, imagínense qué alto. ​¿Ok? ​Y el intervalo de confianza está entre nueve coma tres y diez coma uno. ​¿Se fijan que el margen de error es muy pequeño? ​Es como más o menos cero siete, porque es un nene muy grande. ​¿Estamos? ​Ok.

​Y luego, entonces, esto es una tabla, pero lo mismo, ​solo para mostrarles cómo los intervalos de confianza empiezan a ampliarse un poco, ​porque se empieza a achicar el intervalo, el tamaño muestral, ​porque aquí separaron en tres tipos de localidad, ruralidad, ​lo que llaman urbano y metropolitano, de acuerdo a la cantidad de habitantes. ​Entonces, los intervalos de confianza empiezan a ser más amplios. ​¿Se fijan? ​¿Lo ven? ​Y de nuevo, ¿cuánto es el n muestral? ​¿A cuántas personas representa? ​Expansión, estimador, intervalo confianza. ​¿Ok? ​¿Se entiende?

​Entonces, esta es la manera adecuada de hacer inferencias. ​Y eso, fíjense que lo podríamos hacer las encuestas. ​He visto algunas que están apareciendo ahora, ​una de las últimas de CADEM, de hecho, ​que están presentando sus resultados con intervalo de confianza. ​Y no es tan difícil, ¿se fijan? ​Hay distintas maneras de hacerlo. ​Esta que les estoy mostrando aquí es con tabla. ​En general, estas encuestas públicas trabajan más con imágenes, ​la manera de transmitir, pero les voy a mostrar que es posible también. ​Pero los datos se pueden entregar con intervalo de confianza. ​Lo que pasa es que quedaría en evidencia ​que hay unos intervalos de confianza muy amplios, ​con un margen de error de 10%, ​que como muy bien dicen aquí, ​dejan de ser de utilidad, dejan de ser un informativo.

---

### Encuestas Nacionales en Chile (CASEN, Salud, etc.)

**Profesor:** ​Entonces, aquí les presento nuevamente, vuelvo a Chile, ​el Ministerio de Desarrollo Social de Chile tiene una página web, ​aquí está el observatorio, se llama, ​donde están disponibles muchas encuestas nacionales.

**Germán:** *(En el chat)* ​¿Cuál es un margen de error aceptable, Germán?

**Profesor:** ​Las encuestas nacionales suelen trabajar con un... ​La encuesta nacional chilena... ​Bueno, lo que pasa es que una cosa es el margen de error de encuestas rápidas. ​Estas encuestas tienen objetivos distintos, ¿se fijan? ​Las encuestas de opinión tienen un objetivo que es diferente, ​que es conocer la opinión de las personas, pero rápido. ​Exacto, eso depende del caso de estudio, exactamente, eso quería explicar. ​En cambio, las encuestas poblacionales tienen un objetivo mucho más claro, ​que es conocer la realidad de la población, ​en factores de salud especialmente, pero aquí pueden ver que hay de todo.

​Entonces, requieren de más precisión, pero son más caras, son más lentas, ​son mucho más caras. ​Entonces, depende del objetivo. ​Ahora, si tú vas a hacer una encuesta y efectivamente tienes un 10% de error, ​obviamente no suena aceptable, ​porque ¿cómo vas a entregar información con esa variabilidad? ​Lo razonable suele ser en torno al 3%, eso es un buen margen de error, ​porque si tu estimador es de un 25%, tú dices entre un 22% y un 28%, ​ya suena razonable. ​¿Está bien, Germán?

​Con un margen de error muy alto, no puedes tomar decisiones, ​que es como dice aquí la encuesta mexicana, ​que dejan de ser de utilidad práctica para los tomadores de decisiones. ​Ese es el tema. ​Y en el tema de la opinión pública, el efecto es distinto. ​En encuestas poblacionales no serían de utilidad para los tomadores de decisiones. ​En encuestas de opinión pública no son válidas sus comparaciones, ​así que ese es el tema.

​Decir que un candidato está por sobre otro, ​que se hace mucho en cualquier país en periodos eleccionarios, ​dicen tal candidato tomó la delantera y está dos puntos arriba del candidato B. ​Dos puntos arriba no es estar más arriba. ​Está dentro del margen de error. ​¿Se fijan? ​Entonces ahí es donde yo creo que hay una responsabilidad importante. ​Que yo quisiera que todos los periodistas, gente de prensa, ​y todos ellos hicieran un curso de estadística conmigo. ​¿Ok? ​¿Estamos? ​Porque no está mal hecha la encuesta. ​Está bien. ​El tema es cómo transfieren la información y qué conclusiones sacan de eso. ​¿Estamos? ​¿Contesté Natalia, Germán? Entonces...

**Natalia / Germán:** ​Sí, gracias.

**Profesor:** ​Súper. ​Si les gustan estos temas, ​estas son todas encuestas disponibles. ​Si quieren hacer después sus proyectos o lo que sea, ​estas son todas encuestas disponibles. ​Y pueden ver que hay temas diversos. ​La CASEN es la clásica de caracterización socioeconómica ​que efectivamente es para tomadores de decisiones, ​porque todas las ayudas gubernamentales se basan en su caracterización de CASEN.

​Hay otras menos conocidas, ​estas de actividades de niños y niñas adolescentes. ​Esta ELPI es muy bonita porque efectivamente es de seguimiento, ​es longitudinal. ​Y acaba de salir una última, 2025, si no me equivoco. ​Hay una CASEN en pandemia, ​encuesta social de COVID. ​Estas son especiales que se hicieron. ​Esta de la ENADI, ​de discapacidad 2015, ​y fíjense que no he visto ninguna nueva.

​Bueno, y les quiero mostrar una del Ministerio de Salud, ​esas son del Ministerio de Desarrollo. ​El Ministerio de Salud tiene otro grupo de encuestas asociado a salud, por supuesto, ​donde está la encuesta nacional de salud, ​y hay otras. ​Y otras que les quiero mostrar es la encuesta, ​porque es menos conocida que la de salud, ​para mostrarles algo distinto, ​es la de sexualidad y género.

​Es una encuesta que se hizo por primera vez, ​pos pandemia, entre el 2022 y 2023, ​nunca se había hecho antes, esta encuesta. ​Entonces, población de objetivo, ​18 años y más, chilenos, bla, bla, bla. ​Objetivo de la encuesta, ​conocer las características de salud, sexualidad y género de la población chilena. ​Tiene representatividad nacional, regional, por tramo de edad y sexo.

​El diseño muestral, ​es una encuesta presencial en hogares con diseño probabilístico, ​estratificado geográficamente y multietápico, ​lo mismo que les decía antes. ​Se elige la comuna, de la comuna se elige la manzana, ​de la manzana se elige la vivienda, ​y de la vivienda se elige la persona. ​Error absoluto de 0,7 a nivel nacional. ​¿Se fijan? Porque es grande. ​Calculado bajo el supuesto de aleatoriedad, ​con un 95% de confianza.

​Esto de la prevalencia máxima no se los voy a explicar, ​pero es bajo el peor escenario. ​Lo peor que puede pasar es que algo tenga una probabilidad 0,5. ​Es como lanzar una moneda en vez de hacer la encuesta. ​Factores de expansión calculados en base al censo del 2017. ​¿Ven que es verdad todo lo que les digo? ​Ok, miren, 20.000 personas, es que es mucho. ​20.000 personas. ​Aplicada entre agosto y diciembre. ​Una tasa de logro del 102%. ​Miren qué bonito, se les pasó. ​Eso es porque siempre se calcula el tamaño muestral, ​pero se asume que va a haber cierto rechazo, cierta pérdida, ​entonces se amplía la búsqueda. ​Y aquí les fue bien.

​Y entonces, eso es lo que me interesa. ​Miren qué bonito, cómo se pueden mostrar los resultados. ​Esto lo podrían hacer perfectamente las encuestas de opinión. ​Perfectamente. ​Incluir el intervalo confianza. ​Lo que pasa, lo que les decía, se verían así unos márgenes gigantes ​que no se ven muy bien. ​Pero ven qué bonito. ​Miren, 20.000 encuestados. ​Para una población proyectada, expansión, ​muestra expandida, de hecho esa es la palabra, ​con estructura de factores de expansión, ​calculaba en base al INE, lo que les explicaba, ​que representa 13 millones y medio de personas. ​Son 6 millones y medio chilenos y 7 millones mujeres. ​O sea, hombres y 7 millones mujeres.

​Y aquí hay algunos de los resultados. ​Se fijan a la pregunta, no, esta es la distribución de la muestra. ​Cuántos hombres y mujeres, grupo etario de los hombres ​y grupo etario de las mujeres. ​Esta es recién la distribución de la muestra. ​Aquí traje una de las preguntas, porque acuérdense que eran 300 ​y tantas preguntas. ​Pero una de las preguntas para mostrarles cómo se puede mostrar ​la información con intervalos de confianza.

​Evaluación de la educación sexual en el colegio o escuela según sexo ​y grupo. ​La pregunta era cómo evaluaría, aquí está muy en chiquitito abajo, ​no sé si lo alcanzan a ver, ​cómo evaluaría en general la formación de sexualidad que revisó, ​que recibió en su colegio o escuela. ​Muy mala o mala. ​Ah, están dando el porcentaje de quienes dijeron muy mala o mala. ​Ok, y entonces aquí está por sexo. ​Amarillo es nacional, hombre, mujer. ​Por grupo etario en los hombres, por grupo etario en las mujeres. ​Bueno, este es el resultado principal, supongo que por eso está…

​Bueno, y abajo, muy chiquitito, no sé si lo alcanzan a ver, ​dice, para hombres se observan diferencias estadísticamente ​significativas entre el grupo de 18-29 años en comparación ​con los otros grupos de edad por el intervalo de confianza. ​En los hombres, entre el de 18-29 años con el resto. ​¿Se fijan que el resto está traslapado? ​En cambio, el de 18-19 yo podría tirar una línea recta aquí ​y no topo a nadie. ​Está excluyente. ​Entonces abajo lo reconocen como diferencia significativa.

​Para mujeres, sigo leyendo abajo muy chiquitito, ​se observan diferencias estadísticamente significativas ​entre 18-29 años a 30-39 en comparación a los otros grupos de edad. ​O sea, está diciendo, esta es distinta de esta, ​y estas dos son distintas de las otras. ​Las otras tres se traslapan, según lo que entiendo la redacción.

---

## Conclusiones y Resumen

**Profesor:** ​Pero lo que quiero mostrarles son varias cosas. ​Primero, entender por qué separo estos dos tipos de encuestas. ​En las dos se realiza estimación puntual. ​Pero, bueno, en las dos se obtienen estimadores. ​Esa es la palabra correcta. ​En las dos se obtienen estimadores. ​En las encuestas poblacionales hay mucho más cuidado ​de hacer inferencia con intervalos de confianza ​que en las encuestas de opinión. ​Las razones, yo creo que ya no se las voy a repetir, ¿no? ​Pero ambas son de utilidades distintas. ​Ambas tienen objetivos distintos. ​¿Ok?

​Pero aquí es donde les muestro entonces, ​cuando me fui rápidamente, ​cuando les muestro aquí cómo se hace inferencia ​con estimación puntual. ​Ahora es entender lo que es y que no me gusta, ​que no estoy de acuerdo que se haga, ​no se debiera hacer, ​que es simplemente tomar el valor de la encuesta ​y convertirlo en un estudio... en el resultado de la población.

​Intervalos de confianza, lo que les estoy mostrando ahora, ​es reconocer la variabilidad muestral, que hay un margen de error. Piensen que si yo tomo una ​encuesta ahora, en este minuto, voy a obtener un resultado. Y si lo tomo dos minutos después, ​voy a obtener otro resultado. Y si lo tomo mañana, otro resultado. Todo el rato voy a ​obtener resultados distintos, porque es variabilidad muestral. Si la opinión es un 30%, ​observaré un 30% ahora, un 29% en una hora más, un 32% en una otra más, y todo dentro de un margen ​de variabilidad muestral.

​Entonces, esta clase era sobre mostrarles los tipos de encuestas, ​mostrarles qué es la estimación puntual, por qué no me gusta. Aunque entiendo, ya les dije, ​que hay un contexto, un marco, donde en el fondo se justifica su uso. Y mostrarles encuestas más ​robustas, a las que llamé encuestas poblacionales, donde los resultados, la inferencia, se hace con ​intervalos de confianza. Se suele hacer así. Ahora, igual, uno ve estimación puntual en ​estas encuestas, se hace la encuesta nacional de salud, y sale publicado inmediatamente: "Un 60% ​de los chilenos presenta obesidad", y se les olvida el intervalo de confianza. También pasa. Que se ​hace estimación puntual. Pero los informes son mucho más cuidadosos.

​Con eso termino, ​y abro el espacio para comentarios. ¿Alguien necesita que yo me devuelva alguna diapositiva ​antes de dejar de compartir? ¿Para comentar algo? ¿Preguntar algo de alguna diapositiva ​en particular? Entiendo eso como un no. Ok. Entonces, eso es lo que traía para contarles.

---

### Preguntas Finales

**Eliana:** ​Dime, Eliana. ¿Estimador puntual, o estimador muestral? Porque estimador puntual se hace a partir de la muestra. ​Eso lo que yo entiendo, y en general en otros libros lo llaman estimador muestral. Entonces, ahora que tengo que contestar la tarea, y nos dicen, estimador, y calcule el intervalo intercuartilico del 95%, ¿nos tenemos que utilizar el muestral, o el puntual?

**Profesor:** ​Los que son conceptos distintos. El estimador muestral es el valor que observas, que obtienes de la muestra. ¿Ok? ​Al nosotros referirnos como inferencia, estimación puntual, es porque ese estimador muestral lo conviertes en parámetro poblacional. ​¿Se entiende? ​No te escucho exactamente todo, Eliana, pero estoy tratando de escucharte lo mejor posible. No sé si te respondí la pregunta.

**Eliana:** ​Llevamos a un estimador puntual para poder inferir después el poblacional, ¿cierto?

**Profesor:** ​Ahora te escucho bien. En una encuesta, cualquiera de los dos tipos, observo un 25% tabaquismo. Ese es mi estimador muestral, es el resultado que obtuve de la muestra.

**Eliana:** ​Perfecto.

**Profesor:** ​Hacer estimación puntual, es decir, el 25% de la población presenta tabaquismo. Es hacer el paso a la inferencia usando solo ese valor muestral.

**Eliana:** ​Ya.

**Profesor:** ​¿Se entiende?

**Eliana:** ​Perfecto. Sí, ahora sí.

**Profesor:** ​Por eso, tengo en inferencia puntual, que es tomar el estimador muestral y convertirlo en parámetro, intervalos de confianza, que es lo que vimos ahora y que ustedes están viendo ahora, o test de hipótesis, que es lo que parte la próxima semana. ​Son las tres maneras de hacer inferencia. ¿Cuál no me gusta? La puntual.

**Eliana:** ​La puntual.

**Profesor:** ​Por todo lo que conversamos hoy día, de las cosas que no considera. ¿Está bien? ¿Se entiende?

**Eliana:** ​Perfecto, profesora. Muchas gracias.

**Profesor:** ​De nada, Eliana. ¿Algo más? ​¿Algún otro comentario, pregunta? ​Ok. Bueno, vamos a parar de grabar, yo creo, María José, para que no quede este silencio largo al final.
