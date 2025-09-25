import sys
import os
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

