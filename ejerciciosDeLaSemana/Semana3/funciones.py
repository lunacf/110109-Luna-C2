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

