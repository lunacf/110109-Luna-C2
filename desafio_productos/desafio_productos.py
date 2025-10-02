# 1- productos en comun = interseccion entre conjuntos
# 2- productos esclusivos = diferencia entre conjuntos
# 3- catalogo de productos = productos totales = union entre conjuntos

usuario = [
  "manteca",
  "leche",
  "huevos",
  "azucar",
]

usuario2 = [
  "manteca",
  "leche",
  "huevos",
  "azucar",
  "harina",
  "chocolate"
]

# v1 estatica
def compararUsuariosV1(usuario1, usuario2):
    dictComparaciones = {
        "comun": [], # interseccion
        "exclusivos": [], # diferencia
        "total": [] # union
    }
    for item in usuario1:
        if item in usuario2:
            dictComparaciones["comun"].append(item)
        else:
            dictComparaciones["exclusivos"].append(item)
        dictComparaciones["total"].append(item)
    return dictComparaciones

# v2 dinamica permite tener N usuarios
def compararUsuariosv2(**usuarios):
    comparaciones = []
    for usuario in usuarios: # para cada usuario en usuarios
        # armamos la variable donde vamos a guardar las comparaciones
        dictComparaciones = {
            "en_comun": [], # interseccion
            "exclusivos": [], # diferencia
            "total": [] # union
        }
        
        # calculamos cuales son los otros usuarios
        restoDeUsuarios = [u for u in usuarios if u != usuario] # lista de usuarios menos el actual

        # recorremos los items del usuario actual y los comparamos con los del resto
        for item in usuario: # para cada item del usuario actual
            if all(item in u for u in restoDeUsuarios):
                dictComparaciones["en_comun"].append(item)
            elif all(item not in u for u in restoDeUsuarios):
                dictComparaciones["exclusivos"].append(item)
            dictComparaciones["total"].append(item) # agrego el item actual a total

        # ahora agregamos los items del resto de usuarios a total
        for u in restoDeUsuarios: # para cada usuario de restoDeUsuarios
            for item in u: # para cada item de ese usuario
                if item not in dictComparaciones["total"]: # si el item no esta en total
                    dictComparaciones["total"].append(item) # lo agrego a total

        # agrego el dict de comparaciones a la lista de comparaciones
        comparaciones.append(dictComparaciones)
    
    return comparaciones
    # [
    #     {"en_comun": [manteca, leche, huevos, azucar], "exclusivos": [], "total": [manteca, leche, huevos, azucar, harina, chocolate]}, 
    #     {"en_comun": [manteca, leche, huevos, azucar], "exclusivos": [harina, chocolate], "total": [manteca, leche, huevos, azucar, harina, chocolate]}
    # ]

compararUsuarios(usuario, usuario2)