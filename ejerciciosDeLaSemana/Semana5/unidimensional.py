def generarArray(cantidad: int) -> list[int]:
    return [None] * cantidad

def pedirNumeros(cantidad: int) -> list[int]:
    #genero lista 
    valores = generarArray(cantidad)
    for i in range(cantidad):
        valor = input("Ingrese numeros: ")
        valores[i] = int(valor)      
    return valores
    
# print(pedirNumeros(2))

def calcularPromedio(enteros: list[int]) -> float:
    suma_enteros = 0
    
    for entero in enteros: # 0 1 2 = len 3
        suma_enteros += entero
    return round(suma_enteros / len(enteros), 2)


promedio = (calcularPromedio([2,3,4]))
assert promedio == 3, "La funcion no calculo correctamente el promedio"   
print(f"El promedio es {promedio}")


# Escribir una función parecida a la anterior, 
# pero la misma deberá calcular y devolver el promedio de los números positivos.

def calcularPromedioPositivos(enteros: list[int]) -> float|None:
    if len(enteros) == 0:
        return None
    suma_enteros = 0
    
    for entero in enteros: # 0 1 2 = len 3
        if entero >= 0:
            suma_enteros += entero
    return round(suma_enteros / len(enteros), 2)


# print(calcularPromedioPositivos(pedirNumeros(0)))

#Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
def calcularProducto(enteros: list[int]) -> int:
    producto_entero = 0
    
    for entero in enteros: # 0 1 2 = len 3
        producto_entero *= entero
    return producto_entero

# print(calcularPromedioPositivos(pedirNumeros(3)))

#Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
def buscarIndiceMayorValor(enteros: list[int]) -> int:
    indice = 0
    
    for i in range(len(enteros)):
        # Comparo valores de las dos posiciones
        if enteros[i] > enteros[indice]:
            indice = i 
    return indice

# print(buscarIndiceMayorValor([-4,3,7,-2,9])) # pos 4
        
def reemplazarNombre(nombres: list[str], nombre: str, nombreNuevo: str) -> list[str]:
    
    #Tomo Indice a indice
    for i in range(len(nombres)):
        if nombres[i] == nombre:
            nombres[i] = nombreNuevo
            
    return nombres


assert reemplazarNombre(["Juan","Pedro","Rosa","Mica"], "Juan", "Pablo") == ["Pablo","Pedro","Rosa","Mica"], "La funcion no reemplazo Juan por Pablo"   


def interseccionDosConjuntos(conjuntoM: list, conjuntoN: list) -> list:
    interseccion = []
    
    # Tomo elemento por elemento
    for elemento in conjuntoM:
        if elemento in conjuntoN:
            interseccion.append(elemento)
    return interseccion

interseccion =  interseccionDosConjuntos(["Juan","Pedro","Rosa","Mica"], ["Juan","Santi","Rosa","Mica"])
assert interseccion == ["Juan","Rosa","Mica"], "La funcion no realizo la interseccion correctamente"   
print(f"La interseccion de M y N es {interseccion}")


# 10
def unionDosConjuntos(conjuntoM: list, conjuntoN: list) -> list:
    union = conjuntoM
    
    for elemento in conjuntoN:
        if not elemento in union:
            union.append(elemento)
    return union

union = unionDosConjuntos(["Juan","Pedro","Rosa","Mica"], ["Juan","Santi","Marta","Pepe"])
assert union == ["Juan","Pedro","Rosa","Mica","Santi","Marta","Pepe"]
print(f"La union de M y N es {union}")

# 11
def diferenciaDosConjuntos(conjuntoM: list, conjuntoN: list) -> list:
    diferencia = []
    
    for elemento in conjuntoM:
        if not elemento in conjuntoN:
            diferencia.append(elemento)
    for elemento in conjuntoN:
        if not elemento in conjuntoM:
            diferencia.append(elemento)
    return diferencia

diferencia = diferenciaDosConjuntos(["Juan","Pedro","Rosa","Mica"], ["Juan","Santi","Marta","Pepe"])
assert diferencia == ["Pedro","Rosa","Mica","Santi","Marta","Pepe"]
print(f"La diferencia de M y N es {diferencia}")