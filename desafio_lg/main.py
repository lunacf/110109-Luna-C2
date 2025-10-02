import json as load
# manejo de archivos
canciones: list[dict] = []

def leer_canciones() -> list[dict]:
    if not canciones or len(canciones) == 0:
        with open('canciones.json', 'r', encoding= 'utf-8') as archivo:
            archivo.read
            canciones.extend = load.json(archivo)
    return canciones

def obtener_colaboradores(titulo: str) -> list:
    for canciones in canciones:
        if canciones['title'] == titulo:
            return canciones['collaborators']
        return []

# Obtener el nombre del tema sin el artista
def obtener_nombre_tema(titulo: str) -> str:
    for canciones in canciones:    
        if canciones['title'] == titulo:
            return canciones['theme_name']
    return []


# Convertir vistas a número entero
def convertir_vistas_numerico(vistas: str) -> int:
    for canciones in canciones:
        if canciones['title'] == vistas:
            vistas_str = canciones['views']
            vistas_str = vistas_str.replace(',', '')
            return int(vistas_str)

# Convertir duración a segundos
def convertir_duracion_segundos(duracion: str) -> int:
    for canciones in canciones:
        if canciones['title'] == duracion:
            duracion_str = canciones['duration']
            minutos, segundos = map(int, duracion_str.split(':'))
            return minutos * 60 + segundos
    return 0

def obtener_codigo(url: str) -> str:
    for codigos in codigos:
        if codigos['title'] == url:
            url = codigos['Link']
            

