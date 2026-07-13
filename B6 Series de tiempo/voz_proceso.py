from gtts import gTTS
import os

texto = """
Imagina que cada día de tu vida deja una huella: lo que comiste, cómo dormiste, cuánto caminaste.
Al mirar hacia atrás, notas que algunos días se parecen entre sí, como si el presente aún recordara un poco de su pasado.
Eso, en esencia, es un proceso lineal: una historia donde el presente no aparece de la nada, sino que nace de una mezcla de lo que ya ocurrió.

Un proceso lineal es como un eco del tiempo. Cada valor nuevo —como el precio del dólar, la temperatura o el tráfico diario—
toma un poco del día anterior, un poco del anterior a ese, y así sucesivamente, con cada influencia haciéndose más débil.
Al principio, el pasado pesa mucho. Pero a medida que uno mira más atrás, esos recuerdos se van desvaneciendo.
Por eso decimos que el sistema tiene memoria, pero una memoria que se diluye.

Los modelos AR, MA y ARMA son distintas formas de contar esa historia.
Un modelo AR, o autorregresivo, dice: “El presente depende de los valores pasados”.
Un modelo MA, o de media móvil, dice: “El presente depende de los errores cometidos en el pasado”.
Y el modelo ARMA mezcla ambos mundos: recuerda los valores y también los errores.

Cuando representamos un proceso lineal, estamos escribiendo la receta matemática de esa memoria.
Cada coeficiente indica cuánto pesa el pasado. Si esos pesos se van reduciendo, el proceso es estable: nunca se desborda.
Si no se reducen, la historia se descontrola.

El truco está en que todo proceso estable tiende a regresar a su centro, a su promedio.
Si el tiempo pasa suficiente, cualquier predicción, por muy compleja que sea, terminará acercándose a ese valor medio.
Por eso, los pronósticos a largo plazo siempre parecen constantes: el futuro lejano se comporta como el equilibrio del sistema.

Los gráficos de autocorrelación —la ACF y la PACF— nos muestran esa memoria visualmente.
En un AR, la memoria se apaga lentamente; en un MA, se corta abruptamente; en un ARMA, vibra un poco antes de desvanecerse.
Es la huella digital del tiempo, una firma matemática que nos dice cómo recordar.

En resumen, un proceso lineal es la forma en que la estadística le da estructura al pasado para entender el futuro.
Es una historia de memoria, de ruido, de equilibrio, y de cómo los datos, igual que las personas, nunca se desprenden del todo de su historia.
"""

# Crear el objeto de voz
tts = gTTS(text=texto, lang='es')
# Obtener la ruta de la carpeta donde está este script
ruta_actual = os.path.dirname(__file__)

# Construir la ruta completa del archivo MP3
audio_path = os.path.join(ruta_actual, "procesos_lineales_historia.mp3")

# Guardar el archivo en esa ruta
tts.save(audio_path)

print(f"Archivo generado: {audio_path}")

