import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import csv
import colorama
colorama.init()

from biblioteca.input import get_int
from biblioteca.funciones import cargar_equipos, mostrar_equipos, buscar_equipo, estadisticas, filtrar_por_categoria, ordenar_por_valor, generar_informe, salir

def init():
    MENU = {
        colorama.Fore.BLUE + "1": cargar_equipos,
        colorama.Fore.BLACK + "2": mostrar_equipos,
        colorama.Fore.BLACK + "3": buscar_equipo,
        colorama.Fore.BLACK + "4": estadisticas,
        colorama.Fore.BLACK + "5": filtrar_por_categoria,
        colorama.Fore.BLACK + "6": ordenar_por_valor,
        colorama.Fore.BLACK + "7": generar_informe,
        colorama.Fore.BLACK + "8": salir
    }
    
    MENSAJE_MENU_CARGAR = """
1. Cargar equipos
2. Mostrar inventario
3. Buscar equipo
4. Estadisticas
5. Filtrar por categoria
6. Ordenar por valor
7. Generar informe
8. Salir

Opcion: """
    


    # Lista para almacenar los equipos
    equipos = []

    while(opcion := get_int(colorama.Fore.BLUE + MENSAJE_MENU_CARGAR, "Opcion no valida, solo debe ser de 1 a 8", 1, 8, 3 )) != 8:
        print("")
        for numero in MENU:
            if str(opcion) == numero:
                try:
                    MENU[numero](equipos)
                except ValueError as ve:
                    print(f"    ERROR: {ve}")
                break
    print("\nGracias por usar el programa crack. Hasta luego!")
    
    while(opcion := get_int(colorama.Fore.YELLOW + MENSAJE_MENU_CARGAR, "Opcion no valida, solo debe ser de 1 a 8", 2, 8, 3 )) != 8:
        print("")
        for numero in MENU:
            if str(opcion) == numero:
                try:
                    MENU[numero](equipos)
                except ValueError as ve:
                    print(f"    ERROR: {ve}")
                break
    print("\nGracias por usar el programa crack. Hasta luego!")

if __name__ == "__main__":
    init()
