'''
Programa que guarda un registro de todas las búsquedas
que se realizan en un diccionario, tanto de los elementos
que están como los que no.
El reeultado debe ser:

PREFIJOS INTERNACIONALES
------------------------
País ('q' salir): Chile

CHILE: 56

------------------------
Registro de búsquedas:
CHILE: 1
------------------------

'''

prefijos = {
    "COLOMBIA": 57,
    "ARGENTINA": 54,
    "PERÚ": 51,
    "MÉXICO": 52,
    "BOLIVIA": 591,
    "CHILE": 56,
    "ESPAÑA": 34,
    "ECUADOR": 593
    }

busqueda = {}

print("PREFIJOS INTERNACIONALES")
print("------------------------")

while True:
    pais = input("País ('q' salir): ").upper()
    if pais == "Q":
        break

    prefijo = prefijos.get(pais, "No disponible")
    print()
    print(f"{pais}: {prefijo}")
    print()

    # miramos si el país NO está en el diccionario
    # si está, no hace nada
    busqueda.setdefault(pais, 0)
    # si se repite ese país, se aumenta en un las búsquedas
    busqueda[pais] += 1

    print("------------------------")
    print("Registro de búsquedas:")
    for k, v in busqueda.items():
        print(f"{k}: {v}")
    print("------------------------")
