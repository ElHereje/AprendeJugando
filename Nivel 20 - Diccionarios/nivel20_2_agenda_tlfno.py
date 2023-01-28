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
        opcion = input("->")
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
    print("1. Consultar")
    print("2. Añadir")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Salir")
    print("-------------")

    opcion = ""
    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("-> ")

    if opcion == "1":
        nom = input("Introduce nombre a mostrar: ")
        if nom not in telefonos:
            print("Ese nombre no existe.")
        else:
            num = telefonos[nom]
            print(nom, ":", num)

    elif opcion == "2":
        nom = input("Introduce nombre a introducir: ")
        if nom in telefonos:
            print("Ese nombre ya existe.")
        else:
            num = int(input("Teléfono: "))
            telefonos[nom] = num

    elif opcion == "3":
        nom = input("Introduce nombre a Modificar: ")
        if nom not in telefonos:
            print("Ese nombre no existe.")
        else:
            num = int(input("Teléfono: "))
            telefonos[nom] = num

    elif opcion == "4":
        nom = input("Introduce nombre a Eliminar: ")
        if nom not in telefonos:
            print("Ese nombre no existe.")
        else:
            del telefonos[nom]

    elif opcion == "5":
        consultando = False

