
telefonos = {"José": 1234,
             "María": 3456,
             "Andrés": 5678,
             "Lucía": 9876}

consultando = True

while consultando:
    print()
    print("MIS TELÉFONOS")
    print("-------------")
    print("1. Consultar por nombre")
    print("2. Consultar por teléfono")
    print("3. Listar la agenda")
    print("4. Salir")
    print("-------------")

    opcion = ""
    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("-> ")

    if opcion == "1":
        nom = input("Introduce nombre: ")
        tel = telefonos.get(nom, "Esa entrada no existe...")
        print(f"{nom}: {tel}")

    elif opcion == "2":
        tel = int(input("Introduce teléfono: "))
        if tel in telefonos.values(): # comprobamos que está
            for nom in telefonos: # recorremos el dicc para comprobar el nombre
                if telefonos[nom] == tel:
                    print(f"{tel}: {nom}")
        else:
            print("Ese nº no existe...")

    elif opcion == "3":
        for nom, tel in telefonos.items():
            print(f"{nom}: {tel}")

    elif opcion == "4":
        consultando = False