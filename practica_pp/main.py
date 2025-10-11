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
    
    MENSAJE_MENU_INICIAL = f"""
    {colorama.Fore.BLUE}MENU PRINCIPAL\n{colorama.Style.RESET_ALL}
    {colorama.Fore.GREEN}1. Cargar equipos{colorama.Style.RESET_ALL}
    {colorama.Fore.RED}2. Mostrar inventario{colorama.Style.RESET_ALL}
    {colorama.Fore.RED}3. Buscar equipo{colorama.Style.RESET_ALL}
    {colorama.Fore.RED}4. Estadisticas{colorama.Style.RESET_ALL}
    {colorama.Fore.RED}5. Filtrar por categoria{colorama.Style.RESET_ALL}
    {colorama.Fore.RED}6. Ordenar por valor{colorama.Style.RESET_ALL}
    {colorama.Fore.RED}7. Generar informe{colorama.Style.RESET_ALL}
    {colorama.Fore.GREEN}8. Salir{colorama.Style.RESET_ALL}
    """

    MENSAJE_MENU_COMPLETO = f"""
    {colorama.Fore.GREEN}MENU PRINCIPAL
1. Cargar equipos
2. Mostrar inventario
3. Buscar equipo
4. Estadisticas
5. Filtrar por categoria
6. Ordenar por valor
7. Generar informe
8. Salir
Opcion: 
{colorama.Style.RESET_ALL}

"""

    MENSAJE_MENU_CARGAR = MENSAJE_MENU_INICIAL

    # Lista para almacenar los equipos
    equipos = []

    while(opcion := get_int(colorama.Fore.RED + MENSAJE_MENU_CARGAR, "Opcion no valida, solo debe ser de 1 a 8", 1, 8, 3 )) != 8:
        print("")
        for numero in MENU:
            if str(opcion) == numero:
                try:
                    MENU[numero](equipos)
                    if opcion == 1:
                        MENSAJE_MENU_CARGAR = MENSAJE_MENU_COMPLETO
                except ValueError as ve:
                    print(f"    ERROR: {ve}")
                break
    print("\nGracias por usar el programa crack. Hasta luego!")

if __name__ == "__main__":
    init()
