
import os
import json
from colorama import Fore, Style, init #colores

init(autoreset=True)

archivo = "archivo.txt"

def cargar_usuarios() -> dict:
    if not os.path.exists(archivo):
        return {}
    with open(archivo, 'r', enconding = 'utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Error al leer el archivo. El archivo puede estar corrupto.")
            return {}
        
def guardar_usuarios(usuarios: dict) -> None:
    "dar de alta un usuario en el archivo"
    with open(archivo, 'w', encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)
        
def registrarse(usuarios: dict) -> None:
    "Registrarse"
    email = input("Ingrese su email: ").strip().lower()
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            print(Fore.RED + "❌ Email inválido.")
            return
    if email in usuarios:
            print(Fore.RED + "El email ya está registrado.")
            return
        # nombre = input("Ingrese su nombre: ").strip().title()
    while True:
            nombre = input("Ingrese su nombre: ").strip().title()
            if not re.match(r"^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,50}$", nombre):
                print(Fore.RED + "❌ El nombre solo puede contener letras y espacios (2-50 caracteres).")
                continue
            break
    while True:
            password = input("🔑 Ingrese su contraseña: ").strip()
            if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@#$%^&+=!]{6,}$", password):
                print(Fore.RED + "❌ La contraseña debe tener al menos 6 caracteres, con letras y números.")
                continue
            break
        
    usuarios[email] = {"nombre": nombre, "password": password}
    guardar_usuarios(usuarios)
    print(Fore.GREEN + "✅ Registro exitoso.")
    
def login(usuarios:dict) -> None:
    """login"""
    email = input("Ingrese su email: ").strip().lower()
    password = input("Ingrese su contraseña: ").strip()
    if email in usuarios and usuarios[email]['password'] == password:
        print(Fore.GREEN + f"✅ Bienvenido, {usuarios[email]['nombre']}!")
    else:
        print(Fore.RED + "❌ Email o contraseña incorrectos.")
    

def ver_datos(usuarios:dict) -> None:
    """ver datos"""
    if not usuarios:
        print("No hay usuarios registrados. ")
        return
    print("Lista de usuarios registrados :")
    print("-" *  40)
    for email, datos in usuarios.items():
        print(f"Nombre: {datos['nombre']}, Email: {email}")

def menu() -> None:
    usuarios = cargar_usuarios()
    while True:
        print("Sistema de login")
        print()
        pass
        
        
if __name__ == 'main':
        menu()