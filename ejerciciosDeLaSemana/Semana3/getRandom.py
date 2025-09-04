# Funcion para generar un random entre dos valores 1 y 100. El usuario debe 
# adivinar el numero generado por la computadora, el programa tiene que dar pistas

 
import random

def generar_random(minimo, maximo):
    return random.randint(minimo, maximo)

def adivinar_random(numero_a_adivinar):

    contador = 0

    while True:
        try:
            intento = int(input("Adivina un numero entre 1 y 100: "))
            contador += 1

            if intento < 1 or intento > 100:
                print("Por favor, ingrese un número dentro del rango de 1 a 100.")
                continue

            elif intento < numero_a_adivinar:
                print("El número es mayor. Intenta de nuevo.")

            elif intento > numero_a_adivinar:
                print("El número es menor. Intenta de nuevo.")
            else:
                print(f"¡Congrats, adivinaste el número capo!' {numero_a_adivinar} en {contador} intentos.")
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

# Programa principal
if __name__ == "__main__":
    print("Número secreto entre 1 y 100")
    numero_a_adivinar = generar_random(1, 100)
    adivinar_random(numero_a_adivinar)
