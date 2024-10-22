import pyttsx3
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Opciones de voz / idioma
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

# Función para que el asistente pueda ser escuchado
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", id3)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Informar el día de la semana
def pedir_dia():
    dia = datetime.datetime.today()
    dia_semana = dia.weekday()

    # Diccionario de los días
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miércoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domingo"}

    # Decir el día de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")

# Informar qué hora es
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"

    # Decir la hora
    hablar(hora)

# Función saludo inicial
def saludo_inicial():
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"

    # Decir saludo
    hablar(f"{momento}, en qué te puedo ayudar?")

# Función central del asistente
def centro_pedido():
    saludo_inicial()

    while True:
        # Recibir el pedido por escrito
        pedido = input("Escribe tu comando: ").lower()

        if "abrir youtube" in pedido:
            hablar("Estoy abriendo YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "abrir navegador" in pedido or "abrir el navegador" in pedido:
            hablar("Estoy abriendo el navegador")
            webbrowser.open("https://www.google.com.ar")
        elif "qué día es hoy" in pedido or "que día es hoy" in pedido or "qué día es" in pedido:
            pedir_dia()
        elif "qué hora es" in pedido or "que hora es" in pedido:
            pedir_hora()
        elif "busca en wikipedia" in pedido:
            hablar("buscando en wikipedia")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Encontre esta información en wikipedia")
            hablar(resultado)
        elif "busca en internet" in pedido:
            hablar("Buscando información")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
        elif "reproducir" in pedido:
            hablar("Reproduciendo")
            pedido = pedido.replace("reproducir", "").strip()
            pywhatkit.playonyt(pedido)
        elif "chiste" in pedido:
            hablar(pyjokes.get_joke("es"))
        elif "precio de la acción" in pedido:
            accion = pedido.split("de")[-1].strip().lower()
            cartera = {
                "apple": "AAPL",
                "amazon": "AMZN",
                "google": "GOOGL",
                "tesla": "TSLA"
            }
            try:
                accion_buscada = cartera[accion]
                ticker = yf.Ticker(accion_buscada)
                precio_actual = ticker.info['regularMarketPrice']
                hablar(f"El precio de {accion} es {precio_actual} dólares.")
            except KeyError:
                hablar(f"No tengo información sobre la acción de {accion}.")
            except Exception as e:
                hablar("Perdón, pero no pude encontrar la información de la acción.")
        elif "adiós" in pedido:
            hablar("Nos vemos, avísame si necesitas otra cosa.")
            break

centro_pedido()
