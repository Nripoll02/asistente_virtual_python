
# Asistente Virtual de Consola

Este es un asistente virtual interactivo basado en comandos escritos, diseñado para ofrecer varias funcionalidades útiles como abrir YouTube, realizar búsquedas en Wikipedia, contar chistes, y más. Todo el control se realiza mediante comandos de texto introducidos en la consola.

## Características

- Abrir sitios web populares como YouTube y Google.
- Realizar búsquedas en Wikipedia y en Google.
- Reproducir videos de YouTube.
- Informar la fecha y la hora actual.
- Contar chistes en español.
- Consultar el precio de acciones de empresas importantes.
- Proceso completamente interactivo basado en texto.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

### Instalación de Python y paquetes necesarios

1. **Python**: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [aquí](https://www.python.org/downloads/).
   - Verifica la instalación con: `python --version` o `python3 --version`.

2. **Instalar las dependencias**:
   - Abre la terminal o consola en la carpeta de tu proyecto y ejecuta:
     ```bash
     pip install pyttsx3 pywhatkit yfinance pyjokes wikipedia
     ```

   Estos paquetes son necesarios para que el asistente virtual funcione correctamente:
   - **`pyttsx3`**: Para la síntesis de voz.
   - **`pywhatkit`**: Para realizar búsquedas en la web y reproducir videos de YouTube.
   - **`yfinance`**: Para consultar el precio de acciones.
   - **`pyjokes`**: Para contar chistes.
   - **`wikipedia`**: Para realizar búsquedas en Wikipedia.

## Uso

Sigue los siguientes pasos para ejecutar y utilizar el asistente:

### 1. Clonar el proyecto o copiar el código
Copia el código en tu entorno de desarrollo o clona el repositorio si está en uno.

### 2. Ejecutar el script
- En tu terminal o consola, navega hasta la carpeta del proyecto y ejecuta el siguiente comando:
  ```bash
  python main.py
  ```

  Esto inicializará el asistente, que te saludará y estará listo para recibir comandos.

### 3. Ingresar comandos
Escribe los comandos que deseas en la consola. A continuación, se muestra la lista completa de los comandos disponibles.

## Comandos disponibles

A continuación, se detalla la lista de comandos que el asistente reconoce y sus acciones correspondientes:

### Comandos principales

1. **Abrir YouTube**
   - Comando: `"abrir youtube"`
   - Acción: Abre YouTube en el navegador predeterminado.

2. **Abrir el navegador**
   - Comandos: `"abrir navegador"`, `"abrir el navegador"`
   - Acción: Abre el navegador en Google.

3. **Consultar el día actual**
   - Comandos: `"qué día es hoy"`, `"que día es hoy"`, `"qué día es"`
   - Acción: Te informa qué día de la semana es.

4. **Consultar la hora actual**
   - Comandos: `"qué hora es"`, `"que hora es"`, `"qué hora"`
   - Acción: Te informa la hora actual.

5. **Buscar en Wikipedia**
   - Comando: `"busca en wikipedia [consulta]"` 
   - Acción: Realiza una búsqueda en Wikipedia y te da un resumen de la información encontrada. Solo necesitas reemplazar `[consulta]` por el tema que quieras investigar.

6. **Buscar en Internet**
   - Comando: `"busca en internet [consulta]"`
   - Acción: Realiza una búsqueda en internet usando el motor de Google. Solo necesitas reemplazar `[consulta]` por la información que desees buscar.

7. **Reproducir un video en YouTube**
   - Comando: `"reproducir [nombre del video]"`
   - Acción: Busca y reproduce un video en YouTube según la consulta que ingreses. Solo debes reemplazar `[nombre del video]` por el nombre del video que quieras ver.

8. **Contar un chiste**
   - Comando: `"chiste"`
   - Acción: El asistente te contará un chiste en español.

9. **Consultar el precio de una acción**
   - Comando: `"precio de la acción [nombre de la empresa]"`
   - Acción: Busca el precio actual de las acciones de una empresa. Por ejemplo, puedes consultar los precios de empresas como Apple, Amazon, Google y Tesla.

10. **Finalizar la sesión**
    - Comando: `"adiós"`
    - Acción: El asistente finalizará la interacción y se cerrará el programa.

### Ejemplos de uso

- Para abrir YouTube:
  ```
  abrir youtube
  ```

- Para consultar el precio de las acciones de Apple:
  ```
  precio de la acción apple
  ```

- Para saber la hora:
  ```
  qué hora es
  ```

## Personalización

Puedes personalizar el asistente de la siguiente manera:
- **Voz**: Puedes cambiar la voz que usa el asistente editando la línea `engine.setProperty("voice", id3)` en la función `hablar()`. Elige entre diferentes voces disponibles en tu sistema.
- **Comandos adicionales**: Si deseas agregar más comandos o funcionalidades, puedes expandir el bloque de `elif` en la función `centro_pedido()`.

## Contribuciones

Si deseas contribuir a este proyecto, no dudes en realizar un fork, añadir tus mejoras y enviar un pull request. ¡Toda contribución es bienvenida!
