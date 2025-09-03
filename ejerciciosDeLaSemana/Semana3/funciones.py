# Funciones
# Toda funcion que da None como resultado no retorna nada

"""
 Conversor de monedas 
 Escribir un programa que pida al usuario un monto en dólares y lo convierta a pesos argentinos y a euros. 
 Usar funciones para cada conversión y mostrar el resultado con dos decimales. 

 """
# Funciones de conversion
def dolares_a_pesos(dolares):
    tasa_cambio = 1400.0  # Ejemplo de tasa de cambio
    pesos = dolares * tasa_cambio
    return pesos        

def dolares_a_euros(dolares):
    tasa_cambio = 0.85  # Ejemplo de tasa de cambio
    euros = dolares * tasa_cambio
    return euros    

# Funciones de entrada
def pido_valores(monto):
    monto = float(input("Ingrese el monto en dólares: "))
    return monto

# Funciones de salida
def mostrar_resultados(monto, pesos, euros):
    print(f"{monto:.2f} dólares son {pesos:.2f} pesos argentinos.")
    print(f"{monto:.2f} dólares son {euros:.2f} euros.")    

# Programa principal
print("Conversor de monedas")
monto = pido_valores(0)
pesos = dolares_a_pesos(monto)
euros = dolares_a_euros(monto)
mostrar_resultados(monto, pesos, euros)

"""
Calculadora geométrica 
Crear un programa que permita al usuario elegir una figura geométrica (cuadrado, rectángulo, triángulo, círculo) mediante un menú.
Luego, calcular su área y perímetro usando funciones específicas para cada caso. 

"""
# Funciones de calculo
import math

def area_cuadrado(lado):
    return lado * lado

def rectangulo(largo, ancho):
    area = largo * ancho
    perimetro = 2 * (largo + ancho)
    return area, perimetro

def triangulo(base, altura, lado1, lado2, lado3):
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro  

def circulo(radio):
    area = math.pi * radio * radio
    perimetro = 2 * math.pi * radio
    return area, perimetro

# Funciones de entrada
def pido_valores_entrada(entrada):
    entrada = float(input("Ingrese el valor: "))
    return entrada

# Funciones de salida
def mostrar_resultados_figura(figura, area, perimetro):
    print(f"El área del {figura} es: {area:.2f}")
    print(f"El perímetro del {figura} es: {perimetro:.2f}") 

# Programa principal
print("Calculadora geométrica")
print("Elija una figura geométrica:")   

# Menu
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Círculo")

opcion = input("Ingrese número de las opciones (1-4):  ")

match opcion:
    case "1":
        print("Ha elegido un cuadrado.")
        lado = pido_valores_entrada(0)
        area = area_cuadrado(lado)
        perimetro = 4 * lado
        mostrar_resultados_figura("cuadrado", area, perimetro)
    case "2":
        print("Ha elegido un rectángulo.")
        largo = pido_valores_entrada(0)
        ancho = pido_valores_entrada(0)
        area, perimetro = rectangulo(largo, ancho)
        mostrar_resultados_figura("rectángulo", area, perimetro)
    case "3":
        print("Ha elegido un triángulo.")
        base = pido_valores_entrada(0)
        altura = pido_valores_entrada(0)
        lado1 = pido_valores_entrada(0)
        lado2 = pido_valores_entrada(0)
        lado3 = pido_valores_entrada(0)
        area, perimetro = triangulo(base, altura, lado1, lado2, lado3)
        mostrar_resultados_figura("triángulo", area, perimetro)
    case "4":
        print("Ha elegido un círculo.")
        radio = pido_valores_entrada(0)
        area, perimetro = circulo(radio)
        mostrar_resultados_figura("circulo", area, perimetro)
    case _:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")
