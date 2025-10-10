"""
Una empresa se dedica al almacenamiento y posterior distribución de
cereales en el interior del país. Para ello cuentan con 20 depósitos en CABA,
que generalmente se encuentran en las inmediaciones de las estaciones del
ferrocarril.
Los depósitos pueden almacenar 4 tipos diferentes de cereales: maíz, trigo,
cebada y centeno.
La oficina central, recibe mensualmente una planilla de existencias donde se
indican las existencias de cada cereal para cada depósito.
Realizar un menú de opciones:
1. Obtener existencias: para ello deberá crear una función que cargue la
existencia de cada grano en todos los depósitos. Los valores estarán
comprendidos entre 5000 Kg y 20000 Kg.
2. Calcular por cada depósito la cantidad total de kilos almacenados entre
todos los cereales.
3. Nombre del cereal que almaceno menos kilos en cada depósito.
4. Máxima cantidad de kilos almacenados de cada cereal.
5. Depósito con mayor recaudación, teniendo en cuenta que disponemos
de un vector con los valores por kilo de cada tipo de cereal.
6. Cantidad de depósitos que hayan almacenado más de 50000 kilos
entre los 4 cereales.
7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados.
Además mostrar el nombre del cereal con el máximo porcentaje.
8. Generar un informe con la recaudación de cada depósito, ordenada de
mayor a menor.

"""

precio_por_kilo = {
    "maiz": 1,
    "trigo": 2,
    "cebada": 3,
    "centeno": 4
}

precio_vector = [
    ["maiz", 1],
    ["trigo", 2],
    ["cebada", 3],
    ["centeno", 4]
]

# Class = Molde de galletita
class Deposito:
    def __init__(self, nombre: str, cantidad_maiz: int, cantidad_trigo: int, cantidad_cebada: int, cantidad_centeno: int):
        self.__nombre = nombre
        self.__cantidad_maiz = cantidad_maiz
        self.__cantidad_trigo = cantidad_trigo
        self.__cantidad_cebada = cantidad_cebada
        self.__cantidad_centeno = cantidad_centeno
    
    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad_maiz(self) -> int:
        return self.__cantidad_maiz
    
    def get_cantidad_trigo(self) -> int:
        return self.__cantidad_trigo
    
    def get_cantidad_cebada(self) -> int:
        return self.__cantidad_cebada
    
    def get_cantidad_centeno(self) -> int:
        return self.__cantidad_centeno

    def __repr__(self) -> str:
        return f"Deposito {self.__nombre} -> Maiz: {self.__cantidad_maiz}kg, Trigo: {self.__cantidad_trigo}kg, Cebada: {self.__cantidad_cebada}kg, Centeno: {self.__cantidad_centeno}kg"

# Object/Instance = una galletita con sus valores propios (con sus chispas de chocolate)
# Deposito("Depósito 1", 100, 200, 300, 400)

#2. Calcular por cada depósito la cantidad total de kilos almacenados entre todos los cereales.
def calcular_total_kilos_por_deposito(granos_por_deposito: list[Deposito]) -> list[int] :
    total_kilos_por_deposito = []
    for deposito in granos_por_deposito:
        total_kilos = deposito.get_cantidad_maiz() + deposito.get_cantidad_trigo() + deposito.get_cantidad_cebada() + deposito.get_cantidad_centeno()
        total_kilos_por_deposito.append((deposito.get_nombre(), total_kilos))
    return total_kilos_por_deposito

def menu():
    granos_por_deposito = [
        Deposito("Fulanito", 100, 200, 300, 400),
        Deposito("Menganito", 150, 250, 350, 450),
        Deposito("Sutanito", 200, 300, 400, 500)
    ]

    calcular_total_kilos_por_deposito()

#3. Nombre del cereal que almaceno menos kilos en cada depósito.
def cereal_menos_kilos_por_deposito(granos_por_deposito: list[Deposito]) -> list[tuple[str, str]]:
    cereal_menos_kilos = []
    for deposito in granos_por_deposito:
        cantidades = {
            "maiz": deposito.get_cantidad_maiz(),
            "trigo": deposito.get_cantidad_trigo(),
            "cebada": deposito.get_cantidad_cebada(),
            "centeno": deposito.get_cantidad_centeno()
        }
        cereal_menor = min(cantidades, key=cantidades.get)
        cereal_menos_kilos.append((deposito.get_nombre(), cereal_menor))
    return cereal_menos_kilos