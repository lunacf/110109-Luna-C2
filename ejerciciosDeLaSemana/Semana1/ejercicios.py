# Ejercicios de Condicionales

print("Ejercicio 1")
tamañoJugador = int(input("Ingrese tamaño en cm: "))


if tamañoJugador <= 160:
    print("El jugador es Base ")
elif tamañoJugador > 160 and tamañoJugador < 180:
    print("El jugador es Escolta ")
elif tamañoJugador > 180 and tamañoJugador < 200:
    print("El jugador es Alero ")
elif tamañoJugador > 200 and tamañoJugador < 210:
    print("El jugador es Ala-Pivot o Pivot")
 

print("Ejercicio 2")
nota = int(input("Ingrese la nota del estudiante: "))

match nota:
    case 1 | 2 | 3:
        print("Desaprobado. La nota es: ", nota)
    case 4 | 5:
        print("Aprobado. La nota es: ", nota)
    case 6 | 7 | 8 | 9 | 10:
        print("Promoción directa.. La nota es: ", nota)

