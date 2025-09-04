# Funciones de calculo
def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Funcion para pedir 3 notas del alumno
def pedir_notas_alumno():
    notas = []
    for i in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {i+1}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else: 
                        print("La nota debe estar entro 0 y 10. ")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
    return notas

# Funcion para verificar si el alumno aprobo o desaprobo

def verificar_aprobacion(promedio):
    if promedio >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

# programa principal

def gestor_de_notas():
    
    alumnos_promedios = {} #Diccionario vacío: {nombre: promedio}
    ejecutando = True #control de bucle while

    while ejecutando:
        print("\n" + "="*40)
        print("    Gestor de notas")
        print("="*40)
        print("1. Agregar alumno y notas")
        print("2. Ver estado de un alumno")
        print("3. Calcular promedio de un alumno")
        print("4. Salir")
        
        opcion = input("Ingrese una opción (1-4): ").strip()

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del alumno: ").strip()
                if nombre in alumnos_promedios:
                    print(f"El alumno {nombre} ya existe.")
                    continue
                
                print(f"\nIngresando notas para {nombre}:")
                notas = pedir_notas_alumno()
                promedio = calcular_promedio(notas)

                #guardo notas y promedio
                alumnos_promedios[nombre] = {
                    "notas": notas,
                    "promedio": promedio
                } 
                estado = verificar_aprobacion(promedio)
                
                
                print(f"\n✓ Datos guardados:")
                print(f"  Alumno: {nombre}")
                print(f"  Notas: {notas}")
                print(f"  Promedio: {promedio:.2f}")
                print(f"  Estado: {estado}")

            case "2":
                nombre = input("Ingrese el nombre del alumno: ").strip()
                if nombre in alumnos_promedios:
                    promedio = alumnos_promedios[nombre]
                    estado = verificar_aprobacion(promedio)
                    print(f"\n--- Estado de {nombre} ---")
                    print(f"Promedio: {promedio:.2f}")
                    print(f"Estado: {estado}")
                else:
                    print(f"✗ No se encontró al alumno {nombre}")

            case "3":
                # Esta opción es redundante con la 2, pero la dejamos
                nombre = input("Ingrese el nombre del alumno: ").strip()
                if nombre in alumnos_promedios:
                    promedio = alumnos_promedios[nombre]
                    estado = verificar_aprobacion(promedio)
                    print(f"\n--- Promedio de {nombre} ---")
                    print(f"Promedio: {promedio:.2f}")
                    print(f"Estado: {estado}")
                else:
                    print(f"✗ No se encontró al alumno {nombre}")

            case "4":
                print("\n¡Gracias por usar el Gestor de Notas!")
                print("Saliendo del programa...")
                ejecutando = False

            case _:
                print("✗ Opción no válida. Por favor, elija una opción del 1 al 4.")

# Ejecutar el programa
# Variable de entorno para evitar ejecucion al importar

if __name__ == "__main__":
    gestor_de_notas()
         