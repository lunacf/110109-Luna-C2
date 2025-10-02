# Tarifa base:
#Todas las facturas incluyen un cargo fijo de $7000 ademas del costo por consumo.

# Sistema de Facturación de Agua Potable
print("SISTEMA DE FACTURACIÓN DE AGUA POTABLE")
print("======================================")

# Solicitar datos al usuario
try:
    consumo = float(input("Ingrese la cantidad de metros cúbicos consumidos: "))
except ValueError:
    print("ERROR: Debe ingresar un número válido para el consumo.")
    exit()

print("\nTipos de cliente disponibles:")
print("1. Residencial")
print("2. Comercial") 
print("3. Industrial")
tipo_cliente = input("Ingrese el tipo de cliente: ").lower()

# Cálculos base
cargo_fijo = 7000
costo_por_m3 = 200
costo_consumo = consumo * costo_por_m3
subtotal_base = cargo_fijo + costo_consumo

# Inicializar variables para ajustes
bonificacion = 0
recargo = 0
descuento_especial = 0

# Aplicar reglas según tipo de cliente
if tipo_cliente == "residencial":
    if consumo < 30:
        bonificacion = costo_consumo * 0.10
    if consumo > 80:
        recargo = costo_consumo * 0.15
    if subtotal_base < 35000:
        descuento_especial = subtotal_base * 0.05

elif tipo_cliente == "comercial":
    if consumo > 300:
        bonificacion = costo_consumo * 0.12
    elif consumo > 150:
        bonificacion = costo_consumo * 0.08
    if consumo < 50:
        recargo = costo_consumo * 0.05

elif tipo_cliente == "industrial":
    if consumo > 1000:
        bonificacion = costo_consumo * 0.30
    elif consumo > 500:
        bonificacion = costo_consumo * 0.20
    if consumo < 200:
        recargo = costo_consumo * 0.10

else:
    print("ERROR: Tipo de cliente no valido. Use: Residencial, Comercial o Industrial")
    exit()

# Calculos finales
subtotal_con_ajustes = subtotal_base - bonificacion + recargo - descuento_especial
iva = subtotal_con_ajustes * 0.21
total_pagar = subtotal_con_ajustes + iva

# Mostrar resultados
print("\n" + "="*50)
print("DETALLE DE FACTURA")
print("="*50)
print(f"Tipo de cliente: {tipo_cliente.title()}")
print(f"Consumo: {consumo} m³")
print(f"Cargo fijo: ${cargo_fijo:,.2f}")
print(f"Costo por consumo: ${costo_consumo:,.2f}")
print(f"Subtotal base: ${subtotal_base:,.2f}")

if bonificacion > 0:
    print(f"Bonificación: -${bonificacion:,.2f}")
if recargo > 0:
    print(f"Recargo: +${recargo:,.2f}")
if descuento_especial > 0:
    print(f"Descuento especial: -${descuento_especial:,.2f}")

print(f"Subtotal con ajustes: ${subtotal_con_ajustes:,.2f}")
print(f"IVA (21%): ${iva:,.2f}")
print("="*50)
print(f"TOTAL A PAGAR: ${total_pagar:,.2f}")
print("="*50)