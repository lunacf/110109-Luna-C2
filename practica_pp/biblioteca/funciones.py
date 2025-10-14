import sys
import os
import csv

from practica_pp.biblioteca.menu import mostrar_menu
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from biblioteca.input import get_int

import time
def p(message: str) -> None:
  for letter in message:
    print(letter, end='', flush=True)
    time.sleep(0.01)

import colorama
colorama.init()

def cargar_equipos(equipos: list[dict]) -> None:
    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "🔧 CARGAR EQUIPOS" + colorama.Style.RESET_ALL)
    
    # Verifico si el archivo existe
    if os.path.exists("equipos.csv"):
        opcion = get_int("El archivo equipos.csv ya existe. ¿Desea reemplazar los datos existentes (1) o agregar nuevos equipos (2)? ", "Opción no válida. Ingrese 1 o 2.", 1, 2, 3)
        if opcion is None:
            print("Se cancela la operacion de carga de equipos.")
            return
        # la opcion 1 
        if opcion == 1:
            # Limpio la lista y creo archivo nuevo
            equipos.clear()
            with open("equipos.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["id", "nombre", "categoria", "estado", "valor"])
        
        elif opcion == 2:
            # Cargo equipos existentes del archivo
            with open("equipos.csv", "r") as file:
                reader = csv.DictReader(file)
                equipos.clear()  # Limpiar la lista actual
                for row in reader:
                    # 
                    equipos.append({
                        'id': int(row['id']),
                        'nombre': row['nombre'],
                        'categoria': row['categoria'],
                        'estado': row['estado'],
                        'valor': float(row['valor'])
                    })
    else:
        # Si no existe el archivo, creo uno nuevo
        with open("equipos.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "nombre", "categoria", "estado", "valor"])
    
    # Creo equipos nuevos ya sea que el archivo no existia o se eligio agregar nuevos equipos
    while True:
        print(f"{colorama.Fore.CYAN}\n--- Agregar nuevo equipo ---{colorama.Style.RESET_ALL}")
        
        # Genero ID autoincremental
        if len(equipos) == 0:
            nuevo_id = 1
        else:
            # Obtengo el ID máximo existente
            nuevo_id = max(equipo['id'] for equipo in equipos) + 1
        
        # Solicito datos del equipo
        from biblioteca.input import get_string, get_float

        nombre = get_string(f"{colorama.Fore.CYAN}Ingrese el nombre del equipo: {colorama.Style.RESET_ALL}", "Nombre no válido", 2, 50, 3)
        if nombre is None:
            print("Se cancela la carga del equipo.")
            break

        categorias = ["router", "pc", "notebook", "impresora"]

        categoria_index = mostrar_menu(f"{colorama.Fore.CYAN}Ingrese la categoria del equipo: {colorama.Style.RESET_ALL}", categorias)

        if categoria_index is None:
            print("Se cancela la carga del equipo.")
            break
        
        categoria = categorias[categoria_index]
        
        estados_display = [f"{colorama.Fore.RED}Nuevo{colorama.Style.RESET_ALL}", 
                          f"{colorama.Fore.YELLOW}Usado{colorama.Style.RESET_ALL}", 
                          f"{colorama.Fore.RED}Dañado{colorama.Style.RESET_ALL}"]
        estados_clean = ["Nuevo", "Usado", "Dañado"]
        
        estado_index = mostrar_menu("Ingrese el estado del equipo: ", estados_display)
        
        if estado_index is None:
            print("Se cancela la carga del equipo.")
            break
        estado = estados_clean[estado_index]

        valor = get_float(f"{colorama.Fore.CYAN}Ingrese el valor del equipo: ${colorama.Style.RESET_ALL}", "Valor no válido", 0, 999999, 3)
        if valor is None:
            print("Se cancela la carga del equipo.")
            break
        
        nuevo_equipo = {
            'id': nuevo_id,
            'nombre': nombre,
            'categoria': categoria,
            'estado': estado,
            'valor': valor
        }
        
        # Agrego a la lista
        equipos.append(nuevo_equipo)
        
        # Guardo en el archivo CSV
        with open("equipos.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nuevo_id, nombre, categoria, estado, valor])
        
        print(f"Equipo '{nombre}' agregado exitosamente con ID {nuevo_id}")
        
        # Preguntar si desea agregar otro equipo
        continuar = get_int("¿Desea agregar otro equipo? (1.Sí, 2.No): ", "Opción no válida", 1, 2, 3)
        if continuar != 1:
            break
    
    print(f"Carga completada. Total de equipos: {len(equipos)}")
                
def mostrar_equipos(lista_equipos: list[dict]) -> None:
    if len(lista_equipos) == 0:
        print(colorama.Fore.RED + "❌ No hay equipos cargados." + colorama.Style.RESET_ALL)
        return
    
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "📋 INVENTARIO DE EQUIPOS" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "=" * 110 + colorama.Style.RESET_ALL)
    
    for equipo in lista_equipos:
        # Color según el estado
        if equipo['estado'].lower() in ['nuevo', 'funcional']:
            color_estado = colorama.Fore.GREEN
        elif equipo['estado'].lower() in ['usado']:
            color_estado = colorama.Fore.YELLOW
        else:  # dañado, fuera de servicio
            color_estado = colorama.Fore.RED
            
        print(f"{colorama.Fore.CYAN}ID: {equipo['id']:3d}{colorama.Style.RESET_ALL} | "
              f"{colorama.Fore.BLUE}Nombre: {equipo['nombre']:<20}{colorama.Style.RESET_ALL} | "
              f"{colorama.Fore.MAGENTA}Categoría: {equipo['categoria']:<12}{colorama.Style.RESET_ALL} | "
              f"{color_estado}Estado: {equipo['estado']:<15}{colorama.Style.RESET_ALL} | "
              f"{colorama.Fore.GREEN}Valor: ${equipo['valor']:>8.2f}{colorama.Style.RESET_ALL}")
    
    print(colorama.Fore.YELLOW + "=" * 110 + colorama.Style.RESET_ALL)
    print(f"{colorama.Fore.WHITE}Total de equipos: {len(lista_equipos)}{colorama.Style.RESET_ALL}")
        
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
        print(colorama.Fore.RED + "❌ No hay equipos cargados." + colorama.Style.RESET_ALL)
        return
    
    categorias = ["router", "pc", "notebook", "impresora"]
    categoria_index = mostrar_menu(f"{colorama.Fore.CYAN}Seleccione la categoría a filtrar:{colorama.Style.RESET_ALL}", categorias)
    
    if categoria_index is None:
        print("Operación cancelada.")
        return
        
    categoria = categorias[categoria_index]
    equipos_filtrados = [equipo for equipo in lista_equipos if equipo['categoria'].lower() == categoria.lower()]
    
    if not equipos_filtrados:
        print(colorama.Fore.RED + f"❌ No hay equipos en la categoría '{categoria}'." + colorama.Style.RESET_ALL)
        return
    
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"📋 EQUIPOS - CATEGORÍA: {categoria.upper()}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "=" * 110 + colorama.Style.RESET_ALL)
    
    for equipo in equipos_filtrados:
        # Color según el estado
        if equipo['estado'].lower() in ['nuevo', 'funcional']:
            color_estado = colorama.Fore.GREEN
        elif equipo['estado'].lower() in ['usado']:
            color_estado = colorama.Fore.YELLOW
        else:  # dañado, fuera de servicio
            color_estado = colorama.Fore.RED
            
        print(f"{colorama.Fore.CYAN}ID: {equipo['id']:3d}{colorama.Style.RESET_ALL} | "
              f"{colorama.Fore.BLUE}Nombre: {equipo['nombre']:<20}{colorama.Style.RESET_ALL} | "
              f"{colorama.Fore.MAGENTA}Categoría: {equipo['categoria']:<12}{colorama.Style.RESET_ALL} | "
              f"{color_estado}Estado: {equipo['estado']:<15}{colorama.Style.RESET_ALL} | "
              f"{colorama.Fore.GREEN}Valor: ${equipo['valor']:>8.2f}{colorama.Style.RESET_ALL}")
    
    print(colorama.Fore.YELLOW + "=" * 110 + colorama.Style.RESET_ALL)
    print(f"{colorama.Fore.WHITE}Total de equipos: {len(equipos_filtrados)}{colorama.Style.RESET_ALL}")

def ordenar_por_valor(lista_equipos: list[dict]) -> None:
    if len(lista_equipos) == 0:
        print(colorama.Fore.RED + "❌ No hay equipos cargados." + colorama.Style.RESET_ALL)
        return
    
    opciones_orden = [
        f"{colorama.Fore.GREEN}Mayor a menor valor{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.BLUE}Menor a mayor valor{colorama.Style.RESET_ALL}"
    ]
    
    orden_index = mostrar_menu(f"{colorama.Fore.CYAN}Seleccione el orden:{colorama.Style.RESET_ALL}", opciones_orden)
    
    if orden_index is None:
        print("Operación cancelada.")
    
        return
    
    # True = de mayor a menor, False = de menor a mayor
    reverso = orden_index == 0
    equipos_ordenados = sorted(lista_equipos, key=lambda x: x['valor'], reverse=reverso)
    
    titulo = "EQUIPOS ORDENADOS POR VALOR (MAYOR A MENOR)" if reverso else "EQUIPOS ORDENADOS POR VALOR (MENOR A MAYOR)"
    
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"📋 {titulo}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "=" * 110 + colorama.Style.RESET_ALL)
    
    for equipo in equipos_ordenados:
        # Color según el estado
        if equipo['estado'].lower() in ['nuevo', 'funcional']:
            color_estado = colorama.Fore.GREEN
        elif equipo['estado'].lower() in ['usado']:
            color_estado = colorama.Fore.YELLOW
        else:  # dañado, fuera de servicio
            color_estado = colorama.Fore.RED
            
        print(f"{colorama.Fore.CYAN}ID: {equipo['id']:3d}{colorama.Style.RESET_ALL} | "
              f"{colorama.Fore.BLUE}Nombre: {equipo['nombre']:<20}{colorama.Style.RESET_ALL} | "
              f"{colorama.Fore.MAGENTA}Categoría: {equipo['categoria']:<12}{colorama.Style.RESET_ALL} | "
              f"{color_estado}Estado: {equipo['estado']:<15}{colorama.Style.RESET_ALL} | "
              f"{colorama.Fore.GREEN}Valor: ${equipo['valor']:>8.2f}{colorama.Style.RESET_ALL}")
    
    print(colorama.Fore.YELLOW + "=" * 110 + colorama.Style.RESET_ALL)
    print(f"{colorama.Fore.WHITE}Total de equipos: {len(equipos_ordenados)}{colorama.Style.RESET_ALL}")

def generar_informe(lista_equipos: list[dict]) -> None:
    if len(lista_equipos) == 0:
        print(colorama.Fore.RED + "❌ No hay equipos cargados para generar el informe." + colorama.Style.RESET_ALL)
        return
    
    try:
        from datetime import datetime
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        with open("informe_inventario.txt", "w", encoding="utf-8") as file:
            # Encabezado del informe
            file.write("=" * 80 + "\n")
            file.write("                    INFORME DE INVENTARIO DE EQUIPOS\n")
            file.write("=" * 80 + "\n")
            file.write(f"Fecha de generación: {fecha_actual}\n")
            file.write(f"Total de equipos registrados: {len(lista_equipos)}\n\n")
            
            # Listado detallado de equipos
            file.write("LISTADO DETALLADO DE EQUIPOS:\n")
            file.write("-" * 80 + "\n")
            # que es esto? 
            file.write(f"{'ID':<4} | {'NOMBRE':<25} | {'CATEGORÍA':<12} | {'ESTADO':<15} | {'VALOR':<10}\n")
            file.write("-" * 80 + "\n")
            
            for equipo in lista_equipos:
                file.write(f"{equipo['id']:<4} | {equipo['nombre']:<25} | {equipo['categoria']:<12} | {equipo['estado']:<15} | ${equipo['valor']:<9.2f}\n")
            
            file.write("-" * 80 + "\n\n")
            
            # Estadísticas del inventario
            file.write("ESTADÍSTICAS DEL INVENTARIO:\n")
            file.write("-" * 40 + "\n")
            
            total_equipos = len(lista_equipos)
            valor_total = sum(equipo['valor'] for equipo in lista_equipos)
            valor_promedio = valor_total / total_equipos if total_equipos > 0 else 0
            
            # Estadísticas por categoría
            categorias = {}
            for equipo in lista_equipos:
                cat = equipo['categoria']
                if cat not in categorias:
                    categorias[cat] = {'cantidad': 0, 'valor_total': 0}
                categorias[cat]['cantidad'] += 1
                categorias[cat]['valor_total'] += equipo['valor']
            
            # Estadísticas por estado
            estados = {}
            for equipo in lista_equipos:
                est = equipo['estado']
                if est not in estados:
                    estados[est] = 0
                estados[est] += 1
            
            file.write(f"Total de equipos: {total_equipos}\n")
            file.write(f"Valor total del inventario: ${valor_total:.2f}\n")
            file.write(f"Valor promedio por equipo: ${valor_promedio:.2f}\n\n")
            
            file.write("DISTRIBUCIÓN POR CATEGORÍAS:\n")
            for categoria, datos in categorias.items():
                file.write(f"- {categoria}: {datos['cantidad']} equipos (${datos['valor_total']:.2f})\n")
            
            file.write(f"\nDISTRIBUCIÓN POR ESTADOS:\n")
            for estado, cantidad in estados.items():
                porcentaje = (cantidad / total_equipos) * 100
                file.write(f"- {estado}: {cantidad} equipos ({porcentaje:.1f}%)\n")

        
        print(colorama.Fore.GREEN + "✅ Informe generado exitosamente en 'informe_inventario.txt'" + colorama.Style.RESET_ALL)
        
    except Exception as e:
        print(colorama.Fore.RED + f"❌ Error al generar el informe: {e}" + colorama.Style.RESET_ALL)


def salir(equipos: list[dict]) -> None:
    print(f"{colorama.Fore.YELLOW}🔄 Cerrando el sistema...{colorama.Style.RESET_ALL}")
    if len(equipos) > 0:
        print(f"{colorama.Fore.GREEN}💾 Se han guardado {len(equipos)} equipos en el inventario.{colorama.Style.RESET_ALL}")
    print(f"{colorama.Fore.CYAN}✨ Sistema cerrado correctamente. ¡Hasta pronto!{colorama.Style.RESET_ALL}")
