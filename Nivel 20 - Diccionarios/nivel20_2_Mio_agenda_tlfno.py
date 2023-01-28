"""
Realizar una agenda telefónica con las operaciones básicas
de un diccionario con la siguiente estructura

telefonos = {"José": 1234,
             "María": 3456,
             "Andrés": 5678,
             "Lucía": 9876}

consultando = True

while consultando:
    print()
    print("MIS TELÉFONOS")
    print("-------------")
    print("1. Consultar")
    print("2. Añadir")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Salir")
    print("-------------")

    opcion = ""
    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("-> ")
"""

telefonos = {"José": 1234,
             "María": 3456,
             "Andrés": 5678,
             "Lucía": 9876}

consultando = True

while consultando:
    print()
    print("MIS TELÉFONOS")
    print("-------------")
    print("1. Consultar Individual")
    print("2. Añadir")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Agenda completa")
    print("6. Salir")
    print("-------------")

    opcion = ""
    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("-> ")
    if opcion == "1":
        nom = input("Introduce nombre a mostrar: ")
        while nom not in telefonos:
            nom = input(f"{nom} no se encuentra. Introduce nombre a mostrar: ")
        else:
            print(f"El número de {nom} es {telefonos[nom]}.")
    elif opcion == "2":
        nom = input("Introduce nombre a Añadir: ")
        num = input(f"Introduce número de {nom}: ")
        telefonos[nom] = num
        print(f"Ha sido añadida una nueva entrada. {nom}: {telefonos[nom]}")
    elif opcion == "3":
        nom = input("Introduce nombre a Modificar: ")
        while nom not in telefonos:
            nom = input(f"{nom} no se encuentra. Introduce nombre a Modificar: ")
        else:
            num = input(f"Introduce nuevo número de {nom}: ")
            telefonos[nom] = num
            print(f"La entrad de {nom} a sido Modificada. {nom}: {telefonos[nom]}")
    elif opcion == "4":
        nom = input("Introduce nombre a Eliminar: ")
        while nom not in telefonos:
            nom = input(f"{nom} no se encuentra. Introduce nombre a Eliminar: ")
        else:
            del telefonos[nom]
            print(f"La entrad de {nom} a sido eliminada.")
    elif opcion == "5":
        consultando = False
