# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def solicitarEntero():
    
    valorIngresado = int(input("Ingrese numero: "))
    
    print(f"El numero ingresado es: {valorIngresado}")
    
    return valorIngresado
    

solicitarEntero()

# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def solicitarFlotante():
    valorIngresado = float(input("#Ingrese número flotante: "))
    print(f"El numero ingresado es: {valorIngresado}")
    return valorIngresado

solicitarFlotante()

# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def solicitarCadena(cadena):
    cadena = str(input("Ingrese un nombre o cadena: "))
    print(f"El valor ingresado es: {cadena}")
    return cadena

cadena = solicitarCadena("")

# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

def get_SolicitarEntero(mensaje: str, mensaje_error: str, minimo:int, maximo:int, reintentos:int):
        valorIngresado = {}
        mensaje = input("Esta función solicitará un número entero")
        mensaje_error = input("Eso no es un valor válido, reintente por favor: ")
        
        reintentos = 3
        
        while True: 
            for x in valorIngresado:
                
     pass