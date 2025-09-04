# Cajero automatico (Hacer un programa que pida un PIN para acceder.)

def creacion_de_pin():

    ejecutandose = True

    print("================== CAJERO AUTOMATICO ==================")
    print("Ingrese pin de 4 digitos para comenzar: ")

    while ejecutandose:
        pin = input("Crea tu PIN de 4 digitos: ").strip()

        #Valido PIN
        if not pin.isdigit():
            print("El PIN solo debe contener números.")
            continue
        if len(pin) != 4:
            print("El PIN debe tener exactamente 3 digitos.")

        confirmar_pin = input("Confirme su PIN: ").strip()

        if pin == confirmar_pin:
            print("¡PIN creado exitosamente!.")
            return pin
        else: 
            print("Los PINs no coinciden. Reintente nuevamente.")


    