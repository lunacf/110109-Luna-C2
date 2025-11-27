import random

# Lista de diccionarios con las preguntas
banco_preguntas = [
    {
        "pregunta": "¿Cuánto es 7×6?",
        "opciones": ("36", "42", "48", "40"),
        "correcta": "42",
        "dificultad": "media",
        "puntos": 5
    },
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "opciones": ("Londres", "París", "Berlín", "Madrid"),
        "correcta": "París",
        "dificultad": "fácil",
        "puntos": 3
    },
    {
        "pregunta": "¿Cuánto es 15×8?",
        "opciones": ("120", "125", "115", "130"),
        "correcta": "120",
        "dificultad": "media",
        "puntos": 5
    },
    {
        "pregunta": "¿En qué año llegó el hombre a la Luna?",
        "opciones": ("1965", "1969", "1972", "1968"),
        "correcta": "1969",
        "dificultad": "media",
        "puntos": 5
    },
    {
        "pregunta": "¿Cuánto es 2+2?",
        "opciones": ("3", "4", "5", "6"),
        "correcta": "4",
        "dificultad": "fácil",
        "puntos": 2
    }
]

preguntas_usadas = set()

def seleccionar_pregunta(lista_preguntas, usadas=preguntas_usadas):
    """
    Selecciona una pregunta al azar que no haya sido usada.
    
    Args:
        lista_preguntas: Lista de diccionarios con las preguntas
        usadas: Set de índices de preguntas ya usadas
        
    Returns:
        tupla: (pregunta, opciones) o None si ya se usaron todas
    """
    indices_disponibles = []
    for i in range(len(lista_preguntas)):
        if i not in usadas:
            indices_disponibles.append(i)
    
    if not indices_disponibles:
        return None
    
    indice = random.choice(indices_disponibles)
    usadas.add(indice)
    
    pregunta = lista_preguntas[indice]
    return (pregunta["pregunta"], pregunta["opciones"])

# Ejemplo de uso
if __name__ == "__main__":
    print("=== BANCO DE PREGUNTAS ===\n")
    print("¡Bienvenido al juego de preguntas!\n")
    
    numero_pregunta = 1
    
    while True:
        resultado = seleccionar_pregunta(banco_preguntas)
        
        if resultado is None:
            print("¡Felicidades! Has completado todas las preguntas disponibles.")
            break
        
        pregunta, opciones = resultado
        
        print(f"Pregunta {numero_pregunta}: {pregunta}")
        for i, opcion in enumerate(opciones, 1):
            print(f"  {i}. {opcion}")
        
        respuesta = input("\nTu respuesta (1-4) o 'salir' para terminar: ").strip().lower()
        
        if respuesta == "salir":
            print("\n¡Gracias por jugar!")
            break
        
        print("-" * 50)
        numero_pregunta += 1
    
    print(f"\nResumen: Has respondido {len(preguntas_usadas)} de {len(banco_preguntas)} preguntas.")
