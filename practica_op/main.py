import colorama
colorama.init()

def cargar_datos(empresas, productos, sucursales, ventas):
    
    print(f"{colorama.Fore.CYAN}📊 Cargando datos de la empresa...{colorama.Style.RESET_ALL}")
    
    sucursales.clear()
    sucursales.extend([
        "Sucursal Centro", "Sucursal Norte", "Sucursal Sur", "Sucursal Este", 
        "Sucursal Oeste", "Sucursal Plaza", "Sucursal Mall", "Sucursal Zona",
        "Sucursal Capital", "Sucursal Suburban"
    ])
    
    productos.clear()
    productos.extend([
        {"nombre": "Producto A", "precio_usd": 25.50},
        {"nombre": "Producto B", "precio_usd": 45.75}, 
        {"nombre": "Producto C", "precio_usd": 12.25}
    ])
    
    ventas.clear()
    import random
    for i, sucursal in enumerate(sucursales):
        ventas_sucursal = {}
        for j, producto in enumerate(productos):
            ventas_sucursal[producto["nombre"]] = random.randint(10, 100)
        ventas.append(ventas_sucursal)
    
    print(f"{colorama.Fore.GREEN}✅ Datos cargados: {len(sucursales)} sucursales, {len(productos)} productos{colorama.Style.RESET_ALL}")

def mostrar_ventas_por_sucursal(empresas, productos, sucursales, ventas):
    if not sucursales or not ventas:
        print(f"{colorama.Fore.RED}❌ No hay datos cargados{colorama.Style.RESET_ALL}")
        return
    
    print(f"{colorama.Fore.GREEN}📈 VENTAS TOTALES POR SUCURSAL{colorama.Style.RESET_ALL}")
    print("=" * 50)
    
    for i, sucursal in enumerate(sucursales):
        total_ventas = sum(ventas[i].values())
        print(f"{colorama.Fore.CYAN}{sucursal}{colorama.Style.RESET_ALL}: {total_ventas} unidades")

def mostrar_promedio_productos(empresas, productos, sucursales, ventas):
    if not productos or not ventas:
        print(f"{colorama.Fore.RED}❌ No hay datos cargados{colorama.Style.RESET_ALL}")
        return
    
    print(f"{colorama.Fore.BLUE}📊 PROMEDIO DE VENTAS POR PRODUCTO{colorama.Style.RESET_ALL}")
    print("=" * 50)
    
    for producto in productos:
        total_producto = sum(venta_sucursal.get(producto["nombre"], 0) for venta_sucursal in ventas)
        promedio = total_producto / len(sucursales) if sucursales else 0
        print(f"{colorama.Fore.MAGENTA}{producto['nombre']}{colorama.Style.RESET_ALL}: {promedio:.2f} unidades promedio")

def mostrar_sucursales_ordenadas(empresas, productos, sucursales, ventas):
    if not sucursales or not ventas or not productos:
        print(f"{colorama.Fore.RED}❌ No hay datos cargados{colorama.Style.RESET_ALL}")
        return
    
    print(f"{colorama.Fore.YELLOW}🏢 SUCURSALES ORDENADAS ALFABÉTICAMENTE{colorama.Style.RESET_ALL}")
    print("=" * 60)
    
    sucursales_recaudacion = []
    for i, sucursal in enumerate(sucursales):
        recaudacion_total = 0
        for producto in productos:
            unidades = ventas[i].get(producto["nombre"], 0)
            recaudacion_total += unidades * producto["precio_usd"]
        sucursales_recaudacion.append((sucursal, recaudacion_total))
    
    sucursales_recaudacion.sort(key=lambda x: x[0])
    
    for sucursal, recaudacion in sucursales_recaudacion:
        print(f"{colorama.Fore.CYAN}{sucursal}{colorama.Style.RESET_ALL}: ${recaudacion:.2f} USD")

def mostrar_total_empresa(empresas, productos, sucursales, ventas):
    if not sucursales or not ventas or not productos:
        print(f"{colorama.Fore.RED}❌ No hay datos cargados{colorama.Style.RESET_ALL}")
        return
    
    total_empresa = 0
    for i in range(len(sucursales)):
        for producto in productos:
            unidades = ventas[i].get(producto["nombre"], 0)
            total_empresa += unidades * producto["precio_usd"]
    
    print(f"{colorama.Fore.GREEN}💰 TOTAL RECAUDADO POR LA EMPRESA{colorama.Style.RESET_ALL}")
    print("=" * 40)
    print(f"{colorama.Fore.GREEN}${total_empresa:.2f} USD{colorama.Style.RESET_ALL}")

def salir_programa(empresas, productos, sucursales, ventas):
    print(f"{colorama.Fore.YELLOW}👋 Gracias por usar el sistema de análisis de ventas{colorama.Style.RESET_ALL}")
    return


def mostrar_menu_simple(titulo: str, opciones: list[str]) -> int:
    import os
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{colorama.Fore.CYAN}╔══════════════════════════════════════════════════════════╗{colorama.Style.RESET_ALL}")
        print(f"{colorama.Fore.CYAN}║{colorama.Style.RESET_ALL} {titulo:^54} {colorama.Fore.CYAN}║{colorama.Style.RESET_ALL}")
        print(f"{colorama.Fore.CYAN}╚══════════════════════════════════════════════════════════╝{colorama.Style.RESET_ALL}\n")
        
        for i, opcion in enumerate(opciones):
            print(f"{i + 1}. {opcion}")
        
        print("\n" + "="*60)
        
        try:
            seleccion = input(f"{colorama.Fore.WHITE}Seleccione una opción (1-{len(opciones)}): {colorama.Style.RESET_ALL}").strip()
            
            if not seleccion.isdigit():
                input(f"{colorama.Fore.RED}❌ Por favor ingrese solo números. Presione ENTER...{colorama.Style.RESET_ALL}")
                continue
            
            seleccion = int(seleccion) - 1
            
            if 0 <= seleccion < len(opciones):
                if seleccion == len(opciones) - 1:
                    return None
                else:
                    return seleccion
            else:
                input(f"{colorama.Fore.RED}❌ Opción no válida. Presione ENTER...{colorama.Style.RESET_ALL}")
                
        except KeyboardInterrupt:
            print(f"\n{colorama.Fore.YELLOW}Saliendo...{colorama.Style.RESET_ALL}")
            return None
        except Exception as e:
            input(f"{colorama.Fore.RED}❌ Error: {e}. Presione ENTER...{colorama.Style.RESET_ALL}")

def init():
    empresas = []
    productos = []
    sucursales = []
    ventas = []
    
    MENU = {
        0: cargar_datos,
        1: mostrar_ventas_por_sucursal,
        2: mostrar_promedio_productos,
        3: mostrar_sucursales_ordenadas,
        4: mostrar_total_empresa,
    }
    
    opciones = [
        f"{colorama.Fore.GREEN}🔧 Cargar datos de la empresa{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.BLUE}📈 Ventas totales por sucursal{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.MAGENTA}📊 Promedio por producto{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.YELLOW}🏢 Sucursales ordenadas A-Z{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.GREEN}💰 Total recaudado empresa{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.RED}🚪 Salir{colorama.Style.RESET_ALL}"
    ]
    
    while (seleccion := mostrar_menu_simple("SISTEMA DE ANÁLISIS DE VENTAS", opciones)) is not None:
        if seleccion in MENU:
            try:
                MENU[seleccion](empresas, productos, sucursales, ventas)
                input(f"\n{colorama.Fore.CYAN}📋 Presione ENTER para continuar...{colorama.Style.RESET_ALL}")
            except Exception as e:
                input(f"{colorama.Fore.RED}❌ ERROR: {e}. Presione ENTER...{colorama.Style.RESET_ALL}")
    
    salir_programa(empresas, productos, sucursales, ventas)

if __name__ == "__main__":
    init()
                
