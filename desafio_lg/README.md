🎵 Análisis de Lista de Reproducción - Lady Gaga

Disponemos de información sobre una lista de reproducción de la cantante Lady Gaga, y nuestro objetivo es desarrollar funciones para procesar y normalizar estos datos para un posterior análisis.

📌 Datos de Ejemplo
Tema: "Bradley Cooper | Lukas Nelson - Shallow"
Vistas: "1900 millones"
Duración: "3:37"
Link: "https://www.youtube.com/watch?v=bo_efYhYU2A"
Fecha de Lanzamiento: "2018-09-27"


🚀 Funciones a Implementar
El programa deberá incluir las siguientes funciones:
🔹 obtener_colaboradores(titulo: str) -> list
Recibe como parámetro el título del tema.
Retorna una lista con los colaboradores (excluyendo el nombre del tema).


🔹 obtener_nombre_tema(título: str) -> str
Recibe el título del tema.
Retorna el nombre real del tema, eliminando a los colaboradores.


🔹 convertir_vistas_numerico(vistas: str) -> int
Convierte la cantidad de vistas a un número entero expresado en millones.
Ejemplo: "1900 millones" → 1900000000.
🔹 convertir_duracion_numerico(duracion: str) -> int
Convierte la duración del video a un número entero expresado en segundos.


Ejemplo: "3:37" → 217 segundos.
🔹 obtener_codigo(url: str) -> str
Recibe una URL de YouTube.
Extrae y retorna el código único del video.
Ejemplo: "https://www.youtube.com/watch?v=bo_efYhYU2A" → "bo_efYhYU2A".
🔹 formatear_fecha(fecha: str) -> date
Recibe una fecha en formato YYYY-MM-DD.
Retorna la fecha como un objeto de tipo date.
🎯 Requisitos del Desarrollo
✅ Estructura Modular: Cada función debe cumplir una única responsabilidad.
✅ Uso de Tipado: Incluir anotaciones de tipo para mayor claridad.
✅ Validaciones: Manejar posibles errores de formato en las entradas.
✅ Optimización: Implementar las funciones de manera eficiente y clara.
📌 Objetivo Final
Estas funciones permitirán procesar la lista de reproducción de Lady Gaga, facilitando su análisis y manipulación en futuros desarrollos.