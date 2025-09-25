import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from biblioteca.input import get_int
from funciones import contar_positivos_y_negativos, ingresar_numeros, listar_numeros_posiciones_impares, listar_numeros, listar_numeros_pares, sumar_pares, mayor_impar
 
def init():
    MENU = {
        "1": ingresar_numeros,
        "2": contar_positivos_y_negativos,
        "3": sumar_pares,
        "4": mayor_impar,
        "5": listar_numeros,
        "6": listar_numeros_pares,
        "7": listar_numeros_posiciones_impares,
    }

    MENSAJE_MENU = """
Menu:
    1- Ingresar 10 numeros
    2- Contar numeros positivos y negativos
    3- Sumar numeros pares
    4- Mayor numero impar
    5- Listar numeros
    6- Listar numeros pares
    7- Listar numeros en posiciones impares
    8- Salir

Opcion: """
    opcion: int = -1
    numeros: list[int] = []
    # asigna y devuelve valor recibido
    while (opcion := get_int(MENSAJE_MENU, "Numero no valido, solo debe ser de 1 a 8", 1, 8, 3)) != 8:
        print("")
        for numero in MENU:
            if str(opcion) == numero:
                try:
                    MENU[numero](numeros)
                except ValueError as ve:
                    print(f"    {ve}")
                break
    print("\nGracias por usar el programa")

# si se ejecuta este archivo se llama a init(). Si se importa el archivo, no se llama a nada
if __name__ == "__main__":
    init()

# # for por indice
# # si quisieras modificar los valores dentro de numeros tenes que ir por el indice
# # como por ej: numeros[i] = 4
# numeros = [10, -5, 3, 8, -2]
# for i in range(len(numeros)): # i va a tomar los valores 0, 1, 2, 3, 4 | el range internamente hace esto -> range(5) = [0, 1, 2, 3, 4]
#     # podes hacer cosas accediendo por el indice i a la lista
#     print(f"Indice {i} - Valor {numeros[i]}")

# # for por valor
# for numero in numeros: # numero va a tomar los valores 10, -5, 3, 8, -2
#     # podes hacer cosas con el valor dirX


