import sys
import os
import csv
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from biblioteca.input import get_int
from biblioteca.especificas import es_impar, es_par, es_negativo, es_positivo

def _validar_que_tenga_numeros(numeros: list[int]) -> None:
    if len(numeros) == 0:
        raise ValueError("No hay numeros cargados, por favor ingrese numeros primero")

if __name__ == "__main__":
    assert _validar_que_tenga_numeros([1, 2, 3]) is None
    try:
        _validar_que_tenga_numeros([])
        assert False
    except ValueError as ve:
        assert str(ve) == "No hay numeros cargados, por favor ingrese numeros primero"

# 1- ingresar numeros -> funcion de ingresar numeros por pantalla
#    ingresar 10 numeros
#    numero sea entre -1000 y 1000
def ingresar_numeros(numeros: list[int]) -> None:
    print("Ingrese 10 numeros:")
    for i in range(10):
        numero = get_int(f"    {i + 1} - Ingrese un numero entre -1000 y 1000: ", "Superaste la cantidad de reintentos", -1000, 1000, 3)
        if numero is not None:
            numeros.append(numero)
        else:
            print(f"    Se procede a usar los {len(numeros)} numeros cargados previamente")
            return

# 2- contar positivos y negativos -> funcion de contar positivos y negativos
#    necesitas los numeros
#    iterar los numeros e ir contando por separado
def contar_positivos_y_negativos(numeros: list[int]) -> None:
    _validar_que_tenga_numeros(numeros)
    cantidad_positivos = 0
    cantidad_negativos = 0
    for numero in numeros:
        if es_negativo(numero):
            cantidad_negativos += 1
        else:
            cantidad_positivos += 1
    print(f"    Cantidad de numeros positivos: {cantidad_positivos}")
    print(f"    Cantidad de numeros negativos: {cantidad_negativos}")

# 3- suma de pares -> funcion de sumar pares
#    necesitas los numeros
#    iterar los numeros y sumar solo si es par
def sumar_pares(numeros: list[int]) -> None:
    _validar_que_tenga_numeros(numeros)
    suma_pares = 0
    for numero in numeros:
        if es_par(numero):
            suma_pares += numero
    print(f"    Suma de numeros pares: {suma_pares}")

# 4- mayor numero impar -> funcion de mayor impar
#    necesitas los numeros
#    variable que guarde el mayor numero impar
#    iterar los numeros y checkear si es impar y si es mayor al guardado
def mayor_impar(numeros: list[int]) -> None:
    _validar_que_tenga_numeros(numeros)
    impar_mas_grande: int = None
    for numero in numeros:
        if es_impar(numero) and (impar_mas_grande is None or numero > impar_mas_grande):
            impar_mas_grande = numero
    print(f"    El numero impar mas grande es: {impar_mas_grande}")
            

# 5- listar numeros -> funcion de listar numeros
#    necesitas los numeros
#    iterar los numeros y mostrarlos (print)
def listar_numeros(numeros: list[int]) -> None:
    _validar_que_tenga_numeros(numeros)
    for numero in numeros:
        print(f"    {numero}")

# 6- listar los numeros pares -> funcion de listar pares
#    necesitas los numeros
#    iterar los numeros y, si es par, lo mostras (print)
def listar_numeros_pares(numeros: list[int]) -> None:
    _validar_que_tenga_numeros(numeros)
    for numero in numeros:
        if es_par(numero):
            print(f"    {numero}")

# 7- listar numeros en posiciones (index/i) impares -> funcion de listar en posiciones impares
#    necesitas los numeros
#    iterar los numeros y, si el index (i) es impar, lo mostras (print)
def listar_numeros_posiciones_impares(numeros: list[int]) -> None:
    _validar_que_tenga_numeros(numeros)
    for i in range(len(numeros)):
        if es_impar(i):
            print(f"    {numeros[i]}")


"""
Opción 1. Cargar equipos
Permitir ingresar N equipos (cantidad pedida al usuario).
Cada equipo se representa con un diccionario con las claves:
"id" (entero autoincremental),
"nombre",
"categoria" (router, pc, notebook, impresora),
"estado" (funcional o fuera de servicio),
"valor" (float, validado como número positivo).
Los datos se guardan en una lista y también en el archivo equipos.csv.
Si el archivo ya existe, preguntar:
“¿Desea reemplazar los datos existentes o agregar nuevos equipos?”

"""

import colorama
colorama.init()

def cargar_equipos(equipos: list[dict]) -> None:
    print(colorama.Fore.BLUE + "Cargar equipos")
    
    # Verificar si el archivo existe
    if os.path.exists("equipos.csv"):
        opcion = get_int("El archivo equipos.csv ya existe. ¿Desea reemplazar los datos existentes (1) o agregar nuevos equipos (2)? ", "Opción no válida. Ingrese 1 o 2.", 1, 2, 3)
        if opcion is None:
            print("Se cancela la operación de carga de equipos.")
            return
        if opcion == 1:
            # Limpiar la lista y crear archivo nuevo
            equipos.clear()
            with open("equipos.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["id", "nombre", "categoria", "estado", "valor"])
        elif opcion == 2:
            # Cargar equipos existentes del archivo
            with open("equipos.csv", "r") as file:
                reader = csv.DictReader(file)
                equipos.clear()  # Limpiar la lista actual
                for row in reader:
                    equipos.append({
                        'id': int(row['id']),
                        'nombre': row['nombre'],
                        'categoria': row['categoria'],
                        'estado': row['estado'],
                        'valor': float(row['valor'])
                    })
    else:
        # Si no existe el archivo, crear uno nuevo
        with open("equipos.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "nombre", "categoria", "estado", "valor"])
    
    # Ahora permitir agregar nuevos equipos
    while True:
        print("\n--- Agregar nuevo equipo ---")
        
        # Generar ID automáticamente
        if len(equipos) == 0:
            nuevo_id = 1
        else:
            nuevo_id = max(equipo['id'] for equipo in equipos) + 1
        
        # Solicitar datos del equipo
        from biblioteca.input import get_string, get_float
        
        nombre = get_string("Ingrese el nombre del equipo: ", "Nombre no válido", 2, 50, 3)
        if nombre is None:
            print("Se cancela la carga del equipo.")
            break

        categoria = get_string("Ingrese la categoria del equipo (router, pc, notebook, impresora): ", "Categoria no válida", 2, 30, 3)
        if categoria is None:
            print("Se cancela la carga del equipo.")
            break
            
        estado = get_string("Ingrese el estado del equipo (Nuevo/Usado/Dañado): ", "Estado no válido", 4, 15, 3)
        if estado is None:
            print("Se cancela la carga del equipo.")
            break
            
        valor = get_float("Ingrese el valor del equipo: $", "Valor no válido", 0, 999999, 3)
        if valor is None:
            print("Se cancela la carga del equipo.")
            break
        
        # Crear el equipo
        nuevo_equipo = {
            'id': nuevo_id,
            'nombre': nombre,
            'categoria': categoria,
            'estado': estado,
            'valor': valor
        }
        
        # Agregar a la lista
        equipos.append(nuevo_equipo)
        
        # Guardar en el archivo CSV
        with open("equipos.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nuevo_id, nombre, categoria, estado, valor])
        
        print(f"Equipo '{nombre}' agregado exitosamente con ID {nuevo_id}")
        
        # Preguntar si desea agregar otro equipo
        continuar = get_int("¿Desea agregar otro equipo? (1=Sí, 2=No): ", "Opción no válida", 1, 2, 3)
        if continuar != 1:
            break
    
    print(f"Carga completada. Total de equipos: {len(equipos)}")
                
def mostrar_equipos(lista_equipos: list[dict]) -> None:
    if len(lista_equipos) == 0:
        print("No hay equipos cargados.")
        return
    print("Inventario de equipos:")
    for equipo in lista_equipos:
        print(f"ID: {equipo['id']}, Nombre: {equipo['nombre']}, Categoría: {equipo['categoria']}, Estado: {equipo['estado']}, Valor: ${equipo['valor']:.2f}")
        
def buscar_equipo(lista_equipos: list[dict]) -> None:
    if len(lista_equipos) == 0:
        print("No hay equipos cargados.")
        return
    id_buscar = get_int("Ingrese el ID del equipo a buscar: ", "ID no válido. Ingrese un número entero positivo.", 1, 999999, 3)
    if id_buscar is None:
        print("Operación cancelada.")
        return
    for equipo in lista_equipos:
        if equipo['id'] == id_buscar:
            print(f"Equipo encontrado: ID: {equipo['id']}, Nombre: {equipo['nombre']}, Categoría: {equipo['categoria']}, Estado: {equipo['estado']}, Valor: ${equipo['valor']:.2f}")
            return
    print("Equipo no encontrado.")
    
def estadisticas(lista_equipos: list[dict]) -> None:
    if len(lista_equipos) == 0:
        print("No hay equipos cargados.")
        return
    total_equipos = len(lista_equipos)
    valor_total = sum(equipo['valor'] for equipo in lista_equipos)
    valor_promedio = valor_total / total_equipos
    print(f"Total de equipos: {total_equipos}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print(f"Valor promedio por equipo: ${valor_promedio:.2f}")
    
def filtrar_por_categoria(lista_equipos: list[dict]) -> None:
    if len(lista_equipos) == 0:
        print("No hay equipos cargados.")
        return
    categoria = input("Ingrese la categoría a filtrar (router, pc, notebook, impresora): ").strip().lower()
    categorias_validas = {"router", "pc", "notebook", "impresora"}
    if categoria not in categorias_validas:
        print("Categoría no válida.")
        return
    equipos_filtrados = [equipo for equipo in lista_equipos if equipo['categoria'] == categoria]
    if not equipos_filtrados:
        print(f"No hay equipos en la categoría '{categoria}'.")
        return
    print(f"Equipos en la categoría '{categoria}':")
    for equipo in equipos_filtrados:
        print(f"ID: {equipo['id']}, Nombre: {equipo['nombre']}, Estado: {equipo['estado']}, Valor: ${equipo['valor']:.2f}")

def ordenar_por_valor(lista_equipos: list[dict]) -> None:
    if len(lista_equipos) == 0:
        print("No hay equipos cargados.")
        return
    equipos_ordenados = sorted(lista_equipos, key=lambda x: x['valor'], reverse=True)
    print("Equipos ordenados por valor (de mayor a menor):")
    for equipo in equipos_ordenados:
        print(f"ID: {equipo['id']}, Nombre: {equipo['nombre']}, Categoria: {equipo['categoria']}, Estado: {equipo['estado']}, Valor: ${equipo['valor']:.2f}")
        
def generar_informe(lista_equipos: list[dict]) -> None:
    if len(lista_equipos) == 0:
        print("No hay equipos cargados.")
        return
    try:
        with open("informe.txt", "w") as file:
            file.write("Informe de Inventario de Equipos\n")
            file.write("="*40 + "\n")
            for equipo in lista_equipos:
                file.write(f"ID: {equipo['id']}, Nombre: {equipo['nombre']}, Categoria: {equipo['categoria']}, Estado: {equipo['estado']}, Valor: ${equipo['valor']:.2f}\n")
            total_equipos = len(lista_equipos)
            valor_total = sum(equipo['valor'] for equipo in lista_equipos)
            valor_promedio = valor_total / total_equipos
            file.write("\n")
            file.write(f"Total de equipos: {total_equipos}\n")
            file.write(f"Valor total del inventario: ${valor_total:.2f}\n")
            file.write(f"Valor promedio por equipo: ${valor_promedio:.2f}\n")
        print("Informe generado exitosamente en 'informe.txt'.")
    except Exception as e:
        print(f"Error al generar el informe: {e}")

def salir(numeros: list[int]) -> None:
    print("Saliendo del programa...")
