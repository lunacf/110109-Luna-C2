import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import csv
import colorama
colorama.init()

from biblioteca.funciones import p
from biblioteca.funciones import cargar_equipos, mostrar_equipos, buscar_equipo, estadisticas, filtrar_por_categoria, ordenar_por_valor, generar_informe, salir
from biblioteca.input import get_int
from biblioteca.menu import mostrar_menu

def init():
    MENU = {
        "1": cargar_equipos,
        "2": mostrar_equipos,
        "3": buscar_equipo,
        "4": estadisticas,
        "5": filtrar_por_categoria,
        "6": ordenar_por_valor,
        "7": generar_informe,
        "8": salir
    }

    opciones = [
        f"{colorama.Fore.GREEN}📦 Cargar equipos{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.BLUE}📋 Mostrar inventario{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.MAGENTA}🔍 Buscar equipo{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.CYAN}📊 Estadísticas{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.WHITE}🏷️ Filtrar por categoría{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.YELLOW}💰 Ordenar por valor {colorama.Style.RESET_ALL}",
        f"{colorama.Fore.GREEN}📄 Generar informe{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.RED}Salir{colorama.Style.RESET_ALL}"
    ]
    
    equipos = []

    while (seleccion := mostrar_menu(f"{colorama.Fore.LIGHTBLUE_EX}SISTEMA DE INVENTARIO DE EQUIPOS{colorama.Style.RESET_ALL}", opciones, True)) is not None:
        numero_opcion = str(seleccion + 1)  # Convierto a string y ajusto el indice
        if numero_opcion in MENU:
            try:
                MENU[numero_opcion](equipos)  
            except ValueError as ve:
                print(f"{colorama.Fore.RED}❌ ERROR: {ve}{colorama.Style.RESET_ALL}")

if __name__ == "__main__":
    init()
