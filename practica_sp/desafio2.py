def validar_respuesta(correcta, elegida):
    """
    Valida si la respuesta elegida es correcta.
    Función pura: no modifica estado externo.
    
    Args:
        correcta: La respuesta correcta
        elegida: La respuesta elegida por el usuario
        
    Returns:
        bool: True si es correcta, False si no lo es
    """
    return correcta == elegida


def calcular_puntaje(actual, resultado, puntos):
    """
    Calcula el nuevo puntaje según el resultado.
    Función pura: no modificar el puntaje original.
    
    Args:
        actual: Puntaje actual del jugador
        resultado: True si acertó, False si falló
        puntos: Puntos a sumar o restar
        
    Returns:
        int: Nuevo puntaje calculado
    """
    if resultado:
        return actual + puntos
    else:
        return actual - puntos


def mover_jugador(posicion, resultado):
    """
    Calcula la nueva posición del jugador según el resultado.
    Función pura: no modificar la posición original.
    
    Args:
        posicion: Posición actual del jugador
        resultado: True si acertó, False si falló
        
    Returns:
        int: Nueva posición calculada
    """
    if resultado:
        return posicion + 1
    else:
        return posicion - 1


# Ejemplo de uso
if __name__ == "__main__":
    print("=== VALIDACIÓN DE RESPUESTAS ===\n")
    
    # Datos de ejemplo
    respuesta_correcta = "42"
    respuesta_usuario = "42"
    puntaje_jugador = 10
    posicion_jugador = 5
    puntos_pregunta = 5
    
    # Valida respuesta
    resultado = validar_respuesta(respuesta_correcta, respuesta_usuario)
    print(f"Respuesta correcta: {respuesta_correcta}")
    print(f"Respuesta usuario: {respuesta_usuario}")
    print(f"¿Es correcta? {resultado}\n")
    
    # Calcula nuevo puntaje
    nuevo_puntaje = calcular_puntaje(puntaje_jugador, resultado, puntos_pregunta)
    print(f"Puntaje anterior: {puntaje_jugador}")
    print(f"Nuevo puntaje: {nuevo_puntaje}\n")
    
    # Calcula nueva posición
    nueva_posicion = mover_jugador(posicion_jugador, resultado)
    print(f"Posición anterior: {posicion_jugador}")
    print(f"Nueva posición: {nueva_posicion}\n")
    
    # Ejemplo con respuesta incorrecta
    print("--- Caso con respuesta incorrecta ---\n")
    respuesta_usuario_incorrecta = "36"
    resultado_incorrecto = validar_respuesta(respuesta_correcta, respuesta_usuario_incorrecta)
    
    print(f"Respuesta usuario: {respuesta_usuario_incorrecta}")
    print(f"¿Es correcta? {resultado_incorrecto}")
    
    puntaje_con_error = calcular_puntaje(nuevo_puntaje, resultado_incorrecto, puntos_pregunta)
    posicion_con_error = mover_jugador(nueva_posicion, resultado_incorrecto)
    
    print(f"Puntaje después del error: {puntaje_con_error}")
    print(f"Posición después del error: {posicion_con_error}")


#  Escribir una función genérica, llamada aplicar_accion(valor, funcion),
# donde podés pasar funciones como parámetros.
# Ejemplo:
# nuevo_puntaje = aplicar_accion(puntaje, lambda x: x + 5)


def sumar_cinco(x):
    return x + 5

def restar_tres(x):
    return x - 3

def multiplicar_por_dos(x):
    return x * 2


def aplicar_accion(valor, funcion):
    """
    Aplica una función a un valor dado.
    Función pura: no modifica el valor original.
    
    Args:
        valor: Valor al que se le aplicará la función
        funcion: Función que se aplicará al valor
        
    Returns:
        Resultado de aplicar la función al valor
    """
    return funcion(valor)


# Ejemplo de uso de aplicar_accion
if __name__ == "__main__":
    print("=== APLICAR ACCIÓN GENÉRICA ===\n")
    
    puntaje_inicial = 10
    print(f"Puntaje inicial: {puntaje_inicial}")
    
    # Sumas 5 puntos
    puntaje_sumado = aplicar_accion(puntaje_inicial, sumar_cinco)
    print(f"Puntaje después de sumar 5: {puntaje_sumado}")
    
    # Restas 3 puntos
    puntaje_resta = aplicar_accion(puntaje_sumado, restar_tres)
    print(f"Puntaje después de restar 3: {puntaje_resta}")
    
    # Multiplicas por 2
    puntaje_multiplicado = aplicar_accion(puntaje_resta, multiplicar_por_dos)
    print(f"Puntaje después de multiplicar por 2: {puntaje_multiplicado}\n")