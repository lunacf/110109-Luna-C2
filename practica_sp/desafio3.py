def leer_csv_manual(nombre_archivo):
    """
    Leer archivo CSV manualmente sin usar el módulo csv.
    
    Args:
        nombre_archivo: Ruta del archivo CSV
        
    Returns:
        list: Lista de diccionarios con las preguntas
    """
    preguntas = []
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        
        # Primera línea son los encabezados
        encabezados = lineas[0].strip().split(',')
        
        # Resto de líneas son los datos
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            
            # Dividir por comas, pero respetando las comillas
            valores = []
            valor_actual = ""
            dentro_comillas = False
            
            for caracter in linea:
                if caracter == '"':
                    dentro_comillas = not dentro_comillas
                elif caracter == ',' and not dentro_comillas:
                    valores.append(valor_actual)
                    valor_actual = ""
                else:
                    valor_actual += caracter
            
            # Agrego último valor a la lista
            valores.append(valor_actual)
            
            # Creo diccionario
            pregunta = {}
            for j in range(len(encabezados)):
                clave = encabezados[j]
                valor = valores[j]
                
                # opciones separadas en tupla
                if clave == "opciones":
                    pregunta[clave] = tuple(valor.split('|'))
                # parseo a enteros los puntos
                elif clave == "puntos":
                    pregunta[clave] = int(valor)
                else:
                    pregunta[clave] = valor
            
            preguntas.append(pregunta)
    
    return preguntas


# Ejemplo de uso
if __name__ == "__main__":
    print("=== LEER CSV MANUAL ===\n")
    
    # Leo el archivo
    banco_preguntas = leer_csv_manual("preguntas.csv")
    
    # Muestro resultado
    print(f"Total de preguntas cargadas: {len(banco_preguntas)}\n")
    
    # Muestro cada pregunta
    for i, pregunta in enumerate(banco_preguntas, 1):
        print(f"Pregunta {i}:")
        print(f"  Texto: {pregunta['pregunta']}")
        print(f"  Opciones: {pregunta['opciones']}")
        print(f"  Correcta: {pregunta['respuesta_correcta']}")
        print(f"  Dificultad: {pregunta['dificultad']}")
        print(f"  Puntos: {pregunta['puntos']}")
        print()
